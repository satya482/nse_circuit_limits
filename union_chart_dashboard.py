#!/usr/bin/env python3
"""
Union Watchlist Chart Dashboard
Run after run_ema55_cross_scanner.ps1 (needs today's union watchlist written).

Plots every symbol in the EMA55 union watchlist (ema55_cross_scans.md) as an
interactive candlestick+volume chart, with live client-side controls for
candle color and EMA overlay periods.

Data source: .ohlc_data/market.db (via ohlc_db.load_ohlc_many)
Symbol source: ema55_cross_scans/ema55_cross_scans.md (union tv-paste block)
Output: dashboard/union_charts.html
"""

import json
import os
import re
from datetime import datetime

from ohlc_db import load_ohlc_many
from disclaimer import SEBI_HTML_BANNER, SEBI_HTML_FOOTER

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
EMA55_MD = os.path.join(REPO_DIR, "ema55_cross_scans", "ema55_cross_scans.md")
OUTPUT_PATH = os.path.join(REPO_DIR, "dashboard", "union_charts.html")
TODAY = datetime.now().strftime("%Y-%m-%d")
MIN_BARS = 130
LOOKBACK = 250
SKIP_LABELS = {"INDICES", "COMMODITIES"}
INDEX_ANCHORS = {"NIFTYSMLCAP250", "NIFTYMIDSML400"}


def parse_union_tiers(md_text: str) -> dict[str, str]:
    """Symbol -> confluence tier label, from the first fenced TV-paste block
    in ema55_cross_scans.md (the Union Watchlist block, at the top of the
    file). Mirrors ema55_cross_scanner._symbols_from_tv_block's section-split
    and anchor-exclusion logic, but keeps the tier label per symbol instead
    of discarding it into a flat set."""
    m = re.search(r"```\n(.*?)\n```", md_text, re.S)
    if not m:
        return {}
    tiers: dict[str, str] = {}
    for section in m.group(1).split("###")[1:]:
        label, _, rest = section.partition(",")
        label = label.strip()
        if label.upper() in SKIP_LABELS:
            continue
        for tok in rest.split(","):
            tok = tok.strip()
            if tok.startswith("NSE:") and tok[4:] not in INDEX_ANCHORS:
                tiers[tok[4:]] = label
    return tiers


def load_todays_union(md_path: str, today: str) -> tuple[dict[str, str] | None, str | None]:
    """Returns (tiers, None) if today's union data is present and fresh,
    else (None, reason)."""
    if not os.path.exists(md_path):
        return None, f"{md_path} not found"
    with open(md_path, encoding="utf-8") as fh:
        md = fh.read()
    if not re.search(rf"^#\s.*{re.escape(today)}", md, re.MULTILINE):
        return None, f"{md_path} stale (not today's date)"
    tiers = parse_union_tiers(md)
    if not tiers:
        return None, f"{md_path} has no union watchlist data"
    return tiers, None


def build_chart_data(ohlc_map: dict, tiers: dict[str, str], min_bars: int = MIN_BARS) -> tuple[list[dict], int]:
    """Returns (records, skipped_count), records sorted by symbol.
    Skips symbols missing from ohlc_map or with fewer than min_bars rows."""
    records = []
    skipped = 0
    for symbol, tier in sorted(tiers.items()):
        df = ohlc_map.get(symbol)
        if df is None or len(df) < min_bars:
            skipped += 1
            continue
        bars = [
            [
                row.date.strftime("%Y-%m-%d"),
                float(row.open),
                float(row.high),
                float(row.low),
                float(row.close),
                float(row.volume),
            ]
            for row in df.itertuples(index=False)
        ]
        records.append({"symbol": symbol, "tier": tier, "bars": bars})
    return records, skipped
