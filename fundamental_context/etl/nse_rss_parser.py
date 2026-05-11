"""
NSE RSS Catalyst Parser

Fetches NSE corporate announcements RSS feed, classifies each announcement
into a CatalystType, and MERGEs Catalyst nodes + TRIGGERED edges into Neo4j.

Requires: feedparser, requests, neo4j, python-dotenv
Run     : python nse_rss_parser.py
Re-run  : safe — MERGE on catalyst_id deduplicates
"""
from __future__ import annotations

import hashlib
import os
import re
from datetime import date, datetime
from pathlib import Path
from email.utils import parsedate_to_datetime

import feedparser
import requests
from dotenv import load_dotenv
from neo4j import GraphDatabase

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV  = _HERE.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI  = os.getenv("NEO4J_URI",      "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER",     "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

NSE_HOMEPAGE = "https://www.nseindia.com"
NSE_RSS_URL  = "https://www.nseindia.com/static/rss-feed"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/rss+xml, application/xml, text/xml, */*",
}


# ── Keyword classifier (from 02_daily_pipeline.md) ───────────────────────────
KEYWORD_MAP: dict[str, list[str]] = {
    "OrderWin": [
        "order", "contract", "loa", "letter of award",
        "purchase order", "work order", "awarded", "secured order",
    ],
    "CapacityExpansion": [
        "capacity expansion", "greenfield", "brownfield",
        "new plant", "capex", "capital expenditure", "capacity addition",
    ],
    "GovtApproval": [
        "approval", "pli", "government", "ministry",
        "license", "clearance", "dpiit", "regulatory approval",
    ],
    "PromotorBuy": [
        "acquisition of shares", "inter-se transfer",
        "promoter purchase", "creeping acquisition",
    ],
    "M&A": [
        "merger", "acquisition", "amalgamation",
        "takeover", "stake acquisition",
    ],
    "GovernanceFlag": [
        "investigation", "bse query", "show cause",
        "sebi notice", "auditor resignation", "qualified opinion",
        "fraud", "default",
    ],
}


def classify(title: str, description: str) -> str | None:
    """Return catalyst type name or None if no match."""
    text = (title + " " + description).lower()
    for cat_type, keywords in KEYWORD_MAP.items():
        if any(kw in text for kw in keywords):
            return cat_type
    return None


# ── RSS fetch (NSE requires homepage-first cookie pattern) ────────────────────
def fetch_rss() -> list[feedparser.FeedParserDict]:
    """Fetch NSE RSS entries using session cookies from homepage."""
    session = requests.Session()
    session.headers.update(HEADERS)
    try:
        session.get(NSE_HOMEPAGE, timeout=10)  # seed cookies
        response = session.get(NSE_RSS_URL, timeout=15)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"[RSS] ERROR fetching NSE RSS: {exc}")
        return []

    feed = feedparser.parse(response.content)
    entries = feed.get("entries", [])
    print(f"[RSS] Fetched {len(entries)} NSE announcements")
    return entries


def _parse_date(entry) -> date:
    """Extract published date from RSS entry; fall back to today."""
    pub = entry.get("published", "")
    if pub:
        try:
            return parsedate_to_datetime(pub).date()
        except Exception:
            pass
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
    cat.type            = $cat_type,
    cat.date            = date($pub_date),
    cat.description     = $description,
    cat.source          = 'NSE RSS',
    cat.ep_probability  = $ep_probability,
    cat.conviction_delta = $conviction_delta,
    cat.magnitude       = 'Unknown'
  ON MATCH SET
    cat.description     = $description
WITH cat
MATCH (c:Company {nse_code: $nse_code})
MERGE (c)-[:TRIGGERED]->(cat)
"""


def process_entries(entries: list, session) -> tuple[int, int]:
    """Classify, match universe, and MERGE catalysts. Returns (matched, skipped)."""
    matched = 0
    skipped = 0

    for entry in entries:
        title       = entry.get("title", "")
        description = entry.get("summary", entry.get("description", ""))
        pub_date    = _parse_date(entry)

        # NSE RSS titles often start with the symbol, e.g. "WELCORP | Order win..."
        symbol_match = re.match(r"^([A-Z0-9&]+)\s*[|\-]", title)
        if not symbol_match:
            skipped += 1
            continue
        nse_code = symbol_match.group(1).strip()

        # Must be in graph universe
        if not session.run(_CHECK_COMPANY, nse_code=nse_code).single():
            skipped += 1
            continue

        cat_type = classify(title, description)
        if not cat_type:
            skipped += 1
            continue

        # Look up ep_probability and base_delta from CatalystType node
        ct_row = session.run(_LOOKUP_CT, name=cat_type).single()
        if ct_row:
            ep_prob          = ct_row["ep_prob"]
            conviction_delta = ct_row["base_delta"]
        else:
            ep_prob          = "Low"
            conviction_delta = 3

        catalyst_id = _make_catalyst_id(nse_code, cat_type, pub_date)
        result = session.run(
            _MERGE_CATALYST,
            catalyst_id     = catalyst_id,
            nse_code        = nse_code,
            cat_type        = cat_type,
            pub_date        = pub_date.isoformat(),
            description     = (title[:200] if title else description[:200]),
            ep_probability  = ep_prob,
            conviction_delta= conviction_delta,
        )
        counters = result.consume().counters
        action = "created" if counters.nodes_created > 0 else "updated"
        print(
            f"[GRAPH] Catalyst MERGE | {nse_code} | {cat_type} | {pub_date} | {action}"
        )
        matched += 1

    return matched, skipped


def main() -> None:
    entries = fetch_rss()
    if not entries:
        print("[RSS] No entries to process — check connectivity")
        return

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    with driver.session() as session:
        matched, skipped = process_entries(entries, session)
    driver.close()

    print(
        f"[RSS] Summary | {matched} catalysts created/updated | "
        f"{skipped} entries skipped (not in universe or unclassified)"
    )


if __name__ == "__main__":
    main()
