#!/usr/bin/env python3
"""
scanners/net_thrust_wavetrend.py
=================================
Module A — Net Thrust WaveTrend dual-channel oscillator.

Reads `net_thrust` from `data/breadth_history.csv` (breadth regime time series)
and runs WaveTrend on it via WaveTrendCalculator.calc_from_series().

Two channels:
  fast: n1=5,  n2=10
  slow: n1=10, n2=21

Output: data/net_thrust_wavetrend.csv
  One row per (date, channel), sorted date ASC then channel.
  Columns: date, channel, net_thrust, wt1, wt2, cross_type, is_low_conviction_day

Low-conviction guard (spec §4.2):
  Days where up4_count + down4_count < 30 are flagged as low-conviction.
  Before computing WaveTrend, those net_thrust values are replaced by the
  60-day trailing rolling median to prevent extreme spikes from quiet days.

Anomalous row guard (spec §10):
  Rows where total_eligible < 2000 OR net_thrust is NaN are excluded entirely
  from the output CSV (not useful as signals). NaN is NOT zero-filled — it
  propagates naturally through EMA but we skip these rows from output.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import pandas as pd

# ---------------------------------------------------------------------------
# Repo root path setup — mirrors breadth_monitor.py pattern
# ---------------------------------------------------------------------------
REPO_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_DIR))

from wavetrend_scanner import WaveTrendCalculator  # noqa: E402

# ---------------------------------------------------------------------------
# Channel parameters (spec §4.1)
# ---------------------------------------------------------------------------
CHANNELS: dict[str, dict[str, int]] = {
    "fast": {"n1": 5, "n2": 10},
    "slow": {"n1": 10, "n2": 21},
}

# Anomalous row guard threshold (spec §10)
DEFAULT_MIN_TOTAL_ELIGIBLE = 2000

# Low-conviction threshold (spec §4.2)
LOW_CONVICTION_THRESHOLD = 30

# Rolling window for low-conviction median replacement
LOW_CONVICTION_MEDIAN_WINDOW = 60

# Output CSV column order
OUTPUT_COLUMNS = [
    "date",
    "channel",
    "net_thrust",
    "wt1",
    "wt2",
    "cross_type",
    "is_low_conviction_day",
]


# ---------------------------------------------------------------------------
# Output dataclass (matches spec schema exactly)
# ---------------------------------------------------------------------------
@dataclass
class NetThrustWTSignal:
    date: str  # YYYY-MM-DD string
    channel: Literal["fast", "slow"]
    net_thrust: float
    wt1: float
    wt2: float
    cross_type: Literal["BULL_CROSS", "BEAR_CROSS", "NONE"]
    is_low_conviction_day: bool  # True if up4+down4 < 30


# ---------------------------------------------------------------------------
# Core function
# ---------------------------------------------------------------------------
def compute_net_thrust_wt(
    history_path: Path,
    output_path: Path,
    min_total_eligible: int = DEFAULT_MIN_TOTAL_ELIGIBLE,
) -> pd.DataFrame:
    """
    Run WaveTrend on net_thrust from breadth_history.csv.

    Returns DataFrame with all signal rows (date x channel), also persists
    to output_path as CSV.

    Steps:
    1. Read history_path; filter rows where total_eligible < min_total_eligible
       OR net_thrust is NaN.
    2. Sort by date ascending.
    3. Compute low-conviction mask (up4 + down4 < 30); replace those net_thrust
       values with 60-day trailing rolling median before feeding into WaveTrend.
    4. For each channel ("fast", "slow"):
       a. Call WaveTrendCalculator(n1, n2).calc_from_series(adjusted_series)
       b. Build one row per date per channel in the NetThrustWTSignal schema.
    5. Concatenate channels, sort by date then channel, persist to output_path.
    6. Return the full DataFrame.

    Notes:
    - EMA warm-up (first ~60 rows) is included in output — the validation
      harness (Task 5) skips burn-in when computing lag metrics.
    - Rows excluded by the anomalous guard do NOT appear in output (they
      produce NaN wavetrend values and carry no signal value).
    """
    # ── 1. Load and filter ───────────────────────────────────────────────────
    df = pd.read_csv(history_path, dtype={"date": str})

    # Anomalous row guard: exclude rows with too few eligible stocks or NaN net_thrust
    df = df[df["total_eligible"] >= min_total_eligible].copy()
    df = df[df["net_thrust"].notna()].copy()

    # ── 2. Sort by date ascending ────────────────────────────────────────────
    df = df.sort_values("date").reset_index(drop=True)

    # ── 3. Low-conviction adjustment ─────────────────────────────────────────
    net_thrust_series = df["net_thrust"].copy()
    low_conviction_mask = (
        df["up4_count"] + df["down4_count"]
    ) < LOW_CONVICTION_THRESHOLD

    # 60-day trailing rolling median (min_periods=1 to handle start of series)
    rolling_median = net_thrust_series.rolling(
        LOW_CONVICTION_MEDIAN_WINDOW, min_periods=1
    ).median()

    # Replace low-conviction day values with rolling median
    adjusted_series = net_thrust_series.copy()
    adjusted_series[low_conviction_mask] = rolling_median[low_conviction_mask]

    # Preserve the original flag for output (reset index so alignment is clean)
    adjusted_series.index = df.index

    # ── 4. Compute WaveTrend for each channel ────────────────────────────────
    channel_frames: list[pd.DataFrame] = []

    for channel_name, params in CHANNELS.items():
        calc = WaveTrendCalculator(n1=params["n1"], n2=params["n2"])
        wt_df = calc.calc_from_series(
            adjusted_series,
            n1=params["n1"],
            n2=params["n2"],
        )
        # wt_df columns: wt1, wt2, wt_diff, cross_type  (same index as df)

        channel_rows = pd.DataFrame(
            {
                "date": df["date"].values,
                "channel": channel_name,
                "net_thrust": net_thrust_series.values,  # original (not adjusted)
                "wt1": wt_df["wt1"].values,
                "wt2": wt_df["wt2"].values,
                "cross_type": wt_df["cross_type"].values,
                "is_low_conviction_day": low_conviction_mask.values,
            }
        )
        channel_frames.append(channel_rows)

    # ── 5. Combine, sort, persist ────────────────────────────────────────────
    result = pd.concat(channel_frames, ignore_index=True)
    result = result.sort_values(["date", "channel"]).reset_index(drop=True)

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    result[OUTPUT_COLUMNS].to_csv(output_path, index=False)

    return result[OUTPUT_COLUMNS]


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    history = REPO_DIR / "data" / "breadth_history.csv"
    output = REPO_DIR / "data" / "net_thrust_wavetrend.csv"

    df = compute_net_thrust_wt(history, output)
    print(f"Wrote {len(df)} rows to {output}")

    # Quick sanity check: fast-channel BULL_CROSS events
    bulls = df[(df["channel"] == "fast") & (df["cross_type"] == "BULL_CROSS")]
    print(f"\nFast-channel BULL_CROSS events ({len(bulls)}):")
    print(bulls[["date", "wt1", "wt2", "net_thrust"]].tail(10).to_string())

    # Quick sanity check: fast-channel BEAR_CROSS events
    bears = df[(df["channel"] == "fast") & (df["cross_type"] == "BEAR_CROSS")]
    print(f"\nFast-channel BEAR_CROSS events ({len(bears)}):")
    print(bears[["date", "wt1", "wt2", "net_thrust"]].tail(10).to_string())
