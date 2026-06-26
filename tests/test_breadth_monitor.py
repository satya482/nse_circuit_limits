import pandas as pd
import pytest
import tempfile
import os

# Insert project root into path so imports work from tests/
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.refresh_breadth_universe import filter_instruments
from scanners.breadth_monitor import update_breadth_history, _CSV_COLUMNS


def test_filter_keeps_nse_eq_no_dash():
    raw = pd.DataFrame(
        [
            {
                "exchange": "NSE",
                "segment": "NSE",
                "instrument_type": "EQ",
                "tradingsymbol": "SBIN",
                "instrument_token": 1,
                "name": "State Bank",
            },
            {
                "exchange": "NSE",
                "segment": "NSE",
                "instrument_type": "EQ",
                "tradingsymbol": "SBIN-BE",
                "instrument_token": 2,
                "name": "SBI BE",
            },
            {
                "exchange": "NSE",
                "segment": "INDICES",
                "instrument_type": "INDICES",
                "tradingsymbol": "NIFTY 50",
                "instrument_token": 3,
                "name": "Nifty",
            },
            {
                "exchange": "BSE",
                "segment": "BSE",
                "instrument_type": "EQ",
                "tradingsymbol": "SBIN",
                "instrument_token": 4,
                "name": "SBI BSE",
            },
            {
                "exchange": "NSE",
                "segment": "NSE",
                "instrument_type": "EQ",
                "tradingsymbol": "XYZ-SM",
                "instrument_token": 5,
                "name": "SME stock",
            },
        ]
    )
    result = filter_instruments(raw)
    assert list(result["symbol"]) == ["SBIN"]
    assert "instrument_token" in result.columns
    assert "generated_date" in result.columns


# ── compute_daily_breadth tests ───────────────────────────────────────────────

from datetime import date, timezone, timedelta  # noqa: E402
from scanners.breadth_monitor import compute_daily_breadth  # noqa: E402

IST = timezone(timedelta(hours=5, minutes=30))


def _make_ohlc(
    dates: list[str], closes: list[float], volumes: list[float] = None
) -> pd.DataFrame:
    """Build synthetic OHLC DataFrame matching ohlc_db.load_ohlc_many output format."""
    n = len(dates)
    if volumes is None:
        volumes = [1_000_000] * n
    return pd.DataFrame(
        {
            "date": pd.to_datetime(dates),
            "open": closes,
            "high": [c * 1.01 for c in closes],
            "low": [c * 0.99 for c in closes],
            "close": closes,
            "volume": volumes,
        }
    )


def _universe_df(symbols: list[str]) -> pd.DataFrame:
    return pd.DataFrame({"symbol": symbols})


# ── up4 / down4 counting ──────────────────────────────────────────────────────


def test_up4_count_basic():
    """Stock up 5% on as_of → counted in up4_count."""
    dates = ["2026-06-20", "2026-06-21"]
    ohlc_map = {
        "AA": _make_ohlc(dates, [100.0, 105.0]),  # +5% → up4
        "BB": _make_ohlc(dates, [100.0, 102.0]),  # +2% → not up4
    }
    result = compute_daily_breadth(
        _universe_df(["AA", "BB"]), date(2026, 6, 21), ohlc_map
    )
    assert result["up4_count"] == 1
    assert result["down4_count"] == 0
    assert result["total_eligible"] == 2


def test_down4_count_basic():
    """Stock down 5% on as_of → counted in down4_count."""
    dates = ["2026-06-20", "2026-06-21"]
    ohlc_map = {
        "AA": _make_ohlc(dates, [100.0, 94.0]),  # -6% → down4
        "BB": _make_ohlc(dates, [100.0, 98.0]),  # -2% → not down4
    }
    result = compute_daily_breadth(
        _universe_df(["AA", "BB"]), date(2026, 6, 21), ohlc_map
    )
    assert result["down4_count"] == 1
    assert result["up4_count"] == 0


def test_circuit_frozen_excluded():
    """Stock with close==prev_close and volume==0 excluded from counts and total_eligible."""
    dates = ["2026-06-20", "2026-06-21"]
    ohlc_map = {
        "AA": _make_ohlc(
            dates, [100.0, 100.0], [1_000_000, 0]
        ),  # frozen: volume=0, price unchanged
        "BB": _make_ohlc(dates, [100.0, 105.0]),  # normal +5%
    }
    result = compute_daily_breadth(
        _universe_df(["AA", "BB"]), date(2026, 6, 21), ohlc_map
    )
    assert result["total_eligible"] == 1  # AA excluded
    assert result["up4_count"] == 1  # BB counted


