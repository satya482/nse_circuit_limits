"""Consolidation scanner indicators: EMA compression (Sec 2.1), BB/KC squeeze (Sec 2.2),
volume exhaustion (Sec 2.3), RS character (Sec 2.4). Pure functions over OHLCV DataFrames
from ohlc_db.load_ohlc()/load_ohlc_many() (lowercase date/open/high/low/close/volume,
oldest-first, plain 'date' column)."""

import pandas as pd
import numpy as np

EMA_ATR_GATE = 1.5
EMA_PCT_GATE = 0.03
EMA_MIN_BARS = 10

BB_PERIOD = 20
BB_STD = 2.0
KC_PERIOD = 20
KC_ATR_MULT = 1.5
SQUEEZE_MIN_BARS = 5
BB_WIDTH_PCT_MAX = 20.0

VOL_MA_PERIOD = 50
VOL_PCTILE_LOOKBACK = 252

RS_MIN_WEEKS = 14
RS_FLAT_THRESHOLD = 0.01
PRICE_FLAT_THRESHOLD = 0.05


def _ema(series: pd.Series, period: int) -> pd.Series:
    return series.ewm(span=period, adjust=False).mean()


def _atr_sma(high: pd.Series, low: pd.Series, close: pd.Series, period: int) -> pd.Series:
    tr = pd.concat(
        [high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()],
        axis=1,
    ).max(axis=1)
    return tr.rolling(period).mean()


def ema_compression(df: pd.DataFrame) -> pd.DataFrame:
    """Adds ema50/100/200, atr50 (SMA basis, matches TradingView ta.sma(ta.tr) —
    see pine-script-conventions.md), ema_spread, spread_atr_ratio, spread_pct
    (fraction, e.g. 0.03 = 3%, NOT *100), spread_delta (5-bar change in spread_pct)."""
    df = df.copy()
    close = df["close"].astype(float)
    high = df["high"].astype(float)
    low = df["low"].astype(float)

    df["ema50"] = _ema(close, 50)
    df["ema100"] = _ema(close, 100)
    df["ema200"] = _ema(close, 200)
    df["atr50"] = _atr_sma(high, low, close, 50)

    ema_high = df[["ema50", "ema100", "ema200"]].max(axis=1)
    ema_low = df[["ema50", "ema100", "ema200"]].min(axis=1)
    df["ema_spread"] = ema_high - ema_low
    df["spread_atr_ratio"] = df["ema_spread"] / df["atr50"].replace(0, np.nan)
    df["spread_pct"] = df["ema_spread"] / df["ema200"].replace(0, np.nan)
    df["spread_delta"] = df["spread_pct"] - df["spread_pct"].shift(5)
    return df


def compression_duration(df: pd.DataFrame) -> int:
    """Consecutive tail bars where spread_atr_ratio < EMA_ATR_GATE AND spread_pct < EMA_PCT_GATE."""
    ratio = df["spread_atr_ratio"]
    pct = df["spread_pct"]
    count = 0
    for i in range(len(df) - 1, -1, -1):
        r, p = ratio.iloc[i], pct.iloc[i]
        if pd.isna(r) or pd.isna(p) or not (r < EMA_ATR_GATE and p < EMA_PCT_GATE):
            break
        count += 1
    return count


def ema_dual_gate(df: pd.DataFrame) -> tuple[bool, int]:
    duration = compression_duration(df)
    return duration >= EMA_MIN_BARS, duration


def ema_stage(spread_delta: float) -> str:
    """Sec 2.1 stage classification. NaN (insufficient history) treated as converging,
    the conservative default -- a stock with unknown trajectory shouldn't score as imminent."""
    if pd.isna(spread_delta):
        return "STAGE_1_CONVERGING"
    if spread_delta < -0.001:
        return "STAGE_1_CONVERGING"
    if spread_delta > 0.001:
        return "STAGE_3_DIVERGING"
    return "STAGE_2_COMPRESSED"


