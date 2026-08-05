#!/usr/bin/env python3
"""Daily NIFTY 50 ZLEMA25 uptrend/downtrend age scanner."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime
from io import StringIO
import json
import os
from pathlib import Path
import sys
from typing import Literal

import pandas as pd
import requests

from ema25_zl_scanner import bb_kc_squeeze, get_circuit_limits, zlema
from disclaimer import SEBI_MD_FOOTER, SEBI_MD_HEADER
from ohlc_db import cmf_tag, deliv_tag, liq_tag, load_ohlc
from tv_watchlist import tv_csv, tv_top_sections


REPO_DIR = Path(__file__).resolve().parent
NSE_CONSTITUENTS_URL = (
    "https://nsearchives.nseindia.com/content/indices/ind_nifty50list.csv"
)
CACHE_FILE = REPO_DIR / "data" / "nifty50_constituents.csv"
OUTPUT_FILE = REPO_DIR / "nifty50_zlema25_scans" / "nifty50_zlema25_scans.md"
HTTP_HEADERS = {"User-Agent": "Mozilla/5.0"}
LABELS_FILE = REPO_DIR / "tools" / "stock_labels.json"
AGE_BUCKETS = (
    ("1 DAY", 1, 1),
    ("2 DAYS", 2, 2),
    ("3 DAYS", 3, 3),
    ("4-5 DAYS", 4, 5),
    ("6-10 DAYS", 6, 10),
    ("11-15 DAYS", 11, 15),
    ("15 DAYS+", 16, sys.maxsize),
)


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


def age_bucket(age: int) -> str:
    for label, low, high in AGE_BUCKETS:
        if low <= age <= high:
            return label
    raise ValueError(f"trend age must be >= 1, got {age}")


def sort_findings(
    findings: list[dict[str, object]],
    direction: str,
) -> list[dict[str, object]]:
    return sorted(
        (
            row
            for row in findings
            if row.get("status") == "analysed"
            and row.get("direction") == direction
        ),
        key=lambda row: (int(row["zl_age"]), str(row["symbol"])),
    )


def load_labels() -> dict[str, str]:
    if not LABELS_FILE.exists():
        return {}
    try:
        labels = json.loads(LABELS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return {str(symbol): str(label) for symbol, label in labels.items()}


def _watchlist_parts(
    findings: list[dict[str, object]],
    direction: str,
) -> list[str]:
    prefix = direction.upper()
    parts: list[str] = []
    for label, low, high in AGE_BUCKETS:
        symbols = sorted(
            str(row["symbol"])
            for row in findings
            if low <= int(row["zl_age"]) <= high
        )
        if symbols:
            parts.append(
                f"###{prefix} {label}," + tv_csv(f"NSE:{symbol}" for symbol in symbols)
            )
    return parts


def _table_rows(
    findings: list[dict[str, object]],
    circuits: dict[str, tuple[str, str]],
    labels: dict[str, str],
) -> list[str]:
    rows: list[str] = []
    for finding in findings:
        symbol = str(finding["symbol"])
        tv_url = f"https://in.tradingview.com/chart/?symbol=NSE:{symbol}"
        extras = [
            str(finding.get(key, ""))
            for key in ("liq_tag", "cmf_tag", "deliv_tag")
            if finding.get(key)
        ]
        symbol_cell = f"[{symbol}]({tv_url})"
        if extras:
            symbol_cell += f"<br><sub>{' · '.join(extras)}</sub>"
        zl_change = float(finding["zl_change_pct"])
        day_change = float(finding["day_change_pct"])
        squeeze = "✓" if finding.get("squeeze") else "—"
        circuit, emoji = circuits.get(symbol, ("20%", ""))
        rows.append(
            f"| {symbol_cell} | {int(finding['zl_age'])}d "
            f"| {zl_change:+.2f}% | {labels.get(symbol, '')} "
            f"| {day_change:+.2f}% | {float(finding['close']):.2f} "
            f"| {squeeze} | {circuit} {emoji} |"
        )
    return rows


def _direction_section(
    title: str,
    direction: str,
    findings: list[dict[str, object]],
    circuits: dict[str, tuple[str, str]],
    labels: dict[str, str],
) -> list[str]:
    lines = ["", f"### {title}", ""]
    if not findings:
        return lines + [f"*No ZLEMA25 {direction}trends today.*"]

    lines += [
        "| Symbol | ZL Age | ZL Chg% | Label | Day Chg | Close | Squeeze | Circuit |",
        "|--------|-------:|--------:|-------|--------:|------:|:-------:|:-------:|",
        *_table_rows(findings, circuits, labels),
        "",
        f"#### {direction.title()}trend TradingView Watchlists by Age",
    ]
    for label, low, high in AGE_BUCKETS:
        symbols = sorted(
            str(row["symbol"])
            for row in findings
            if low <= int(row["zl_age"]) <= high
        )
        if not symbols:
            continue
        lines += [
            "",
            f"**{label}** ({len(symbols)})",
            "```",
            tv_csv(f"NSE:{symbol}" for symbol in symbols),
            "```",
        ]
    return lines


def build_markdown(
    results: list[dict[str, object]],
    circuits: dict[str, tuple[str, str]],
    universe_source: str,
    generated_at: str,
) -> str:
    uptrends = sort_findings(results, "up")
    downtrends = sort_findings(results, "down")
    analysed = [row for row in results if row.get("status") == "analysed"]
    skipped = [row for row in results if row.get("status") == "skipped"]
    flat = [row for row in analysed if row.get("direction") == "flat"]
    labels = load_labels()
    watchlist = _watchlist_parts(uptrends, "up") + _watchlist_parts(
        downtrends,
        "down",
    )

    lines = [
        "# NIFTY 50 ZLEMA25 Trend Scan",
        "",
        f"*Generated: {generated_at}*",
        f"*Universe source: {universe_source}*",
        "",
        (
            f"**Requested: {len(results)} · Analysed: {len(analysed)} · "
            f"Skipped: {len(skipped)} · Flat: {len(flat)} · "
            f"Uptrend: {len(uptrends)} · Downtrend: {len(downtrends)}**"
        ),
        "",
        "Daily ZLEMA25 direction is based on strict day-over-day slope. "
        "Age counts consecutive trading bars, with a new direction starting at 1d.",
        "",
        "**TradingView watchlist** *(sectioned by direction and trend age)*",
        "```",
        ",".join(tv_top_sections() + watchlist),
        "```",
    ]
    lines += _direction_section(
        "ZLEMA25 Uptrend Start and Age",
        "up",
        uptrends,
        circuits,
        labels,
    )
    lines += _direction_section(
        "ZLEMA25 Downtrend Start and Age",
        "down",
        downtrends,
        circuits,
        labels,
    )
    if flat:
        lines += [
            "",
            "### Flat ZLEMA25",
            "",
            ", ".join(str(row["symbol"]) for row in flat),
        ]
    if skipped:
        lines += ["", "### Skipped Symbols", ""]
        lines += [
            f"- {row['symbol']}: {row.get('reason', 'unknown reason')}"
            for row in skipped
        ]

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


def write_report_atomic(text: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_suffix(output_path.suffix + ".tmp")
    tmp_path.write_text(text, encoding="utf-8", newline="\n")
    os.replace(tmp_path, output_path)


def run_scan() -> tuple[list[dict[str, object]], str]:
    symbols, source = load_nifty50_constituents()
    return [analyse_symbol(symbol) for symbol in symbols], source


def main() -> int:
    try:
        results, source = run_scan()
        circuits = get_circuit_limits()
        generated_at = datetime.now().strftime("%Y-%m-%d %H:%M IST")
        report = build_markdown(results, circuits, source, generated_at)
        write_report_atomic(report, OUTPUT_FILE)

        analysed = [row for row in results if row.get("status") == "analysed"]
        skipped = [row for row in results if row.get("status") == "skipped"]
        uptrends = sort_findings(results, "up")
        downtrends = sort_findings(results, "down")
        flat = [row for row in analysed if row.get("direction") == "flat"]
        print(
            f"Requested: {len(results)}  Analysed: {len(analysed)}  "
            f"Skipped: {len(skipped)}  Flat: {len(flat)}"
        )
        print(f"Uptrend: {len(uptrends)}  Downtrend: {len(downtrends)}")
        print(f"Universe source: {source}")
        for row in skipped:
            print(f"Skipped {row['symbol']}: {row.get('reason', 'unknown reason')}")
        print(f"Report: {OUTPUT_FILE}")
        return 0
    except Exception as exc:
        print(f"NIFTY 50 ZLEMA25 scan failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
