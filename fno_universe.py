#!/usr/bin/env python3
"""
fno_universe.py  —  NSE F&O underlyings list with 30-day local cache

Cache: .fno_cache.csv  (gitignored)
Source: NSE equity-stockIndices API (requires session cookie, same pattern as main.py)
"""

import csv, time
from datetime import datetime, timedelta
from pathlib import Path

import requests

CACHE_FILE = Path(__file__).parent / ".fno_cache.csv"
CACHE_DAYS = 30

_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept":          "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer":         "https://www.nseindia.com/",
}


def _cache_fresh() -> bool:
    if not CACHE_FILE.exists():
        return False
    age = datetime.now() - datetime.fromtimestamp(CACHE_FILE.stat().st_mtime)
    return age < timedelta(days=CACHE_DAYS)


def _fetch_nse() -> list[str]:
    session = requests.Session()
    session.headers.update(_HEADERS)
    session.get("https://www.nseindia.com", timeout=15)
    time.sleep(1)
    r = session.get(
        "https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O",
        timeout=15,
    )
    r.raise_for_status()
    symbols = []
    for item in r.json().get("data", []):
        sym = item.get("symbol", "").strip()
        # skip index-level entries (they contain spaces or are all lowercase)
        if sym and " " not in sym and sym == sym.upper():
            symbols.append(sym)
    return symbols


def _save(symbols: list[str]) -> None:
    with open(CACHE_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["symbol"])
        for s in symbols:
            w.writerow([s])


def _load() -> list[str]:
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return [row["symbol"] for row in csv.DictReader(f) if row.get("symbol")]


def get_fno_symbols(force_refresh: bool = False) -> list[str]:
    """Return NSE F&O underlying symbols. Refreshes from NSE if cache is older than 30 days."""
    if not force_refresh and _cache_fresh():
        syms = _load()
        age  = (datetime.now() - datetime.fromtimestamp(CACHE_FILE.stat().st_mtime)).days
        print(f"  F&O universe: {len(syms)} symbols  (cached, {age}d old)")
        return syms

    print("  Fetching F&O universe from NSE...")
    try:
        syms = _fetch_nse()
        if syms:
            _save(syms)
            print(f"  F&O universe: {len(syms)} symbols  (refreshed from NSE)")
            return syms
        print("  NSE returned empty list — falling back to cache")
    except Exception as e:
        print(f"  NSE fetch failed: {e}  — falling back to cache")

    if CACHE_FILE.exists():
        syms = _load()
        print(f"  F&O universe: {len(syms)} symbols  (stale cache fallback)")
        return syms

    raise RuntimeError("F&O symbol list unavailable: no cache and NSE fetch failed")


if __name__ == "__main__":
    syms = get_fno_symbols(force_refresh=True)
    print("\n".join(syms[:20]))
    print(f"... total: {len(syms)}")
