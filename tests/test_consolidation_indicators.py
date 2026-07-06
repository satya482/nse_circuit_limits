import pandas as pd
import numpy as np
from consolidation import indicators


def _flat_df(n: int, price: float = 100.0, vol: float = 1_000_000.0) -> pd.DataFrame:
    """n bars, dead-flat OHLCV -- EMAs converge to `price`, spread -> 0."""
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": [price] * n, "high": [price * 1.001] * n,
        "low": [price * 0.999] * n, "close": [price] * n,
        "volume": [vol] * n,
    })


def test_ema_compression_spread_shrinks_as_ramp_flattens_out():
    """A dead-flat series has spread=0 at every bar (nothing to shrink from) --
    to observe convergence, start with a ramp that leaves EMAs spread apart,
    then flatten and watch the spread decay toward zero."""
    n = 300
    prices = [50.0 + i * 2.0 for i in range(50)] + [150.0] * (n - 50)
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": prices, "high": [p * 1.01 for p in prices],
        "low": [p * 0.99 for p in prices], "close": prices,
        "volume": [1_000_000.0] * n,
    })
    df = indicators.ema_compression(df)
    assert df["ema_spread"].iloc[-1] < df["ema_spread"].iloc[60]
    assert df["spread_pct"].iloc[-1] < df["spread_pct"].iloc[60]


def test_compression_duration_counts_consecutive_tail_bars():
    df = indicators.ema_compression(_flat_df(300))
    duration = indicators.compression_duration(df)
    assert duration > indicators.EMA_MIN_BARS


def test_ema_dual_gate_passes_on_long_flat_series():
    df = indicators.ema_compression(_flat_df(300))
    passes, duration = indicators.ema_dual_gate(df)
    assert passes is True
    assert duration >= indicators.EMA_MIN_BARS


def test_ema_dual_gate_fails_on_trending_series():
    n = 300
    prices = [100.0 + i * 0.5 for i in range(n)]  # steadily trending, never compresses
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": prices, "high": [p * 1.02 for p in prices],
        "low": [p * 0.98 for p in prices], "close": prices,
        "volume": [1_000_000.0] * n,
    })
    df = indicators.ema_compression(df)
    passes, _ = indicators.ema_dual_gate(df)
    assert passes is False


def test_ema_stage_classification():
    assert indicators.ema_stage(-0.01) == "STAGE_1_CONVERGING"
    assert indicators.ema_stage(0.0) == "STAGE_2_COMPRESSED"
    assert indicators.ema_stage(0.0005) == "STAGE_2_COMPRESSED"
    assert indicators.ema_stage(0.01) == "STAGE_3_DIVERGING"
    assert indicators.ema_stage(float("nan")) == "STAGE_1_CONVERGING"


def test_bollinger_keltner_flat_series_is_squeezed():
    df = indicators.bollinger_keltner(_flat_df(300))
    assert bool(df["squeeze_on"].iloc[-1]) is True
    assert df["bb_width_percentile"].iloc[-1] <= indicators.BB_WIDTH_PCT_MAX


def test_squeeze_gate_passes_on_flat_series():
    df = indicators.bollinger_keltner(_flat_df(300))
    passes, days = indicators.squeeze_gate(df)
    assert passes is True
    assert days >= 5


def test_squeeze_gate_fails_on_trending_series():
    """A steady linear ramp with near-zero daily range: BB width scales with the
    *dispersion of closes across the window* (wide, for a ramp spanning a large
    range), while KC width scales with *daily bar range* (narrow, since each
    day's own high-low is tiny) -- BB ends up well outside KC, squeeze off.
    (Alternating chop was tried first but widens ATR by the same reversal gap
    that widens BB, so BB stays inside KC -- that's not a valid counter-example.)"""
    n = 300
    prices = [100.0 + i * 1.0 for i in range(n)]
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": prices, "high": [p + 0.01 for p in prices],
        "low": [p - 0.01 for p in prices], "close": prices,
        "volume": [1_000_000.0] * n,
    })
    df = indicators.bollinger_keltner(df)
    passes, _ = indicators.squeeze_gate(df)
    assert passes is False


