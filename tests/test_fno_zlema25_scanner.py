import pandas as pd
import pytest

import ema25_zl_scanner as broad


def test_downtrend_turn_stats_starts_at_one_day_and_uses_pre_turn_close():
    zl25 = pd.Series([3.0, 3.0, 2.0])
    closes = pd.Series([100.0, 110.0, 99.0])

    assert broad.zl25_turn_stats(zl25, closes, direction="down") == (1, -10.0)


def test_downtrend_turn_stats_counts_continuing_bars():
    zl25 = pd.Series([3.0, 3.0, 2.0, 1.0])
    closes = pd.Series([100.0, 110.0, 99.0, 90.0])

    assert broad.zl25_turn_stats(zl25, closes, direction="down") == (2, -18.18)


def test_turn_stats_rejects_unknown_direction():
    with pytest.raises(ValueError, match="direction"):
        broad.zl25_turn_stats(
            pd.Series([1.0, 2.0, 3.0]),
            pd.Series([1.0, 2.0, 3.0]),
            direction="sideways",
        )


def test_analyse_exposes_current_direction_and_downtrend_stats(monkeypatch):
    dates = pd.date_range("2026-01-01", periods=65, freq="D")
    closes = pd.Series(list(range(100, 160)) + [150, 130, 110, 90, 70], dtype=float)
    raw = pd.DataFrame(
        {
            "date": dates,
            "open": closes,
            "high": closes + 1,
            "low": closes - 1,
            "close": closes,
            "volume": 1_000.0,
        }
    )
    index_s = pd.Series(100.0, index=dates)
    expected_days, expected_pct = broad.zl25_turn_stats(
        broad.zlema(closes, 25), closes, "down"
    )

    monkeypatch.setattr(broad, "load_ohlc", lambda _symbol: raw)
    monkeypatch.setattr(broad, "_rs_gate", lambda *_args: True)
    monkeypatch.setattr(broad, "_weekly_rs_gate", lambda *_args: True)
    monkeypatch.setattr(broad, "float_metrics", lambda *_args: {})
    monkeypatch.setattr(broad, "passes_hard_gate", lambda _metrics: True)
    monkeypatch.setattr(broad, "trap_label", lambda _metrics: "✓ SAFE")
    monkeypatch.setattr(broad, "_rvol_ss", lambda _raw: (1.0, False))
    monkeypatch.setattr(broad, "liq_tag", lambda _raw: "")
    monkeypatch.setattr(broad, "cmf_tag", lambda _raw: "")
    monkeypatch.setattr(broad, "deliv_tag", lambda _symbol: "")

    result = broad.analyse("TEST", index_s, float_shares=1_000_000)

    assert result["zl_direction"] == "down"
    assert result["zl_down_days"] == expected_days
    assert result["zl_down_pct"] == expected_pct


def _finding(symbol: str, direction: str, up_days: int, down_days: int) -> dict:
    return {
        "symbol": symbol,
        "close": 100.0,
        "day_chg": 1.0,
        "zl_rising": direction == "up",
        "zl_direction": direction,
        "zl_days": up_days,
        "zl_pct": 5.0,
        "zl_down_days": down_days,
        "zl_down_pct": -4.0,
        "squeeze": False,
        "trap": "✓ SAFE",
        "rs_weekly_gate": False,
        "rvol": 1.0,
        "strong_start": False,
        "liq_tag": "",
        "cmf_tag": "",
        "deliv_tag": "",
    }


def test_directional_report_has_symmetric_tables_watchlists_and_flat_count():
    findings = [
        _finding("UPSYM", "up", up_days=1, down_days=8),
        _finding("DOWNSYM", "down", up_days=9, down_days=2),
        _finding("FLATSYM", "flat", up_days=3, down_days=4),
    ]

    report = broad.build_markdown(
        findings,
        {},
        {},
        title="NSE F&O ZLEMA25 Scan — 2026-07-20",
        universe_label="NSE F&O underlyings eligible under broad EMA25 ZL filters",
        directional=True,
        universe_stats="209 NSE F&O stocks · 180 TradingView-eligible",
    )

    assert "# NSE F&O ZLEMA25 Scan — 2026-07-20" in report
    assert "NSE F&O underlyings eligible under broad EMA25 ZL filters" in report
    assert "209 NSE F&O stocks · 180 TradingView-eligible" in report
    assert "ZLEMA25 Uptrend: 1" in report
    assert "ZLEMA25 Downtrend: 1" in report
    assert "Flat: 1" in report
    assert "### ZLEMA25 Uptrend" in report
    assert "### ZLEMA25 Downtrend" in report
    assert "###UP 1 DAY,NSE:UPSYM" in report
    assert "###DOWN 2 DAYS,NSE:DOWNSYM" in report
    assert "| DOWNSYM" not in report
    assert "[DOWNSYM]" in report
    assert "| 2d | -4.0% |" in report
    assert "SEBI registered" in report


def test_default_report_contract_remains_rising_and_watch():
    report = broad.build_markdown(
        [
            _finding("UPSYM", "up", up_days=1, down_days=8),
            _finding("DOWNSYM", "down", up_days=9, down_days=2),
        ],
        {},
        {},
    )

    assert "# NSE EMA25 ZL Scan" in report
    assert "| Exchange | NSE common equity |" in report
    assert "### ZLEMA25 Rising" in report
    assert "### ZLEMA25 Watch *(pullback / flat)*" in report
