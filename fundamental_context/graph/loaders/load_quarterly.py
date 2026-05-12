"""
Quarterly Results Loader (screener.in)

For every company in the Neo4j universe, fetches the quarterly results table
from screener.in (standalone page) and creates/updates Quarter nodes + REPORTED
edges with YoY revenue and PAT growth as a beat-streak proxy.

Beat proxy: pat_yoy_pct > 0 is treated as beat_pct > 0 in recompute_scores.py
-> 3+ consecutive beats unlock +7 in the Earnings Quality layer.

Run  : python load_quarterly.py
Flags: --symbol RVNL   (single company)
       --limit  100    (process first N unprocessed)
Re-run: safe — MERGE is idempotent; cache skips already-done companies
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import time
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from neo4j import GraphDatabase

# ── Config ────────────────────────────────────────────────────────────────────
_HERE  = Path(__file__).parent
_ENV   = _HERE.parent.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI  = os.getenv("NEO4J_URI",      "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER",     "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")
SCR_EMAIL  = os.getenv("SCREENER_EMAIL",  "")
SCR_PASS   = os.getenv("SCREENER_PASSWORD", "")

SCREENER_BASE = "https://www.screener.in"
CACHE_FILE    = _HERE.parent.parent / "data" / "quarterly_cache.json"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36"
    ),
}


# ── Auth ──────────────────────────────────────────────────────────────────────
def make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update(HEADERS)
    lp   = s.get(f"{SCREENER_BASE}/login/", timeout=15)
    csrf = BeautifulSoup(lp.text, "html.parser").select_one("input[name=csrfmiddlewaretoken]")
    if not csrf:
        raise RuntimeError("Could not get CSRF token from screener.in")
    s.post(
        f"{SCREENER_BASE}/login/",
        data={
            "csrfmiddlewaretoken": csrf["value"],
            "username": SCR_EMAIL,
            "password": SCR_PASS,
            "next": "/",
        },
        headers={"Referer": f"{SCREENER_BASE}/login/"},
        timeout=15,
    )
    return s


# ── Quarter helpers ───────────────────────────────────────────────────────────
def _to_quarter_id(month_year: str) -> str | None:
    """'Jun 2024' -> 'Q1FY25'"""
    try:
        dt = datetime.strptime(month_year.strip(), "%b %Y")
    except ValueError:
        return None
    m, y = dt.month, dt.year
    if m <= 3:
        q, fy = 4, y
    elif m <= 6:
        q, fy = 1, y + 1
    elif m <= 9:
        q, fy = 2, y + 1
    else:
        q, fy = 3, y + 1
    return f"Q{q}FY{fy % 100:02d}"


def _parse_num(text: str) -> float | None:
    """'1,234' -> 1234.0; '' or '-' -> None"""
    cleaned = text.replace(",", "").replace("%", "").strip()
    if not cleaned or cleaned in ("-", "N/A", "--"):
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


# ── Scraper ───────────────────────────────────────────────────────────────────
def fetch_quarters(session: requests.Session, nse_code: str) -> dict[str, dict]:
    """
    Returns {quarter_id: {'revenue': float, 'pat': float}} for visible quarters.
    Uses the standalone (non-consolidated) page which renders without lazy-load.
    Falls back to /consolidated/ if standalone has no data.
    """
    for path in [f"/company/{nse_code}/", f"/company/{nse_code}/consolidated/"]:
        r = session.get(f"{SCREENER_BASE}{path}", timeout=15)
        if r.status_code != 200:
            continue
        soup = BeautifulSoup(r.text, "html.parser")
        sec  = soup.find(id="quarters")
        if not sec:
            continue
        table = sec.find("table")
        if not table:
            continue

        rows = table.find_all("tr")
        if len(rows) < 11:
            continue

        # Row 0: header row with quarter labels
        header_cells = [td.get_text(strip=True) for td in rows[0].find_all(["td", "th"])]
        # header_cells[0] is empty label column; [1:] are quarter labels
        quarter_labels = header_cells[1:]
        if not quarter_labels or not quarter_labels[0]:
            continue  # no data, try next path

        def _row_values(row_idx: int) -> list[float | None]:
            cells = [td.get_text(strip=True) for td in rows[row_idx].find_all(["td", "th"])]
            return [_parse_num(c) for c in cells[1:]]

        sales_vals  = _row_values(1)   # Sales+
        pat_vals    = _row_values(10)  # Net Profit+

        result: dict[str, dict] = {}
        for i, label in enumerate(quarter_labels):
            qid = _to_quarter_id(label)
            if not qid:
                continue
            rev = sales_vals[i] if i < len(sales_vals) else None
            pat = pat_vals[i]   if i < len(pat_vals)   else None
            if rev is not None or pat is not None:
                result[qid] = {"revenue": rev, "pat": pat, "label": label}

        if result:
            return result

    return {}


def compute_yoy(quarters: dict[str, dict]) -> dict[str, dict]:
    """
    Add pat_yoy_pct and revenue_yoy_pct to each quarter by matching with same
    quarter one fiscal year earlier (e.g. Q1FY25 vs Q1FY24).
    """
    # Parse FY and Q from each key
    def parse_qid(qid: str):
        m = re.match(r"Q(\d)FY(\d\d)", qid)
        if m:
            return int(m.group(1)), int(m.group(2))
        return None, None

    enriched = {k: dict(v) for k, v in quarters.items()}
    for qid, data in enriched.items():
        q, fy = parse_qid(qid)
        if q is None:
            continue
        prev_id = f"Q{q}FY{(fy - 1) % 100:02d}"
        prev = quarters.get(prev_id)
        if prev:
            if data.get("pat") is not None and prev.get("pat") and prev["pat"] != 0:
                data["pat_yoy_pct"] = round(
                    (data["pat"] - prev["pat"]) / abs(prev["pat"]) * 100, 1
                )
            if data.get("revenue") is not None and prev.get("revenue") and prev["revenue"] != 0:
                data["revenue_yoy_pct"] = round(
                    (data["revenue"] - prev["revenue"]) / abs(prev["revenue"]) * 100, 1
                )
    return enriched


# ── Neo4j writes ──────────────────────────────────────────────────────────────
_MERGE_QUARTER = """
MERGE (q:Quarter {quarter_id: $qid})
  ON CREATE SET
    q.period           = $period,
    q.revenue          = $revenue,
    q.pat              = $pat,
    q.pat_yoy_pct      = $pat_yoy_pct,
    q.revenue_yoy_pct  = $rev_yoy_pct,
    q.beat_pct         = $pat_yoy_pct,
    q.source           = 'screener_quarterly'
  ON MATCH SET
    q.revenue          = $revenue,
    q.pat              = $pat,
    q.pat_yoy_pct      = $pat_yoy_pct,
    q.revenue_yoy_pct  = $rev_yoy_pct,
    q.beat_pct         = $pat_yoy_pct
