import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))

from near_52w_high_scanner import (
    high52w_stats,
    is_new_high,
    passes_gate,
    bucket_for,
    build_markdown,
    BAND_PCT,
)


def test_high52w_stats_uses_rolling_max_of_high_not_close():
    high = pd.Series([10, 20, 15, 12, 11])
    close = pd.Series([9, 18, 14, 11, 10])
    high_52w, pct = high52w_stats(high, close, period=5)
    assert high_52w == 20
    assert pct == (10 - 20) / 20 * 100


def test_high52w_stats_pct_is_zero_on_new_high_day():
    high = pd.Series([10, 12, 15])
    close = pd.Series([10, 12, 15])
    high_52w, pct = high52w_stats(high, close, period=3)
    assert high_52w == 15
    assert pct == 0.0


def test_is_new_high_true_within_epsilon_of_zero():
    assert is_new_high(0.0) is True
    assert is_new_high(-0.005) is True


def test_is_new_high_false_below_epsilon():
    assert is_new_high(-0.5) is False
    assert is_new_high(-30.0) is False


def test_passes_gate_true_within_band_and_above_ema200():
    assert passes_gate(pct_from_high=-15.0, close=100.0, ema200=90.0) is True


def test_passes_gate_false_outside_band():
    assert passes_gate(pct_from_high=-31.0, close=100.0, ema200=90.0) is False


def test_passes_gate_false_below_ema200():
    assert passes_gate(pct_from_high=-5.0, close=100.0, ema200=101.0) is False


def test_passes_gate_boundary_inclusive_at_band_edge():
    assert passes_gate(pct_from_high=BAND_PCT, close=100.0, ema200=90.0) is True
    assert passes_gate(pct_from_high=0.0, close=100.0, ema200=90.0) is True


def test_bucket_for_at_new_high():
    assert bucket_for(0.0) == "AT/NEW HIGH"


def test_bucket_for_0_to_10():
    assert bucket_for(-9.99) == "0-10%"


def test_bucket_for_10_to_20():
    assert bucket_for(-15.0) == "10-20%"


def test_bucket_for_20_to_30():
    assert bucket_for(-25.0) == "20-30%"


def _finding(symbol, pct_from_high, day_chg=1.0, new_high=False, bucket="0-10%"):
    return {
        "symbol": symbol,
        "close": 100.0,
        "day_chg": day_chg,
        "high_52w": 120.0,
        "pct_from_high": pct_from_high,
        "ema200": 90.0,
        "new_high": new_high,
        "bucket": bucket,
        "trap": "n/a",
        "liq_tag": "",
        "cmf_tag": "",
        "deliv_tag": "",
    }


def test_build_markdown_includes_sebi_disclaimer():
    md = build_markdown([], {})
    assert "SEBI registered" in md


def test_build_markdown_sorts_closest_to_high_first():
    findings = [
        _finding("FAR", pct_from_high=-25.0, bucket="20-30%"),
        _finding("NEAR", pct_from_high=-2.0, bucket="0-10%"),
    ]
    md = build_markdown(findings, {})
    assert md.index("[NEAR]") < md.index("[FAR]")


def test_build_markdown_no_signals_writes_placeholder_not_empty_table():
    md = build_markdown([], {})
    assert "*No signals.*" in md
