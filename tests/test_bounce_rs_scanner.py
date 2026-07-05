import sys
from datetime import date
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from scanners.bounce_rs_scanner import find_dip_bounce, rs_and_ema_check, detect_setup, composite_score  # noqa: E402


def _breadth_df(dates: list[str], ratios: list[float], eligible: list[int] = None) -> pd.DataFrame:
    n = len(dates)
    if eligible is None:
        eligible = [2000] * n
    return pd.DataFrame({"date": dates, "ratio_5d": ratios, "total_eligible": eligible})


def test_no_bounce_returns_empty():
    """ratio_5d is currently IN dip (not bouncing) -> None."""
    dates = ["2026-06-01", "2026-06-02", "2026-06-03"]
    ratios = [0.90, 0.60, 0.55]  # still in dip on as_of
    result = find_dip_bounce(_breadth_df(dates, ratios), date(2026, 6, 3))
    assert result is None


def test_dip_bounce_detected():
    """2-bar dip block below 0.70, then today bounces >= 0.05 above dip low."""
    dates = ["2026-06-01", "2026-06-02", "2026-06-03", "2026-06-04"]
    ratios = [0.90, 0.60, 0.55, 0.85]  # dip=[0.60,0.55] low=0.55, today 0.85 (>0.70) -> bounce 0.30
    result = find_dip_bounce(_breadth_df(dates, ratios), date(2026, 6, 4))
    assert result == {
        "dip_start": "2026-06-02",
        "dip_end": "2026-06-03",
        "dip_low_ratio": 0.55,
        "ratio_5d_now": 0.85,
        "bounce_mag": 0.3,
    }


def test_broken_breadth_row_handled():
    """Row with total_eligible=10 (known-broken) must not corrupt dip detection."""
    dates = ["2026-06-01", "2026-06-02", "2026-06-03", "2026-06-04", "2026-06-05"]
    ratios = [0.90, 0.60, 0.55, 0.20, 0.85]
    eligible = [2000, 2000, 2000, 10, 2000]  # 06-04 is the broken row
    result = find_dip_bounce(_breadth_df(dates, ratios, eligible), date(2026, 6, 5))
    # broken row dropped entirely -> remaining sequence is 0.90, 0.60, 0.55, 0.85
    # dip block = [0.60, 0.55], today 0.85 (>0.70), bounce 0.30
    assert result["dip_start"] == "2026-06-02"
    assert result["dip_end"] == "2026-06-03"
    assert result["bounce_mag"] == 0.3


def _ohlc(dates: list[str], closes: list[float], ema_buffer: float = 1.0) -> pd.DataFrame:
    """Synthetic OHLC. ema_buffer > 1.0 pads high/low so EMA break checks are exact."""
    n = len(dates)
    return pd.DataFrame({
        "date": pd.to_datetime(dates),
        "open": closes,
        "high": [c * ema_buffer for c in closes],
        "low": [c / ema_buffer for c in closes],
        "close": closes,
        "volume": [1_000_000] * n,
    })


def test_rs_filter_removes_underperformer():
    """Stock fell MORE than benchmark during dip -> excluded (None)."""
    dates = [f"2026-05-{d:02d}" for d in range(1, 11)]
    stock = _ohlc(dates, [100, 99, 98, 97, 96, 95, 94, 93, 92, 91])  # -9%
    bench = _ohlc(dates, [100, 99, 98, 97, 96, 96, 96, 96, 96, 97])  # -3%
    result = rs_and_ema_check(stock, bench, "2026-05-06", "2026-05-10")
    assert result is None


def test_ema_type_a_held_above_throughout():
    """Stock outperforms benchmark and never closes below EMA20 during dip -> Type A."""
    dates = [f"2026-05-{d:02d}" for d in range(1, 21)]
    # Flat-ish uptrend so close stays comfortably above its own EMA20 throughout.
    closes = [100 + i * 0.5 for i in range(20)]
    stock = _ohlc(dates, closes)
    bench = _ohlc(dates, [100 - i * 0.3 for i in range(20)])  # benchmark falling
    result = rs_and_ema_check(stock, bench, dates[15], dates[19])
    assert result is not None
    rs_pct, ema_type = result
    assert rs_pct > 0
    assert ema_type == "A"


