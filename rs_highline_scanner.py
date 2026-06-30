#!/usr/bin/env python3
"""
NSE RS High-Line Cross Scanner
Fires when close crosses above the high of the last bar where RS line was declining.
RS line = (close / NIFTY MIDSML 400 close) * 1000  — mirrors Pine Script latestRsHigh logic.
Run after 4:05 PM IST on trading days (after run_fetch_data.ps1).
"""

import sys
import os
import csv
import json
from math import nan, isnan
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc_many, get_names, liq_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR  = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "rs_highline_scans")
_LABELS_FILE = os.path.join(REPO_DIR, "tools", "stock_labels.json")
_LABELS: dict = (
    json.loads(open(_LABELS_FILE, encoding="utf-8").read())
    if os.path.exists(_LABELS_FILE)
    else {}
)
TODAY     = datetime.now().strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "rs_highline_latest.md")
MD_DATED  = os.path.join(SCANS_DIR, f"rs_highline_{TODAY}.md")

MC_LOW      = 8_000 * 1_00_00_000        # 8B INR = 800 Cr
MC_HIGH     = 5_00_000 * 1_00_00_000     # 5T INR = 5 lakh Cr
ATR_PCT_MIN = 3.0                         # ATR(14)/close*100 must exceed this
BENCH_SYM   = "NIFTY MIDSML 400"
ZL_TURN_CAP = 60


# ── Indicators ────────────────────────────────────────────────────────────────

def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def _zlema(s: pd.Series, n: int) -> pd.Series:
    e = _ema(s, n)
    return 2 * e - _ema(e, n)


def _atr_wilder(df: pd.DataFrame, period: int = 14) -> pd.Series:
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    c = df["close"].astype(float)
    tr = pd.concat(
        [h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1
    ).max(axis=1)
    return tr.ewm(span=period, adjust=False).mean()


def _atr_pct(df: pd.DataFrame, period: int = 14) -> float:
    """ATR(period, Wilder EWM) / close[-1] * 100."""
    if len(df) < period + 1:
        return 0.0
    atr = _atr_wilder(df, period)
    close = float(df["close"].iloc[-1])
    if close == 0:
        return 0.0
    return float(atr.iloc[-1] / close * 100)


def _bb_kc_squeeze(df: pd.DataFrame) -> bool:
    """True if BB(20,2.0,SMA) is fully inside KC(20,1.5,SMA ATR) on the last bar."""
    if len(df) < 21:
        return False
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    bb_basis = c.rolling(20).mean()
    bb_std   = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std
    tr       = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(axis=1)
    kc_atr   = tr.rolling(20).mean()
    kc_basis = c.rolling(20).mean()
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr
    return bool(bb_upper.iloc[-1] < kc_upper.iloc[-1] and bb_lower.iloc[-1] > kc_lower.iloc[-1])


def _zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n     = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i + 1
            pct  = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


def _rs_state(df: pd.DataFrame, bench: pd.Series | None) -> str:
    """Returns 'transition' (weak→strong flip today), 'strong', or 'weak'."""
    if bench is None or len(bench) < 11:
        return "weak"
    try:
        stock_close = df.set_index("date")["close"].astype(float)
        b           = bench.reindex(stock_close.index)
        valid       = b.notna()
        if valid.sum() < 11:
            return "weak"
        rs      = (stock_close[valid] / b[valid]) * 1000
        rs_ema9 = rs.ewm(span=9, adjust=False).mean()
        now_strong = bool(rs.iloc[-1] > rs_ema9.iloc[-1])
        was_weak   = bool(rs.iloc[-2] < rs_ema9.iloc[-2])
        if was_weak and now_strong:
            return "transition"
        return "strong" if now_strong else "weak"
    except Exception:
        return "weak"


def _cavgc(c: pd.Series, length: int = 10) -> tuple[float, bool]:
    avg   = c.ewm(span=length, adjust=False).mean()
    ratio = c / avg
    if pd.isna(ratio.iloc[-1]):
        return 1.0, False
    return float(ratio.iloc[-1]), bool(ratio.iloc[-1] > ratio.iloc[-2])


def _earliness(rs_state: str, zl_days: int, cavgc: float, cavgc_rising: bool, squeeze: bool) -> float:
    score = 0.0
    if squeeze:
        score += 40
    if rs_state == "transition":
        score += 30
    score += max(0, 20 - zl_days)
    if cavgc_rising and 1.0 < cavgc < 1.015:
        score += 10
    elif cavgc_rising and cavgc < 1.03:
        score += 5
    return round(score, 1)


# ── Core signal ───────────────────────────────────────────────────────────────

def _rs_highline_cross(
    df: pd.DataFrame,
    bench: pd.Series,
) -> tuple[bool, float, float]:
    """
    (signal, latest_rs_high_price, pct_above_rs_high)

    latestRsHigh = high of most recent bar where RS line was declining.
    signal = close[-1] crossed above latestRsHigh (Pine ta.crossover equivalent).
    pct_above: positive when close is above the RS-high level.
    Returns (False, nan, nan) on insufficient data.
    """
    if len(df) < 3:
        return False, nan, nan

    stock_close   = df.set_index("date")["close"].astype(float)
    bench_aligned = bench.reindex(stock_close.index)
    valid         = bench_aligned.notna()
    if valid.sum() < 3:
        return False, nan, nan

    rs_line = (stock_close[valid] / bench_aligned[valid]) * 1000
    highs   = df.set_index("date")["high"].astype(float).reindex(rs_line.index)

    # Scan backwards for most recent RS-declining bar
    latest_rs_high = nan
    for i in range(len(rs_line) - 1, 0, -1):
        if rs_line.iloc[i] < rs_line.iloc[i - 1]:
            latest_rs_high = float(highs.iloc[i])
            break

    if isnan(latest_rs_high):
        return False, nan, nan

    c_today = float(stock_close.iloc[-1])
    c_prev  = float(stock_close.iloc[-2])
    crossed  = c_today > latest_rs_high and c_prev <= latest_rs_high
    pct_above = (c_today / latest_rs_high - 1) * 100
    return crossed, round(latest_rs_high, 2), round(pct_above, 2)
