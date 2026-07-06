# consolidation/consolidation_scanner.py
"""Consolidation Tracker — daily scanner. run(universe_df, as_of) -> pd.DataFrame
per spec Sec 0's required interface. Universe: own TradingView Query() mirroring
wt_bullcross_scanner.py (NSE common stock, mcap 1,000-5,00,000 Cr, price > Rs 50).
Gate: EMA dual gate AND BB squeeze gate only (2-gate definition, user decision --
volume/RS are scored components, not filters). No signals.db: tier-transition
history is derived by diffing today's output against the most recent prior
results/*-consolidation.csv."""

import os
import sys
from datetime import datetime, timezone, timedelta

import pandas as pd
from tradingview_screener import Query, col

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ohlc_db
from ohlc_db import load_ohlc_many, cmf_series
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

from consolidation import indicators, quality, imminence, tiers
from capital import regime_throttle
from capital.regime_throttle import HISTORY_PATH

IST = timezone(timedelta(hours=5, minutes=30))
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(REPO_DIR, "results")
MD_DIR = os.path.join(REPO_DIR, "consolidation_scans")
BENCH_SYM = "NIFTY MIDSML 400"

MC_LOW = 1_000 * 1_00_00_000
MC_HIGH = 5_00_000 * 1_00_00_000
MIN_BARS = 250

COLUMNS = [
    "symbol", "quality", "imminence", "tier", "age_bars", "ema_stage",
    "vol_phase", "rs_char", "cmf", "deliv_trend", "prebreak_count",
    "regime", "action",
]
_TIER_RANK = {"TIER_1_HOT": 3, "TIER_2_WARM": 2, "TIER_3_COLD": 1, "NONE": 0}

_ACTION_BY_TIER = {
    "TIER_1_HOT": "DEPLOY_ELIGIBLE",
    "TIER_2_WARM": "ARM",
    "TIER_3_COLD": "WATCH",
    "NONE": "NONE",
}


def action_for(tier_label: str, regime: str) -> str:
    if regime == "RED":
        return "NO_DEPLOY" if tier_label != "NONE" else "NONE"
    return _ACTION_BY_TIER[tier_label]


def get_universe() -> list[str]:
    """TV screener, mirrors wt_bullcross_scanner.py's own band exactly."""
    _, df = (
        Query()
        .set_markets("india")
        .select("name")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 50,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(2000)
        .get_scanner_data()
    )
    return df["name"].tolist()


def analyse(symbol: str, df: pd.DataFrame, bench_df: pd.DataFrame | None, regime: str) -> dict | None:
    if df is None or len(df) < MIN_BARS or bench_df is None:
        return None

    df = indicators.ema_compression(df)
    df = indicators.bollinger_keltner(df)
    df = indicators.volume_exhaustion(df)

    ema_ok, _ = indicators.ema_dual_gate(df)
    sq_ok, _ = indicators.squeeze_gate(df)
    if not (ema_ok and sq_ok):
        return None

    metrics = indicators.rs_metrics(df, bench_df)
    if metrics is None:
        return None
    rs_char = indicators.classify_rs_character(metrics)

    cmf_vals = cmf_series(df, n=20)
    cmf_today = float(cmf_vals.iloc[-1]) if len(cmf_vals) else 0.0

    deliv_trend_label = quality.deliv_trend(symbol)

    stage = indicators.ema_stage(df["spread_delta"].iloc[-1])
    bb_pct = float(df["bb_width_percentile"].iloc[-1])
    vol_pct = float(df["vol_percentile"].iloc[-1])

    q_score = quality.quality_score(bb_pct, stage, vol_pct, rs_char, cmf_today, deliv_trend_label)
    age_bars = tiers.consolidation_age(df)

    stage3 = imminence.ema_stage3_flag(df["spread_delta"])
    rs_breakout_flag = rs_char == "CHAR_5_RS_BREAKOUT"
    bb_breathe = imminence.bb_breathing(df["bb_width_percentile"])
    range_pos = imminence.range_position(df, age_bars)

    sig1 = bool(metrics["rs_52wk_high"] and not metrics["price_20d_high"])
    sig2 = imminence.spread_delta_crossover(df["spread_delta"])
    quiet_today = bool(df["quiet_accum_bar"].iloc[-1])
    deliv_df = ohlc_db.load_delivery(symbol, lookback=21)
    deliv_spike_today = deliv_df is not None and ohlc_db.deliv_spike(deliv_df) is not None
    sig3_wt = imminence.signal3_weight(quiet_today, deliv_spike_today)
    sig5 = imminence.higher_low(df)
    sig6 = imminence.wick_rejection_absorbed(df, age_bars)

    imm_score, prebreak_count = imminence.imminence_score(
        sig1, sig2, sig3_wt, bb_breathe, sig5, sig6,
        stage3, rs_breakout_flag, bb_breathe, range_pos,
    )

    tier_label = tiers.tier(q_score, imm_score)

    return {
        "symbol": symbol,
        "quality": q_score,
        "imminence": imm_score,
        "tier": tier_label,
        "age_bars": age_bars,
        "ema_stage": stage,
        "vol_phase": indicators.volume_phase(df),
        "rs_char": rs_char,
        "cmf": round(cmf_today, 3),
        "deliv_trend": deliv_trend_label or "UNKNOWN",
        "prebreak_count": prebreak_count,
        "regime": regime,
        "action": action_for(tier_label, regime),
    }


