#!/usr/bin/env python3
"""Technical indicator calculations for EMA compression + BB squeeze scanner."""

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


def bollinger_keltner(
    df: pd.DataFrame,
    bb_period: int,
    bb_std_dev: float,
    kc_period: int,
    kc_atr_mult: float,
) -> pd.DataFrame:
    """
    Add BB and KC columns plus squeeze signal.

    Columns added:
        bb_upper, bb_lower, bb_width, bb_width_pct_rank (0-100, lower = tighter)
        kc_upper, kc_lower
        squeeze_on (bool): BB fully inside KC
    """
    df = df.copy()
    close = df["close"].astype(float)
    high  = df["high"].astype(float)
    low   = df["low"].astype(float)

    # Bollinger Bands: SMA basis, rolling std (TradingView default)
    bb_basis = close.rolling(bb_period).mean()
    bb_std   = close.rolling(bb_period).std()
    df["bb_upper"] = bb_basis + bb_std_dev * bb_std
    df["bb_lower"] = bb_basis - bb_std_dev * bb_std
    df["bb_width"] = df["bb_upper"] - df["bb_lower"]

    # BB width percentile rank over trailing 252 bars (0 = tightest, 100 = widest)
    lookback = min(252, len(df))
    bb_roll  = df["bb_width"].rolling(lookback, min_periods=max(lookback // 2, bb_period))
    bb_min   = bb_roll.min()
    bb_max   = bb_roll.max()
    width_range = (bb_max - bb_min).replace(0, float("nan"))
    df["bb_width_pct_rank"] = (df["bb_width"] - bb_min) / width_range * 100

    # Keltner Channels: SMA basis, Wilder ATR
    kc_basis = close.rolling(kc_period).mean()
    kc_atr   = _atr(high, low, close, kc_period)
    df["kc_upper"] = kc_basis + kc_atr_mult * kc_atr
    df["kc_lower"] = kc_basis - kc_atr_mult * kc_atr

    # Squeeze: BB fully inside KC
    df["squeeze_on"] = (df["bb_upper"] < df["kc_upper"]) & (df["bb_lower"] > df["kc_lower"])

    return df


def squeeze_stats(df: pd.DataFrame, squeeze_min_bars: int, bb_width_pct_max: float) -> tuple[bool, int]:
    """
    Returns (squeeze_active, squeeze_days).
    squeeze_days: consecutive tail bars where squeeze_on is True.
    squeeze_active: True if squeeze_days >= min_bars AND bb_width_pct_rank <= pct_max.
    """
    if "squeeze_on" not in df.columns:
        return False, 0

    count = 0
    sq = df["squeeze_on"]
    for i in range(len(sq) - 1, -1, -1):
        if bool(sq.iloc[i]):
            count += 1
        else:
            break

    last_pct_rank = df["bb_width_pct_rank"].iloc[-1] if "bb_width_pct_rank" in df.columns else 100.0
    width_ok = pd.notna(last_pct_rank) and float(last_pct_rank) <= bb_width_pct_max
    return count >= squeeze_min_bars and width_ok, count


def rs_line(
    stock_df: pd.DataFrame,
    benchmark_df: pd.DataFrame,
    rs_ema_period: int,
    slope_lookback_weeks: int,
) -> tuple[bool, bool, float, float]:
    """
    Compute weekly RS line (stock / NiftyMidSml400) and directionality.

    Returns (rs_above_ema, rs_slope_positive, rs_gap, rs_slope).
        rs_gap:   (rs_weekly[-1] - rs_ema9[-1]) / rs_ema9[-1]  — normalized
        rs_slope: rs_weekly.diff(slope_lookback_weeks).iloc[-1]
    """
    close_stock = stock_df.set_index("date")["close"].astype(float)
    close_bench = benchmark_df.set_index("date")["close"].astype(float)

    # Align on stock dates, forward-fill any benchmark gaps
    rs = close_stock / close_bench.reindex(close_stock.index).ffill()
    rs = rs.dropna()

    min_bars = (rs_ema_period + slope_lookback_weeks) * 5 + 10
    if len(rs) < min_bars:
        return False, False, 0.0, 0.0

    # Resample to weekly (Friday close)
    rs_weekly = rs.resample("W").last().dropna()

    if len(rs_weekly) < rs_ema_period + slope_lookback_weeks + 1:
        return False, False, 0.0, 0.0

    rs_ema = rs_weekly.ewm(span=rs_ema_period, adjust=False).mean()

    current_rs  = float(rs_weekly.iloc[-1])
    current_ema = float(rs_ema.iloc[-1])
    rs_gap      = (current_rs - current_ema) / current_ema if current_ema != 0 else 0.0
    rs_slope    = float(rs_weekly.diff(slope_lookback_weeks).iloc[-1])

    return current_rs > current_ema, rs_slope > 0, rs_gap, rs_slope


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

    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl.iloc[i] > zl.iloc[i - 1] and zl.iloc[i - 1] <= zl.iloc[i - 2]:
            bars_ago = (n - 1) - i
            chg = round((close.iloc[-1] / close.iloc[i] - 1) * 100, 2)
            return zl_rising, bars_ago, chg

    cap_idx = max(0, n - ZL_TURN_CAP - 1)
    chg = round((close.iloc[-1] / close.iloc[cap_idx] - 1) * 100, 2)
    return zl_rising, ZL_TURN_CAP, chg