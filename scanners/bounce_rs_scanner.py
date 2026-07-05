#!/usr/bin/env python3
"""
Bounce-RS Scanner — timing + RS confluence layer.
Identifies NSE stocks with positive RS during a breadth (ratio_5d) dip,
firing a setup trigger as the dip bounces.
Pairs with: scanners/breadth_monitor.py (regime source), no standalone overlay.
Alert message format: N/A -- this module returns a DataFrame, no alerts emitted directly.
"""

from datetime import date
from pathlib import Path

import pandas as pd

import ohlc_db

RATIO_DIP_THRESHOLD = 0.70
MIN_DIP_BARS = 2
BOUNCE_MIN = 0.05
POCKET_PIVOT_LB = 10
NR_PERIOD = 7
MIN_BARS = 60
OHLC_LOOKBACK = 260
BENCH_SYM = "NIFTY MIDSML 400"

DEFAULT_BREADTH_CSV = Path(__file__).parent.parent / "data" / "breadth_history.csv"

OUTPUT_COLUMNS = [
    "symbol", "rs_during_dip_%", "ema_type", "setup",
    "dip_low_ratio", "ratio_5d_now", "bounce_mag", "score",
]


def find_dip_bounce(breadth_df: pd.DataFrame, as_of: date) -> dict | None:
    """Find the most recent dip-then-bounce window ending on as_of.

    Requires the dip block to end on the bar immediately before as_of --
    'bouncing' means just having left the dip, not an arbitrarily stale one.
    """
    df = breadth_df[breadth_df["total_eligible"] >= 100].copy()
    df["date"] = df["date"].astype(str)
    as_of_str = as_of.strftime("%Y-%m-%d")
    df = df[df["date"] <= as_of_str].sort_values("date").reset_index(drop=True)

    if df.empty or df["date"].iloc[-1] != as_of_str:
        return None

    ratios = df["ratio_5d"].tolist()
    dates = df["date"].tolist()
    n = len(ratios)

    current = ratios[-1]
    if pd.isna(current) or current <= RATIO_DIP_THRESHOLD:
        return None  # not bouncing yet

    i = n - 2
    if i < 0 or pd.isna(ratios[i]) or ratios[i] > RATIO_DIP_THRESHOLD:
        return None  # no dip immediately preceding today

    dip_end_idx = i
    dip_start_idx = i
    j = i - 1
    while j >= 0 and not pd.isna(ratios[j]) and ratios[j] <= RATIO_DIP_THRESHOLD:
        dip_start_idx = j
        j -= 1

    dip_len = dip_end_idx - dip_start_idx + 1
    if dip_len < MIN_DIP_BARS:
        return None

    dip_low_ratio = min(ratios[dip_start_idx: dip_end_idx + 1])
    bounce_mag = current - dip_low_ratio
    if bounce_mag < BOUNCE_MIN:
        return None

    return {
        "dip_start": dates[dip_start_idx],
        "dip_end": dates[dip_end_idx],
        "dip_low_ratio": round(dip_low_ratio, 4),
        "ratio_5d_now": round(current, 4),
        "bounce_mag": round(bounce_mag, 4),
    }


def rs_and_ema_check(
    ohlc: pd.DataFrame,
    bench_ohlc: pd.DataFrame,
    dip_start: str,
    dip_end: str,
) -> tuple[float, str] | None:
    """RS filter + EMA20 dip-hold classification (Layer 2).

    Returns (rs_pct, ema_type) with ema_type in {'A','B'}, or None if
    RS_dip <= 0 or the stock broke EMA50 at any point during the dip (Type C).
    """
    dates = ohlc["date"].dt.strftime("%Y-%m-%d")
    window_mask = (dates >= dip_start) & (dates <= dip_end)
    window = ohlc[window_mask]
    if len(window) < 2:
        return None
    stock_return = float(window["close"].iloc[-1]) / float(window["close"].iloc[0]) - 1

    b_dates = bench_ohlc["date"].dt.strftime("%Y-%m-%d")
    b_window = bench_ohlc[(b_dates >= dip_start) & (b_dates <= dip_end)]
    if len(b_window) < 2:
        return None
    bench_return = float(b_window["close"].iloc[-1]) / float(b_window["close"].iloc[0]) - 1

    rs_pct = (stock_return - bench_return) * 100
    if rs_pct <= 0:
        return None

    close = ohlc["close"].astype(float)
    ema20 = close.ewm(span=20, adjust=False).mean()
    ema50 = close.ewm(span=50, adjust=False).mean()

    close_in_dip = close[window_mask]
    ema20_in_dip = ema20[window_mask]
    ema50_in_dip = ema50[window_mask]

    if (close_in_dip < ema50_in_dip).any():
        return None  # Type C: broke EMA50 during dip

    if (close_in_dip > ema20_in_dip).all():
        ema_type = "A"
    elif float(close.iloc[-1]) > float(ema20.iloc[-1]):
        ema_type = "B"
    else:
        return None  # dipped below EMA20, hasn't reclaimed today

    return round(rs_pct, 4), ema_type


def detect_setup(ohlc: pd.DataFrame) -> tuple[str, int]:
    """Layer 3 setup trigger on today's bar. Always returns a pair;
    ('NONE', 0) is a valid result, not an error."""
    if len(ohlc) < POCKET_PIVOT_LB + 2:
        return "NONE", 0

    close = ohlc["close"].astype(float).reset_index(drop=True)
    high = ohlc["high"].astype(float).reset_index(drop=True)
    low = ohlc["low"].astype(float).reset_index(drop=True)
    volume = ohlc["volume"].astype(float).reset_index(drop=True)
    ema10 = close.ewm(span=10, adjust=False).mean()

    n = len(close)
    today_vol = volume.iloc[-1]
    today_close = close.iloc[-1]
    today_high = high.iloc[-1]
    today_low = low.iloc[-1]
    yesterday_high = high.iloc[-2]
    yesterday_low = low.iloc[-2]

    # Down-day volumes in the prior POCKET_PIVOT_LB bars (excluding today)
    prior_closes = close.iloc[n - POCKET_PIVOT_LB - 1: n - 1].reset_index(drop=True)
    prior_prev_closes = close.iloc[n - POCKET_PIVOT_LB - 2: n - 2].reset_index(drop=True)
    prior_vols = volume.iloc[n - POCKET_PIVOT_LB - 1: n - 1].reset_index(drop=True)
    down_mask = prior_closes < prior_prev_closes
    down_vols = prior_vols[down_mask]
    max_down_vol = float(down_vols.max()) if len(down_vols) else 0.0

    is_pocket_pivot = today_vol > max_down_vol and today_close >= ema10.iloc[-1] * 0.99

    today_range = today_high - today_low
    other_ranges = (high - low).iloc[n - NR_PERIOD: n - 1]
    is_nr7 = len(other_ranges) == NR_PERIOD - 1 and (today_range <= other_ranges).all()
    is_inside = today_high < yesterday_high and today_low > yesterday_low

    if is_pocket_pivot:
        return "POCKET_PIVOT", 3
    if is_nr7 and is_inside:
        return "NR7_IB", 3
    if is_nr7:
        return "NR7", 2
    if is_inside:
        return "INSIDE_BAR", 1
    return "NONE", 0
