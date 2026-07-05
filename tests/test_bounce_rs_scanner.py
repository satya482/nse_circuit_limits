import sys
from datetime import date
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from scanners.bounce_rs_scanner import find_dip_bounce, rs_and_ema_check  # noqa: E402


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