def test_same_price_nonzero_volume_not_frozen():
    """Stock with same close but nonzero volume is NOT circuit-frozen — count it."""
    dates = ["2026-06-20", "2026-06-21"]
    ohlc_map = {
        "AA": _make_ohlc(
            dates, [100.0, 100.0], [1_000_000, 500_000]
        ),  # same price, has volume
    }
    result = compute_daily_breadth(_universe_df(["AA"]), date(2026, 6, 21), ohlc_map)
    assert result["total_eligible"] == 1


def test_as_of_bounds_future_data():
    """Stock with data beyond as_of must not be used — as_of row is last allowed."""
    dates = ["2026-06-19", "2026-06-20", "2026-06-21"]
    # as_of = 2026-06-20; row at 2026-06-21 is future and must be ignored
    ohlc_map = {
        "AA": _make_ohlc(
            dates, [100.0, 105.0, 90.0]
        ),  # 90 is future, must not affect result
    }
    result = compute_daily_breadth(_universe_df(["AA"]), date(2026, 6, 20), ohlc_map)
    # pct_1d at 2026-06-20 = 105/100 - 1 = 5% → up4
    assert result["up4_count"] == 1


def test_stock_with_no_as_of_row_skipped():
    """Stock whose last row is before as_of → function returns None (not a trading day)."""
    ohlc_map = {
        "AA": _make_ohlc(["2026-06-18", "2026-06-19"], [100.0, 102.0]),
    }
    result = compute_daily_breadth(_universe_df(["AA"]), date(2026, 6, 21), ohlc_map)
    assert result is None


# ── ratio_5d / ratio_10d ──────────────────────────────────────────────────────


def test_ratio_5d():
    """ratio_5d = sum(up4 last 5 days) / max(1, sum(down4 last 5 days))."""
    # Build 11 days: last 5 have 3 up4-days and 1 down4-day
    dates = [f"2026-06-{i:02d}" for i in range(11, 22)]  # 2026-06-11 to 2026-06-21
    # Alternate: day 17,18,19 up4; day 20 down4; day 21 flat
    closes = [
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        105.0,  # day 17: +5% → up4
        110.25,  # day 18: +5% → up4
        115.76,  # day 19: +5% → up4
        109.97,  # day 20: -5% → down4
        110.0,  # day 21: +0.02% → flat
    ]
    ohlc_map = {"AA": _make_ohlc(dates, closes)}
    result = compute_daily_breadth(_universe_df(["AA"]), date(2026, 6, 21), ohlc_map)
    # Last 5 days (17,18,19,20,21): up4=3, down4=1 → ratio = 3/1 = 3.0
    assert result["ratio_5d"] == pytest.approx(3.0, abs=0.01)


def test_ratio_divide_by_zero_guard():
    """When down4_count=0 for the window, denominator uses max(1,...) → no ZeroDivisionError."""
    dates = [f"2026-06-{i:02d}" for i in range(11, 22)]
    closes = [100.0 * (1.05**i) for i in range(11)]  # every day up 5%
    ohlc_map = {"AA": _make_ohlc(dates, closes)}
    result = compute_daily_breadth(_universe_df(["AA"]), date(2026, 6, 21), ohlc_map)
    assert result["ratio_5d"] is not None
    assert result["ratio_5d"] > 0


# ── pct_63d / up25_quarter ────────────────────────────────────────────────────


def test_up25_quarter_counted():
    """Stock up >=25% over 63 days → counted in up25_quarter."""
    import numpy as np

    closes_arr = [100.0] + list(np.linspace(100.0, 130.0, 63))
    d_list = (
        pd.date_range("2026-04-01", periods=64, freq="B").strftime("%Y-%m-%d").tolist()
    )
    ohlc_map = {"AA": _make_ohlc(d_list, closes_arr)}
    as_of = date.fromisoformat(d_list[-1])
    result = compute_daily_breadth(_universe_df(["AA"]), as_of, ohlc_map)
    assert result["up25_quarter"] == 1
    assert result["down25_quarter"] == 0


def test_up25_quarter_excluded_when_insufficient_history():
    """Stock with <64 bars excluded from up25_quarter but still in total_eligible."""
    dates = (
        pd.date_range("2026-06-01", periods=10, freq="B").strftime("%Y-%m-%d").tolist()
    )
    closes = list(range(100, 110))
    ohlc_map = {"AA": _make_ohlc(dates, closes)}
    as_of = date.fromisoformat(dates[-1])
    result = compute_daily_breadth(_universe_df(["AA"]), as_of, ohlc_map)
    assert result["total_eligible"] == 1  # still counted in denominator
    assert result["up25_quarter"] == 0  # excluded from quarterly calc


# ── pct_above_sma200 ─────────────────────────────────────────────────────────


