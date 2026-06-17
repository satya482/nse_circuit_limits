"""
Export Neo4j graph data to static JSON files for GitHub Pages.

Outputs (all written to project_root/graph_data/):
  graph.json        — Cytoscape.js nodes + edges
  catalysts.json    — last 30 days of Catalyst nodes
  ep_watchlist.json — current EP candidates from today's ep_watchlist CSV
  themes.json       — Theme hierarchy + linked companies

Run: python export_to_json.py
"""

from __future__ import annotations

import csv
import json
import os
from datetime import date
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV = _HERE.parent.parent / ".env"
_ROOT = _HERE.parent.parent.parent  # nse_circuit_limits/
_OUT_DIR = _ROOT / "graph_data"
_OUT_DIR.mkdir(exist_ok=True)

load_dotenv(_ENV)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

# EP watchlist from today's run
_EP_DIR = _HERE.parent.parent / "data" / "processed"


# ── Queries ───────────────────────────────────────────────────────────────────
_Q_COMPANIES = """
MATCH (c:Company)
WHERE c.conviction_score IS NOT NULL
OPTIONAL MATCH (c)-[:BELONGS_TO]->(i:Industry)
OPTIONAL MATCH (i)-[:PART_OF]->(s:Sector)
RETURN
  c.nse_code         AS id,
  c.name             AS name,
  c.conviction_score AS conviction,
  c.quality_score    AS quality,
  c.mcap             AS mcap,
  c.order_book_to_revenue_ratio AS ob_ratio,
  c.sector_name      AS sector,
  i.name             AS industry
"""

_Q_THEME_EDGES = """
MATCH (c:Company)-[:BENEFITS_FROM]->(t:Theme)
WHERE c.conviction_score IS NOT NULL
RETURN c.nse_code AS company, t.name AS theme
"""

_Q_SUPPLY_EDGES = """
MATCH (a:Company)-[r:SUPPLIES_TO]->(b:Company)
WHERE a.conviction_score IS NOT NULL AND b.conviction_score IS NOT NULL
RETURN a.nse_code AS source, b.nse_code AS target, r.product AS product
"""

_Q_SECTOR_NODES = """
MATCH (s:Sector)
RETURN s.name AS name
"""

_Q_THEME_NODES = """
MATCH (t:Theme)
OPTIONAL MATCH (child:Theme)-[:SUBTHEME_OF]->(t)
WITH t, collect(child.name) AS children
OPTIONAL MATCH (c:Company)-[:BENEFITS_FROM]->(t)
RETURN
  t.name          AS name,
  t.theme_maturity AS maturity,
  t.vikram_thesis  AS thesis,
  children,
  collect({
    id:         c.nse_code,
    name:       c.name,
    conviction: c.conviction_score,
    quality:    c.quality_score
  }) AS companies
"""

_Q_CATALYSTS = """
MATCH (c:Company)-[:TRIGGERED]->(cat:Catalyst)
WHERE cat.date >= date() - duration('P30D')
RETURN
  c.nse_code        AS symbol,
  c.name            AS company,
  c.conviction_score AS conviction,
  cat.type          AS type,
  toString(cat.date) AS date,
  cat.magnitude     AS magnitude,
  cat.ep_probability AS ep_prob,
  cat.description   AS description
ORDER BY cat.date DESC
"""


# ── Helpers ───────────────────────────────────────────────────────────────────
def _safe(v):
    """Convert Neo4j temporal types and Nones for JSON serialisation."""
    if v is None:
        return None
    if hasattr(v, "isoformat"):
        return v.isoformat()
    return v


