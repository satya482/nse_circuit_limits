import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))

from minervini_trend_scanner import (
    sma,
    trend_template_checks,
    passes_trend_template,
    build_markdown,
)


def _uptrend_series(n=300, start=100.0, step=0.5):
    return pd.Series([start + i * step for i in range(n)])


def test_sma_matches_rolling_mean():
    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
    result = sma(s, 3)
    assert result.iloc[-1] == (3.0 + 4.0 + 5.0) / 3
    assert pd.isna(result.iloc[0])


def test_all_checks_pass_on_clean_steady_uptrend():
    close = _uptrend_series(300)
    checks = trend_template_checks(close)
    assert all(checks.values()), checks
    assert passes_trend_template(checks)


def test_fails_when_price_below_sma50():
    close = _uptrend_series(300)
    close.iloc[-1] = close.iloc[-60]  # crash the last close well below SMA50
    checks = trend_template_checks(close)
    assert checks["above_sma50"] is False
    assert passes_trend_template(checks) is False


def test_fails_when_sma200_not_trending_up():
    close = pd.Series([100.0] * 300)
    checks = trend_template_checks(close)
    assert checks["sma200_trending_up"] is False
    assert passes_trend_template(checks) is False


def test_fails_when_more_than_25pct_off_52wk_high():
    close = _uptrend_series(300)
    peak = close.iloc[-30]
    close.iloc[-1] = peak * 0.70  # 30% off a recent-ish high, still within 252d window
    checks = trend_template_checks(close)
    assert checks["within_25pct_of_52wk_high"] is False


def test_fails_when_not_30pct_above_52wk_low():
    close = _uptrend_series(300, start=100.0, step=0.05)  # slow crawl
    checks = trend_template_checks(close)
    assert checks["above_52wk_low_30pct"] is False


def test_build_markdown_empty_findings_writes_no_signals_not_empty_file():
    md = build_markdown([])
    assert "No signals." in md
    assert "SEBI registered" in md  # disclaimer present


def test_build_markdown_populated_includes_symbol_and_close():
    findings = [{
        "symbol": "TESTSTOCK",
        "close": 123.45,
        "day_chg": 1.23,
        "off_high_pct": -4.5,
        "above_low_pct": 45.0,
    }]
    md = build_markdown(findings)
    assert "TESTSTOCK" in md
    assert "123.45" in md
    assert "SEBI registered" in md


if __name__ == "__main__":
    test_sma_matches_rolling_mean()
    test_all_checks_pass_on_clean_steady_uptrend()
    test_fails_when_price_below_sma50()
    test_fails_when_sma200_not_trending_up()
    test_fails_when_more_than_25pct_off_52wk_high()
    test_fails_when_not_30pct_above_52wk_low()
    test_build_markdown_empty_findings_writes_no_signals_not_empty_file()
    test_build_markdown_populated_includes_symbol_and_close()
    print("ok")
