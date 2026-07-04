#!/usr/bin/env python3
"""
US WaveTrend Bull Cross Scanner
Run after the existing US data pipeline (fetch_us_data.py @ 4:40 PM IST,
us_zl_squeeze_scanner.py @ 4:50 PM IST) — this scanner runs last, ~5:00 PM IST.

Universe: NYSE + NASDAQ common equity, MCap $300M-$10B, price > $5,
          avg 10d vol > 300K (matches fetch_us_data.py's backfill universe exactly —
          lookups miss for any symbol outside this range).
          No RS filter — WT captures oversold reversals before RS turns positive.

Signal hierarchy (wt_signal_rank) — external contract, never renumbered:
  +5  BULL_OS_PPV    - deep oversold cross + Pocket Pivot Volume [strongest]
  +4  BULL_ANY_PPV   - any cross + Pocket Pivot Volume
  +3  BULL_OVERSOLD  - deep oversold cross (wt2 <= -60)
  +2  BULL_OS_L2     - soft oversold cross (wt2 <= -53)
  +1  BULL_ANY_MID   - mid-range cross (WT2 > -53, no PPV)

Output: us_wt_scans/us_wt_bullcross_latest.md
        us_wt_scans/us_wt_bullcross_YYYY-MM-DD.md
        us_wt_scans/us_wt_bullcross_dashboard.html
"""

import sys
import os
from datetime import datetime, timezone, timedelta

import pandas as pd
from tradingview_screener import Query, col

from us_ohlc_db import load_ohlc_many
from wavetrend_scanner import WaveTrendCalculator
from disclaimer import (
    SEBI_MD_HEADER,
    SEBI_MD_FOOTER,
    SEBI_HTML_BANNER,
    SEBI_HTML_FOOTER,
)

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "us_wt_scans")
IST = timezone(timedelta(hours=5, minutes=30))
TODAY = datetime.now(IST).strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "us_wt_bullcross_latest.md")
MD_DATED = os.path.join(SCANS_DIR, f"us_wt_bullcross_{TODAY}.md")
HTML_DASHBOARD = os.path.join(SCANS_DIR, "us_wt_bullcross_dashboard.html")

MC_LOW = 300_000_000  # $300M
MC_HIGH = 10_000_000_000  # $10B
MIN_RANK = 1
ZL_TURN_CAP = 60
BENCH_SYM = "SPY"
RS_SCALE = 100  # matches us_zl_squeeze_scanner.py convention (not NSE's x1000)
RVOL_FLAG = 8.0
SS_LOWMULT = 0.995


# -- Indicators ---------------------------------------------------------------


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


def _zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i + 1
            pct = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


def _rs_state(df: pd.DataFrame, bench_series: pd.Series | None) -> str:
    """Returns 'transition' (weak->strong flip today), 'strong', or 'weak'."""
    if bench_series is None or len(bench_series) < 11:
        return "weak"
    try:
        stock_close = df.set_index("date")["close"].astype(float)
        bench = bench_series.reindex(stock_close.index)
        valid = bench.notna()
        if valid.sum() < 11:
            return "weak"
        rs = (stock_close[valid] / bench[valid]) * RS_SCALE
        rs_ema9 = rs.ewm(span=9, adjust=False).mean()
        now_strong = bool(rs.iloc[-1] > rs_ema9.iloc[-1])
        was_weak = bool(rs.iloc[-2] < rs_ema9.iloc[-2])
        if was_weak and now_strong:
            return "transition"
        return "strong" if now_strong else "weak"
    except Exception:
        return "weak"


def _compute_rs_pct_map(all_data: dict, bench_series: pd.Series) -> dict[str, float]:
    """IBD-style RS percentile rank vs SPY. RS line = (close/SPY_close)*RS_SCALE;
    weighted 3m/6m/9m/12m return. Scale cancels out in the ratio, so RS_SCALE
    doesn't affect the resulting percentiles."""
    WINDOWS = [63, 126, 189, 252]
    WEIGHTS = [0.4, 0.2, 0.2, 0.2]
    scores: dict[str, float] = {}
    for sym, df in all_data.items():
        if df is None or len(df) < 253:
            continue
        try:
            stock_c = df.set_index("date")["close"].astype(float)
            bench = bench_series.reindex(stock_c.index)
            valid = bench.notna()
            if valid.sum() < 253:
                continue
            rs_line = (stock_c[valid] / bench[valid]) * RS_SCALE
            score = sum(
                wt * (rs_line.iloc[-1] / rs_line.iloc[-w] - 1)
                for w, wt in zip(WINDOWS, WEIGHTS)
                if len(rs_line) >= w + 1
            )
            scores[sym] = score
        except Exception:
            continue
    if not scores:
        return {}
    s = pd.Series(scores)
    pct = s.rank(pct=True) * 100
    return pct.round(1).to_dict()
