#!/usr/bin/env python3
"""Gate filters: EMA dual gate + BB squeeze gate."""

import pandas as pd


def _bar_compressed(row: pd.Series, atr_threshold: float, pct_threshold: float) -> bool:
    spread_atr = row.get("spread_atr_ratio")
    spread_pct = row.get("spread_pct")
    if pd.isna(spread_atr) or pd.isna(spread_pct):
        return False
    return spread_atr < atr_threshold and spread_pct < pct_threshold


def compression_duration(df: pd.DataFrame, atr_threshold: float, pct_threshold: float) -> int:
    """Count consecutive bars at the tail where both EMA gates pass."""
    count = 0
    for i in range(len(df) - 1, -1, -1):
        if _bar_compressed(df.iloc[i], atr_threshold, pct_threshold):
            count += 1
        else:
            break
    return count


def passes(df: pd.DataFrame, settings: dict) -> tuple[bool, int]:
    """EMA dual gate. Returns (qualifies, duration_bars)."""
    g = settings["gate"]
    duration = compression_duration(df, g["ema_spread_atr_ratio"], g["ema_spread_pct"])
    return duration >= g["min_compression_bars"], duration


def bb_squeeze_passes(df: pd.DataFrame, settings: dict) -> tuple[bool, int]:
    """
    BB squeeze gate. Expects bollinger_keltner() already called on df.
    Returns (passes, squeeze_days).
    squeeze_days >= squeeze.min_bars AND bb_width_pct_rank <= squeeze.bb_width_pct_max.
    """
    if "squeeze_on" not in df.columns:
        return False, 0

    sq = settings["squeeze"]
    count = 0
    squeeze_col = df["squeeze_on"]
    for i in range(len(squeeze_col) - 1, -1, -1):
        if bool(squeeze_col.iloc[i]):
            count += 1
        else:
            break

    last_pct_rank = df["bb_width_pct_rank"].iloc[-1] if "bb_width_pct_rank" in df.columns else 100.0
    width_ok = pd.notna(last_pct_rank) and float(last_pct_rank) <= sq["bb_width_pct_max"]
    return count >= sq["min_bars"] and width_ok, count