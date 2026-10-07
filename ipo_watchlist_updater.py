"""Append NSE EQ IPO symbols to both watchlists before the daily data fetch."""

from pathlib import Path
import re

import requests


PAGE_URL = 'https://www.nseindia.com/market-data/all-upcoming-issues-ipo'
API_URL = 'https://www.nseindia.com/api/all-upcoming-issues?category=ipo'
REPO_DIR = Path(__file__).resolve().parent
WATCHLIST_PATHS = [REPO_DIR / 'new_listings.txt', REPO_DIR / 'ipo_listings.txt']


def parse_eq_symbols(payload: object) -> list[str]:
    if not isinstance(payload, list) or any(not isinstance(row, dict) for row in payload):
        raise ValueError('Unexpected NSE IPO response: expected a list of issue objects')
    symbols = []
    for row in payload:
        if str(row.get('series', '')).strip().upper() != 'EQ':
            continue
        symbol = str(row.get('symbol') or '').strip().upper().removeprefix('NSE:')
        if not re.fullmatch(r'[A-Z0-9&._-]+', symbol):
            raise ValueError('NSE EQ issue has a missing or invalid symbol')
        if symbol not in symbols:
            symbols.append(symbol)
    return symbols


def fetch_eq_symbols() -> list[str]:
    with requests.Session() as session:
        session.headers.update({
            'User-Agent': 'Mozilla/5.0',
            'Referer': PAGE_URL,
            'Accept-Language': 'en-US,en;q=0.9',
        })
        # Warm up NSE cookies before requesting the page's JSON feed.
        session.get(PAGE_URL, timeout=30).raise_for_status()
        response = session.get(API_URL, timeout=30)
        response.raise_for_status()
        return parse_eq_symbols(response.json())


def append_missing(path: Path, symbols: list[str]) -> list[str]:
    original = path.read_bytes()
    existing = {
        line.strip().upper() for line in original.decode('utf-8-sig').splitlines()
        if line.strip() and not line.strip().startswith('#')
    }
    added = []
    for symbol in symbols:
        if symbol not in existing:
            added.append(symbol)
            existing.add(symbol)
    if added:
        separator = b'\n' if original and not original.endswith((b'\n', b'\r')) else b''
        with path.open('ab') as handle:
            handle.write(separator + ('\n'.join(added) + '\n').encode('utf-8'))
    return added


def main() -> int:
    try:
        symbols = fetch_eq_symbols()
        print(f'[ipo_watchlist_updater] NSE feed: {len(symbols)} EQ symbols')
        for path in WATCHLIST_PATHS:
            added = append_missing(path, symbols)
            print(f'[ipo_watchlist_updater] {path.name}: added {len(added)}'
                  + (f" ({', '.join(added)})" if added else ''))
    except (requests.RequestException, ValueError, OSError) as exc:
        print(f'[ipo_watchlist_updater] ERROR: {exc}')
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
