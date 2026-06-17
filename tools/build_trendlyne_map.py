#!/usr/bin/env python3
"""
Parse trendlyne equity sitemap → trendlyne_id_map.json
Run once to bootstrap, then monthly alongside company fetch.

Sitemap URL: https://trendlyne.com/equity-sitemap-stocks.xml
Each <loc>:  https://trendlyne.com/equity/{id}/{TICKER}/{slug}/
"""

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

sys.stdout.reconfigure(encoding="utf-8")

SITEMAP_URL = "https://trendlyne.com/equity-sitemap-stocks.xml"
OUT_FILE = Path(__file__).parent / "trendlyne_id_map.json"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

# /equity/{id}/{TICKER}/{slug}/
_LOC_RE = re.compile(r"/equity/(\d+)/([^/]+)/([^/]+)/?$")


def build_map() -> dict:
    print(f"Fetching {SITEMAP_URL} …")
    resp = requests.get(SITEMAP_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    root = ET.fromstring(resp.text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    mapping = {}
    skipped = 0
    for url_el in root.findall("sm:url", ns):
        loc = url_el.findtext("sm:loc", namespaces=ns) or ""
        m = _LOC_RE.search(loc)
        if not m:
            skipped += 1
            continue
        tid, ticker, slug = m.group(1), m.group(2), m.group(3)
        mapping[ticker] = {"id": tid, "slug": slug}

    print(f"Parsed {len(mapping)} stocks (skipped {skipped} non-equity entries)")
    return mapping


def main():
    mapping = build_map()
    OUT_FILE.write_text(
        json.dumps(mapping, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Written: {OUT_FILE}  ({len(mapping)} entries)")

    # Quick sanity check
    for sym in ["KRN", "ICICIBANK", "RELIANCE"]:
        entry = mapping.get(sym)
        status = f"id={entry['id']}" if entry else "MISSING"
        print(f"  {sym}: {status}")


if __name__ == "__main__":
    sys.exit(main())
