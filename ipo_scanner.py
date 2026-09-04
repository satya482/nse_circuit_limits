#!/usr/bin/env python3
"""
NSE IPO Listings Scanner
Run after 4:05 PM IST on trading days (after run_fetch_data.ps1 completes).

Tracks recent IPO listings from ipo_listings.txt -- no signal gate,
informational only. Mirrors near_52w_high_scanner.py's "New Listings"
section, but as its own standalone list/dashboard since the IPO list is
far larger and turns over faster than that manual watchlist.

Data source: .ohlc_data/market.db  (populated by fetch_data.py)
Output:      ipo_scans/ipo_scans.md
"""

import os
from datetime import datetime

import ema25_zl_scanner as base
from near_52w_high_scanner import read_new_listings, analyse_new_listing, _new_listing_rows
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from tv_watchlist import tv_csv

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "ipo_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_FILE = os.path.join(SCANS_DIR, "ipo_scans.md")
IPO_LISTINGS_FILE = os.path.join(REPO_DIR, "ipo_listings.txt")


def build_markdown(entries: list[dict], circuit: dict[str, tuple]) -> str:
    entries = sorted(entries, key=lambda x: x["symbol"])
    lines = [
        f"# NSE IPO Listings Watchlist - {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        "*(manual watchlist from `ipo_listings.txt` -- no signal gate, informational only)*",
        "",
        f"**Tracked: {len(entries)}**",
        "",
    ]
    if entries:
        hdr = [
            "| Symbol | Close | Day Chg | Days Tracked | Circuit |",
            "|--------|------:|--------:|-------------:|:-------:|",
        ]
        lines += hdr + _new_listing_rows(entries, circuit)
        lines += ["", "```", tv_csv((f"NSE:{f['symbol']}" for f in entries), label="IPO"), "```"]
    else:
        lines.append("*No listings tracked yet (no OHLC data available).*")

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching NSE circuit limits...")
    circuit = base.get_circuit_limits()
    print(f"  Circuit data: {len(circuit)} stocks with recent limit changes")

    symbols = read_new_listings(IPO_LISTINGS_FILE)
    print(f"  IPO watchlist: {len(symbols)} symbols")

    entries = []
    for sym in symbols:
        result = analyse_new_listing(sym)
        if result:
            entries.append(result)
    print(f"  Tracked: {len(entries)} (have OHLC data)")

    dated_file = os.path.join(SCANS_DIR, f"ipo_scans_{TODAY}.md")
    md = build_markdown(entries, circuit)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
