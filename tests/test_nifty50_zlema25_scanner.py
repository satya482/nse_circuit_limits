import csv
from io import StringIO
from pathlib import Path

import pytest
import requests
import pandas as pd
from pandas.testing import assert_series_equal

from ema25_zl_scanner import zlema as broad_zlema

import nifty50_zlema25_scanner as scanner


def constituent_csv(symbols) -> str:
    out = StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=["Company Name", "Industry", "Symbol", "Series", "ISIN Code"],
        lineterminator="\n",
    )
    writer.writeheader()
    for symbol in symbols:
        writer.writerow({"Company Name": symbol, "Symbol": symbol, "Series": "EQ"})
    return out.getvalue()


def symbols_50() -> list[str]:
    return [f"SYM{i:02d}" for i in range(50)]


def test_parse_constituents_requires_exactly_50_unique_nonblank_symbols():
    assert scanner.parse_constituents_csv(
        constituent_csv(reversed(symbols_50()))
    ) == symbols_50()

    with pytest.raises(ValueError, match="exactly 50"):
        scanner.parse_constituents_csv(constituent_csv(symbols_50()[:-1]))
    with pytest.raises(ValueError, match="unique"):
        scanner.parse_constituents_csv(
            constituent_csv(symbols_50()[:-1] + ["SYM00"])
        )
    with pytest.raises(ValueError, match="blank"):
        scanner.parse_constituents_csv(constituent_csv(symbols_50()[:-1] + [""]))


def test_remote_refresh_replaces_cache_and_reports_source(tmp_path):
    class Response:
        text = constituent_csv(symbols_50())

        @staticmethod
        def raise_for_status():
            return None

    class Client:
        @staticmethod
        def get(url, headers, timeout):
            return Response()

    cache = tmp_path / "nifty50.csv"
    symbols, source = scanner.load_nifty50_constituents(cache, Client)

    assert symbols == symbols_50()
    assert source == "NSE refresh"
    assert scanner.parse_constituents_csv(
        cache.read_text(encoding="utf-8")
    ) == symbols_50()


def test_failed_refresh_uses_valid_cache(tmp_path):
    class Client:
        @staticmethod
        def get(url, headers, timeout):
            raise requests.RequestException("offline")

    cache = tmp_path / "nifty50.csv"
    cache.write_text(constituent_csv(symbols_50()), encoding="utf-8")

    assert scanner.load_nifty50_constituents(cache, Client) == (
        symbols_50(),
        "cached CSV",
    )


def test_invalid_remote_response_preserves_and_uses_cache(tmp_path):
    class Response:
        text = constituent_csv(symbols_50()[:-1])

        @staticmethod
        def raise_for_status():
            return None

    class Client:
        @staticmethod
        def get(url, headers, timeout):
            return Response()

    cache = tmp_path / "nifty50.csv"
    valid_text = constituent_csv(symbols_50())
    cache.write_text(valid_text, encoding="utf-8")

    assert scanner.load_nifty50_constituents(cache, Client) == (
        symbols_50(),
        "cached CSV",
    )
    assert cache.read_text(encoding="utf-8") == valid_text


def test_no_valid_remote_or_cache_fails_clearly(tmp_path):
    class Client:
        @staticmethod
        def get(url, headers, timeout):
            raise requests.RequestException("offline")

    with pytest.raises(RuntimeError, match="no valid NIFTY 50"):
        scanner.load_nifty50_constituents(tmp_path / "missing.csv", Client)


@pytest.mark.parametrize(
    ("zl", "expected_direction", "expected_age", "expected_start"),
    [
        ([10, 9, 10], "up", 1, 2),
        ([10, 9, 10, 11, 12], "up", 3, 2),
        ([10, 11, 10], "down", 1, 2),
        ([10, 11, 10, 9, 8], "down", 3, 2),
        ([10, 11, 11], "flat", 0, None),
    ],
)
def test_trend_stats_direction_age_and_start(
    zl, expected_direction, expected_age, expected_start
):
    series = pd.Series(zl, dtype=float)
    closes = pd.Series([100 + i * 10 for i in range(len(zl))], dtype=float)

    result = scanner.trend_stats(series, closes)

    assert (result.direction, result.age, result.start_position) == (
        expected_direction,
        expected_age,
        expected_start,
    )


