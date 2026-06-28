#!/usr/bin/env python3
"""
scanners/sma200_context.py
===========================
Module B — SMA200 structural context and confirm/diverge gate.

Pure functions for classifying breadth regime context around WT cross events.
Used by Task 5 (validation harness) to enrich BULL_CROSS rows with SMA200 context.

Functions:
  - sma200_band(pct_above_sma200: float) -> str
      Classify structural regime (extreme_bottom, washout, weakening, healthy_bull, overbought_peak_risk)

  - sma200_roc_10d(series: pd.Series) -> pd.Series
      Compute 10-day rate of change (raw diff)

  - sma200_slope_label(roc_value: float) -> str
      Classify slope direction (rising, flat, falling)

  - confirm_or_diverge(sma200_roc_10d_at_cross: float) -> str
      Classify if a WT cross is confirmed, divergent, or neutral by breadth momentum

  - breadth_cross_tier(band: str, roc: float) -> int
      Assign conviction tier (1=highest, 4=lowest/caution) for a BULL_CROSS event

  - enrich_bull_crosses(wt_df: pd.DataFrame, history_df: pd.DataFrame) -> pd.DataFrame
      Join BULL_CROSS rows with SMA200 context (sma200_band, sma200_roc_10d,
      confirm_or_diverge, breadth_cross_tier)
"""

from __future__ import annotations

import pandas as pd


def sma200_band(pct_above_sma200: float) -> str:
    """
    Classify structural SMA200 regime based on % of stocks above 200-day SMA.

    Parameters
    ----------
    pct_above_sma200 : float
        Percentage (0-100) of universe above SMA200, or NaN if not available

    Returns
    -------
    str
        One of: "overbought_peak_risk", "healthy_bull", "weakening",
                "washout", "extreme_bottom", or NaN (when input is NaN)

    Notes
    -----
    Boundary logic (spec §5.1):
      > 80%           → "overbought_peak_risk" (strict >)
      [50, 80]        → "healthy_bull"
      [20, 50)        → "weakening"
      [15, 20)        → "washout"
      < 15%           → "extreme_bottom"
      NaN             → NaN (propagate missing data)
    """
    import pandas as pd
    import numpy as np

    if pd.isna(pct_above_sma200) or np.isnan(pct_above_sma200):
        return np.nan

    if pct_above_sma200 > 80:
        return "overbought_peak_risk"
    elif pct_above_sma200 >= 50:
        return "healthy_bull"
    elif pct_above_sma200 >= 20:
        return "weakening"
    elif pct_above_sma200 >= 15:
        return "washout"
    else:
        return "extreme_bottom"


def sma200_roc_10d(series: pd.Series) -> pd.Series:
    """
    Compute 10-day rate of change (raw difference).

    Parameters
    ----------
    series : pd.Series
        Time series (typically pct_above_sma200 column), oldest-first

    Returns
    -------
    pd.Series
        Raw 10-day diff; first 10 values are NaN

    Notes
    -----
    Callers classify result as:
      > 1.0  → "rising"
      < -1.0 → "falling"
      [-1.0, +1.0] → "flat"
    """
    return series.diff(10)


def sma200_slope_label(roc_value: float) -> str:
    """
    Classify SMA200 slope direction based on 10-day ROC value.

    Parameters
    ----------
    roc_value : float
        10-day ROC from sma200_roc_10d()

    Returns
    -------
    str
        One of: "rising", "falling", "flat"
    """
    if roc_value > 1.0:
        return "rising"
    elif roc_value < -1.0:
        return "falling"
    else:
        return "flat"


def confirm_or_diverge(sma200_roc_10d_at_cross: float) -> str:
    """
    Classify if a WT cross is confirmed, divergent, or neutral by SMA200 momentum.

    Parameters
    ----------
    sma200_roc_10d_at_cross : float
        10-day ROC of pct_above_sma200 at the time of the WT cross

    Returns
    -------
    str
        One of: "CONFIRMED", "DIVERGENT", "NEUTRAL"

    Notes
    -----
    CONFIRMED   → ROC > 1.0: breadth strengthening, cross has tailwind
    DIVERGENT   → ROC < -1.0: breadth weakening, cross fights headwind
    NEUTRAL     → ROC in [-1.0, +1.0]: breadth flat, no directional momentum
    """
    if sma200_roc_10d_at_cross > 1.0:
        return "CONFIRMED"
    elif sma200_roc_10d_at_cross < -1.0:
        return "DIVERGENT"
    else:
        return "NEUTRAL"


