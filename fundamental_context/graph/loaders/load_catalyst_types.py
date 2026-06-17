"""
Load CatalystType nodes with SUBTYPE_OF hierarchy into Neo4j.
Each leaf node carries ep_probability and base_delta used by recompute_scores.py.

Run     : python load_catalyst_types.py
Re-run  : safe — idempotent via MERGE
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV = _HERE.parent.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")


# ── Catalyst type taxonomy ────────────────────────────────────────────────────
# Format: {name: {parent, ep_probability, base_delta, description}}
CATALYST_TYPES: dict[str, dict] = {
    # Root
    "Catalyst": {
        "parent": None,
        "ep_probability": None,
        "base_delta": 0,
        "description": "Root catalyst type — do not assign directly",
    },
    # Mid-level groups
    "RevenueVisibility": {
        "parent": "Catalyst",
        "ep_probability": "High",
        "base_delta": 9,
        "description": "Catalysts that extend revenue line-of-sight",
    },
    "PolicyCatalyst": {
        "parent": "Catalyst",
        "ep_probability": "Medium",
        "base_delta": 7,
        "description": "Government policy, approvals, and scheme inclusions",
    },
    "ManagementSignal": {
        "parent": "Catalyst",
        "ep_probability": "Medium",
        "base_delta": 5,
        "description": "Management actions signalling confidence",
    },
    "CorporateAction": {
        "parent": "Catalyst",
        "ep_probability": "Situational",
        "base_delta": 3,
        "description": "M&A, mergers, stake changes",
    },
    "NegativeCatalyst": {
        "parent": "Catalyst",
        "ep_probability": None,
        "base_delta": -15,
        "description": "Governance events that reduce conviction",
    },
    # RevenueVisibility leaves
    "OrderWin": {
        "parent": "RevenueVisibility",
        "ep_probability": "High",
        "base_delta": 10,
        "description": "New order, LoA, purchase order, work order awarded",
    },
    "CapacityExpansion": {
        "parent": "RevenueVisibility",
        "ep_probability": "Medium",
        "base_delta": 7,
        "description": "Greenfield / brownfield capacity addition announced or approved",
    },
    "EarningsBeat": {
        "parent": "RevenueVisibility",
        "ep_probability": "High",
        "base_delta": 8,
        "description": "Quarterly results beating consensus estimate (>15% beat)",
    },
    # PolicyCatalyst leaves
    "GovtApproval": {
        "parent": "PolicyCatalyst",
        "ep_probability": "High",
        "base_delta": 8,
        "description": "Regulatory, ministry, or SEBI approval unlocking business",
    },
    "PLIInclusion": {
        "parent": "PolicyCatalyst",
        "ep_probability": "Medium",
        "base_delta": 5,
        "description": "Company included in PLI scheme or similar govt incentive",
    },
    "SectorPolicy": {
        "parent": "PolicyCatalyst",
        "ep_probability": "Medium",
        "base_delta": 4,
        "description": "Budget allocation or policy announcement benefiting the sector",
    },
    # ManagementSignal leaves
    "PromotorBuy": {
        "parent": "ManagementSignal",
        "ep_probability": "Medium",
        "base_delta": 5,
        "description": "Promoter purchase, creeping acquisition, inter-se transfer",
    },
    "ManagementGuidanceRaise": {
        "parent": "ManagementSignal",
        "ep_probability": "High",
        "base_delta": 6,
        "description": "Management raises revenue or margin guidance in concall",
    },
    # CorporateAction leaves
    "M&A": {
        "parent": "CorporateAction",
        "ep_probability": "Situational",
        "base_delta": 3,
        "description": "Merger, acquisition, amalgamation, or stake acquisition",
    },
    # NegativeCatalyst leaves
    "GovernanceFlag": {
        "parent": "NegativeCatalyst",
        "ep_probability": None,
        "base_delta": -20,
        "description": "BSE query, SEBI notice, auditor resignation, qualified opinion",
    },
}


# ── Cypher ────────────────────────────────────────────────────────────────────
_MERGE_CT = """
MERGE (ct:CatalystType {name: $name})
  ON CREATE SET
    ct.ep_probability = $ep_probability,
    ct.base_delta     = $base_delta,
    ct.description    = $description
  ON MATCH SET
    ct.ep_probability = $ep_probability,
    ct.base_delta     = $base_delta,
    ct.description    = $description
"""

_LINK_SUBTYPE = """
MATCH (child:CatalystType  {name: $child})
MATCH (parent:CatalystType {name: $parent})
MERGE (child)-[:SUBTYPE_OF]->(parent)
"""


def main() -> None:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    count = 0
    with driver.session() as session:
        for name, meta in CATALYST_TYPES.items():
            session.run(
                _MERGE_CT,
                name=name,
                ep_probability=meta["ep_probability"],
                base_delta=meta["base_delta"],
                description=meta["description"],
            )
            print(f"[GRAPH] CatalystType MERGE | CatalystType | {name} | ok")
            count += 1

        for name, meta in CATALYST_TYPES.items():
            if meta["parent"]:
                session.run(_LINK_SUBTYPE, child=name, parent=meta["parent"])
                print(f"[GRAPH] SUBTYPE_OF | {name} -> {meta['parent']}")

    driver.close()
    print(f"[GRAPH] Summary | {count} catalyst types loaded")


if __name__ == "__main__":
    main()