def test_ema_type_b_reclaimed():
    """Stock dips below EMA20 at some point during dip window, but closes above EMA20
    on the latest bar -> Type B. Stock also outperforms benchmark (positive RS)."""
    dates = [f"2026-04-{d:02d}" for d in range(1, 31)] + [f"2026-05-{d:02d}" for d in range(1, 26)]
    # Strong uptrend baseline (100 to 120), then pullback during dip window.
    # In uptrend, EMA20 > EMA50, so a pullback can dip below EMA20 but stay above EMA50.
    stock_closes = [100 + i * 0.4 for i in range(50)] + [120, 117, 116, 117, 120]
    bench_closes = [100 + i * 0.2 for i in range(50)] + [118, 115, 114, 114, 114]

    stock = _ohlc(dates, stock_closes)
    bench = _ohlc(dates, bench_closes)

    # dip window is dates[50:55] = "2026-05-21" to "2026-05-25" (indices 50-54)
    result = rs_and_ema_check(stock, bench, dates[50], dates[54])
    assert result is not None
    rs_pct, ema_type = result
    assert rs_pct > 0
    assert ema_type == "B"


def test_ema_type_c_excluded():
    """Stock breaks below EMA50 at some point during dip -> excluded (None),
    even though it still outperforms the benchmark on raw RS (bench falls harder,
    so this isolates the EMA50-break check from the RS check)."""
    dates = [f"2026-05-{d:02d}" for d in range(1, 21)]
    closes = [100] * 15 + [80, 79, 78, 77, 76]  # sharp drop breaks EMA50 in the dip window
    stock = _ohlc(dates, closes)
    bench = _ohlc(dates, [100 - i * 3 for i in range(20)])  # bench falls much harder -> RS still positive
    result = rs_and_ema_check(stock, bench, dates[15], dates[19])
    assert result is None


def test_pocket_pivot_detection():
    """Today's volume exceeds every down-day volume in the prior 10 bars,
    and close is at/above EMA10*0.99 -> POCKET_PIVOT."""
    dates = [f"2026-05-{d:02d}" for d in range(1, 14)]
    closes = [100, 101, 99, 102, 98, 103, 97, 104, 96, 105, 95, 106, 107]
    volumes = [1_000_000] * 12 + [5_000_000]  # today's volume dwarfs every prior down-day
    df = pd.DataFrame({
        "date": pd.to_datetime(dates),
        "open": closes,
        "high": [c * 1.01 for c in closes],
        "low": [c * 0.99 for c in closes],
        "close": closes,
        "volume": volumes,
    })
    setup, score = detect_setup(df)
    assert setup == "POCKET_PIVOT"
    assert score == 3


def test_score_ordering():
    """Highest RS + Type A + Pocket Pivot ranks above a lower combo."""
    strong = composite_score(rs_pct=8.0, ema_type="A", bounce_mag=0.10, setup_score=3)
    weak = composite_score(rs_pct=1.0, ema_type="B", bounce_mag=0.05, setup_score=0)
    assert strong > weak


def test_score_caps_rs_and_bounce():
    """RS component caps at 10, bounce component caps at 5."""
    capped = composite_score(rs_pct=50.0, ema_type="A", bounce_mag=10.0, setup_score=0)
    assert capped == 10.0 + 3.0 + 5.0 + 0


from scanners.bounce_rs_scanner import run, OUTPUT_COLUMNS  # noqa: E402


def _universe_df(symbols: list[str]) -> pd.DataFrame:
    return pd.DataFrame({"symbol": symbols})


