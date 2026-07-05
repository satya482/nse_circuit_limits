import sys
from datetime import date
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from scanners.bounce_rs_scanner import find_dip_bounce


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
