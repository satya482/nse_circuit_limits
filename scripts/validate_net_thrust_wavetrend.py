#!/usr/bin/env python3
"""
scripts/validate_net_thrust_wavetrend.py
=========================================
Module D — Validation harness for the Net-Thrust WaveTrend oscillator.

Reads Module A output (data/net_thrust_wavetrend.csv) and breadth history
(data/breadth_history.csv), runs a full historical backtest, and prints a
go/no-go verdict based on three acceptance criteria (spec §7.5):

  C1 — Median lag from WT BULL_CROSS to SMA200 inflection: 0–15 calendar days
  C2 — WT median lag shorter than SMA10 turn-up baseline lag
  C3 — False-cross rate not materially worse than baseline (≤ 1.5× baseline)

Outputs:
  data/net_thrust_wt_validation.csv — per-cross enriched rows

Usage:
  python scripts/validate_net_thrust_wavetrend.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_DIR))
sys.path.insert(0, str(REPO_DIR / "scanners"))

import pandas as pd
import numpy as np

from sma200_context import (
    enrich_bull_crosses,
)


# ---------------------------------------------------------------------------
# Step 2 helpers — sanity checks
# ---------------------------------------------------------------------------


def _check_cross_near(
    wt_df: pd.DataFrame, date_str: str, cross_type: str, tolerance_days: int, label: str
) -> bool:
    """
    Verify a cross of the given type exists within ±tolerance_days of date_str.
    Prints a PASS/FAIL line and returns bool.
    """
    target = pd.Timestamp(date_str)
    window = wt_df[
        (wt_df["cross_type"] == cross_type)
        & (wt_df["date"] >= target - pd.Timedelta(days=tolerance_days))
        & (wt_df["date"] <= target + pd.Timedelta(days=tolerance_days))
    ]
    ok = len(window) > 0
    dates_found = window["date"].dt.strftime("%Y-%m-%d").tolist() if ok else []
    print(
        f"  Sanity {label}: {'PASS' if ok else 'FAIL'} — "
        f"{'found ' + str(dates_found) if ok else 'no cross found'}"
    )
    return ok


# ---------------------------------------------------------------------------
# Step 4a — Detect SMA10 turn-up events
# ---------------------------------------------------------------------------


def detect_sma10_turnups(
    history_df: pd.DataFrame, threshold: float = 30.0
) -> pd.DatetimeIndex:
    """
    SMA10 turn-up: pct_above_sma10 was < threshold previous session AND
    current > previous.

    Parameters
    ----------
    history_df : pd.DataFrame
        breadth_history filtered rows, with 'date' and 'pct_above_sma10' columns.
    threshold : float
        Oversold level below which we watch for a turn-up.

    Returns
    -------
    pd.DatetimeIndex
        Dates of SMA10 turn-up events.
    """
    s = history_df.sort_values("date")["pct_above_sma10"].values
    dates = history_df.sort_values("date")["date"].values
    events = []
    for i in range(1, len(s)):
        if (
            pd.notna(s[i - 1])
            and pd.notna(s[i])
            and s[i - 1] < threshold
            and s[i] > s[i - 1]
        ):
            events.append(dates[i])
    return pd.DatetimeIndex(events)


# ---------------------------------------------------------------------------
# Step 4b — Detect SMA200 local-min-then-rising inflections
# ---------------------------------------------------------------------------


def detect_sma200_inflections(
    history_df: pd.DataFrame, lookback: int = 20, min_consecutive_rising: int = 3
) -> pd.DatetimeIndex:
    """
    Local min in rolling lookback-bar window, followed by min_consecutive_rising
    consecutive non-decreasing bars.

    Returns list of dates marking the start of the rising run.
    """
    s = history_df.sort_values("date").set_index("date")["pct_above_sma200"]
    events = []
    vals = s.values
    dates = s.index
    for i in range(lookback, len(vals) - min_consecutive_rising):
        if pd.isna(vals[i]):
            continue
        # Is this a local min in the lookback window?
        window = vals[max(0, i - lookback) : i + 1]
        if pd.isna(window).any():
            continue
        if vals[i] == window.min():
            # Check consecutive non-decreasing
            run = vals[i : i + min_consecutive_rising + 1]
            if len(run) >= min_consecutive_rising + 1 and all(
                run[j] >= run[j - 1] for j in range(1, min_consecutive_rising + 1)
            ):
                events.append(dates[i])
    return pd.DatetimeIndex(events)


# ---------------------------------------------------------------------------
# Step 4c — Lag computation
# ---------------------------------------------------------------------------


def lag_to_nearest(
    cross_dates: pd.DatetimeIndex,
    event_dates: pd.DatetimeIndex,
    max_lag_days: int = 120,
) -> list:
    """
    For each cross date, find nearest event date (forward preferred).

    Returns array of lags in calendar days:
      positive  → WT cross leads the event (WT fired early, event came after)
      negative  → WT cross lags the event (event happened before the cross)
      None      → no event within max_lag_days in either direction

    Note: Uses calendar days for simplicity. NSE trading-day count ≈ 0.71×
    calendar days — sufficient for hypothesis comparison.
    """
    lags = []
    event_arr = pd.DatetimeIndex(event_dates)
    for cd in cross_dates:
        future = event_arr[event_arr >= cd]
        past = event_arr[event_arr < cd]
        forward_lag = int((future[0] - cd).days) if len(future) > 0 else None
        backward_lag = -int((cd - past[-1]).days) if len(past) > 0 else None
        candidates = [
            x
            for x in [forward_lag, backward_lag]
            if x is not None and abs(x) <= max_lag_days
        ]
        lags.append(min(candidates, key=abs) if candidates else None)
    return lags


# ---------------------------------------------------------------------------
# Step 6 — False-cross classification
# ---------------------------------------------------------------------------

# Labeled chop windows (UTC dates).  Add more as detected.
CHOP_WINDOWS = [
    ("2026-05-19", "2026-06-11"),  # oscillating breadth, labeled in spec
]


def classify_false_crosses(
    wt_df: pd.DataFrame,
    chop_start: str,
    chop_end: str,
    continuation_calendar_days: int = 7,
) -> pd.Series:
    """
    Within the chop window [chop_start, chop_end], mark each cross as True
    (false cross) or False (true cross).

    A cross is "false" if an opposite-direction cross fires within
    continuation_calendar_days calendar days.

    Returns a Series indexed like wt_df with bool/NaN values.
    - True  → false cross (reversed quickly)
    - False → true cross (no reversal within window)
    - NaN   → cross is outside any labeled chop window
    """
    result = pd.Series(np.nan, index=wt_df.index, dtype=object)

    start_ts = pd.Timestamp(chop_start)
    end_ts = pd.Timestamp(chop_end)

    in_window_mask = (wt_df["date"] >= start_ts) & (wt_df["date"] <= end_ts)

    opposite = {"BULL_CROSS": "BEAR_CROSS", "BEAR_CROSS": "BULL_CROSS"}

    for idx, row in wt_df[in_window_mask].iterrows():
        if row["cross_type"] not in ("BULL_CROSS", "BEAR_CROSS"):
            continue
        opp = opposite[row["cross_type"]]
        cd = row["date"]
        reversal = wt_df[
            (wt_df["date"] > cd)
            & (wt_df["date"] <= cd + pd.Timedelta(days=continuation_calendar_days))
            & (wt_df["cross_type"] == opp)
            & (wt_df["channel"] == row["channel"])
        ]
        result.at[idx] = len(reversal) > 0

    return result


# ---------------------------------------------------------------------------
# Step 8 — Print acceptance criteria verdict
# ---------------------------------------------------------------------------


def print_verdict(
    validation_df: pd.DataFrame,
    baseline_lags: list,
    chop_false_rate: float,
    baseline_false_rate: float,
) -> bool:
    """
    Print C1/C2/C3 acceptance criteria and return True (GO) or False (NO-GO).
    """
    fast_bull = validation_df[
        (validation_df["channel"] == "fast")
        & (validation_df["cross_type"] == "BULL_CROSS")
        & validation_df["lag_to_sma200_inflection"].notna()
    ]["lag_to_sma200_inflection"]

    print("\n=== ACCEPTANCE CRITERIA (spec §7.5) ===")

    # Criterion 1: Median lag positive and ≤15 calendar days (~10 trading days)
    if len(fast_bull) == 0:
        median_lag = None
        c1 = False
        print("  C1 - Median lag to SMA200 inflection: N/A (no data)")
        print("       FAIL (no fast BULL_CROSS with matched inflection)")
    else:
        median_lag = fast_bull.median()
        c1 = 0 < median_lag <= 15
        print(f"  C1 - Median lag to SMA200 inflection: {median_lag:.1f} calendar days")
        print(f"       {'PASS' if c1 else 'FAIL'} (target: 0–15 days)")

    # Criterion 2: WT lag shorter than SMA10 baseline
    baseline_series = pd.Series(baseline_lags).dropna()
    if len(baseline_series) == 0 or median_lag is None:
        c2 = False
        baseline_median = None
        print("  C2 - WT lag vs SMA10 baseline: N/A")
        print("       FAIL (insufficient data)")
    else:
        baseline_median = baseline_series.median()
        c2 = (
            median_lag is not None
            and baseline_median is not None
            and abs(median_lag) < abs(baseline_median)
        )
        print(
            f"  C2 - |WT lag| ({abs(median_lag):.1f}) vs |SMA10 baseline| ({abs(baseline_median):.1f})"
        )
        print(f"       {'PASS' if c2 else 'FAIL'} (WT absolute lag must be shorter)")

    # Criterion 3: False-cross rate not materially worse than baseline
    print(
        f"  C3 - False-cross rate: {chop_false_rate:.0%} vs baseline {baseline_false_rate:.0%}"
    )
    c3 = chop_false_rate <= baseline_false_rate * 1.5  # 50% worse = "materially worse"
    print(f"       {'PASS' if c3 else 'FAIL'}")

    verdict = (
        "GO — build dashboard panel"
        if (c1 and c2 and c3)
        else "NO-GO — do not build dashboard panel"
    )
    print(f"\n>>> VERDICT: {verdict}")
    return c1 and c2 and c3


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    print("=== Net-Thrust WaveTrend Validation Harness ===\n")

    # ------------------------------------------------------------------
    # Step 1: Load and filter data
    # ------------------------------------------------------------------
    history = pd.read_csv(REPO_DIR / "data" / "breadth_history.csv")
    wt = pd.read_csv(REPO_DIR / "data" / "net_thrust_wavetrend.csv")

    # Exclude anomalous rows (total_eligible < 2000) — including known bad 2026-06-26
    history = history[history["total_eligible"] >= 2000].copy()
    history["date"] = pd.to_datetime(history["date"])

    wt["date"] = pd.to_datetime(wt["date"])

    # Fast channel only for primary analysis
    fast_wt = wt[wt["channel"] == "fast"].copy()
    slow_wt = wt[wt["channel"] == "slow"].copy()

    print(
        f"Loaded breadth history: {len(history)} rows "
        f"({history['date'].min().date()} to {history['date'].max().date()})"
    )
    print(
        f"Loaded WT data: {len(wt)} rows "
        f"({wt['date'].min().date()} to {wt['date'].max().date()})"
    )
    fast_crosses = fast_wt[fast_wt["cross_type"] != "NONE"]
    print(
        f"Fast-channel crosses: {len(fast_crosses)} "
        f"({fast_wt[fast_wt['cross_type']=='BULL_CROSS'].shape[0]} bull, "
        f"{fast_wt[fast_wt['cross_type']=='BEAR_CROSS'].shape[0]} bear)"
    )

    # ------------------------------------------------------------------
    # Step 2: Sanity checks (spec §7.1)
    # ------------------------------------------------------------------
    print("\n--- Sanity checks ---")
    ok1 = _check_cross_near(
        fast_wt,
        "2026-06-12",
        "BULL_CROSS",
        tolerance_days=1,
        label="BULL_CROSS near 2026-06-12",
    )
    ok2 = _check_cross_near(
        fast_wt,
        "2026-06-22",
        "BEAR_CROSS",
        tolerance_days=2,
        label="BEAR_CROSS near 2026-06-22",
    )

    if not (ok1 and ok2):
        print("\nSANITY CHECK FAILED — debug params before proceeding")
        sys.exit(1)

    print("  Sanity checks PASSED — proceeding\n")

    # ------------------------------------------------------------------
    # Step 3: Enrich bull crosses with SMA200 context
    # ------------------------------------------------------------------
    bull_crosses = enrich_bull_crosses(fast_wt, history)
    slow_bull_crosses = enrich_bull_crosses(
        slow_wt, history
    )  # enriched for completeness

    print(f"Fast BULL_CROSS rows enriched: {len(bull_crosses)}")
    print(f"Slow BULL_CROSS rows enriched: {len(slow_bull_crosses)} (informational)")
    if len(bull_crosses) > 0:
        tier_counts = (
            pd.to_numeric(bull_crosses["breadth_cross_tier"], errors="coerce")
            .dropna()
            .astype(int)
            .value_counts()
            .sort_index()
        )
        print(f"  Tier distribution: {tier_counts.to_dict()}")

    # ------------------------------------------------------------------
    # Step 4a: Detect SMA10 turn-up events
    # ------------------------------------------------------------------
    sma10_turnups = detect_sma10_turnups(history, threshold=30.0)
    print(f"\nSMA10 turn-up events (below 30% then rising): {len(sma10_turnups)}")
    if len(sma10_turnups) > 0:
        print(
            f"  Dates: {[str(d.date()) for d in sma10_turnups[:10]]}{'...' if len(sma10_turnups) > 10 else ''}"
        )

    # ------------------------------------------------------------------
    # Step 4b: Detect SMA200 local-min-then-rising inflections
    # ------------------------------------------------------------------
    sma200_inflections = detect_sma200_inflections(
        history, lookback=20, min_consecutive_rising=3
    )
    print(f"SMA200 inflection events (local min + 3 rising): {len(sma200_inflections)}")
    if len(sma200_inflections) > 0:
        print(
            f"  Dates: {[str(d.date()) for d in sma200_inflections[:10]]}{'...' if len(sma200_inflections) > 10 else ''}"
        )

    # ------------------------------------------------------------------
    # Step 4c: Lag from each fast BULL_CROSS to nearest SMA200 inflection
    # ------------------------------------------------------------------
    fast_bull_dates = pd.DatetimeIndex(
        fast_wt[fast_wt["cross_type"] == "BULL_CROSS"]["date"]
    )
    lags_to_inflection = lag_to_nearest(
        fast_bull_dates, sma200_inflections, max_lag_days=120
    )
    print("\nLag to SMA200 inflection (fast BULL_CROSS -> inflection):")
    lag_series = pd.Series(lags_to_inflection).dropna()
    if len(lag_series) > 0:
        print(
            f"  n={len(lag_series)}, median={lag_series.median():.1f}d, "
            f"mean={lag_series.mean():.1f}d, min={lag_series.min():.0f}d, max={lag_series.max():.0f}d"
        )
    else:
        print("  No matched lags within max_lag_days=120")

    # ------------------------------------------------------------------
    # Step 5: Baseline — SMA10 turn-up → SMA200 inflection lag
    # ------------------------------------------------------------------
    baseline_lags = lag_to_nearest(sma10_turnups, sma200_inflections, max_lag_days=120)
    baseline_series = pd.Series(baseline_lags).dropna()
    print("\nBaseline lag (SMA10 turn-up -> SMA200 inflection):")
    if len(baseline_series) > 0:
        print(
            f"  n={len(baseline_series)}, median={baseline_series.median():.1f}d, "
            f"mean={baseline_series.mean():.1f}d, min={baseline_series.min():.0f}d, max={baseline_series.max():.0f}d"
        )
    else:
        print("  No matched baseline lags")

    # ------------------------------------------------------------------
    # Step 6: False-cross rate
    # ------------------------------------------------------------------
    print("\n--- False-cross analysis ---")

    # Compute is_false_cross for fast channel
    fast_all = fast_wt[fast_wt["cross_type"].isin(["BULL_CROSS", "BEAR_CROSS"])].copy()
    is_false = pd.Series(np.nan, index=fast_all.index, dtype=object)

    for chop_start, chop_end in CHOP_WINDOWS:
        window_result = classify_false_crosses(
            fast_all, chop_start, chop_end, continuation_calendar_days=7
        )
        # Merge: only overwrite NaN positions
        for idx in window_result.index:
            if not pd.isna(window_result.at[idx]):
                is_false.at[idx] = window_result.at[idx]

    # False-cross rate in chop windows
    labeled_mask = is_false.notna()
    chop_crosses_total = labeled_mask.sum()
    chop_false_count = (is_false[labeled_mask] == True).sum()  # noqa: E712
    chop_false_rate = (
        chop_false_count / chop_crosses_total if chop_crosses_total > 0 else 0.0
    )

    print(
        f"  Chop window crosses: {chop_crosses_total} "
        f"({chop_false_count} false, {chop_crosses_total - chop_false_count} true)"
    )
    print(f"  WT false-cross rate in chop: {chop_false_rate:.0%}")

    # Baseline false-cross rate: SMA10 turn-ups in same chop window that reverse quickly
    # Use a simple proxy: fraction of SMA10 turnups that were followed by a re-drop within 7 days
    sma10_sorted = history.sort_values("date").reset_index(drop=True)
    sma10_vals = sma10_sorted["pct_above_sma10"].values
    sma10_dates = pd.DatetimeIndex(sma10_sorted["date"])

    baseline_false_count = 0
    baseline_total = 0
    for chop_start, chop_end in CHOP_WINDOWS:
        cs = pd.Timestamp(chop_start)
        ce = pd.Timestamp(chop_end)
        for tu_date in sma10_turnups:
            if cs <= tu_date <= ce:
                # Check if pct_above_sma10 drops below its turn-up level within 7 calendar days
                tu_idx = np.searchsorted(sma10_dates, tu_date)
                tu_level = sma10_vals[tu_idx] if tu_idx < len(sma10_vals) else None
                if tu_level is None:
                    continue
                baseline_total += 1
                reversal_window = sma10_dates[
                    (sma10_dates > tu_date)
                    & (sma10_dates <= tu_date + pd.Timedelta(days=7))
                ]
                if len(reversal_window) == 0:
                    continue
                # Get the values in the reversal window
                end_idx = min(
                    np.searchsorted(
                        sma10_dates, tu_date + pd.Timedelta(days=7), side="right"
                    ),
                    len(sma10_vals),
                )
                window_vals = sma10_vals[tu_idx + 1 : end_idx]
                if len(window_vals) > 0 and window_vals.min() < tu_level:
                    baseline_false_count += 1

    if baseline_total > 0:
        baseline_false_rate = baseline_false_count / baseline_total
    else:
        baseline_false_rate = 0.5
        print(
            "  WARNING: No SMA10 turn-up events found in any chop window — "
            "C3 baseline defaulting to 50% (arbitrary). "
            "Check that chop window dates overlap with history.",
            flush=True,
        )
    print(
        f"  SMA10 baseline false-cross rate in chop: "
        f"{baseline_false_count}/{baseline_total} = {baseline_false_rate:.0%}"
    )

    # ------------------------------------------------------------------
    # Step 7: Build output table + write CSV
    # ------------------------------------------------------------------
    print("\n--- Building validation output table ---")

    # Build fast bull cross rows with all computed metrics
    fast_bull_df = (
        fast_wt[fast_wt["cross_type"] == "BULL_CROSS"].copy().reset_index(drop=True)
    )
    fast_bear_df = (
        fast_wt[fast_wt["cross_type"] == "BEAR_CROSS"].copy().reset_index(drop=True)
    )

    # Merge enrichment context for bull crosses
    if len(bull_crosses) > 0:
        context_cols = [
            "date",
            "sma200_band",
            "sma200_roc_10d",
            "confirm_or_diverge",
            "breadth_cross_tier",
        ]
        enrichment = bull_crosses[context_cols].copy()
    else:
        enrichment = pd.DataFrame(
            columns=[
                "date",
                "sma200_band",
                "sma200_roc_10d",
                "confirm_or_diverge",
                "breadth_cross_tier",
            ]
        )

    # Merge lags (indexed like fast_bull_df)
    fast_bull_df_reset = fast_bull_df.copy()
    fast_bull_df_reset["lag_to_sma200_inflection"] = lags_to_inflection

    # Lag to SMA10 turn-up (for each BULL_CROSS)
    lags_to_sma10 = lag_to_nearest(fast_bull_dates, sma10_turnups, max_lag_days=120)
    fast_bull_df_reset["lag_to_sma10_uptick"] = lags_to_sma10

    # Merge context
    fast_bull_final = fast_bull_df_reset.merge(enrichment, on="date", how="left")

    # is_false_cross: look up from is_false (indexed on fast_all)
    false_map = {}
    for orig_idx, val in is_false.items():
        if not pd.isna(val):
            row = fast_all.loc[orig_idx]
            false_map[row["date"]] = val

    fast_bull_final["is_false_cross"] = fast_bull_final["date"].map(false_map)

    # Also add BEAR_CROSS rows for completeness (without enrichment cols)
    fast_bear_df_reset = fast_bear_df.copy()
    fast_bear_df_reset["lag_to_sma200_inflection"] = np.nan
    fast_bear_df_reset["lag_to_sma10_uptick"] = np.nan
    fast_bear_df_reset["sma200_band"] = np.nan
    fast_bear_df_reset["sma200_roc_10d"] = np.nan
    fast_bear_df_reset["confirm_or_diverge"] = np.nan
    fast_bear_df_reset["breadth_cross_tier"] = np.nan
    fast_bear_df_reset["is_false_cross"] = fast_bear_df_reset["date"].map(false_map)

    # Combine bull + bear, sort by date
    combined = (
        pd.concat([fast_bull_final, fast_bear_df_reset], ignore_index=True)
        .sort_values("date")
        .reset_index(drop=True)
    )

    # Select output columns
    output_cols = [
        "date",
        "channel",
        "cross_type",
        "breadth_cross_tier",
        "sma200_band",
        "sma200_roc_10d",
        "confirm_or_diverge",
        "lag_to_sma10_uptick",
        "lag_to_sma200_inflection",
        "is_false_cross",
    ]
    output = combined[output_cols].copy()

    # Write CSV — rename 'date' -> 'cross_date' per spec §7 column contract
    output_df = output.rename(columns={"date": "cross_date"})
    out_path = REPO_DIR / "data" / "net_thrust_wt_validation.csv"
    output_df.to_csv(out_path, index=False)
    print(f"Wrote {len(output_df)} rows to {out_path}")

    # Summary stats
    print("\n--- Summary ---")
    print(f"  Fast BULL_CROSS: {(output['cross_type']=='BULL_CROSS').sum()}")
    print(f"  Fast BEAR_CROSS: {(output['cross_type']=='BEAR_CROSS').sum()}")
    tier_out = pd.to_numeric(
        output.loc[output["cross_type"] == "BULL_CROSS", "breadth_cross_tier"],
        errors="coerce",
    ).dropna()
    if len(tier_out) > 0:
        print(
            f"  BULL_CROSS tier distribution: {tier_out.astype(int).value_counts().sort_index().to_dict()}"
        )
    bull_with_lag = output[
        (output["cross_type"] == "BULL_CROSS")
        & output["lag_to_sma200_inflection"].notna()
    ]
    print(
        f"  BULL_CROSS with SMA200 lag match: {len(bull_with_lag)}/{(output['cross_type']=='BULL_CROSS').sum()}"
    )

    # ------------------------------------------------------------------
    # Step 8: Print acceptance criteria verdict
    # ------------------------------------------------------------------
    print_verdict(output, baseline_lags, chop_false_rate, baseline_false_rate)


if __name__ == "__main__":
    main()
