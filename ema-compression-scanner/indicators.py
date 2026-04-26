#!/usr/bin/env python3
"""Technical indicator calculations for EMA compression scanner."""

import pandas as pd


def _ema(series: pd.Series, period: int) -> pd.Series:
    return series.ewm(span=period, adjust=False).mean()


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int) -> pd.Series:
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    return tr.ewm(span=period, adjust=False).mean()


def compute(df: pd.DataFrame) -> pd.DataFrame:
    """Add EMA50/100/200, ATR50, vol_ma50, ema_spread, spread_atr_ratio, spread_pct."""
    df = df.copy()
    close  = df["close"].astype(float)
    high   = df["high"].astype(float)
    low    = df["low"].astype(float)
    volume = df["volume"].astype(float)

    df["ema50"]  = _ema(close, 50)
    df["ema100"] = _ema(close, 100)
    df["ema200"] = _ema(close, 200)
    df["atr50"]  = _atr(high, low, close, 50)
    df["vol_ma50"] = volume.rolling(50, min_periods=25).mean()

    ema_high = df[["ema50", "ema100", "ema200"]].max(axis=1)
    ema_low  = df[["ema50", "ema100", "ema200"]].min(axis=1)
    df["ema_spread"] = ema_high - ema_low
    df["spread_atr_ratio"] = df["ema_spread"] / df["atr50"].replace(0, float("nan"))
    df["spread_pct"] = df["ema_spread"] / df["ema200"].replace(0, float("nan")) * 100

    return df


ZL_TURN_CAP = 60


def zl25_stats(df: pd.DataFrame) -> tuple[bool, int, float]:
    """
    Returns (zl_rising, zl_days, zl_chg_pct).
    zl_rising: True if ZLEMA25 slope is currently up (last bar > second-to-last).
    zl_days:   Bars since last ZLEMA25 turn-up (capped at ZL_TURN_CAP).
    zl_chg_pct: % price change from the turn-up bar to today.
    """
    close = df["close"].astype(float)
    e25 = close.ewm(span=25, adjust=False).mean()
    zl = 2 * e25 - e25.ewm(span=25, adjust=False).mean()

    n = len(zl)
    if n < 3:
        return False, ZL_TURN_CAP, 0.0

    zl_rising = bool(zl.iloc[-1] > zl.iloc[-2])

    # Walk back to find last turn-up: slope flipped from flat/down → up
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl.iloc[i] > zl.iloc[i - 1] and zl.iloc[i - 1] <= zl.iloc[i - 2]:
            bars_ago = (n - 1) - i
            chg = round((close.iloc[-1] / close.iloc[i] - 1) * 100, 2)
            return zl_rising, bars_ago, chg

    cap_idx = max(0, n - ZL_TURN_CAP - 1)
    chg = round((close.iloc[-1] / close.iloc[cap_idx] - 1) * 100, 2)
    return zl_rising, ZL_TURN_CAP, chg