# ── Exporters ─────────────────────────────────────────────────────────────────
def export_graph(session) -> None:
    """Build Cytoscape.js graph.json — companies, themes, sectors as nodes + edges."""
    nodes: list[dict] = []
    edges: list[dict] = []
    seen_nodes: set[str] = set()

    def add_node(node_id: str, data: dict) -> None:
        if node_id not in seen_nodes:
            nodes.append({"data": {"id": node_id, **data}})
            seen_nodes.add(node_id)

    # Company nodes
    for row in session.run(_Q_COMPANIES):
        conviction = _safe(row["conviction"]) or 0
        add_node(
            row["id"],
            {
                "label": row["id"],
                "name": row["name"] or row["id"],
                "type": "Company",
                "conviction": conviction,
                "quality": _safe(row["quality"]) or 0,
                "mcap": _safe(row["mcap"]) or 0,
                "ob_ratio": _safe(row["ob_ratio"]),
                "sector": row["sector"] or "Unknown",
                "industry": row["industry"] or "Unknown",
            },
        )
        # Sector node + edge
        if row["sector"]:
            add_node(row["sector"], {"label": row["sector"], "type": "Sector"})
            edges.append(
                {
                    "data": {
                        "id": f"{row['id']}_{row['sector']}",
                        "source": row["id"],
                        "target": row["sector"],
                        "rel": "BELONGS_TO",
                    }
                }
            )

    # Theme nodes + BENEFITS_FROM edges
    for row in session.run(_Q_THEME_NODES):
        add_node(
            row["name"],
            {
                "label": row["name"],
                "type": "Theme",
                "maturity": row["maturity"],
                "thesis": row["thesis"],
            },
        )

    for row in session.run(_Q_THEME_EDGES):
        edge_id = f"{row['company']}_BF_{row['theme']}"
        edges.append(
            {
                "data": {
                    "id": edge_id,
                    "source": row["company"],
                    "target": row["theme"],
                    "rel": "BENEFITS_FROM",
                }
            }
        )

    # SUPPLIES_TO edges
    for row in session.run(_Q_SUPPLY_EDGES):
        edge_id = f"{row['source']}_ST_{row['target']}"
        edges.append(
            {
                "data": {
                    "id": edge_id,
                    "source": row["source"],
                    "target": row["target"],
                    "rel": "SUPPLIES_TO",
                    "product": row["product"],
                }
            }
        )

    out = {"nodes": nodes, "edges": edges}
    path = _OUT_DIR / "graph.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[EXPORT] graph.json -> {len(nodes)} nodes, {len(edges)} edges")


def export_catalysts(session) -> None:
    """Export last 30 days of Catalyst nodes."""
    catalysts = []
    for row in session.run(_Q_CATALYSTS):
        catalysts.append({k: _safe(v) for k, v in row.items()})

    path = _OUT_DIR / "catalysts.json"
    path.write_text(
        json.dumps(catalysts, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"[EXPORT] catalysts.json -> {len(catalysts)} entries")


def export_themes(session) -> None:
    """Export theme hierarchy + linked companies."""
    themes = []
    for row in session.run(_Q_THEME_NODES):
        companies = [
            {k: _safe(v) for k, v in c.items()}
            for c in (row["companies"] or [])
            if c.get("id")
        ]
        companies.sort(key=lambda x: x.get("conviction") or 0, reverse=True)
        themes.append(
            {
                "name": row["name"],
                "maturity": row["maturity"],
                "thesis": row["thesis"],
                "children": row["children"] or [],
                "companies": companies,
            }
        )

    path = _OUT_DIR / "themes.json"
    path.write_text(json.dumps(themes, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[EXPORT] themes.json -> {len(themes)} themes")


def export_ep_watchlist() -> None:
    """Copy today's EP watchlist CSV to graph_data/ep_watchlist.json."""
    today_str = date.today().isoformat()
    csv_path = _EP_DIR / f"ep_watchlist_{today_str}.csv"

    if not csv_path.exists():
        print(
            f"[EXPORT] ep_watchlist.json — no CSV for today ({csv_path.name}), skipping"
        )
        (_OUT_DIR / "ep_watchlist.json").write_text("[]", encoding="utf-8")
        return

    records = []
    with open(csv_path, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            records.append(row)

    path = _OUT_DIR / "ep_watchlist.json"
    path.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[EXPORT] ep_watchlist.json -> {len(records)} candidates")


def main() -> None:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    with driver.session() as session:
        export_graph(session)
        export_catalysts(session)
        export_themes(session)
    driver.close()

    export_ep_watchlist()
    print("[EXPORT] All graph_data/ files written")


if __name__ == "__main__":
    main()
