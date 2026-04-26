#!/usr/bin/env python3
"""Dual-gate compression filter."""

import pandas as pd


def _bar_compressed(row: pd.Series, atr_threshold: float, pct_threshold: float) -> bool:
    spread_atr = row.get("spread_atr_ratio")
    spread_pct = row.get("spread_pct")
    if pd.isna(spread_atr) or pd.isna(spread_pct):
        return False
    return spread_atr < atr_threshold and spread_pct < pct_threshold


def compression_duration(df: pd.DataFrame, atr_threshold: float, pct_threshold: float) -> int:
    """Count consecutive bars at the tail where both gates pass."""
    count = 0
    for i in range(len(df) - 1, -1, -1):
        if _bar_compressed(df.iloc[i], atr_threshold, pct_threshold):
            count += 1
        else:
            break
    return count


def passes(df: pd.DataFrame, settings: dict) -> tuple[bool, int]:
    """Returns (qualifies, duration_bars)."""
    g = settings["gate"]
    duration = compression_duration(df, g["ema_spread_atr_ratio"], g["ema_spread_pct"])
    return duration >= g["min_compression_bars"], duration