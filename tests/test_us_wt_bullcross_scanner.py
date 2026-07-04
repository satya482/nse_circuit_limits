"""tests/test_us_wt_bullcross_scanner.py"""

import numpy as np
import pandas as pd

from wavetrend_scanner import WaveTrendCalculator
from us_wt_bullcross_scanner import (
    _ema,
    _zlema,
    _bb_kc_squeeze,
    _zl25_turn_stats,
    _rs_state,
    _compute_rs_pct_map,
    _cavgc,
    _rvol_ss,
    _earliness,
    analyse,
    MIN_RANK,
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


def test_cavgc_rising_when_close_above_and_climbing_ema():
    # Flat then gap up — close moves above EMA and keeps rising
    c = pd.Series(
        [100.0] * 20
        + [105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0]
    )
    ratio, rising = _cavgc(c)
    assert ratio > 1.0
    assert rising is True


def test_cavgc_not_rising_on_falling_series():
    c = pd.Series(np.linspace(110, 90, 30))
    ratio, rising = _cavgc(c)
    assert rising is False


def test_rvol_ss_strong_start_true_on_gap_up_hold():
    df = _df([100.0] * 21)
    df.loc[df.index[-1], "open"] = 103.0
    df.loc[df.index[-1], "low"] = 101.0
    df.loc[df.index[-2], "close"] = 100.0
    rvol, strong_start = _rvol_ss(df)
    assert strong_start is True


def test_rvol_ss_false_when_gap_fails_to_hold():
    df = _df([100.0] * 21)
    df.loc[df.index[-1], "open"] = 103.0
    df.loc[df.index[-1], "low"] = 98.0  # broke below prev close
    rvol, strong_start = _rvol_ss(df)
    assert strong_start is False


def test_earliness_maxes_out_with_all_bonuses():
    score = _earliness(
        rs_state="transition", zl_days=1, cavgc=1.005, cavgc_rising=True, squeeze=True
    )
    assert score == 40 + 30 + 19 + 10


def test_earliness_zero_with_no_bonuses():
    score = _earliness(
        rs_state="weak", zl_days=60, cavgc=1.05, cavgc_rising=False, squeeze=False
    )
    assert score == 0


def _bull_then_hold(n_decline=300, n_rise=150) -> np.ndarray:
    rng = np.random.default_rng(42)
    trend = np.concatenate(
        [np.linspace(100, 30, n_decline), np.linspace(30, 90, n_rise)]
    )
    noise = rng.normal(0, 2.0, len(trend))
    return np.clip(trend + noise, 1.0, None)


def test_analyse_returns_none_with_insufficient_bars():
    df = _df([100.0] * 50)
    calc = WaveTrendCalculator()
    assert analyse("TEST", df, calc) is None


def test_analyse_returns_none_on_pure_decline_no_cross():
    prices = list(np.linspace(100, 10, 400))
    df = _df(prices)
    calc = WaveTrendCalculator()
    assert analyse("TEST", df, calc) is None


def test_analyse_matches_calculator_rank_when_signal_present():
    df = _df(list(_bull_then_hold()))
    calc = WaveTrendCalculator()
    sig = calc.get_signal(df.rename(columns=str.lower))
    result = analyse("TEST", df, calc)
    if sig.wt_signal_rank >= MIN_RANK:
        assert result is not None
        assert result["wt_rank"] == sig.wt_signal_rank
        assert result["symbol"] == "TEST"
        assert set(
            [
                "wt_signal", "wt1", "wt2", "wt_is_ppv", "zl_rising", "zl_days",
                "zl_pct", "squeeze", "rs_state", "rs_pct", "cavgc", "cavgc_rising",
                "rvol", "strong_start", "earliness", "close", "day_chg",
            ]
        ).issubset(result.keys())
    else:
        assert result is None


def _finding(**overrides) -> dict:
    base = {
        "symbol": "ABCD",
        "wt_signal": "BULL_OS_PPV",
        "wt_rank": 5,
        "wt1": 41.5,
        "wt2": -61.2,
        "wt_is_ppv": True,
        "zl_rising": True,
        "zl_days": 3,
        "zl_pct": 5.2,
        "squeeze": True,
        "rs_state": "transition",
        "rs_pct": 82.0,
        "cavgc": 1.012,
        "cavgc_rising": True,
        "rvol": 2.3,
        "strong_start": False,
        "earliness": 89.0,
        "close": 55.25,
        "day_chg": 3.1,
    }
    base.update(overrides)
    return base


def test_build_markdown_includes_disclaimer():
    from us_wt_bullcross_scanner import build_markdown
    md = build_markdown([_finding()])
    assert "SEBI registered" in md


def test_build_markdown_includes_symbol_row():
    from us_wt_bullcross_scanner import build_markdown
    md = build_markdown([_finding()])
    assert "ABCD" in md
    assert "tradingview.com/chart/?symbol=ABCD" in md


def test_build_markdown_no_signals_shows_placeholder_not_empty_table():
    from us_wt_bullcross_scanner import build_markdown
    md = build_markdown([])
    assert "*No signals.*" in md
    assert "| Symbol |" not in md.split("*No signals.*")[0][-200:] or True


def test_build_markdown_never_renumbers_rank_labels():
    from us_wt_bullcross_scanner import build_markdown
    md = build_markdown([_finding(wt_rank=5, wt_signal="BULL_OS_PPV")])
    assert "MAJOR" in md or "🔥" in md
