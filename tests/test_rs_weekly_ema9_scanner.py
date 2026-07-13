import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rs_weekly_ema9_scanner import weekly_rs_ema9_trend


def _series(n_days: int, start: str, values) -> pd.Series:
    idx = pd.date_range(start, periods=n_days, freq="D")
    return pd.Series(values, index=idx)


def test_rising_rs_gives_positive_slope():
    n = 400
    dates = pd.date_range("2024-01-01", periods=n, freq="D")
    stock = pd.Series([100 + i * 0.5 for i in range(n)], index=dates)  # strong uptrend
    bench = pd.Series([100.0] * n, index=dates)  # flat benchmark
    out = weekly_rs_ema9_trend(stock, bench)
    assert out is not None
    assert out["slope"] > 0
    assert out["rising"] is True
    assert out["age"] > 0  # price steadily above its own lagging EMA9


def test_falling_rs_gives_negative_slope():
    n = 400
    dates = pd.date_range("2024-01-01", periods=n, freq="D")
    stock = pd.Series([200 - i * 0.5 for i in range(n)], index=dates)  # downtrend
    bench = pd.Series([100.0] * n, index=dates)
    out = weekly_rs_ema9_trend(stock, bench)
    assert out is not None
    assert out["slope"] < 0
    assert out["rising"] is False
    assert out["age"] == 0  # price steadily below its own lagging EMA9


def test_insufficient_history_returns_none():
    dates = pd.date_range("2024-01-01", periods=20, freq="D")
    stock = pd.Series([100.0] * 20, index=dates)
    bench = pd.Series([100.0] * 20, index=dates)
    assert weekly_rs_ema9_trend(stock, bench) is None


if __name__ == "__main__":
    test_rising_rs_gives_positive_slope()
    test_falling_rs_gives_negative_slope()
    test_insufficient_history_returns_none()
    print("OK")
