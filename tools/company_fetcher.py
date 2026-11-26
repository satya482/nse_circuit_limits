#!/usr/bin/env python3
"""
Monthly company description fetcher.
Phase 1a: discover NSE common equities (price >25, MCap 1000cr-5lakh cr).
Phase 1b: fetch descriptions from trendlyne.com + screener.in, cache as JSON.

Usage:
    python tools/company_fetcher.py              # fetch all stale/missing
    python tools/company_fetcher.py --symbols KRN ICICIBANK   # specific symbols
    python tools/company_fetcher.py --force      # re-fetch even if fresh

Cache: .company_cache/{SYMBOL}.json  (gitignored, 30-day stale threshold)
"""

import argparse
import json
import random
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tradingview_screener import Query, col

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_DIR))
CACHE_DIR = REPO_DIR / ".company_cache"
TOOLS_DIR = Path(__file__).parent
ID_MAP_FILE = TOOLS_DIR / "trendlyne_id_map.json"
UNIVERSE_OUT = TOOLS_DIR / "sector_rotation_universe.json"

STALE_DAYS = 30
MC_LOW = 1000 * 10_000_000
MC_HIGH = 500000 * 10_000_000
MIN_PRICE = 25

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# ── Universe ───────────────────────────────────────────────────────────────────


def fetch_universe() -> list[dict]:
    """Return list of {symbol, name} from TradingView screener."""
    print("Fetching universe from TradingView screener...")
    from cluster_membership import atomic_json, is_eligible

    stocks = {}
    offset = 0
    expected = None
    while True:
        total, df = (
            Query().set_markets("india")
            .select("name", "description", "market_cap_basic", "close")
            .where(col("exchange") == "NSE", col("type") == "stock",
                   col("typespecs").has(["common"]), col("close") > MIN_PRICE,
                   col("market_cap_basic").between(MC_LOW, MC_HIGH))
            .order_by("name").offset(offset).limit(offset + 1000)
            .get_scanner_data(timeout=45)
        )
        if expected is None:
            expected = total
        if total != expected or not total or df.empty:
            raise ValueError("Empty or changing cluster universe; previous snapshot preserved")
        for _, row in df.iterrows():
            entry = {"symbol": str(row["name"]).strip().upper(),
                     "name": str(row.get("description", row["name"])),
                     "price": float(row["close"]), "market_cap": float(row["market_cap_basic"])}
            if not entry["symbol"] or not is_eligible(entry) or entry["symbol"] in stocks:
                raise ValueError("Invalid or duplicate cluster universe row")
            stocks[entry["symbol"]] = entry
        offset += len(df)
        if offset >= expected:
            break
    if len(stocks) != expected:
        raise ValueError("Incomplete cluster universe; previous snapshot preserved")
    stocks = sorted(stocks.values(), key=lambda row: row["symbol"])
    print(f"  Universe: {len(stocks)} stocks")

    atomic_json(UNIVERSE_OUT, {"fetched_at": _now_iso(), "count": len(stocks), "stocks": stocks})
    return stocks


# ── Cache helpers ──────────────────────────────────────────────────────────────


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _cache_path(symbol: str) -> Path:
    return CACHE_DIR / f"{symbol}.json"


def _is_fresh(symbol: str) -> bool:
    p = _cache_path(symbol)
    if not p.exists():
        return False
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        fetched = datetime.fromisoformat(data.get("fetched_at", "2000-01-01"))
        if fetched.tzinfo is None:
            fetched = fetched.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - fetched) < timedelta(days=STALE_DAYS)
    except Exception:
        return False


# ── Trendlyne fetcher ──────────────────────────────────────────────────────────


def _trendlyne_url(symbol: str, id_map: dict) -> str | None:
    entry = id_map.get(symbol)
    if not entry:
        return None
    tid, slug = entry["id"], entry["slug"]
    return f"https://trendlyne.com/equity/{tid}/{symbol}/{slug}/"


def fetch_trendlyne(symbol: str, id_map: dict) -> str:
    url = _trendlyne_url(symbol, id_map)
    if not url:
        return ""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            return ""
        soup = BeautifulSoup(resp.text, "html.parser")

        # Support both legacy CSS and the current generated CSS-module prefix.
        el = soup.select_one('span.abt-desc-wrapper, span[class$="__abt-desc-wrapper"]')
        if el:
            return el.get_text(separator=" ", strip=True)

        # Fallback: h3 inside div.about
        el = soup.select_one("div.about h3")
        if el:
            text = el.get_text(separator=" ", strip=True)
            if len(text) > 50:
                return text

        return ""
    except Exception as e:
        print(f"    [trendlyne] {symbol}: {e}")
        return ""


