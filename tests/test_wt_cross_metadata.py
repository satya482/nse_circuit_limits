"""
tests/test_wt_cross_metadata.py
Unit tests for the cross_type/divergence/rs_rising helpers added to
wt_bullcross_scanner.py (concepts adopted from research/wt_cross_metadata_spec.md).
"""

import sys
from pathlib import Path
from datetime import date, timedelta

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))
from wt_bullcross_scanner import _classify_cross_type, _divergence, _rs_rising


def _dates(n: int, start: str = "2020-01-02") -> list[str]:
    d = date.fromisoformat(start)
    out = []
    for _ in range(n):
        while d.weekday() >= 5:
            d += timedelta(days=1)
        out.append(d.isoformat())
        d += timedelta(days=1)
    return out


def test_trap_door_overrides_deep_os():
    # wt2 deep at -70 (would otherwise be PHOENIX) but structural context broken
    wt2 = pd.Series([-20, -70, -70, -70])
    assert _classify_cross_type(wt2, above_ema50=False, rs_rising=False) == "TRAP_DOOR"


def test_grind_shallow_os():
    wt2 = pd.Series([-10, -15, -18, -20])
    assert _classify_cross_type(wt2, above_ema50=True, rs_rising=True) == "GRIND"


def test_phoenix_deep_v_bottom():
    # Sharp drop then cross — wide range in the pre-cross window, deep now
    wt2 = pd.Series([-30, -40, -68, -70])
    assert _classify_cross_type(wt2, above_ema50=True, rs_rising=True) == "PHOENIX"


def test_slingshot_flat_bottom():
    # Sat narrowly in OS for the pre-cross window, not deep enough for Phoenix
    wt2 = pd.Series([-56, -57, -55, -54])
    assert _classify_cross_type(wt2, above_ema50=True, rs_rising=True) == "SLINGSHOT"


def test_divergence_confirmed():
    # Prior trough at position 3 (wt2=-60, low=100); today's low undercuts it
    # while wt2 makes a higher low.
    wt2 = pd.Series([0] * 3 + [-60] + [0] * 6 + [-55])
    low = pd.Series([100] * 3 + [100] + [100] * 6 + [95])
    assert _divergence(wt2, low) is True


def test_divergence_not_confirmed_when_price_holds():
    wt2 = pd.Series([0] * 3 + [-60] + [0] * 6 + [-55])
    low = pd.Series([100] * 3 + [90] + [100] * 6 + [95])  # today's low above trough
    assert _divergence(wt2, low) is False


def test_divergence_false_insufficient_history():
    wt2 = pd.Series([-60, -55])
    low = pd.Series([100, 95])
    assert _divergence(wt2, low) is False


def test_rs_rising_true():
    n = 5
    df = pd.DataFrame({"date": _dates(n), "close": [10, 11, 12, 13, 14.0]})
    bench = pd.Series([100, 100, 100, 100, 100.0], index=pd.to_datetime(_dates(n)))
    assert _rs_rising(df, bench) is True


def test_rs_rising_false_no_bench():
    df = pd.DataFrame({"date": _dates(3), "close": [10, 11, 12.0]})
    assert _rs_rising(df, None) is False
