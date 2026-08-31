#!/usr/bin/env python3
"""
TradingView Watchlist Chart Dashboard
Run after run_union_chart_dashboard.ps1 (reuses its industry cache/renderer).

Scrapes the public shared TradingView watchlist page (no login) for its
ordered symbol list, then renders interactive candlestick+volume charts
grouped by TradingView industry -- reusing union_chart_dashboard.py's chart
renderer so both pages stay feature-identical.

Data source: .ohlc_data/market.db (NSE) + .us_ohlc_data/us_market.db (US)
Symbol source: public TradingView shared watchlist page
Output: dashboard/charts.html
"""

import json
import os
import re
from datetime import datetime

import requests

from ohlc_db import load_ohlc_many
from us_ohlc_db import load_ohlc_many as load_us_ohlc_many
from tv_watchlist import INDEX_WATCHLIST_SYMBOLS, COMMODITY_WATCHLIST_SYMBOLS
from union_chart_dashboard import build_chart_data, build_html, resolve_industries, INDUSTRY_CACHE, BENCH_SYM

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
WATCHLIST_URL = "https://in.tradingview.com/watchlists/156673583/"
OUTPUT_PATH = os.path.join(REPO_DIR, "dashboard", "charts.html")
TODAY = datetime.now().strftime("%Y-%m-%d")
LOOKBACK = 600  # >= 6mo default view (~126 bars) + HIGH52W_PERIOD (260) warmup, so the 52W High line covers the entire default view
SUPPORTED_EXCHANGES = {"NSE", "NASDAQ", "AMEX"}
SKIP_SYMBOLS = set(INDEX_WATCHLIST_SYMBOLS + COMMODITY_WATCHLIST_SYMBOLS)
_INIT_DATA_RE = re.compile(
    r'<script type="application/prs\.init-data\+json">(.*?)</script>', re.S
)


def fetch_watchlist_symbols(url: str = WATCHLIST_URL) -> list[str]:
    """Ordered, deduped EXCHANGE:TICKER symbols from a public shared TV
    watchlist page. Returns [] on any fetch/parse failure -- caller must
    treat that as 'no update', never overwrite the existing dashboard."""
    try:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
        resp.raise_for_status()
        m = _INIT_DATA_RE.search(resp.text)
        if not m:
            return []
        symbols = json.loads(m.group(1))["sharedWatchlist"]["list"]["symbols"]
    except Exception as exc:
        print(f"[tradingview_watchlist_dashboard] fetch/parse failed: {exc}")
        return []
    seen = set()
    ordered = []
    for s in symbols:
        if s not in seen:
            seen.add(s)
            ordered.append(s)
    return ordered


def split_by_exchange(symbols: list[str]) -> tuple[dict[str, str], list[str]]:
    """Returns (ticker -> exchange) for supported exchanges, plus the raw
    entries skipped (benchmark/commodity anchors or unsupported exchange)."""
    exchange_map = {}
    skipped = []
    for raw in symbols:
        if raw in SKIP_SYMBOLS:
            continue
        exchange, _, ticker = raw.partition(":")
        if exchange in SUPPORTED_EXCHANGES and ticker:
            exchange_map[ticker] = exchange
        else:
            skipped.append(raw)
    return exchange_map, skipped


def load_all_ohlc(exchange_map: dict[str, str]) -> dict:
    nse_symbols = [s for s, ex in exchange_map.items() if ex == "NSE"]
    us_symbols = [s for s, ex in exchange_map.items() if ex != "NSE"]
    ohlc_map = load_ohlc_many(nse_symbols, lookback=LOOKBACK)
    ohlc_map.update(load_us_ohlc_many(us_symbols, lookback=LOOKBACK))
    return ohlc_map


def main() -> None:
    raw_symbols = fetch_watchlist_symbols()
    if not raw_symbols:
        print("[tradingview_watchlist_dashboard] SKIP: fetch/parse returned no symbols -- not overwriting existing dashboard")
        return

    exchange_map, skipped = split_by_exchange(raw_symbols)
    if skipped:
        print(f"[tradingview_watchlist_dashboard] {len(skipped)} unsupported symbols skipped: {skipped}")
    if not exchange_map:
        print("[tradingview_watchlist_dashboard] SKIP: 0 supported symbols -- not overwriting existing dashboard")
        return

    industries = resolve_industries(exchange_map.keys(), INDUSTRY_CACHE, TODAY)
    ohlc_map = load_all_ohlc(exchange_map)
    bench_df = load_ohlc_many([BENCH_SYM], lookback=LOOKBACK).get(BENCH_SYM)
    records, skipped_ohlc = build_chart_data(
        ohlc_map, exchange_map, industries=industries, symbol_exchange=exchange_map,
        bench_df=bench_df,
    )
    print(
        f"[tradingview_watchlist_dashboard] {len(records)} charted, {skipped_ohlc} skipped "
        f"(insufficient OHLCV or annotation failure)"
    )

    if not records:
        print("[tradingview_watchlist_dashboard] SKIP: 0 symbols charted -- not overwriting existing dashboard")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    html = build_html(records, TODAY, title="TradingView Watchlist Charts", group_sort="alpha")
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