def breadth_cross_tier(band: str, roc: float) -> int:
    """
    Assign conviction tier (1=highest, 4=lowest/caution) for a BULL_CROSS event.

    Parameters
    ----------
    band : str
        SMA200 structural regime from sma200_band(), or NaN if not available
    roc : float
        10-day ROC of pct_above_sma200, or NaN if not available

    Returns
    -------
    int
        One of: 1 (highest conviction), 2, 3, 4 (caution/lowest),
                or NaN if band or roc is NaN

    Notes
    -----
    Tiering logic (spec §6):
      Tier 1 (highest conviction):
        - (extreme_bottom OR washout) AND roc > 1.0
          → Deep pullback with breadth recovery → strong reversal signal

      Tier 2:
        - weakening AND roc > 1.0
          → Weakening regime but breadth turning up → still positive

      Tier 4 (caution/lowest):
        - overbought_peak_risk (regardless of ROC)
          → Extended, reduced upside surprise; wait for correction first

      Tier 3 (default):
        - Everything else (momentum-only signal without breadth tailwind)
          Examples: healthy_bull + any ROC, weakening + flat/falling, washout + flat/falling

      NaN:
        - When band or roc is NaN, return NaN (missing data)
    """
    import pandas as pd
    import numpy as np

    if pd.isna(band) or pd.isna(roc) or np.isnan(roc):
        return np.nan

    if band in ("extreme_bottom", "washout") and roc > 1.0:
        return 1
    elif band == "weakening" and roc > 1.0:
        return 2
    elif band == "overbought_peak_risk":
        return 4
    else:
        return 3


def enrich_bull_crosses(wt_df: pd.DataFrame, history_df: pd.DataFrame) -> pd.DataFrame:
    """
    Join BULL_CROSS rows from Module A output with SMA200 context.

    Parameters
    ----------
    wt_df : pd.DataFrame
        Output from compute_net_thrust_wt (Module A).
        Columns expected: date, channel, cross_type, ... (and others from WT)
    history_df : pd.DataFrame
        From breadth_history.csv.
        Columns expected: date, pct_above_sma200, ... (and others from breadth)

    Returns
    -------
    pd.DataFrame
        BULL_CROSS rows with added columns:
          - sma200_band (str): regime classification
          - sma200_roc_10d (float): 10-day ROC of pct_above_sma200
          - confirm_or_diverge (str): CONFIRMED / DIVERGENT / NEUTRAL
          - breadth_cross_tier (int): 1-4 conviction tier

        Columns order: original wt_df columns + [sma200_band, sma200_roc_10d,
                       confirm_or_diverge, breadth_cross_tier]
        Sorted by date (ascending), then channel if multiple channels present on same date.

    Notes
    -----
    1. Only BULL_CROSS rows are returned; non-cross rows are dropped.
    2. Rows in wt_df without a matching date in history_df will have
       pct_above_sma200=NaN and thus sma200_roc_10d=NaN.
    3. Dates without pct_above_sma200 data will have NaN in sma200_band
       and breadth_cross_tier; confirm_or_diverge will be "NEUTRAL" (NaN < -1.0 is False).
    4. Output is sorted by date ascending, then channel (if present).
    """
    # Step 1: Filter to BULL_CROSS rows only
    bull_crosses = wt_df[wt_df["cross_type"] == "BULL_CROSS"].copy()

    if len(bull_crosses) == 0:
        # Return empty DataFrame with the expected columns
        result_cols = list(bull_crosses.columns) + [
            "sma200_band",
            "sma200_roc_10d",
            "confirm_or_diverge",
            "breadth_cross_tier",
        ]
        return pd.DataFrame(columns=result_cols)

    # Step 2: Compute ROC series from history_df
    history_sorted = history_df.sort_values("date").reset_index(drop=True)
    roc_series = sma200_roc_10d(history_sorted["pct_above_sma200"])

    # Rebuild as a dict for easier merge (date -> roc_value)
    roc_map = dict(zip(history_sorted["date"], roc_series))

    # Step 3: Merge on date to attach pct_above_sma200 and roc
    history_for_merge = history_df[["date", "pct_above_sma200"]].copy()
    merged = bull_crosses.merge(history_for_merge, on="date", how="left")

    # Step 4: Attach ROC via the map (same date lookup)
    merged["sma200_roc_10d"] = merged["date"].map(roc_map)

    # Step 5: Apply classification functions row-by-row
    merged["sma200_band"] = merged["pct_above_sma200"].apply(sma200_band)
    merged["confirm_or_diverge"] = merged["sma200_roc_10d"].apply(confirm_or_diverge)
    merged["breadth_cross_tier"] = merged.apply(
        lambda row: breadth_cross_tier(row["sma200_band"], row["sma200_roc_10d"]),
        axis=1,
    )

    # Step 6: Sort by date, then channel if present
    if "channel" in merged.columns:
        merged = merged.sort_values(["date", "channel"]).reset_index(drop=True)
    else:
        merged = merged.sort_values("date").reset_index(drop=True)

    # Remove the temporary pct_above_sma200 column (it was for context only)
    merged = merged.drop(columns=["pct_above_sma200"])

    return merged