def test_run_regime_guard_returns_empty(tmp_path, monkeypatch):
    """No valid dip-bounce window as_of -> empty DataFrame with correct columns."""
    csv_path = tmp_path / "breadth_history.csv"
    dates = ["2026-06-01", "2026-06-02", "2026-06-03"]
    _breadth_df(dates, [0.90, 0.85, 0.88]).assign(universe_tag="breadth_broad").to_csv(
        csv_path, index=False
    )
    universe_df = _universe_df(["AA"])
    result = run(universe_df, date(2026, 6, 3), breadth_csv_path=csv_path)
    assert list(result.columns) == OUTPUT_COLUMNS
    assert len(result) == 0


def test_detect_setup_remaining_branches():
    """Table-driven test for NONE, INSIDE_BAR, NR7, NR7_IB branches.

    NONE: today's range > all prior 6, and not inside yesterday.
    INSIDE_BAR: today inside yesterday, but range not smallest of 7.
    NR7: today's range is smallest of 7, but not inside yesterday.
    NR7_IB: today's range is smallest of 7, and inside yesterday.

    Base pattern: mixed up/down days (no extreme volume spike) to avoid
    accidentally triggering POCKET_PIVOT. All volumes = 1M, so today_vol > max_down_vol
    is false (max_down_vol = 1M, today_vol = 1M).
    """
    # Base: 13 bars with mixed up/down closes (steady range 2.0), all volumes 1M
    base_dates = [f"2026-05-{d:02d}" for d in range(1, 14)]
    base_closes = [100, 102, 101, 103, 100, 104, 98, 105, 96, 106, 95, 107, 100]
    base_highs = [100 + 1.0, 102 + 1.0, 101 + 1.0, 103 + 1.0, 100 + 1.0, 104 + 1.0,
                  98 + 1.0, 105 + 1.0, 96 + 1.0, 106 + 1.0, 95 + 1.0, 107 + 1.0, 100 + 1.0]
    base_lows = [100 - 1.0, 102 - 1.0, 101 - 1.0, 103 - 1.0, 100 - 1.0, 104 - 1.0,
                 98 - 1.0, 105 - 1.0, 96 - 1.0, 106 - 1.0, 95 - 1.0, 107 - 1.0, 100 - 1.0]

    test_cases = [
        (
            "NONE",
            # yesterday (idx 13): high=107.5, low=105, range=2.5
            # today (idx 14): high=109, low=106, range=3 (NOT smallest, NOT inside)
            # Ranges of indices 8-13: [2, 2, 2, 2, 2, 2.5]
            # 3 > 2.5, so not NR7. high 109 > 107.5, so not inside.
            pd.DataFrame({
                "date": pd.to_datetime(base_dates + ["2026-05-14", "2026-05-15"]),
                "open": base_closes + [106.5, 107.5],
                "high": base_highs + [107.5, 109.0],
                "low": base_lows + [105.0, 106.0],
                "close": base_closes + [106.5, 107.5],
                "volume": [1_000_000] * 15,
            }),
            "NONE",
            0,
        ),
        (
            "INSIDE_BAR",
            # yesterday (idx 13): high=108.5, low=104.5, range=4
            # today (idx 14): high=108, low=105, range=3
            # Is inside: 108 < 108.5 and 105 > 104.5? Yes.
            # Ranges of indices 8-13: [2, 2, 2, 2, 2, 4]
            # 3 > 2 (not <= all), so not NR7. Is inside, so INSIDE_BAR.
            pd.DataFrame({
                "date": pd.to_datetime(base_dates + ["2026-05-14", "2026-05-15"]),
                "open": base_closes + [106.5, 106.5],
                "high": base_highs + [108.5, 108.0],
                "low": base_lows + [104.5, 105.0],
                "close": base_closes + [106.5, 106.5],
                "volume": [1_000_000] * 15,
            }),
            "INSIDE_BAR",
            1,
        ),
        (
            "NR7",
            # yesterday (idx 13): high=107.5, low=105.5, range=2
            # today (idx 14): high=107.6, low=106.1, range=1.5
            # Is inside: 107.6 < 107.5? No, so not inside.
            # Ranges of indices 8-13: [2, 2, 2, 2, 2, 2]
            # 1.5 <= 2 (all), so is NR7. Not inside, so NR7.
            pd.DataFrame({
                "date": pd.to_datetime(base_dates + ["2026-05-14", "2026-05-15"]),
                "open": base_closes + [106.5, 106.85],
                "high": base_highs + [107.5, 107.6],
                "low": base_lows + [105.5, 106.1],
                "close": base_closes + [106.5, 106.85],
                "volume": [1_000_000] * 15,
            }),
            "NR7",
            2,
        ),
        (
            "NR7_IB",
            # yesterday (idx 13): high=107.5, low=105.5, range=2
            # today (idx 14): high=107.4, low=105.6, range=1.8
            # Is inside: 107.4 < 107.5 and 105.6 > 105.5? Yes.
            # Ranges of indices 8-13: [2, 2, 2, 2, 2, 2]
            # 1.8 <= 2 (all), so is NR7. Is inside, so NR7_IB.
            pd.DataFrame({
                "date": pd.to_datetime(base_dates + ["2026-05-14", "2026-05-15"]),
                "open": base_closes + [106.5, 106.5],
                "high": base_highs + [107.5, 107.4],
                "low": base_lows + [105.5, 105.6],
                "close": base_closes + [106.5, 106.5],
                "volume": [1_000_000] * 15,
            }),
            "NR7_IB",
            3,
        ),
    ]

    for name, df, expected_setup, expected_score in test_cases:
        setup, score = detect_setup(df)
        assert setup == expected_setup, f"{name}: expected setup={expected_setup}, got {setup}"
        assert score == expected_score, f"{name}: expected score={expected_score}, got {score}"


