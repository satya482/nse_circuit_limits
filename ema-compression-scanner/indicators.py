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