def test_trend_change_uses_close_before_start():
    result = scanner.trend_stats(
        pd.Series([10.0, 9.0, 10.0, 11.0]),
        pd.Series([100.0, 110.0, 121.0, 132.0]),
    )

    assert result.change_pct == 20.0


def test_zlema_is_identical_to_broad_scanner():
    close = pd.Series(range(1, 81), dtype=float)

    assert_series_equal(scanner.zlema(close, 25), broad_zlema(close, 25))


def synthetic_ohlc(rows: int = 65) -> pd.DataFrame:
    close = pd.Series([100.0 + i for i in range(rows)])
    return pd.DataFrame(
        {
            "date": pd.date_range("2026-01-01", periods=rows, freq="B"),
            "open": close - 0.25,
            "high": close + 1.0,
            "low": close - 1.0,
            "close": close,
            "volume": 1_000_000,
        }
    )


def test_analyse_symbol_returns_direction_age_prices_and_tags(monkeypatch):
    monkeypatch.setattr(scanner, "load_ohlc", lambda symbol: synthetic_ohlc())
    monkeypatch.setattr(scanner, "bb_kc_squeeze", lambda frame: True)
    monkeypatch.setattr(scanner, "liq_tag", lambda frame: "LIQ")
    monkeypatch.setattr(scanner, "cmf_tag", lambda frame: "CMF")
    monkeypatch.setattr(scanner, "deliv_tag", lambda symbol: "DEL")

    result = scanner.analyse_symbol("TEST")

    assert result["status"] == "analysed"
    assert result["direction"] == "up"
    assert result["zl_age"] == 64
    assert result["close"] == 164.0
    assert (result["liq_tag"], result["cmf_tag"], result["deliv_tag"]) == (
        "LIQ",
        "CMF",
        "DEL",
    )


def test_analyse_symbol_reports_short_history(monkeypatch):
    monkeypatch.setattr(scanner, "load_ohlc", lambda symbol: synthetic_ohlc(59))

    assert scanner.analyse_symbol("SHORT") == {
        "symbol": "SHORT",
        "status": "skipped",
        "reason": "fewer than 60 OHLC rows",
    }


def test_analyse_symbol_raises_contextual_error_for_bad_schema(monkeypatch):
    monkeypatch.setattr(
        scanner,
        "load_ohlc",
        lambda symbol: synthetic_ohlc().drop(columns="close"),
    )

    with pytest.raises(RuntimeError, match="BROKEN: analysis failed"):
        scanner.analyse_symbol("BROKEN")


@pytest.mark.parametrize(
    ("age", "bucket"),
    [
        (1, "1 DAY"),
        (2, "2 DAYS"),
        (3, "3 DAYS"),
        (4, "4-5 DAYS"),
        (5, "4-5 DAYS"),
        (6, "6-10 DAYS"),
        (10, "6-10 DAYS"),
        (11, "11-15 DAYS"),
        (15, "11-15 DAYS"),
        (16, "15 DAYS+"),
        (80, "15 DAYS+"),
    ],
)
def test_age_bucket_boundaries(age, bucket):
    assert scanner.age_bucket(age) == bucket


def finding(symbol: str, direction: str, age: int) -> dict[str, object]:
    return {
        "symbol": symbol,
        "status": "analysed",
        "direction": direction,
        "zl_age": age,
        "zl_change_pct": 1.25,
        "day_change_pct": 0.5,
        "close": 100.0,
        "squeeze": False,
        "liq_tag": "",
        "cmf_tag": "",
        "deliv_tag": "",
    }


