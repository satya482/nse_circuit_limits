import pandas as pd
from zscore_meanreversion_scanner import zscore, zscore_zone_days


def test_zscore_matches_pine_formula():
    # 55 flat bars at 100, then a sharp drop that should read close to a real z-score.
    closes = [100.0] * 55 + [80.0]
    s = pd.Series(closes)
    z = zscore(s, len=55)
    # sma of last 55 bars ending at the new bar = mean(54 x 100, 1 x 80) != 100
    sma = s.rolling(55, min_periods=55).mean().iloc[-1]
    sd = s.rolling(55, min_periods=55).std().iloc[-1]
    expected = (80.0 - sma) / sd
    assert abs(z.iloc[-1] - expected) < 1e-9
    assert pd.isna(z.iloc[53])  # not enough bars yet (need 55)


def test_zscore_zone_days_counts_consecutive_extreme_bars():
    # z-series: 3 bars at z=-3.5 (extreme), then not extreme before that
    z = pd.Series([-1.0, -1.0, -3.5, -3.2, -3.1])
    days, turning_up = zscore_zone_days(z, threshold=-3.0, cap=60)
    assert days == 3
    # -3.5 -> -3.2 -> -3.1 is rising each bar
    assert turning_up is True


def test_zscore_zone_days_not_turning_up_when_still_falling():
    z = pd.Series([-1.0, -3.0, -3.5, -4.0])
    days, turning_up = zscore_zone_days(z, threshold=-3.0, cap=60)
    assert days == 3
    assert turning_up is False


def test_zscore_zone_days_zero_when_not_currently_extreme():
    z = pd.Series([-3.5, -3.2, -1.0])
    days, turning_up = zscore_zone_days(z, threshold=-3.0, cap=60)
    assert days == 0
    assert turning_up is False
