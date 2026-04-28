#!/usr/bin/env python3
"""
Composite 0-100 scorer — 5 components scored across the candidate set.
All normalization is min-max across today's candidates (not historical).
"""

import pandas as pd


def _normalize(values: list[float]) -> list[float]:
    """Min-max normalize. Returns list of 0.0-1.0 values."""
    if not values:
        return []
    lo, hi = min(values), max(values)
    if hi == lo:
        return [1.0] * len(values)
    return [(v - lo) / (hi - lo) for v in values]


def score_all(candidates: list[dict], settings: dict) -> list[float]:
    """
    Score all candidates together using cross-candidate min-max normalization.

    Each candidate dict must have:
        df           — DataFrame with compute() + bollinger_keltner() already applied
        duration     — int, EMA compression bars
        squeeze_days — int, consecutive BB squeeze bars
        rs_gap       — float, normalized RS gap above EMA9
        rs_slope     — float, RS 4-week diff
        rs_rating    — float 0-1, percentile rank vs all 962 stocks

    Returns list of scores (0-100) in same order as candidates.
    """
    if not candidates:
        return []

    w  = settings["scoring"]
    rw = settings["rs_weights"]
    g  = settings["gate"]

    tightness_raw    = []
    duration_raw     = []
    vol_trend_raw    = []
    bb_intensity_raw = []
    rs_gap_raw       = []
    rs_slope_raw     = []
    rs_rating_raw    = []

    for c in candidates:
        df       = c["df"]
        duration = c["duration"]
        last     = df.iloc[-1]

        # 1. EMA tightness: invert spread/ATR so higher = tighter
        spread_atr = float(last.get("spread_atr_ratio", g["ema_spread_atr_ratio"]))
        tightness_raw.append(1.0 / max(spread_atr, 0.01))

        # 2. Duration: capped at 60 bars
        duration_raw.append(min(duration, 60))

        # 3. Volume trend: contraction during compression vs long-run average
        comp_start = max(0, len(df) - duration)
        recent_vol = float(df["volume"].iloc[comp_start:].mean())
        long_vol   = float(last.get("vol_ma50", 0) or 0)
        if long_vol > 0:
            contraction = max(0.0, 1.0 - recent_vol / long_vol)
        else:
            contraction = 0.5
        vol_trend_raw.append(contraction)

        # 4. BB intensity: squeeze depth + width tightness (both 0-1, equal weight)
        squeeze_days  = c["squeeze_days"]
        bb_pct_rank   = float(last.get("bb_width_pct_rank", 50.0) or 50.0)
        depth_score   = min(squeeze_days, 20) / 20          # more days = deeper
        width_score   = 1.0 - bb_pct_rank / 100             # lower rank = tighter
        bb_intensity_raw.append(depth_score * 0.5 + width_score * 0.5)

        # 5. RS strength sub-components (normalized separately below)
        rs_gap_raw.append(c["rs_gap"])
        rs_slope_raw.append(c["rs_slope"])
        rs_rating_raw.append(c["rs_rating"])  # already 0-1 percentile

    # Cross-candidate normalization
    t_norm  = _normalize(tightness_raw)
    d_norm  = _normalize(duration_raw)
    v_norm  = _normalize(vol_trend_raw)
    b_norm  = _normalize(bb_intensity_raw)
    rg_norm = _normalize(rs_gap_raw)
    rs_norm = _normalize(rs_slope_raw)
    # rs_rating is already 0-1; still normalize across candidates for consistency
    rr_norm = _normalize(rs_rating_raw)

    scores = []
    for i in range(len(candidates)):
        rs_score = (
            rw["gap"]    * rg_norm[i] +
            rw["slope"]  * rs_norm[i] +
            rw["rating"] * rr_norm[i]
        )
        total = (
            w["ema_tightness"] * t_norm[i] +
            w["duration"]      * d_norm[i] +
            w["volume_trend"]  * v_norm[i] +
            w["bb_intensity"]  * b_norm[i] +
            w["rs_strength"]   * rs_score
        )
        scores.append(round(total * 100, 1))

    return scores