import csv
from io import StringIO

import pytest
import requests

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