def _bench_series(n: int, val: float = 100.0, start: str = "2024-01-01") -> pd.DataFrame:
    """start MUST match the stock df's start date -- rs_metrics() aligns on
    the 'date' column, and misaligned date ranges give a fully-empty aligned
    series (rs_metrics correctly returns None on that, it isn't a bug)."""
    return pd.DataFrame({
        "date": pd.date_range(start, periods=n, freq="B"),
        "open": [val] * n, "high": [val] * n, "low": [val] * n,
        "close": [val] * n, "volume": [1_000_000.0] * n,
    })


def test_volume_exhaustion_declining_volume_low_percentile():
    n = 300
    # elevated volume for first 100 bars, then steadily declining to multi-month lows
    vol = [3_000_000.0] * 100 + list(np.linspace(3_000_000.0, 200_000.0, n - 100))
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": [100.0] * n, "high": [101.0] * n, "low": [99.0] * n,
        "close": [100.0] * n, "volume": vol,
    })
    result = indicators.volume_exhaustion(df)
    assert result["vol_percentile"].iloc[-1] < 20


def test_volume_phase_c_on_multi_month_lows():
    n = 300
    vol = [3_000_000.0] * 100 + list(np.linspace(3_000_000.0, 200_000.0, n - 100))
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": [100.0] * n, "high": [101.0] * n, "low": [99.0] * n,
        "close": [100.0] * n, "volume": vol,
    })
    df = indicators.volume_exhaustion(df)
    assert indicators.volume_phase(df) == "PHASE_C"


def test_quiet_accum_bar_flags_high_volume_flat_price():
    n = 60
    close = [100.0] * (n - 1) + [100.3]  # <1% move on the last bar
    vol = [1_000_000.0] * (n - 1) + [2_000_000.0]  # 2x the 10-bar average
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": close, "high": [c * 1.005 for c in close],
        "low": [c * 0.995 for c in close], "close": close, "volume": vol,
    })
    result = indicators.volume_exhaustion(df)
    assert bool(result["quiet_accum_bar"].iloc[-1]) is True


def test_rs_metrics_none_on_insufficient_history():
    stock = _bench_series(30, 100.0)
    bench = _bench_series(30, 100.0)
    assert indicators.rs_metrics(stock, bench) is None


def test_rs_metrics_char_1_declining_when_rs_falls_below_ema():
    n = 260  # ~52 weeks
    stock_close = [100.0] * 200 + list(np.linspace(100.0, 70.0, n - 200))  # stock falling vs flat bench
    stock = pd.DataFrame({
        "date": pd.date_range("2023-01-02", periods=n, freq="B"),
        "open": stock_close, "high": [c * 1.01 for c in stock_close],
        "low": [c * 0.99 for c in stock_close], "close": stock_close,
        "volume": [1_000_000.0] * n,
    })
    bench = _bench_series(n, 100.0, start="2023-01-02")  # must match stock's date range
    metrics = indicators.rs_metrics(stock, bench)
    assert metrics is not None
    assert indicators.classify_rs_character(metrics) == "CHAR_1_DECLINING"


def test_rs_metrics_char_4_rising_when_rs_climbs_price_flat():
    """Stock price stays perfectly flat while the BENCHMARK declines -- RS =
    stock/bench rises even though the stock itself never moves (the 'quiet
    accumulation' case: price flat, RS grinding up). A rising stock price
    instead (tried first) also trips price_20d_high and pushes rs_slope just
    under RS_FLAT_THRESHOLD -- not a clean CHAR_4 case."""
    n = 260
    stock_close = [100.0] * n
    stock = pd.DataFrame({
        "date": pd.date_range("2023-01-02", periods=n, freq="B"),
        "open": stock_close, "high": [c * 1.01 for c in stock_close],
        "low": [c * 0.99 for c in stock_close], "close": stock_close,
        "volume": [1_000_000.0] * n,
    })
    bench_close = [100.0] * 200 + list(np.linspace(100.0, 90.0, n - 200))
    bench = pd.DataFrame({
        "date": pd.date_range("2023-01-02", periods=n, freq="B"),
        "open": bench_close, "high": bench_close, "low": bench_close,
        "close": bench_close, "volume": [1_000_000.0] * n,
    })
    metrics = indicators.rs_metrics(stock, bench)
    assert metrics is not None
    assert indicators.classify_rs_character(metrics) == "CHAR_4_RISING"
