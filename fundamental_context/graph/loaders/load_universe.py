"""
Load NSE stock universe into Neo4j as Company, Industry, Sector nodes.

Source  : TradingView screener (MCap ₹800 Cr – ₹1 Lakh Cr, price > ₹50, NSE common equity)
Run     : python load_universe.py
Re-run  : safe — idempotent via MERGE
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase
from tradingview_screener import Query, col

# ── Config ────────────────────────────────────────────────────────────────────
MC_LOW  = 8_000_000_000        # ₹800 Cr  (in absolute INR)
MC_HIGH = 1_000_000_000_000    # ₹1 Lakh Cr

_ENV = Path(__file__).parent.parent.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI  = os.getenv("NEO4J_URI",      "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER",     "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")


# ── TradingView screener ──────────────────────────────────────────────────────
def fetch_universe() -> list[dict]:
    """Return [{nse_code, close, mcap, sector, industry}] from TradingView."""
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "market_cap_basic", "sector", "industry")
        .where(
            col("exchange")          == "NSE",
            col("type")              == "stock",
            col("typespecs").has(["common"]),
            col("close")             >  50,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(700)
        .get_scanner_data()
    )
    records: list[dict] = []
    for _, row in df.iterrows():
        records.append({
            "nse_code": str(row["name"]).strip(),
            "close":    float(row.get("close")              or 0),
            "mcap":     round(float(row.get("market_cap_basic") or 0) / 1e7, 2),  # -> ₹ Cr
            "sector":   str(row.get("sector")   or "Unknown").strip(),
            "industry": str(row.get("industry") or "Unknown").strip(),
        })
    return records


# ── Cypher templates ──────────────────────────────────────────────────────────
_MERGE_SECTOR = """
MERGE (s:Sector {name: $sector})
  ON CREATE SET s.policy_sensitivity = 'Medium'
"""

_MERGE_INDUSTRY = """
MERGE (i:Industry {name: $industry})
  ON CREATE SET i.sector = $sector
"""

_LINK_INDUSTRY_SECTOR = """
MATCH (i:Industry {name: $industry})
MATCH (s:Sector   {name: $sector})
MERGE (i)-[:PART_OF]->(s)
"""

_MERGE_COMPANY = """
MERGE (c:Company {nse_code: $nse_code})
  ON CREATE SET
    c.sector_name   = $sector,
    c.industry_name = $industry,
    c.close         = $close,
    c.mcap          = $mcap,
    c.updated_at    = date()
  ON MATCH SET
    c.close      = $close,
    c.mcap       = $mcap,
    c.updated_at = date()
"""

_LINK_COMPANY_INDUSTRY = """
MATCH (c:Company  {nse_code: $nse_code})
MATCH (i:Industry {name: $industry})
MERGE (c)-[:BELONGS_TO]->(i)
"""


# ── Loader ────────────────────────────────────────────────────────────────────
def load(records: list[dict]) -> tuple[int, int, int]:
    """Write records to Neo4j. Returns (companies, industries, sectors)."""
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    sectors:    set[str] = set()
    industries: set[str] = set()
    companies = 0

    with driver.session() as session:
        for r in records:
            sec = r["sector"]
            ind = r["industry"]

            if sec not in sectors:
                session.run(_MERGE_SECTOR, sector=sec)
                sectors.add(sec)

            if ind not in industries:
                session.run(_MERGE_INDUSTRY,       industry=ind, sector=sec)
                session.run(_LINK_INDUSTRY_SECTOR, industry=ind, sector=sec)
                industries.add(ind)

            session.run(_MERGE_COMPANY,        **r)
            session.run(_LINK_COMPANY_INDUSTRY, nse_code=r["nse_code"], industry=ind)
            print(f"[GRAPH] Company MERGE | Company | {r['nse_code']} | ok")
            companies += 1

    driver.close()
    return companies, len(industries), len(sectors)


def main() -> None:
    print("[GRAPH] Universe load starting...")
    records = fetch_universe()
    print(f"[GRAPH] TradingView screener | {len(records)} stocks fetched")
    if not records:
        print("ERROR: no records returned — check TradingView screener connectivity")
        sys.exit(1)
    companies, industries, sectors = load(records)
    print(
        f"[GRAPH] Summary | {companies} companies | "
        f"{industries} industries | {sectors} sectors"
    )


if __name__ == "__main__":
    main()