def test_run_end_to_end_smoke(tmp_path, monkeypatch):
    """Wiring smoke test: one qualifying stock flows through all 3 layers into output."""
    csv_path = tmp_path / "breadth_history.csv"
    dates = ["2026-06-01", "2026-06-02", "2026-06-03", "2026-06-04"]
    _breadth_df(dates, [0.90, 0.60, 0.55, 0.85]).assign(
        universe_tag="breadth_broad", total_eligible=2000
    ).to_csv(csv_path, index=False)

    # 66 bars of history before the 4 breadth dates -> 70 total, clears MIN_BARS=60
    long_dates = pd.date_range("2026-03-01", periods=66).strftime("%Y-%m-%d").tolist() + dates
    aa_closes = [100 + i * 0.3 for i in range(len(long_dates))]  # steady uptrend, outperforms bench
    bench_closes = [100 - i * 0.1 for i in range(len(long_dates))]

    aa_df = _ohlc(long_dates, aa_closes)
    aa_df.loc[aa_df.index[-1], "volume"] = 9_000_000  # trigger pocket pivot on last bar
    bench_df = _ohlc(long_dates, bench_closes)

    def fake_load_ohlc(symbol, lookback=260, db_path=None):
        return aa_df if symbol == "AA" else None

    def fake_load_ohlc_many(symbols, lookback=260, db_path=None):
        return {"NIFTY MIDSML 400": bench_df}

    monkeypatch.setattr("scanners.bounce_rs_scanner.ohlc_db.load_ohlc", fake_load_ohlc)
    monkeypatch.setattr("scanners.bounce_rs_scanner.ohlc_db.load_ohlc_many", fake_load_ohlc_many)

    universe_df = _universe_df(["AA"])
    result = run(universe_df, date(2026, 6, 4), breadth_csv_path=csv_path)

    assert list(result.columns) == OUTPUT_COLUMNS
    assert len(result) == 1
    assert result.iloc[0]["symbol"] == "AA"
    assert result.iloc[0]["ema_type"] == "A"
