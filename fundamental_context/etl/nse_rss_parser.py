"""
NSE Corporate Announcements Catalyst Parser

Fetches the NSE corporate-announcements JSON API (returns ~20 most recent
across all equities), classifies each announcement into a CatalystType, and
MERGEs Catalyst nodes + TRIGGERED edges into Neo4j.

Run daily after market close (5:00–5:15 PM IST); run multiple times safely —
MERGE on catalyst_id deduplicates.

Requires: requests, neo4j, python-dotenv
Run     : python nse_rss_parser.py
"""

from __future__ import annotations

import hashlib
import os
from datetime import date, datetime
from pathlib import Path

import requests
from dotenv import load_dotenv
from neo4j import GraphDatabase

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV = _HERE.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

NSE_HOMEPAGE = "https://www.nseindia.com"
NSE_API_URL = "https://www.nseindia.com/api/corporate-announcements?index=equities"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.nseindia.com/",
}


# ── Keyword classifier ────────────────────────────────────────────────────────
# Matches against: desc (category) + attchmntText (summary sentence)
KEYWORD_MAP: dict[str, list[str]] = {
    "OrderWin": [
        "order",
        "contract",
        "loa",
        "letter of award",
        "purchase order",
        "work order",
        "awarded",
        "secured order",
        "bagged",
        "new orders",
        "order win",
    ],
    "CapacityExpansion": [
        "capacity expansion",
        "greenfield",
        "brownfield",
        "new plant",
        "capex",
        "capital expenditure",
        "capacity addition",
        "new facility",
        "manufacturing unit",
    ],
    "GovtApproval": [
        "pli",
        "production linked incentive",
        "ministry",
        "license",
        "clearance",
        "dpiit",
        "regulatory approval",
        "government approval",
        "govt approval",
        "noc",
    ],
    "PromotorBuy": [
        "acquisition of shares by promoter",
        "inter-se transfer",
        "promoter purchase",
        "creeping acquisition",
        "insider buying",
    ],
    "M&A": [
        "merger",
        "acquisition",
        "amalgamation",
        "takeover",
        "stake acquisition",
        "demerger",
        "business transfer",
        "slump sale",
    ],
    "GovernanceFlag": [
        "investigation",
        "show cause",
        "sebi notice",
        "auditor resignation",
        "qualified opinion",
        "fraud",
        "default",
        "non-payment",
        "bse query",
        "promoter pledge",
    ],
}


def classify(desc: str, text: str) -> str | None:
    """Return catalyst type name or None if no match."""
    combined = (desc + " " + text).lower()
    for cat_type, keywords in KEYWORD_MAP.items():
        if any(kw in combined for kw in keywords):
            return cat_type
    return None


# ── NSE API fetch ─────────────────────────────────────────────────────────────
def fetch_announcements() -> list[dict]:
    """Fetch NSE corporate announcements via JSON API."""
    session = requests.Session()
    session.headers.update(HEADERS)
    try:
        session.get(NSE_HOMEPAGE, timeout=10)  # seed cookies
        response = session.get(NSE_API_URL, timeout=15)
        response.raise_for_status()
        data = response.json()
        print(f"[NSE] Fetched {len(data)} announcements")
        return data if isinstance(data, list) else []
    except Exception as exc:
        print(f"[NSE] ERROR fetching announcements: {exc}")
        return []


def _parse_date(entry: dict) -> date:
    """Parse sort_date or an_dt field; fall back to today."""
    for field in ("sort_date", "an_dt"):
        val = entry.get(field, "")
        if val:
            for fmt in ("%Y-%m-%d %H:%M:%S", "%d-%b-%Y %H:%M:%S"):
                try:
                    return datetime.strptime(val[:19], fmt).date()
                except ValueError:
                    continue
    return date.today()


def _make_catalyst_id(nse_code: str, cat_type: str, pub_date: date) -> str:
    raw = f"{nse_code}:{cat_type}:{pub_date.isoformat()}"
    return hashlib.md5(raw.encode()).hexdigest()


# ── Neo4j writes ──────────────────────────────────────────────────────────────
_CHECK_COMPANY = """
MATCH (c:Company {nse_code: $nse_code}) RETURN c.nse_code AS code LIMIT 1
"""

_LOOKUP_CT = """
MATCH (ct:CatalystType {name: $name})
RETURN ct.ep_probability AS ep_prob, ct.base_delta AS base_delta
"""

_MERGE_CATALYST = """
MERGE (cat:Catalyst {catalyst_id: $catalyst_id})
  ON CREATE SET
    cat.type             = $cat_type,
    cat.date             = date($pub_date),
    cat.description      = $description,
    cat.source           = 'NSE API',
    cat.ep_probability   = $ep_probability,
    cat.conviction_delta = $conviction_delta,
    cat.magnitude        = 'Unknown'
  ON MATCH SET
    cat.description      = $description
WITH cat
MATCH (c:Company {nse_code: $nse_code})
MERGE (c)-[:TRIGGERED]->(cat)
"""


def process_announcements(entries: list[dict], session) -> tuple[int, int]:
    """Classify, match universe, MERGE catalysts. Returns (matched, skipped)."""
    matched = 0
    skipped = 0

    for entry in entries:
        nse_code = (entry.get("symbol") or "").strip().upper()
        if not nse_code:
            skipped += 1
            continue

        # Must be in graph universe
        if not session.run(_CHECK_COMPANY, nse_code=nse_code).single():
            skipped += 1
            continue

        desc = entry.get("desc", "")
        text = entry.get("attchmntText", "")
        pub_date = _parse_date(entry)

        cat_type = classify(desc, text)
        if not cat_type:
            skipped += 1
            continue

        # Look up ep_probability and base_delta from CatalystType node
        ct_row = session.run(_LOOKUP_CT, name=cat_type).single()
        if ct_row:
            ep_prob = ct_row["ep_prob"]
            conviction_delta = ct_row["base_delta"]
        else:
            ep_prob = "Low"
            conviction_delta = 3

        # Combine desc + first 200 chars of text for description field
        description = f"{desc}: {text[:180]}" if text else desc

        catalyst_id = _make_catalyst_id(nse_code, cat_type, pub_date)
        result = session.run(
            _MERGE_CATALYST,
            catalyst_id=catalyst_id,
            nse_code=nse_code,
            cat_type=cat_type,
            pub_date=pub_date.isoformat(),
            description=description[:300],
            ep_probability=ep_prob,
            conviction_delta=conviction_delta,
        )
        counters = result.consume().counters
        action = "created" if counters.nodes_created > 0 else "exists"
        print(
            f"[GRAPH] Catalyst MERGE | {nse_code} | {cat_type} | {pub_date} | {action}"
        )
        matched += 1

    return matched, skipped


def main() -> None:
    entries = fetch_announcements()
    if not entries:
        print("[NSE] No entries to process — check connectivity")
        return

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    with driver.session() as session:
        matched, skipped = process_announcements(entries, session)
    driver.close()

    print(
        f"[NSE] Summary | {matched} catalysts created/updated | "
        f"{skipped} entries skipped (not in universe or unclassified)"
    )


if __name__ == "__main__":
    main()
