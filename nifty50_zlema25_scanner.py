#!/usr/bin/env python3
"""Daily NIFTY 50 ZLEMA25 uptrend/downtrend age scanner."""

from __future__ import annotations

import csv
from io import StringIO
import os
from pathlib import Path

import requests


REPO_DIR = Path(__file__).resolve().parent
NSE_CONSTITUENTS_URL = (
    "https://nsearchives.nseindia.com/content/indices/ind_nifty50list.csv"
)
CACHE_FILE = REPO_DIR / "data" / "nifty50_constituents.csv"
HTTP_HEADERS = {"User-Agent": "Mozilla/5.0"}


def parse_constituents_csv(text: str) -> list[str]:
    reader = csv.DictReader(StringIO(text.lstrip("\ufeff")))
    if not reader.fieldnames or "Symbol" not in reader.fieldnames:
        raise ValueError("constituent CSV is missing Symbol column")

    symbols = [str(row.get("Symbol", "")).strip().upper() for row in reader]
    if any(not symbol for symbol in symbols):
        raise ValueError("constituent CSV contains a blank symbol")
    if len(symbols) != 50:
        raise ValueError(
            f"constituent CSV must contain exactly 50 symbols, got {len(symbols)}"
        )
    if len(set(symbols)) != 50:
        raise ValueError("constituent CSV symbols must be unique")
    return sorted(symbols)


def load_nifty50_constituents(
    cache_path: Path = CACHE_FILE,
    http_client=requests,
) -> tuple[list[str], str]:
    try:
        response = http_client.get(
            NSE_CONSTITUENTS_URL,
            headers=HTTP_HEADERS,
            timeout=15,
        )
        response.raise_for_status()
        symbols = parse_constituents_csv(response.text)
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = cache_path.with_suffix(cache_path.suffix + ".tmp")
        tmp_path.write_text(response.text, encoding="utf-8", newline="")
        os.replace(tmp_path, cache_path)
        return symbols, "NSE refresh"
    except (requests.RequestException, OSError, ValueError):
        if not cache_path.exists():
            raise RuntimeError("no valid NIFTY 50 constituent source is available")
        try:
            cached_text = cache_path.read_text(encoding="utf-8")
            return parse_constituents_csv(cached_text), "cached CSV"
        except (OSError, ValueError) as exc:
            raise RuntimeError(
                "no valid NIFTY 50 constituent source is available"
            ) from exc
