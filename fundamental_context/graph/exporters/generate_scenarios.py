"""
Generate macro scenario JSON files for the GitHub Pages Macro Simulator.

For each theme (root + leaves), queries Neo4j for Tier 1 and Tier 2 beneficiaries,
then calls Claude API (Haiku — cheap/fast) for a Vikram-style 2-line verdict.

Output: project_root/graph_data/scenarios/{theme_slug}.json

Run: python generate_scenarios.py
"""

from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase

try:
    import anthropic

    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV = _HERE.parent.parent / ".env"
_ROOT = _HERE.parent.parent.parent
_OUT_DIR = _ROOT / "graph_data" / "scenarios"
_OUT_DIR.mkdir(parents=True, exist_ok=True)

load_dotenv(_ENV)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")

HAIKU_MODEL = "claude-haiku-4-5-20251001"


# ── Neo4j queries ─────────────────────────────────────────────────────────────
_Q_ALL_THEMES = "MATCH (t:Theme) RETURN t.name AS name ORDER BY t.name"

_Q_TIER1 = """
MATCH (target:Theme {name: $theme})
OPTIONAL MATCH (sub:Theme)-[:SUBTHEME_OF*0..]->(target)
WITH collect(DISTINCT coalesce(sub, target)) AS theme_family
UNWIND theme_family AS t
MATCH (c:Company)-[:BENEFITS_FROM]->(t)
WHERE c.conviction_score IS NOT NULL
RETURN DISTINCT
  c.nse_code         AS symbol,
  c.name             AS name,
  c.conviction_score AS conviction,
  c.quality_score    AS quality,
  t.name             AS via_theme
ORDER BY c.conviction_score DESC
LIMIT 20
"""

_Q_TIER2 = """
MATCH (target:Theme {name: $theme})
OPTIONAL MATCH (sub:Theme)-[:SUBTHEME_OF*0..]->(target)
WITH collect(DISTINCT coalesce(sub, target)) AS theme_family
UNWIND theme_family AS t
MATCH (supplier:Company)-[:SUPPLIES_TO*1..2]->(c:Company)-[:BENEFITS_FROM]->(t)
WHERE supplier.conviction_score IS NOT NULL
  AND NOT EXISTS {
    MATCH (supplier)-[:BENEFITS_FROM]->(any_t:Theme)
    WHERE any_t IN theme_family
  }
RETURN DISTINCT
  supplier.nse_code  AS symbol,
  supplier.name      AS name,
  supplier.conviction_score AS conviction,
  c.nse_code         AS via_company
ORDER BY supplier.conviction_score DESC
LIMIT 10
"""


# ── Claude API verdict ────────────────────────────────────────────────────────
def _vikram_verdict(theme: str, tier1: list[dict]) -> str:
    if not ANTHROPIC_AVAILABLE or not ANTHROPIC_KEY or not tier1:
        return f"Theme '{theme}' activated — check top beneficiaries for entry opportunities."

    top5 = tier1[:5]
    stocks_str = ", ".join(
        f"{r['symbol']} (conviction {r['conviction']}, via {r['via_theme']})"
        for r in top5
    )
    prompt = (
        f"You are Vikram Iyer, 30-year Indian equity veteran. "
        f"A macro event related to '{theme}' just occurred. "
        f"Top beneficiaries: {stocks_str}. "
        f"In exactly 2 lines, give your investment verdict: "
        f"which stock to focus on and the key number to watch. "
        f"Format: [stock] — [reason] — [key metric]. Be blunt."
    )
    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
        msg = client.messages.create(
            model=HAIKU_MODEL,
            max_tokens=150,
            messages=[{"role": "user", "content": prompt}],
        )
        return msg.content[0].text.strip()
    except Exception as exc:
        return f"Vikram verdict unavailable: {exc}"


# ── Main ──────────────────────────────────────────────────────────────────────
def _slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def main() -> None:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    generated = 0

    with driver.session() as session:
        themes = [row["name"] for row in session.run(_Q_ALL_THEMES)]
        print(f"[SCENARIOS] Generating for {len(themes)} themes...")

        for theme in themes:
            tier1 = [dict(r) for r in session.run(_Q_TIER1, theme=theme)]
            tier2 = [dict(r) for r in session.run(_Q_TIER2, theme=theme)]

            if not tier1 and not tier2:
                continue  # no companies wired to this theme yet

            verdict = _vikram_verdict(theme, tier1)
            time.sleep(0.3)  # rate limit buffer for Haiku

            scenario = {
                "theme": theme,
                "tier1": tier1,
                "tier2": tier2,
                "vikram_verdict": verdict,
                "generated_date": __import__("datetime").date.today().isoformat(),
            }

            slug = _slugify(theme)
            out_path = _OUT_DIR / f"{slug}.json"
            out_path.write_text(
                json.dumps(scenario, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            print(
                f"[SCENARIOS] {theme} -> {slug}.json ({len(tier1)} T1, {len(tier2)} T2)"
            )
            generated += 1

    driver.close()
    print(f"[SCENARIOS] Done — {generated} scenario files written to {_OUT_DIR}")


if __name__ == "__main__":
    main()
