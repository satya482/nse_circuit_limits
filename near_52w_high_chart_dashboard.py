#!/usr/bin/env python3
"""
Near-52W-High Chart Dashboard
Run after run_near_52w_high_scanner.ps1 (needs today's report written).

Plots every symbol in the Near-52W-High watchlist (near_52w_high_scans.md) as
an interactive candlestick+volume chart, reusing union_chart_dashboard.py's
renderer -- including its "52W High" blue-stepline overlay.

Data source: .ohlc_data/market.db (via ohlc_db.load_ohlc_many)
Symbol source: near_52w_high_scans/near_52w_high_scans.md (bucketed TV-paste block)
Output: dashboard/near_52w_high_charts.html
"""

import os
import re
from datetime import datetime

from ohlc_db import load_ohlc_many
from union_chart_dashboard import build_chart_data, build_html, resolve_industries, INDUSTRY_CACHE, BENCH_SYM
from near_52w_high_scanner import _PCT_BUCKETS_ORDER

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
MD_FILE = os.path.join(REPO_DIR, "near_52w_high_scans", "near_52w_high_scans.md")
OUTPUT_PATH = os.path.join(REPO_DIR, "dashboard", "near_52w_high_charts.html")
TODAY = datetime.now().strftime("%Y-%m-%d")
LOOKBACK = 600  # >= 6mo default view (~126 bars) + HIGH52W_PERIOD (260) warmup, so the 52W High line covers the entire default view
MIN_BARS = 260
_VALID_BUCKETS = set(_PCT_BUCKETS_ORDER)


def parse_near_52w_buckets(md_text: str) -> dict[str, str]:
    """Symbol -> pct-bucket label, from the first fenced TV-paste block in
    near_52w_high_scans.md. Mirrors union_chart_dashboard.parse_union_tiers's
    section-split shape; index/commodity anchor sections are dropped simply
    because their labels aren't in _VALID_BUCKETS."""
    m = re.search(r"```\n(.*?)\n```", md_text, re.S)
    if not m:
        return {}
    buckets: dict[str, str] = {}
    for section in m.group(1).split("###")[1:]:
        label, _, rest = section.partition(",")
        label = label.strip()
        if label not in _VALID_BUCKETS:
            continue
        for tok in rest.split(","):
            tok = tok.strip()
            if tok.startswith("NSE:"):
                buckets[tok[4:]] = label
    return buckets


def load_todays_near_52w(md_path: str, today: str) -> tuple[dict[str, str] | None, str | None]:
    """Returns (buckets, None) if today's report is present and fresh, else
    (None, reason)."""
    if not os.path.exists(md_path):
        return None, f"{md_path} not found"
    with open(md_path, encoding="utf-8") as fh:
        md = fh.read()
    if not re.search(rf"^#\s.*{re.escape(today)}", md, re.MULTILINE):
        return None, f"{md_path} stale (not today's date)"
    buckets = parse_near_52w_buckets(md)
    if not buckets:
        return None, f"{md_path} has no signals today"
    return buckets, None


def main() -> None:
    buckets, err = load_todays_near_52w(MD_FILE, TODAY)
    if err:
        print(f"[near_52w_high_chart_dashboard] SKIP: {err}")
        return

    industries = resolve_industries(buckets.keys(), INDUSTRY_CACHE, TODAY)
    ohlc_map = load_ohlc_many(list(buckets.keys()), lookback=LOOKBACK)
    bench_df = load_ohlc_many([BENCH_SYM], lookback=LOOKBACK).get(BENCH_SYM)
    records, skipped = build_chart_data(
        ohlc_map, buckets, industries=industries, min_bars=MIN_BARS, bench_df=bench_df,
    )
    print(
        f"[near_52w_high_chart_dashboard] {len(records)} charted, {skipped} skipped "
        f"(insufficient OHLCV or annotation failure)"
    )

    if buckets and not records:
        print("[near_52w_high_chart_dashboard] SKIP: 0 symbols charted (OHLC data unavailable) -- not overwriting existing dashboard")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    html = build_html(records, TODAY, title="Near 52W High Charts", high52w_default_visible=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
