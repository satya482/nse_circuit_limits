#!/usr/bin/env python3
"""
NSE Breadth Monitor — regime/timing layer (not a candidate-selection scanner).

Answers: "is the market environment supportive right now?"
Accumulates a rolling time series; one row per (date, universe_tag) in breadth_history.csv.

Interface deviation from other scanners: this module accumulates a time series rather
than emitting per-day candidate lists. Deliberate — documented here and in CLAUDE.md.
"""

import sys
from datetime import date, timezone, timedelta
from pathlib import Path

import pandas as pd

REPO_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_DIR))

IST = timezone(timedelta(hours=5, minutes=30))

UNIVERSE_TAG = "breadth_broad"
THRUST_THRESHOLD = (
    1.6  # TODO: validate against >=1yr NSE history before treating as production signal
)
CAPITULATION_THRESHOLD = (
    0.6  # TODO: validate against >=1yr NSE history before treating as production signal
)
HISTORY_PATH = REPO_DIR / "data" / "breadth_history.csv"
UNIVERSE_PATH = REPO_DIR / "data" / "breadth_universe.csv"
DASHBOARD_PATH = REPO_DIR / "dashboard" / "nse_breadth_monitor.html"
NIFTY50_SYM = "NIFTY 50"
OHLC_LOOKBACK = 2500  # ~10yr trading bars

_CSV_COLUMNS = [
    "date",
    "universe_tag",
    "total_eligible",
    "up4_count",
    "down4_count",
    "ratio_5d",
    "ratio_10d",
    "up25_quarter",
    "down25_quarter",
    "pct_above_sma200",
    "composite_score",
]


def compute_daily_breadth(
    universe_df: pd.DataFrame,
    as_of: date,
    ohlc_map: dict[str, pd.DataFrame],
) -> dict | None:
    """Single-day breadth snapshot. Pure function, no I/O.

    as_of strictly bounds all calculations — never reads closes after as_of.
    Returns None when as_of is not present as a trading date in ohlc_map.
    Circuit-frozen (v1): excluded if close == prev_close AND volume == 0.
    """
    as_of_str = as_of.strftime("%Y-%m-%d")

    # Filter ohlc_map to universe symbols only — prevents benchmark or other
    # non-universe symbols in SQLite from being silently counted in breadth metrics
    universe_syms = set(universe_df["symbol"].tolist())
    ohlc_map = {s: df for s, df in ohlc_map.items() if s in universe_syms}

    # Collect all trading dates up to as_of to build ratio window
    all_dates: set[str] = set()
    for df in ohlc_map.values():
        date_strs = df["date"].dt.strftime("%Y-%m-%d")
        all_dates.update(d for d in date_strs if d <= as_of_str)

    sorted_dates = sorted(all_dates)
    if not sorted_dates or as_of_str not in sorted_dates:
        return None  # as_of is not a trading day in this dataset

    # Window: last 10 trading dates (ratio_10d uses all 10; ratio_5d uses last 5)
    window_10 = sorted_dates[-10:]
    window_set = set(window_10)

    # Per-date accumulators for ratio computation
    up4: dict[str, int] = {d: 0 for d in window_10}
    dn4: dict[str, int] = {d: 0 for d in window_10}

    # as_of-specific accumulators
    total_eligible = 0
    up25 = 0
    dn25 = 0
    above_sma200 = 0
    elig_sma200 = 0

    for sym, df in ohlc_map.items():
        # Filter strictly to as_of and before
        mask = df["date"].dt.strftime("%Y-%m-%d") <= as_of_str
        df_s = df[mask].reset_index(drop=True)
        if len(df_s) < 2:
            continue

        closes = df_s["close"].astype(float).values
        volumes = df_s["volume"].astype(float).values
        dates_arr = df_s["date"].dt.strftime("%Y-%m-%d").values

        # Stock must have a row on as_of
        if dates_arr[-1] != as_of_str:
            continue

        date_to_pos = {d: i for i, d in enumerate(dates_arr)}

        # Per-date up4/dn4 for the ratio window
        for target_d in window_set:
            if target_d not in date_to_pos:
                continue
            pos = date_to_pos[target_d]
            if pos == 0:
                continue
            c, pc, v = closes[pos], closes[pos - 1], volumes[pos]
            if c == pc and v == 0:  # circuit-frozen: skip
                continue
            pct = c / pc - 1
            if pct >= 0.04:
                up4[target_d] += 1
            if pct <= -0.04:
                dn4[target_d] += 1

        # as_of row metrics
        today_close = closes[-1]
        today_vol = volumes[-1]
        prev_close = closes[-2]

        if today_close == prev_close and today_vol == 0:  # circuit-frozen
            continue

        total_eligible += 1

        # pct_63d — exclude stocks with <64 bars from quarterly calc only
        if len(df_s) >= 64:
            pct_63d = today_close / closes[-64] - 1
            if pct_63d >= 0.25:
                up25 += 1
            if pct_63d <= -0.25:
                dn25 += 1

        # SMA200 — plain SMA, min_periods=200
        # Known limitation: circuit-gap days distort plain SMA. Flagged, deferred to v1.1.
        if len(df_s) >= 200:
            elig_sma200 += 1
            if today_close > closes[-200:].mean():
                above_sma200 += 1

    up4_today = up4.get(as_of_str, 0)
    dn4_today = dn4.get(as_of_str, 0)

    def _ratio(n: int) -> float | None:
        last_n = window_10[-n:]
        if len(last_n) < n:
            return None
        up_sum = sum(up4.get(d, 0) for d in last_n)
        dn_sum = sum(dn4.get(d, 0) for d in last_n)
        return round(up_sum / max(1, dn_sum), 4)

    pct_sma200 = round(above_sma200 / elig_sma200 * 100, 2) if elig_sma200 > 0 else None

    return {
        "date": as_of_str,
        "universe_tag": UNIVERSE_TAG,
        "total_eligible": total_eligible,
        "up4_count": up4_today,
        "down4_count": dn4_today,
        "ratio_5d": _ratio(5),
        "ratio_10d": _ratio(10),
        "up25_quarter": up25,
        "down25_quarter": dn25,
        "pct_above_sma200": pct_sma200,
        "composite_score": None,  # v1.1: backtest normalization bounds before enabling
    }


def update_breadth_history(history_path: str, new_row: dict) -> None:
    """Upsert new_row into breadth_history.csv keyed on (date, universe_tag). Idempotent."""
    path = Path(history_path)
    if path.exists():
        df = pd.read_csv(path)
        # Ensure all expected columns present (handles schema evolution)
        for col in _CSV_COLUMNS:
            if col not in df.columns:
                df[col] = None
        df = df[_CSV_COLUMNS]
    else:
        df = pd.DataFrame(columns=_CSV_COLUMNS)

    # Remove existing row for this (date, universe_tag) — idempotent upsert
    mask = (df["date"] == new_row["date"]) & (
        df["universe_tag"] == new_row["universe_tag"]
    )
    df = df[~mask]

    new_df = pd.DataFrame([{c: new_row.get(c) for c in _CSV_COLUMNS}])
    df = pd.concat([df, new_df], ignore_index=True)
    df = df.sort_values("date").reset_index(drop=True)

    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
