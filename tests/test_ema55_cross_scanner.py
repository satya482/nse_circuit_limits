import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))

from ema55_cross_scanner import ema55_cross_stats


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


if __name__ == "__main__":
    test_cross_up_detected_at_correct_age()
    test_no_cross_within_cap_returns_cap_sentinel()
    print("ok")