def test_tables_sort_by_age_then_symbol():
    rows = [
        finding("ZZZ", "up", 2),
        finding("BBB", "up", 1),
        finding("AAA", "up", 1),
    ]

    assert [
        row["symbol"] for row in scanner.sort_findings(rows, "up")
    ] == ["AAA", "BBB", "ZZZ"]


def test_report_has_two_tables_and_symmetric_watchlists(monkeypatch):
    monkeypatch.setattr(scanner, "load_labels", lambda: {"UP1": "Leader"})
    results = [
        finding("UP1", "up", 1),
        finding("UP4", "up", 4),
        finding("DN1", "down", 1),
        finding("DN4", "down", 4),
        {
            "symbol": "FLAT",
            "status": "analysed",
            "direction": "flat",
            "zl_age": 0,
        },
        {"symbol": "SKIP", "status": "skipped", "reason": "short"},
    ]

    report = scanner.build_markdown(
        results,
        {},
        "cached CSV",
        "2026-07-17 16:30 IST",
    )

    assert "### ZLEMA25 Uptrend Start and Age" in report
    assert "### ZLEMA25 Downtrend Start and Age" in report
    assert "###UP 1 DAY,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:UP1" in report
    assert "###DOWN 1 DAY,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:DN1" in report
    assert report.index("NSE:UP1") < report.index("NSE:UP4")
    assert "Requested: 6" in report
    assert "Analysed: 5" in report
    assert "Skipped: 1" in report
    assert "Flat: 1" in report
    assert "Leader" in report
    assert "SEBI registered" in report


def test_write_report_atomic_replaces_target_without_temp_residue(tmp_path):
    output = tmp_path / "report.md"
    output.write_text("old", encoding="utf-8")

    scanner.write_report_atomic("new\n", output)

    assert output.read_text(encoding="utf-8") == "new\n"
    assert not (tmp_path / "report.md.tmp").exists()


def test_main_writes_report_and_prints_counts(monkeypatch, tmp_path, capsys):
    output = tmp_path / "nifty50.md"
    rows = [finding("UP", "up", 1), finding("DOWN", "down", 2)]
    monkeypatch.setattr(
        scanner,
        "load_nifty50_constituents",
        lambda: (["DOWN", "UP"], "cached CSV"),
    )
    monkeypatch.setattr(
        scanner,
        "analyse_symbol",
        lambda symbol: next(row for row in rows if row["symbol"] == symbol),
    )
    monkeypatch.setattr(scanner, "get_circuit_limits", lambda: {})
    monkeypatch.setattr(scanner, "OUTPUT_FILE", output)

    assert scanner.main() == 0

    report = output.read_text(encoding="utf-8")
    console = capsys.readouterr().out
    assert "ZLEMA25 Uptrend Start and Age" in report
    assert "ZLEMA25 Downtrend Start and Age" in report
    assert "Requested: 2" in console
    assert "Uptrend: 1" in console
    assert "Downtrend: 1" in console


def test_main_returns_one_without_report_on_fatal_error(monkeypatch, tmp_path, capsys):
    output = tmp_path / "nifty50.md"

    def fail():
        raise RuntimeError("universe unavailable")

    monkeypatch.setattr(scanner, "load_nifty50_constituents", fail)
    monkeypatch.setattr(scanner, "OUTPUT_FILE", output)

    assert scanner.main() == 1
    assert not output.exists()
    assert "universe unavailable" in capsys.readouterr().err


def test_runner_and_orchestrator_contracts():
    root = Path(__file__).resolve().parents[1]
    runner = (root / "run_nifty50_zlema25_scanner.ps1").read_text(
        encoding="utf-8"
    )
    orchestrator = (root / "run_all_scanners.ps1").read_text(encoding="utf-8")

    assert "nifty50_zlema25_scanner.py" in runner
    assert "nifty50_zlema25_scans/" in runner
    assert "data/nifty50_constituents.csv" in runner
    assert "commit --no-verify" in runner
    assert 'Run-Scanner "NIFTY50_ZLEMA25"' in orchestrator