def find_previous_csv(as_of: str) -> str | None:
    """Most recent results/*-consolidation.csv strictly before as_of. Globbing
    existing files (rather than assuming yesterday's calendar date exists) skips
    weekends/holidays automatically."""
    if not os.path.isdir(RESULTS_DIR):
        return None
    candidates = sorted(
        f for f in os.listdir(RESULTS_DIR)
        if f.endswith("-consolidation.csv") and f[:10] < as_of
    )
    return os.path.join(RESULTS_DIR, candidates[-1]) if candidates else None


def compute_transitions(rows: list[dict], as_of: str) -> dict:
    prev_path = find_previous_csv(as_of)
    prev_tiers = {}
    if prev_path:
        prev_df = pd.read_csv(prev_path)
        prev_tiers = dict(zip(prev_df["symbol"], prev_df["tier"]))

    curr_symbols = {r["symbol"] for r in rows}
    promoted, demoted = [], []
    for r in rows:
        prev_t = prev_tiers.get(r["symbol"])
        if prev_t is None:
            continue
        if _TIER_RANK[r["tier"]] > _TIER_RANK.get(prev_t, 0):
            promoted.append(r["symbol"])
        elif _TIER_RANK[r["tier"]] < _TIER_RANK.get(prev_t, 0):
            demoted.append(r["symbol"])
    abandoned = [sym for sym in prev_tiers if sym not in curr_symbols]
    return {"promoted": promoted, "demoted": demoted, "abandoned": abandoned}


def build_markdown(rows: list[dict], as_of: str, transitions: dict) -> str:
    sorted_rows = sorted(rows, key=lambda r: (-_TIER_RANK[r["tier"]], -r["imminence"]))
    lines = [f"## Consolidation Scan — {as_of}", ""]
    lines.append(f"**Promotions:** {', '.join(transitions['promoted']) or 'none'}")
    lines.append(f"**Demotions:** {', '.join(transitions['demoted']) or 'none'}")
    lines.append(f"**Abandoned:** {', '.join(transitions['abandoned']) or 'none'}")
    lines.append("")
    if sorted_rows:
        lines.append("| " + " | ".join(COLUMNS) + " |")
        lines.append("|" + "---|" * len(COLUMNS))
        for r in sorted_rows:
            lines.append("| " + " | ".join(str(r[c]) for c in COLUMNS) + " |")
    else:
        lines.append("*No signals.*")
    lines.append("")
    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


def run(universe_df: pd.DataFrame, as_of: str) -> pd.DataFrame:
    """Spec's required interface. universe_df must have a 'symbol' column."""
    symbols = universe_df["symbol"].tolist()
    all_data = load_ohlc_many(symbols + [BENCH_SYM], lookback=600)
    bench_df = all_data.pop(BENCH_SYM, None)

    regime_info = regime_throttle.regime_for_date(as_of, history_path=HISTORY_PATH)
    regime = regime_info["regime"]

    rows = []
    for sym, sym_df in all_data.items():
        result = analyse(sym, sym_df, bench_df, regime)
        if result:
            rows.append(result)

    return pd.DataFrame(rows, columns=COLUMNS)


def main() -> None:
    os.makedirs(RESULTS_DIR, exist_ok=True)
    os.makedirs(MD_DIR, exist_ok=True)
    as_of = datetime.now(IST).strftime("%Y-%m-%d")

    print("Fetching universe from TradingView screener...")
    symbols = get_universe()
    print(f"  {len(symbols)} stocks after screener filters")

    universe_df = pd.DataFrame({"symbol": symbols})
    result_df = run(universe_df, as_of)
    print(f"  {len(result_df)} stocks passed EMA+squeeze gates")

    rows = result_df.to_dict("records")
    transitions = compute_transitions(rows, as_of)

    csv_path = os.path.join(RESULTS_DIR, f"{as_of}-consolidation.csv")
    result_df.to_csv(csv_path, index=False)

    md = build_markdown(rows, as_of, transitions)
    with open(os.path.join(MD_DIR, "consolidation_scan_latest.md"), "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(os.path.join(MD_DIR, f"consolidation_scan_{as_of}.md"), "w", encoding="utf-8") as fh:
        fh.write(md)

    print(f"  Saved -> {csv_path}")
    print("  Saved -> consolidation_scans/consolidation_scan_latest.md")


if __name__ == "__main__":
    main()
