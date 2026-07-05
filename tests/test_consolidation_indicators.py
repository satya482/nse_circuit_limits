import pandas as pd
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
