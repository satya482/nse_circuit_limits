"""tests/test_us_wt_bullcross_scanner.py"""
import numpy as np
import pandas as pd
import pytest

from us_wt_bullcross_scanner import (
    _ema,
    _zlema,
    _bb_kc_squeeze,
    _zl25_turn_stats,
    _rs_state,
    _compute_rs_pct_map,
)


def _df(closes: list[float]) -> pd.DataFrame:
    n = len(closes)
    dates = pd.date_range("2024-01-01", periods=n, freq="B")
    c = np.asarray(closes, dtype=float)
    return pd.DataFrame(
        {
            "date": dates,
            "open": c * 0.99,
            "high": c * 1.01,
            "low": c * 0.98,
            "close": c,
            "volume": np.ones(n) * 1_000_000,
        }
    )


def test_ema_matches_pandas_ewm():
    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
    result = _ema(s, 3)
    expected = s.ewm(span=3, adjust=False).mean()
    pd.testing.assert_series_equal(result, expected)


def test_zlema_is_ema_of_double_ema_minus_ema():
    s = pd.Series(np.linspace(10, 20, 30))
    e = s.ewm(span=5, adjust=False).mean()
    expected = 2 * e - e.ewm(span=5, adjust=False).mean()
    result = _zlema(s, 5)
    pd.testing.assert_series_equal(result, expected)


def test_bb_kc_squeeze_false_when_insufficient_bars():
    df = _df([100.0] * 10)
    assert _bb_kc_squeeze(df) is False


def test_bb_kc_squeeze_true_on_flat_low_vol_series():
    # Flat price -> BB std ~0 -> BB fully inside KC -> squeeze True
    df = _df([100.0] * 25)
    assert _bb_kc_squeeze(df) is True


def test_bb_kc_squeeze_false_on_wide_range_series():
    # Large daily swings -> BB wider than KC -> squeeze False
    rng = np.random.default_rng(1)
    closes = 100 + np.cumsum(rng.normal(0, 5, 25))
    df = _df(list(closes))
    assert _bb_kc_squeeze(df) is False


def test_zl25_turn_stats_finds_most_recent_upturn():
    # zl25 falls then turns up exactly 3 bars ago
    zl25 = pd.Series([10, 9, 8, 7, 8, 9, 10])
    closes = pd.Series([100, 98, 96, 94, 96, 98, 101])
    bars, pct = _zl25_turn_stats(zl25, closes)
    assert bars == 3
    assert pct == round((101 / 94 - 1) * 100, 2)


def test_zl25_turn_stats_caps_at_zl_turn_cap():
    # Monotonically falling zl25 -> no upturn found -> capped result
    zl25 = pd.Series(list(range(100, 0, -1)), dtype=float)
    closes = pd.Series(list(range(1, 101)), dtype=float)
    bars, pct = _zl25_turn_stats(zl25, closes)
    assert bars == 60  # ZL_TURN_CAP


def _bench(prices: list[float]) -> pd.Series:
    n = len(prices)
    dates = pd.date_range("2024-01-01", periods=n, freq="B")
    return pd.Series(prices, index=dates)


def test_rs_state_returns_weak_with_no_benchmark():
    df = _df([100.0] * 15)
    assert _rs_state(df, None) == "weak"


def test_rs_state_transition_when_rs_crosses_above_ema9():
    # Stock flat while bench outperforms briefly then crashes -> RS was weak, now strong
    closes = [100.0] * 15
    df = _df(closes)
    bench_prices = [100.0] * 12 + [120.0, 120.0, 80.0]  # bench +20%, then crashes to 80
    bench = _bench(bench_prices)
    state = _rs_state(df, bench)
    assert state == "transition"


def test_rs_state_weak_when_rs_stays_below_ema9():
    closes = [100.0] * 15
    df = _df(closes)
    bench_prices = [100.0] * 13 + [100.0, 120.0]  # bench rallies -> RS drops today
    bench = _bench(bench_prices)
    assert _rs_state(df, bench) == "weak"


def test_compute_rs_pct_map_ranks_higher_relative_return_higher():
    n = 260
    dates = pd.date_range("2023-01-01", periods=n, freq="B")
    bench_close = pd.Series(np.linspace(100, 110, n), index=dates)  # bench +10%
    strong = _df(list(np.linspace(100, 200, n)))  # stock +100%
    strong["date"] = dates
    weak = _df(list(np.linspace(100, 105, n)))  # stock +5%
    weak["date"] = dates
    all_data = {"STRONG": strong, "WEAK": weak}
    pct = _compute_rs_pct_map(all_data, bench_close)
    assert pct["STRONG"] > pct["WEAK"]
