"""Unit tests for _rs_highline_cross signal function."""

import pandas as pd
import pytest
from rs_highline_scanner import _rs_highline_cross


def _df(closes: list[float], highs: list[float] | None = None) -> pd.DataFrame:
    """Build a 12-bar DataFrame. closes/highs define the LAST len(closes) bars; earlier bars are filled with closes[0]."""
    target = 12
    pad = target - len(closes)
    c = [closes[0]] * pad + list(closes)
    h = None
    if highs is not None:
        h = [highs[0]] * pad + list(highs)
    n = len(c)
    dates = pd.date_range("2024-01-01", periods=n, freq="B")
    return pd.DataFrame(
        {
            "date": dates,
            "open": c,
            "high": h if h is not None else [x * 1.02 for x in c],
            "low": [x * 0.98 for x in c],
            "close": c,
            "volume": [1_000_000] * n,
        }
    )


def _bench(n: int, val: float = 100.0) -> pd.Series:
    """Build a bench Series covering the same 12-bar date range as _df."""
    dates = pd.date_range("2024-01-01", periods=max(n, 12), freq="B")
    return pd.Series([val] * max(n, 12), index=dates)


def test_basic_crossover():
    """close[-1] crosses above high of last RS-down bar → signal=True."""
    # RS line (bench flat=100): [900,850,920,880,1050]
    # RS declining at i=3 (880<920) → latestRsHigh = high[3] = 92
    # close[-2]=88 ≤ 92, close[-1]=105 > 92 → signal=True
    closes = [90.0, 85.0, 92.0, 88.0, 105.0]
    highs = [92.0, 88.0, 95.0, 92.0, 108.0]
    signal, rs_high, pct = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is True
    assert rs_high == 92.0
    assert pct > 0


def test_today_rs_down_no_signal():
    """If today is the RS-down bar, latestRsHigh = today's high → close>high impossible."""
    # RS: [900,850,920,880,800] — declining today (i=4: 800<880)
    # latestRsHigh = high[4] = 85, close[-1]=80 → 80>85 is False
    closes = [90.0, 85.0, 92.0, 88.0, 80.0]
    highs = [92.0, 88.0, 95.0, 92.0, 85.0]
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
    highs = [92.0, 88.0, 95.0, 98.0, 108.0]
    signal, _, _ = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is False


def test_insufficient_data():
    """Fewer than 10 valid bench bars → (False, nan, nan)."""
    import math
    import pandas as pd

    # 5-bar bench — below valid.sum() < 10 threshold
    closes = [100.0, 101.0, 102.0, 103.0, 104.0]
    dates = pd.date_range("2024-01-01", periods=5, freq="B")
    df5 = pd.DataFrame(
        {
            "date": dates,
            "open": closes,
            "high": [c * 1.02 for c in closes],
            "low": [c * 0.98 for c in closes],
            "close": closes,
            "volume": [1_000_000] * 5,
        }
    )
    bench5 = pd.Series([100.0] * 5, index=dates)
    signal, rs_high, pct = _rs_highline_cross(df5, bench5)
    assert signal is False
    assert math.isnan(rs_high)


def test_pct_above_positive_on_signal():
    """pct_above is positive when signal fires (close > rs_high)."""
    closes = [90.0, 85.0, 92.0, 88.0, 105.0]
    highs = [92.0, 88.0, 95.0, 92.0, 108.0]
    signal, rs_high, pct = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is True
    assert pct == round((105.0 / 92.0 - 1) * 100, 2)
