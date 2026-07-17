#!/usr/bin/env python3
"""Daily NIFTY 50 ZLEMA25 uptrend/downtrend age scanner."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from io import StringIO
import os
from pathlib import Path
from typing import Literal

import pandas as pd
import requests

from ema25_zl_scanner import bb_kc_squeeze, get_circuit_limits, zlema
from ohlc_db import cmf_tag, deliv_tag, liq_tag, load_ohlc


REPO_DIR = Path(__file__).resolve().parent
NSE_CONSTITUENTS_URL = (
    "https://nsearchives.nseindia.com/content/indices/ind_nifty50list.csv"
)
CACHE_FILE = REPO_DIR / "data" / "nifty50_constituents.csv"
HTTP_HEADERS = {"User-Agent": "Mozilla/5.0"}


@dataclass(frozen=True)
class TrendStats:
    direction: Literal["up", "down", "flat"]
    age: int
    change_pct: float
    start_position: int | None


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


def trend_stats(zl25: pd.Series, closes: pd.Series) -> TrendStats:
    if len(zl25) != len(closes) or len(zl25) < 2:
        raise ValueError("ZLEMA and close series must have equal length >= 2")

    slopes = zl25.astype(float).diff()
    last_slope = float(slopes.iloc[-1])
    if last_slope == 0:
        return TrendStats("flat", 0, 0.0, None)

    direction: Literal["up", "down"] = "up" if last_slope > 0 else "down"
    age = 0
    for slope in reversed(slopes.iloc[1:].tolist()):
        if (direction == "up" and slope > 0) or (
            direction == "down" and slope < 0
        ):
            age += 1
        else:
            break

    start_position = len(zl25) - age
    base_position = start_position - 1
    change_pct = round(
        (float(closes.iloc[-1]) / float(closes.iloc[base_position]) - 1) * 100,
        2,
    )
    return TrendStats(direction, age, change_pct, start_position)


def analyse_symbol(symbol: str) -> dict[str, object]:
    raw = load_ohlc(symbol)
    if raw is None or len(raw) < 60:
        return {
            "symbol": symbol,
            "status": "skipped",
            "reason": "fewer than 60 OHLC rows",
        }

    try:
        df = raw.sort_values("date").reset_index(drop=True)
        close = df["close"].astype(float)
        stats = trend_stats(zlema(close, 25), close)
        previous_close = float(close.iloc[-2])
        latest_close = float(close.iloc[-1])
        return {
            "symbol": symbol,
            "status": "analysed",
            "direction": stats.direction,
            "zl_age": stats.age,
            "zl_change_pct": stats.change_pct,
            "close": latest_close,
            "day_change_pct": round(
                (latest_close / previous_close - 1) * 100,
                2,
            ),
            "squeeze": bb_kc_squeeze(df),
            "liq_tag": liq_tag(df),
            "cmf_tag": cmf_tag(df),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception as exc:
        raise RuntimeError(f"{symbol}: analysis failed: {exc}") from exc
