import pandas as pd

from ohlc_db import cmf_days, cmf_tag


def _synthetic_cross_df() -> pd.DataFrame:
    """6 bars with MFM=-1 (close=low) then 6 bars with MFM=+1 (close=high).
    Constant volume=100 makes CMF(n=5) equal the rolling average of MFM,
    giving a deterministic zero-cross 3 bars before the last bar.
    """
    rows = []
    for _ in range(6):
        rows.append({"open": 100.0, "high": 110.0, "low": 100.0, "close": 100.0, "volume": 100.0})
    for _ in range(6):
        rows.append({"open": 110.0, "high": 110.0, "low": 100.0, "close": 110.0, "volume": 100.0})
    return pd.DataFrame(rows)


def test_cmf_days_detects_zero_cross():
    df = _synthetic_cross_df()
    assert cmf_days(df, n=5, cap=30) == (True, 3)


def test_cmf_tag_formats_marker():
    df = _synthetic_cross_df()
    assert cmf_tag(df, n=5, cap=30) == "↑CMF3d"


def test_cmf_days_zero_range_bar_no_crash():
    rows = [
        {"open": 100.0, "high": 100.0, "low": 100.0, "close": 100.0, "volume": 100.0}
        for _ in range(10)
    ]
    df = pd.DataFrame(rows)
    result = cmf_days(df, n=5, cap=30)
    assert result is not None
    positive, days = result
    assert isinstance(positive, bool)
    assert isinstance(days, int)


def test_cmf_days_insufficient_bars_returns_none():
    rows = [
        {"open": 100.0, "high": 110.0, "low": 100.0, "close": 105.0, "volume": 100.0}
        for _ in range(3)
    ]
    df = pd.DataFrame(rows)
    assert cmf_days(df, n=20, cap=30) is None
    assert cmf_tag(df, n=20, cap=30) == ""


def test_cmf_series_matches_cmf_days_internal_calc():
    """Regression guard for the cmf_days() refactor: cmf_series()'s last value
    must have the same sign cmf_days() would report as cmf_positive."""
    from ohlc_db import cmf_series

    df = _synthetic_cross_df()
    series = cmf_series(df, n=5)
    positive, _ = cmf_days(df, n=5, cap=30)
    assert (series.iloc[-1] > 0) == positive
