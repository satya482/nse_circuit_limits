import csv
from io import StringIO

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