def test_pct_above_sma200_requires_200_bars():
    """Stock with <200 bars excluded from sma200 count but in total_eligible."""
    dates = (
        pd.date_range("2026-01-01", periods=50, freq="B").strftime("%Y-%m-%d").tolist()
    )
    closes = [100.0] * 50
    ohlc_map = {"AA": _make_ohlc(dates, closes)}
    as_of = date.fromisoformat(dates[-1])
    result = compute_daily_breadth(_universe_df(["AA"]), as_of, ohlc_map)
    assert result["total_eligible"] == 1
    assert result["pct_above_sma200"] is None  # no eligible stocks for sma200


def test_pct_above_sma200_above():
    """Stock with close above its 200-day SMA → counted."""
    dates = (
        pd.date_range("2020-01-01", periods=210, freq="B").strftime("%Y-%m-%d").tolist()
    )
    # Closes: first 200 at 100, last 10 at 120 → sma200 ≈ slightly above 100; close=120 → above
    closes = [100.0] * 200 + [120.0] * 10
    ohlc_map = {"AA": _make_ohlc(dates, closes)}
    as_of = date.fromisoformat(dates[-1])
    result = compute_daily_breadth(_universe_df(["AA"]), as_of, ohlc_map)
    assert result["pct_above_sma200"] == pytest.approx(100.0, abs=0.1)


# ── composite_score always null ───────────────────────────────────────────────


def test_composite_score_is_null():
    dates = ["2026-06-20", "2026-06-21"]
    ohlc_map = {"AA": _make_ohlc(dates, [100.0, 105.0])}
    result = compute_daily_breadth(_universe_df(["AA"]), date(2026, 6, 21), ohlc_map)
    assert result["composite_score"] is None


# ── universe_tag ──────────────────────────────────────────────────────────────


def test_universe_tag_is_breadth_broad():
    dates = ["2026-06-20", "2026-06-21"]
    ohlc_map = {"AA": _make_ohlc(dates, [100.0, 105.0])}
    result = compute_daily_breadth(_universe_df(["AA"]), date(2026, 6, 21), ohlc_map)
    assert result["universe_tag"] == "breadth_broad"


# ── update_breadth_history upsert tests ───────────────────────────────────────


def _sample_row(date_str: str, up4: int = 10, dn4: int = 5) -> dict:
    return {
        "date": date_str,
        "universe_tag": "breadth_broad",
        "total_eligible": 1500,
        "up4_count": up4,
        "down4_count": dn4,
        "ratio_5d": 2.0,
        "ratio_10d": 1.8,
        "up25_quarter": 100,
        "down25_quarter": 50,
        "pct_above_sma200": 55.0,
        "composite_score": None,
    }


def test_upsert_creates_file_on_first_run():
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
        path = f.name
    os.unlink(path)  # ensure file doesn't exist
    try:
        update_breadth_history(path, _sample_row("2026-06-20"))
        df = pd.read_csv(path)
        assert len(df) == 1
        assert df.iloc[0]["date"] == "2026-06-20"
    finally:
        if os.path.exists(path):
            os.unlink(path)


def test_upsert_appends_new_date():
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
        path = f.name
    os.unlink(path)
    try:
        update_breadth_history(path, _sample_row("2026-06-20"))
        update_breadth_history(path, _sample_row("2026-06-21"))
        df = pd.read_csv(path)
        assert len(df) == 2
        assert list(df["date"]) == ["2026-06-20", "2026-06-21"]
    finally:
        if os.path.exists(path):
            os.unlink(path)


def test_upsert_overwrites_existing_date():
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
        path = f.name
    os.unlink(path)
    try:
        update_breadth_history(path, _sample_row("2026-06-20", up4=10))
        update_breadth_history(
            path, _sample_row("2026-06-20", up4=99)
        )  # same date, different value
        df = pd.read_csv(path)
        assert len(df) == 1  # no duplicate
        assert df.iloc[0]["up4_count"] == 99  # updated value
    finally:
        if os.path.exists(path):
            os.unlink(path)


def test_upsert_sorted_by_date():
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
        path = f.name
    os.unlink(path)
    try:
        update_breadth_history(path, _sample_row("2026-06-21"))
        update_breadth_history(
            path, _sample_row("2026-06-20")
        )  # older date inserted second
        df = pd.read_csv(path)
        assert list(df["date"]) == ["2026-06-20", "2026-06-21"]  # always sorted
    finally:
        if os.path.exists(path):
            os.unlink(path)


def test_columns_match_schema():
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
        path = f.name
    os.unlink(path)
    try:
        update_breadth_history(path, _sample_row("2026-06-20"))
        df = pd.read_csv(path)
        assert list(df.columns) == _CSV_COLUMNS
    finally:
        if os.path.exists(path):
            os.unlink(path)