def bollinger_keltner(df: pd.DataFrame) -> pd.DataFrame:
    """Adds bb_upper/lower/width, bb_width_percentile (true rolling percentile rank,
    252-bar window, 0=tightest-ever), kc_upper/lower, squeeze_on."""
    df = df.copy()
    close = df["close"].astype(float)
    high = df["high"].astype(float)
    low = df["low"].astype(float)

    bb_basis = close.rolling(BB_PERIOD).mean()
    bb_std = close.rolling(BB_PERIOD).std()
    df["bb_upper"] = bb_basis + BB_STD * bb_std
    df["bb_lower"] = bb_basis - BB_STD * bb_std
    df["bb_width"] = df["bb_upper"] - df["bb_lower"]

    lookback = min(252, len(df))
    roll = df["bb_width"].rolling(lookback, min_periods=max(lookback // 2, BB_PERIOD))
    df["bb_width_percentile"] = roll.rank(method='min', pct=True) * 100

    kc_atr = _atr_sma(high, low, close, KC_PERIOD)
    kc_basis = close.rolling(KC_PERIOD).mean()
    df["kc_upper"] = kc_basis + KC_ATR_MULT * kc_atr
    df["kc_lower"] = kc_basis - KC_ATR_MULT * kc_atr

    df["squeeze_on"] = (df["bb_upper"] < df["kc_upper"]) & (df["bb_lower"] > df["kc_lower"])
    return df


def squeeze_gate(df: pd.DataFrame) -> tuple[bool, int]:
    """(passes, squeeze_bars). squeeze_on true >= SQUEEZE_MIN_BARS consecutive tail
    bars AND today's bb_width_percentile <= BB_WIDTH_PCT_MAX."""
    sq = df["squeeze_on"]
    count = 0
    for i in range(len(sq) - 1, -1, -1):
        if bool(sq.iloc[i]):
            count += 1
        else:
            break
    last_pct = df["bb_width_percentile"].iloc[-1]
    width_ok = pd.notna(last_pct) and float(last_pct) <= BB_WIDTH_PCT_MAX
    return count >= SQUEEZE_MIN_BARS and width_ok, count


def volume_exhaustion(df: pd.DataFrame) -> pd.DataFrame:
    """Adds vol_ma50, vol_percentile (true rolling percentile rank of the 5-bar
    average volume, 252-bar window), quiet_accum_bar (Sec 2.3: volume 1.5x+ the
    10-bar average with <1% price move -- volume without price move)."""
    df = df.copy()
    volume = df["volume"].astype(float)
    close = df["close"].astype(float)

    df["vol_ma50"] = volume.rolling(VOL_MA_PERIOD, min_periods=VOL_MA_PERIOD // 2).mean()
    vol5 = volume.rolling(5, min_periods=3).mean()
    lookback = min(VOL_PCTILE_LOOKBACK, len(df))
    df["vol_percentile"] = (
        vol5.rolling(lookback, min_periods=max(lookback // 2, 5)).rank(pct=True) * 100
    )
    df["quiet_accum_bar"] = (
        volume >= 1.5 * volume.rolling(10, min_periods=5).mean()
    ) & ((close / close.shift(1) - 1).abs() < 0.01)
    return df


def volume_declining(df: pd.DataFrame) -> bool:
    """True if the 5-bar average volume today is below its level 5 bars ago."""
    vol5 = df["volume"].astype(float).rolling(5, min_periods=3).mean()
    if len(vol5) < 6 or pd.isna(vol5.iloc[-1]) or pd.isna(vol5.iloc[-6]):
        return False
    return bool(vol5.iloc[-1] < vol5.iloc[-6])


def volume_phase(df: pd.DataFrame) -> str:
    """Sec 2.3 PHASE_A/B/C, informational context (not part of the numeric quality
    score, which uses vol_percentile directly). PHASE_C (multi-month lows) takes
    priority over the A/B declining-volume split."""
    vol_pctile = df["vol_percentile"].iloc[-1]
    if pd.notna(vol_pctile) and float(vol_pctile) <= 20:
        return "PHASE_C"
    last_vol = float(df["volume"].iloc[-1])
    vol_ma50 = df["vol_ma50"].iloc[-1]
    if pd.isna(vol_ma50):
        return "PHASE_A"
    return "PHASE_A" if last_vol > vol_ma50 else "PHASE_B"


def rs_metrics(df: pd.DataFrame, bench_df: pd.DataFrame) -> dict | None:
    """Weekly RS = stock_close / bench_close (Friday close). None if fewer than
    RS_MIN_WEEKS weeks of aligned history. RS_FLAT_THRESHOLD / PRICE_FLAT_THRESHOLD
    are first-pass interpretations of the spec's qualitative 'flat'/'holding'
    language -- unvalidated, Sec 14 backtest territory."""
    close_stock = df.set_index("date")["close"].astype(float)
    close_bench = bench_df.set_index("date")["close"].astype(float)
    rs = (close_stock / close_bench.reindex(close_stock.index).ffill()).dropna()
    rs_weekly = rs.resample("W-FRI").last().dropna()

    if len(rs_weekly) < RS_MIN_WEEKS:
        return None

    rs_ema9 = rs_weekly.ewm(span=9, adjust=False).mean()
    rs_slope = float(rs_weekly.pct_change(4).iloc[-1])
    above_ema = bool(rs_weekly.iloc[-1] > rs_ema9.iloc[-1])

    price_now = float(close_stock.iloc[-1])
    idx_4w = max(0, len(close_stock) - 20)
    price_4w_ago = float(close_stock.iloc[idx_4w])
    price_flat = abs(price_now / price_4w_ago - 1) < PRICE_FLAT_THRESHOLD

    rs_52wk_max = rs_weekly.rolling(52, min_periods=26).max().iloc[-1]
    rs_52wk_high = bool(rs_weekly.iloc[-1] >= rs_52wk_max * 0.999)

    price_20d_max = close_stock.rolling(20, min_periods=10).max().iloc[-1]
    price_20d_high = bool(price_now >= price_20d_max * 0.999)

    return {
        "rs_weekly_last": float(rs_weekly.iloc[-1]),
        "rs_ema9_last": float(rs_ema9.iloc[-1]),
        "rs_slope": rs_slope,
        "above_ema": above_ema,
        "price_flat": price_flat,
        "rs_52wk_high": rs_52wk_high,
        "price_20d_high": price_20d_high,
    }


def classify_rs_character(metrics: dict) -> str:
    """Sec 2.4 CHAR_1..5. Order matters: CHAR_5 (breakout) and CHAR_4 (rising) are
    checked before the flatter CHAR_3/CHAR_1/CHAR_2 fallbacks."""
    rs_slope = metrics["rs_slope"]
    above_ema = metrics["above_ema"]
    price_flat = metrics["price_flat"]

    if metrics["rs_52wk_high"] and price_flat and not metrics["price_20d_high"]:
        return "CHAR_5_RS_BREAKOUT"
    if rs_slope > RS_FLAT_THRESHOLD and price_flat:
        return "CHAR_4_RISING"
    if above_ema and abs(rs_slope) <= RS_FLAT_THRESHOLD:
        return "CHAR_3_HOLDING"
    if not above_ema and rs_slope < -RS_FLAT_THRESHOLD:
        return "CHAR_1_DECLINING"
    return "CHAR_2_FLAT"
