"""Unit tests for _rs_highline_cross signal function."""
import pandas as pd
import pytest
from rs_highline_scanner import _rs_highline_cross


def _df(closes: list[float], highs: list[float] | None = None) -> pd.DataFrame:
    n = len(closes)
    dates = pd.date_range("2024-01-01", periods=n, freq="B")
    return pd.DataFrame({
        "date":   dates,
        "open":   closes,
        "high":   highs if highs else [c * 1.02 for c in closes],
        "low":    [c * 0.98 for c in closes],
        "close":  closes,
        "volume": [1_000_000] * n,
    })


def _bench(n: int, val: float = 100.0) -> pd.Series:
    dates = pd.date_range("2024-01-01", periods=n, freq="B")
    return pd.Series([val] * n, index=dates)


def test_basic_crossover():
    """close[-1] crosses above high of last RS-down bar → signal=True."""
    # RS line (bench flat=100): [900,850,920,880,1050]
    # RS declining at i=3 (880<920) → latestRsHigh = high[3] = 92
    # close[-2]=88 ≤ 92, close[-1]=105 > 92 → signal=True
    closes = [90.0, 85.0, 92.0, 88.0, 105.0]
    highs  = [92.0, 88.0, 95.0, 92.0, 108.0]
    signal, rs_high, pct = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is True
    assert rs_high == 92.0
    assert pct > 0


def test_today_rs_down_no_signal():
    """If today is the RS-down bar, latestRsHigh = today's high → close>high impossible."""
    # RS: [900,850,920,880,800] — declining today (i=4: 800<880)
    # latestRsHigh = high[4] = 85, close[-1]=80 → 80>85 is False
    closes = [90.0, 85.0, 92.0, 88.0, 80.0]
    highs  = [92.0, 88.0, 95.0, 92.0, 85.0]
    signal, _, _ = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is False


def test_no_rs_down_bars():
    """RS always rising → no latestRsHigh → no signal."""
    closes = [80.0, 85.0, 90.0, 95.0, 100.0]
    signal, rs_high, _ = _rs_highline_cross(_df(closes), _bench(5))
    assert signal is False
    import math
    assert math.isnan(rs_high)


def test_prev_close_already_above_no_signal():
    """Crossover only fires on the exact cross bar — prev_close must be ≤ rs_high."""
    # RS declining at i=1 → latestRsHigh = high[1] = 88
    # close[-2]=96 > 88, so crossover already happened before → no signal
    closes = [90.0, 85.0, 92.0, 96.0, 105.0]
    highs  = [92.0, 88.0, 95.0, 98.0, 108.0]
    signal, _, _ = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is False


def test_insufficient_data():
    """Fewer than 10 valid bench bars → (False, nan, nan)."""
    import math
    closes = [100.0, 101.0]
    signal, rs_high, pct = _rs_highline_cross(_df(closes), _bench(2))
    assert signal is False
    assert math.isnan(rs_high)


def test_pct_above_positive_on_signal():
    """pct_above is positive when signal fires (close > rs_high)."""
    closes = [90.0, 85.0, 92.0, 88.0, 105.0]
    highs  = [92.0, 88.0, 95.0, 92.0, 108.0]
    signal, rs_high, pct = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is True
    assert pct == round((105.0 / 92.0 - 1) * 100, 2)
