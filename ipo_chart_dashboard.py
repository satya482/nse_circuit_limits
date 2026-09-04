#!/usr/bin/env python3
"""
IPO Listings Chart Dashboard
Run after run_ipo_scanner.ps1 (needs today's report written).

Plots every symbol in the IPO watchlist (ipo_scans.md) as an interactive
candlestick+volume chart, reusing union_chart_dashboard.py's renderer.
Charting-only gate: weekly RS EMA9 flat or rising (reuses
minervini_trend_scanner._weekly_rs_ema9_gate -- symbols with under ~12 weeks
of history can't be judged and are excluded). ipo_scans.md itself stays
gate-free -- it's the informational source list; this dashboard is the
filtered view of it.

Data source: .ohlc_data/market.db (via ohlc_db.load_ohlc_many)
Symbol source: ipo_scans/ipo_scans.md (TV-paste block)
Output: dashboard/ipo_charts.html
"""

import os
import re
from datetime import datetime

import pandas as pd

from ohlc_db import load_ohlc_many
from union_chart_dashboard import build_chart_data, build_html, resolve_industries, INDUSTRY_CACHE, BENCH_SYM
from minervini_trend_scanner import _weekly_rs_ema9_gate

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
MD_FILE = os.path.join(REPO_DIR, "ipo_scans", "ipo_scans.md")
OUTPUT_PATH = os.path.join(REPO_DIR, "dashboard", "ipo.html")
TODAY = datetime.now().strftime("%Y-%m-%d")
LOOKBACK = 600
MIN_BARS = 5  # newly listed stocks; just enough bars for a candlestick chart to render
MIN_RS_OVERLAP_BARS = 30  # daily bars vs benchmark before the weekly RS gate is even meaningful


def parse_ipo_symbols(md_text: str) -> list[str]:
    """Symbols from the ###IPO section of the first fenced TV-paste block."""
    m = re.search(r"```\n(.*?)\n```", md_text, re.S)
    if not m:
        return []
    symbols = []
    for section in m.group(1).split("###")[1:]:
        label, _, rest = section.partition(",")
        if label.strip() != "IPO":
            continue
        for tok in rest.split(","):
            tok = tok.strip()
            if tok.startswith("NSE:"):
                symbols.append(tok[4:])
    return symbols


def load_todays_ipo(md_path: str, today: str) -> tuple[list[str] | None, str | None]:
    """Returns (symbols, None) if today's report is present and fresh, else (None, reason)."""
    if not os.path.exists(md_path):
        return None, f"{md_path} not found"
    with open(md_path, encoding="utf-8") as fh:
        md = fh.read()
    if not re.search(rf"^#\s.*{re.escape(today)}", md, re.MULTILINE):
        return None, f"{md_path} stale (not today's date)"
    symbols = parse_ipo_symbols(md)
    if not symbols:
        return None, f"{md_path} has no symbols today"
    return symbols, None


def weekly_rs9_pass(symbols: list[str], ohlc_map: dict, index_s: pd.Series) -> list[str]:
    """Keeps symbols whose weekly RS EMA9 (vs index_s) is flat or rising.
    Excludes anything without enough daily overlap to judge -- new listings
    younger than ~12 weeks fail this, which is correct: there isn't enough
    history yet to call a trend either way."""
    passed = []
    for sym in symbols:
        df = ohlc_map.get(sym)
        if df is None or len(df) < MIN_RS_OVERLAP_BARS:
            continue
        c = df.set_index("date")["close"].astype(float)
        c.index = pd.to_datetime(c.index)
        common = c.index.intersection(index_s.index)
        if len(common) < MIN_RS_OVERLAP_BARS:
            continue
        if _weekly_rs_ema9_gate(c.loc[common], index_s.loc[common]):
            passed.append(sym)
    return passed


def main() -> None:
    symbols, err = load_todays_ipo(MD_FILE, TODAY)
    if err:
        print(f"[ipo_chart_dashboard] SKIP: {err}")
        return

    ohlc_map = load_ohlc_many(symbols, lookback=LOOKBACK)
    bench_df = load_ohlc_many([BENCH_SYM], lookback=LOOKBACK).get(BENCH_SYM)
    index_s = bench_df.set_index("date")["close"].astype(float)
    index_s.index = pd.to_datetime(index_s.index)

    gated_symbols = weekly_rs9_pass(symbols, ohlc_map, index_s)
    print(f"[ipo_chart_dashboard] weekly RS9 gate: {len(gated_symbols)}/{len(symbols)} passed")
    if not gated_symbols:
        print("[ipo_chart_dashboard] SKIP: 0 symbols passed the RS9 gate -- not overwriting existing dashboard")
        return

    tiers = {sym: "IPO" for sym in gated_symbols}
    industries = resolve_industries(gated_symbols, INDUSTRY_CACHE, TODAY)
    records, skipped = build_chart_data(
        ohlc_map, tiers, industries=industries, min_bars=MIN_BARS, bench_df=bench_df,
    )
    print(f"[ipo_chart_dashboard] {len(records)} charted, {skipped} skipped (insufficient OHLCV or annotation failure)")

    if not records:
        print("[ipo_chart_dashboard] SKIP: 0 symbols charted (OHLC data unavailable) -- not overwriting existing dashboard")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    html = build_html(records, TODAY, title="IPO Listings Charts", high52w_default_visible=False)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
