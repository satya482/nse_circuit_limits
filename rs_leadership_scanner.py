#!/usr/bin/env python3
"""
NSE RS Leadership Scanner
Mirrors pine_scripts/Satya RS Relative Leadership.txt: fires when a stock's
Relative Performance % vs NIFTY MIDSML 400 is non-negative AND its EMA is
rising, on the bar these two conditions first align together (combined cross).
Run after 4:05 PM IST on trading days (after run_fetch_data.ps1).
"""

import sys
import os
import json
from math import nan, isnan
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc_many, get_names, liq_tag, cmf_tag, deliv_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "rs_leadership_scans")
_LABELS_FILE = os.path.join(REPO_DIR, "tools", "stock_labels.json")

TODAY = datetime.now().strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "rs_leadership_latest.md")
MD_DATED = os.path.join(SCANS_DIR, f"rs_leadership_{TODAY}.md")

MC_LOW = 8_000 * 1_00_00_000  # 8B INR = 800 Cr
MC_HIGH = 5_00_000 * 1_00_00_000  # 5T INR = 5 lakh Cr
BENCH_SYM = "NIFTY MIDSML 400"

RS_EMA_LONG_LEN = 9
RS_EMA_SHORT_LEN = 5
PERF_LOOKBACK = 9
PERF_SMOOTH = 5


def _load_labels() -> dict:
    if not os.path.exists(_LABELS_FILE):
        return {}
    with open(_LABELS_FILE, encoding="utf-8") as fh:
        return json.loads(fh.read())


_LABELS: dict = _load_labels()


# ── Indicators ────────────────────────────────────────────────────────────────


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def _zlema(s: pd.Series, n: int) -> pd.Series:
    e = _ema(s, n)
    return 2 * e - _ema(e, n)


def _bb_kc_squeeze(df: pd.DataFrame) -> bool:
    """True if BB(20,2.0,SMA) is fully inside KC(20,1.5,SMA ATR) on the last bar."""
    if len(df) < 21:
        return False
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    bb_basis = c.rolling(20).mean()
    bb_std = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std
    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(
        axis=1
    )
    kc_atr = tr.rolling(20).mean()
    kc_basis = c.rolling(20).mean()
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr
    return bool(
        bb_upper.iloc[-1] < kc_upper.iloc[-1] and bb_lower.iloc[-1] > kc_lower.iloc[-1]
    )


# ── Core signal ───────────────────────────────────────────────────────────────


def _rel_perf_series(
    stock_close: pd.Series, bench_close: pd.Series
) -> tuple[pd.Series, pd.Series]:
    """Aligned (rel_perf, rel_perf_ema) over the overlap of the two series."""
    bench_aligned = bench_close.reindex(stock_close.index)
    valid = bench_aligned.notna()
    sc = stock_close[valid]
    bc = bench_aligned[valid]
    stock_ret = sc / sc.shift(PERF_LOOKBACK)
    bench_ret = bc / bc.shift(PERF_LOOKBACK)
    rel_perf = ((stock_ret / bench_ret) - 1) * 100
    rel_perf_ema = rel_perf.ewm(span=PERF_SMOOTH, adjust=False).mean()
    return rel_perf, rel_perf_ema


def _rs_leadership_signal(
    df: pd.DataFrame, bench: pd.Series
) -> tuple[bool, float, float]:
    """
    (signal, rel_perf_today, rel_perf_ema_today)

    signal = combined cross: (rel_perf>=0 AND rel_perf_ema rising) true today,
    NOT both true yesterday. Returns (False, nan, nan) on insufficient data.
    """
    min_bars = PERF_LOOKBACK + PERF_SMOOTH + 3
    if len(df) < min_bars:
        return False, nan, nan

    stock_close = df.set_index("date")["close"].astype(float)
    rel_perf, rel_perf_ema = _rel_perf_series(stock_close, bench)

    valid_count = rel_perf_ema.notna().sum()
    if valid_count < 3:
        return False, nan, nan

    rel_perf = rel_perf.dropna()
    rel_perf_ema = rel_perf_ema.dropna()
    if len(rel_perf) < 2 or len(rel_perf_ema) < 2:
        return False, nan, nan

    perf_positive = rel_perf >= 0
    ema_rising = rel_perf_ema > rel_perf_ema.shift(1)

    if len(ema_rising.dropna()) < 2:
        return False, nan, nan

    combined = perf_positive & ema_rising
    combined = combined.dropna()
    if len(combined) < 2:
        return False, nan, nan

    combined_today = bool(combined.iloc[-1])
    combined_yesterday = bool(combined.iloc[-2])
    signal = combined_today and not combined_yesterday

    return signal, round(float(rel_perf.iloc[-1]), 2), round(float(rel_perf_ema.iloc[-1]), 2)


def _leadership_score(df: pd.DataFrame, bench: pd.Series) -> tuple[int, str]:
    """(score 0-5, rs_state) mirroring the .txt's leadershipScore formula."""
    if len(df) < RS_EMA_LONG_LEN + 3:
        return 0, "weak"

    stock_close = df.set_index("date")["close"].astype(float)
    bench_aligned = bench.reindex(stock_close.index)
    valid = bench_aligned.notna()
    if valid.sum() < RS_EMA_LONG_LEN + 3:
        return 0, "weak"

    sc = stock_close[valid]
    bc = bench_aligned[valid]
    rs_line = (sc / bc) * 1000
    rs_ema_long = _ema(rs_line, RS_EMA_LONG_LEN)
    rs_ema_short = _ema(rs_line, RS_EMA_SHORT_LEN)

    rel_perf, _ = _rel_perf_series(stock_close, bench)
    rel_perf = rel_perf.reindex(rs_line.index)

    rs_above_ema = bool(rs_line.iloc[-1] > rs_ema_long.iloc[-1])
    short_rs_bullish = bool(rs_ema_short.iloc[-1] > rs_ema_long.iloc[-1])
    rs_ema_rising = bool(rs_ema_long.iloc[-1] > rs_ema_long.iloc[-2])
    outperforming = bool(rel_perf.iloc[-1] > 0) if not pd.isna(rel_perf.iloc[-1]) else False
    performance_rising = (
        bool(rel_perf.iloc[-1] > rel_perf.iloc[-2])
        if not pd.isna(rel_perf.iloc[-1]) and not pd.isna(rel_perf.iloc[-2])
        else False
    )

    score = sum(
        [rs_above_ema, short_rs_bullish, rs_ema_rising, outperforming, performance_rising]
    )

    now_strong = rs_above_ema
    was_strong = bool(rs_line.iloc[-2] > rs_ema_long.iloc[-2])
    if now_strong and not was_strong:
        rs_state = "transition"
    elif now_strong:
        rs_state = "strong"
    else:
        rs_state = "weak"

    return score, rs_state