WITH q
MATCH (c:Company {nse_code: $nse_code})
MERGE (c)-[:REPORTED]->(q)
"""

def write_quarters(nse_code: str, quarters: dict[str, dict], session) -> int:
    written = 0
    for qid, data in quarters.items():
        # Only write last 5 quarters (to keep graph lean — we only need 4 for beat_streak)
        pat_yoy = data.get("pat_yoy_pct")
        rev_yoy = data.get("revenue_yoy_pct")
        session.run(
            _MERGE_QUARTER,
            qid        = f"{nse_code}_{qid}",
            period     = qid,
            nse_code   = nse_code,
            revenue    = data.get("revenue"),
            pat        = data.get("pat"),
            pat_yoy_pct = pat_yoy,
            rev_yoy_pct = rev_yoy,
        )
        written += 1
    return written


# ── Cache ─────────────────────────────────────────────────────────────────────
def load_cache() -> dict:
    if CACHE_FILE.exists():
        with open(CACHE_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache: dict) -> None:
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2)


# ── Recompute trigger ─────────────────────────────────────────────────────────
def _rescore(nse_code: str) -> None:
    try:
        etl  = _HERE.parent.parent / "etl" / "recompute_scores.py"
        spec = importlib.util.spec_from_file_location("recompute_scores", etl)
        mod  = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.run(nse_code)
    except Exception as exc:
        print(f"  [SCORES] recompute skipped: {exc}")


# ── Main ──────────────────────────────────────────────────────────────────────
def run(symbol: str | None = None, limit: int | None = None) -> None:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))

    with driver.session() as neo:
        if symbol:
            rows = list(neo.run(
                "MATCH (c:Company {nse_code: $s}) RETURN c.nse_code AS code", s=symbol
            ))
        else:
            rows = list(neo.run(
                "MATCH (c:Company) WHERE c.roe_3yr_avg IS NOT NULL "
                "RETURN c.nse_code AS code ORDER BY c.nse_code"
            ))

    codes = [r["code"] for r in rows]
    print(f"[QUARTERLY] {len(codes)} companies to process")

    cache   = load_cache()
    session = make_session()
    print(f"[QUARTERLY] Authenticated as {SCR_EMAIL}")

    processed = 0
    for nse_code in codes:
        if limit and processed >= limit:
            break
        if nse_code in cache and not symbol:
            continue

        print(f"\n[QUARTERLY] {nse_code}...", end=" ", flush=True)

        quarters = fetch_quarters(session, nse_code)
        if not quarters:
            print("no data")
            cache[nse_code] = {"status": "no_data"}
            save_cache(cache)
            processed += 1
            time.sleep(0.5)
            continue

        enriched = compute_yoy(quarters)

        # Keep only the last 5 quarters (most recent — have YoY data)
        yoy_quarters = {k: v for k, v in enriched.items() if "pat_yoy_pct" in v}
        recent_keys  = sorted(yoy_quarters.keys())[-5:]  # oldest to newest
        recent       = {k: yoy_quarters[k] for k in recent_keys}

        with driver.session() as neo:
            written = write_quarters(nse_code, recent, neo)

        beats = sum(1 for v in recent.values() if (v.get("pat_yoy_pct") or 0) > 0)
        print(f"{len(recent)} quarters | {beats} beats | "
              f"latest: {sorted(recent.keys())[-1] if recent else '-'}")
        if recent:
            latest_q = sorted(recent.keys())[-1]
            d = recent[latest_q]
            print(f"  revenue={d.get('revenue')} pat={d.get('pat')} "
                  f"pat_yoy={d.get('pat_yoy_pct')}%")

        cache[nse_code] = {"status": "done", "quarters": len(recent), "beats": beats}
        save_cache(cache)
        _rescore(nse_code)
        processed += 1
        time.sleep(0.8)

    driver.close()
    print(f"\n[QUARTERLY] Done — {processed} processed, {len(cache)} total in cache")


def main() -> None:
    parser = argparse.ArgumentParser(description="Load screener.in quarterly results")
    parser.add_argument("--symbol", help="Single NSE symbol")
    parser.add_argument("--limit",  type=int, help="Max companies this run")
    args = parser.parse_args()
    run(symbol=args.symbol, limit=args.limit)


if __name__ == "__main__":
    main()