# ── Screener.in fetcher ────────────────────────────────────────────────────────


def fetch_screener(symbol: str) -> tuple[str, list[str]]:
    """Return (description, peers_list)."""
    url = f"https://www.screener.in/company/{symbol}/"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            return "", []
        soup = BeautifulSoup(resp.text, "html.parser")

        description = ""
        # Try multiple selectors in order (confirmed: div.about p works)
        for sel in [
            "div.about p",
            "div.company-profile div.about p",
            "section.about-section p",
            "div.company-about p",
        ]:
            el = soup.select_one(sel)
            if el:
                text = el.get_text(separator=" ", strip=True)
                if len(text) > 50:
                    description = text
                    break

        # Screener peer table: links in the peers section
        peers: list[str] = []
        peer_section = soup.select_one("div#peers table") or soup.select_one(
            "table.peers"
        )
        if peer_section:
            for a in peer_section.select("a[href*='/company/']"):
                href = a.get("href", "")
                parts = [p for p in href.split("/") if p]
                # href like /company/SYMBOL/
                if len(parts) >= 2 and parts[0] == "company":
                    peer_sym = parts[1].upper()
                    if peer_sym and peer_sym != symbol:
                        peers.append(peer_sym)

        return description, peers[:20]
    except Exception as e:
        print(f"    [screener] {symbol}: {e}")
        return "", []


# ── Merge + save ───────────────────────────────────────────────────────────────


def _combine(*texts: str) -> str:
    seen, parts = set(), []
    for t in texts:
        t = t.strip()
        if t and t not in seen:
            seen.add(t)
            parts.append(t)
    return " ".join(parts)


def fetch_and_cache(symbol: str, name: str, id_map: dict) -> dict:
    print(f"  {symbol} ...", end=" ", flush=True)

    tl_desc = fetch_trendlyne(symbol, id_map)
    time.sleep(3 + random.uniform(0, 1))  # trendlyne: 3–4s

    sc_desc, sc_peers = fetch_screener(symbol)
    time.sleep(2 + random.uniform(0, 1))  # screener.in: 2–3s

    sources = []
    if tl_desc:
        sources.append("trendlyne")
    if sc_desc:
        sources.append("screener")

    combined = _combine(tl_desc, sc_desc)

    path = _cache_path(symbol)
    if len(combined.strip()) < 40 and path.exists():
        previous = json.loads(path.read_text(encoding="utf-8"))
        if len(previous.get("combined_description", "").strip()) >= 40:
            print("fetch failed; retained previous description")
            return previous

    entry = {
        "symbol": symbol,
        "name": name,
        "trendlyne_description": tl_desc,
        "screener_description": sc_desc,
        "combined_description": combined,
        "screener_peers": sc_peers,
        "fetched_at": _now_iso(),
        "sources": sources,
    }

    from cluster_membership import atomic_json
    atomic_json(path, entry)

    status = f"trendlyne={bool(tl_desc)} screener={bool(sc_desc)}"
    print(status)
    return entry


# ── Main ───────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbols", nargs="+", help="Specific symbols to fetch")
    parser.add_argument(
        "--force", action="store_true", help="Re-fetch even if cache is fresh"
    )
    args = parser.parse_args()

    CACHE_DIR.mkdir(exist_ok=True)

    if not ID_MAP_FILE.exists():
        print(
            f"ERROR: {ID_MAP_FILE} not found. Run tools/build_trendlyne_map.py first."
        )
        return 1

    id_map = json.loads(ID_MAP_FILE.read_text(encoding="utf-8"))

    if args.symbols:
        stocks = [{"symbol": s, "name": s} for s in args.symbols]
    else:
        stocks = fetch_universe()

    total = len(stocks)
    fetched = 0
    skipped = 0

    for i, stock in enumerate(stocks, 1):
        sym = stock["symbol"]
        name = stock.get("name", sym)

        if not args.force and _is_fresh(sym):
            skipped += 1
            continue

        print(f"[{i}/{total}]", end=" ")
        fetch_and_cache(sym, name, id_map)
        fetched += 1

    print(f"\nDone. Fetched={fetched}  Skipped(fresh)={skipped}  Total={total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
