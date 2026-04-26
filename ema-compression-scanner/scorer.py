#!/usr/bin/env python3
"""Composite 0-100 compression quality scorer."""

import pandas as pd


def score(df: pd.DataFrame, duration: int, settings: dict) -> tuple[float, dict]:
    """
    Returns (total_score, component_scores).
    Higher = tighter + longer + drier volume + cleaner uptrend + price near cluster.
    """
    last = df.iloc[-1]
    w = settings["scoring"]
    g = settings["gate"]

    # Tightness: 100 when spread/ATR → 0, 0 at threshold
    tightness = max(0.0, 1.0 - last["spread_atr_ratio"] / g["ema_spread_atr_ratio"]) * 100

    # Duration: 100 at 60 bars, linear below
    duration_score = min(duration / 60, 1.0) * 100

    # Volume contraction during compression vs long-run average
    comp_start = max(0, len(df) - duration)
    recent_vol = df["volume"].iloc[comp_start:].mean()
    long_vol = last["vol_ma50"]
    if pd.notna(long_vol) and long_vol > 0:
        vol_contraction = max(0.0, 1.0 - recent_vol / long_vol) * 100
    else:
        vol_contraction = 50.0

    # Trend: EMA50 > EMA100 > EMA200 = full uptrend (100), partial (50), none (0)
    e50, e100, e200 = last["ema50"], last["ema100"], last["ema200"]
    if e50 > e100 > e200:
        trend_score = 100.0
    elif e50 > e200:
        trend_score = 50.0
    else:
        trend_score = 0.0

    # Price proximity to EMA cluster midpoint
    ema_mid = (e50 + e100 + e200) / 3
    price_dist_pct = abs(last["close"] - ema_mid) / ema_mid * 100 if ema_mid > 0 else 0
    proximity_score = max(0.0, 100.0 - price_dist_pct * 5)

    total = (
        tightness      * w["tightness"] +
        duration_score * w["duration"] +
        vol_contraction * w["volume_contraction"] +
        trend_score    * w["trend"] +
        proximity_score * w["proximity"]
    )

    components = {
        "tightness":        round(tightness, 1),
        "duration":         round(duration_score, 1),
        "vol_contraction":  round(vol_contraction, 1),
        "trend":            round(trend_score, 1),
        "proximity":        round(proximity_score, 1),
    }
    return round(total, 1), components