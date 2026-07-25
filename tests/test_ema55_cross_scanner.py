import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))

import ema25_zl_scanner as base
from ema55_cross_scanner import ema55_cross_stats, ema55_trend_age


def test_cross_up_detected_at_correct_age():
    # close crosses above ema on the 3rd-from-last bar -> age 3
    close = pd.Series([10, 10, 10, 10, 9, 11, 12, 13])
    ema = pd.Series([10, 10, 10, 10, 10, 10, 10, 10])
    days, pct = ema55_cross_stats(close, ema)
    assert days == 3
    assert pct == round((13 / 9 - 1) * 100, 2)


def test_no_cross_within_cap_returns_cap_sentinel():
    # always above ema, never crosses -> capped age, pct measured from cap bar
    close = pd.Series([20.0] * 70)
    ema = pd.Series([10.0] * 70)
    days, pct = ema55_cross_stats(close, ema)
    assert days == 60
    assert pct == 0.0


def test_trend_age_diverges_from_cross_age_on_a_whipsaw():
    # long steady uptrend interrupted by one sharp one-day dip below EMA55,
    # then resumes: cross age should reset low (fresh recross) but the
    # 5-bar-smoothed trend age should stay high (still an established
    # uptrend) -- proves trend age isn't just a copy of cross age (a raw
    # per-bar EMA slope-turn always equals the crossover, see
    # ema55_cross_stats docstring).
    close = pd.Series([100.0 + i for i in range(100)])
    close.iloc[-3] -= 40
    close.iloc[-2] = close.iloc[-4] + 1
    close.iloc[-1] = close.iloc[-2] + 1
    ema55 = base.ema(close, 55)

    cross_days, _ = ema55_cross_stats(close, ema55)
    trend_days, _ = ema55_trend_age(ema55, close)

    assert cross_days <= 3
    assert trend_days > cross_days


if __name__ == "__main__":
    test_cross_up_detected_at_correct_age()
    test_no_cross_within_cap_returns_cap_sentinel()
    test_trend_age_diverges_from_cross_age_on_a_whipsaw()
    print("ok")
