"""
Telegram Themes → Knowledge Graph Loader

Reads telegram_themes/themes_YYYY-MM-DD.json (today by default) and:
  - MERGEs Theme nodes for each extracted theme
  - MERGEs BENEFITS_FROM edges between Company and Theme nodes
    (only for companies that already exist in the KG universe)
  - Tags edges with source="telegram", conviction, sentiment, report_date

Run  : python telegram_kg_loader.py
       python telegram_kg_loader.py --date 2026-05-11   (specific date)
       python telegram_kg_loader.py --dry-run            (print without writing)

Needs: neo4j, python-dotenv
Creds: fundamental_context/.env  (NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

try:
    from neo4j import GraphDatabase
except ImportError:
    print("[KG] ERROR: neo4j package not installed. Run: pip install neo4j")
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV = _HERE / "fundamental_context" / ".env"
load_dotenv(_ENV)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

_THEMES_DIR = _HERE / "telegram_themes"

# ── Cypher ────────────────────────────────────────────────────────────────────
_MERGE_THEME = """
MERGE (t:Theme {name: $name})
  ON CREATE SET
    t.theme_maturity  = $maturity,
    t.vikram_thesis   = $thesis,
    t.source          = 'telegram',
    t.created_date    = date($report_date)
  ON MATCH SET
    t.source          = CASE WHEN t.source IS NULL THEN 'telegram' ELSE t.source END
RETURN t.name AS name
"""

_CHECK_COMPANY = """
MATCH (c:Company {nse_code: $nse_code}) RETURN c.nse_code AS code LIMIT 1
"""

_MERGE_BENEFITS = """
MATCH (c:Company {nse_code: $nse_code})
MATCH (t:Theme {name: $theme})
MERGE (c)-[r:BENEFITS_FROM]->(t)
  ON CREATE SET
    r.direct       = true,
    r.magnitude    = $magnitude,
    r.sentiment    = $sentiment,
    r.source       = 'telegram',
    r.report_date  = date($report_date)
  ON MATCH SET
    r.magnitude    = $magnitude,
    r.sentiment    = $sentiment,
    r.report_date  = date($report_date)
RETURN c.nse_code AS co, t.name AS theme
"""

# ── Theme bridge: link telegram themes to curated KG themes ───────────────────
_FETCH_CURATED_THEMES = """
MATCH (t:Theme)
WHERE NOT coalesce(t.source, '') = 'telegram'
RETURN t.name AS name
"""

_MERGE_SUBTHEME = """
MATCH (child:Theme {name: $child_name})
MATCH (parent:Theme {name: $parent_name})
MERGE (child)-[r:SUBTHEME_OF]->(parent)
RETURN child.name AS child, parent.name AS parent
"""

_STOP = {
    "and",
    "the",
    "of",
    "in",
    "for",
    "a",
    "an",
    "by",
    "with",
    "to",
    "at",
    "on",
    "is",
    "its",
    "via",
    "into",
    "from",
    "through",
}


def _camel_to_tokens(s: str) -> set[str]:
    """GovernmentCapex → {government, capex}"""
    return set(re.sub(r"([A-Z])", r" \1", s).lower().split()) - _STOP


def _match_curated_theme(
    telegram_name: str, curated_names: list[str], threshold: float = 0.38
) -> str | None:
    """Fuzzy-match a natural-language telegram theme to a CamelCase curated theme."""
    tg_tokens = set(re.sub(r"[&,\-\(\)/]", " ", telegram_name).lower().split()) - _STOP
    if not tg_tokens:
        return None
    best_score, best = 0.0, None
    for cname in curated_names:
        c_tokens = _camel_to_tokens(cname)
        if not c_tokens:
            continue
        overlap = len(tg_tokens & c_tokens)
        if not overlap:
            continue
        score = overlap / max(len(tg_tokens), len(c_tokens))
        if score > best_score:
            best_score, best = score, cname
    return best if best_score >= threshold else None


def _bridge_to_curated(session, theme_names: set[str]) -> None:
    """Create SUBTHEME_OF edges from telegram themes to matching curated themes."""
    curated = [r["name"] for r in session.run(_FETCH_CURATED_THEMES)]
    if not curated:
        print(
            "[KG] No curated themes in KG — run load_themes.py first to enable bridging"
        )
        return
    bridges = 0
    for tname in sorted(theme_names):
        parent = _match_curated_theme(tname, curated)
        if not parent:
            continue
        res = session.run(_MERGE_SUBTHEME, child_name=tname, parent_name=parent)
        rec = res.single()
        if rec:
            print(f"  [KG] SUBTHEME_OF | {rec['child']} -> {rec['parent']}")
            bridges += 1
    print(
        f"[KG] Theme bridges: {bridges}/{len(theme_names)} telegram themes linked to curated KG themes"
    )


# ── Helpers ───────────────────────────────────────────────────────────────────
def _magnitude(conviction: str) -> str:
    c = (conviction or "").lower()
    if "high" in c:
        return "High"
    if "medium" in c:
        return "Medium"
    return "Low"


def _normalize_symbol(symbol: str) -> str:
    """Strip .BO/.NS suffixes that may come from Claude extraction."""
    return re.sub(r"\.(BO|NS)$", "", symbol.strip().upper())


def load_themes(date: str, driver, dry_run: bool = False) -> None:
    json_path = _THEMES_DIR / f"themes_{date}.json"
    if not json_path.exists():
        print(f"[KG] No JSON found for {date}: {json_path}")
        return

    with open(json_path, encoding="utf-8") as fh:
        obj = json.load(fh)
    reports: list[dict] = obj.get("reports", [])
    print(f"[KG] {len(reports)} reports to process for {date}")

    theme_count = 0
    benefit_count = 0
    skipped_cos = 0
    all_theme_names: set[str] = set()

    with driver.session() as session:
        for report in reports:
            themes = report.get("themes") or []
            companies = report.get("companies") or []
            conviction = report.get("conviction") or "Medium"
            summary = report.get("summary") or ""
            magnitude = _magnitude(conviction)

            # 1. MERGE Theme nodes
            for theme_name in themes:
                if not theme_name.strip():
                    continue
                all_theme_names.add(theme_name)
                if dry_run:
                    print(f"  [DRY] MERGE Theme: {theme_name!r}")
                    theme_count += 1
                    continue
                res = session.run(
                    _MERGE_THEME,
                    name=theme_name,
                    maturity="Emerging",
                    thesis=summary[:500] if summary else "",
                    report_date=date,
                )
                rec = res.single()
                if rec:
                    print(f"  [KG] Theme MERGE | Theme | {rec['name']}")
                    theme_count += 1

            # 2. MERGE BENEFITS_FROM edges (only for companies in universe)
            for co in companies:
                # Prefer resolver-verified nse_code; fall back to raw symbol
                resolved = (co.get("nse_code") or "").strip()
                raw_sym = co.get("symbol") or ""
                nse_code = (
                    resolved
                    if resolved and resolved != "None"
                    else _normalize_symbol(raw_sym)
                )
                if not nse_code or nse_code == "—":
                    continue
                sentiment = (co.get("sentiment") or "neutral").capitalize()

                if not dry_run:
                    exists = session.run(_CHECK_COMPANY, nse_code=nse_code).single()
                    if not exists:
                        print(f"  [KG] Skip (not in universe): {nse_code}")
                        skipped_cos += 1
                        continue

                for theme_name in themes:
                    if not theme_name.strip():
                        continue
                    if dry_run:
                        print(
                            f"  [DRY] MERGE BENEFITS_FROM: {nse_code} -> {theme_name!r} ({sentiment}, {magnitude})"
                        )
                        benefit_count += 1
                        continue
                    res = session.run(
                        _MERGE_BENEFITS,
                        nse_code=nse_code,
                        theme=theme_name,
                        magnitude=magnitude,
                        sentiment=sentiment,
                        report_date=date,
                    )
                    rec = res.single()
                    if rec:
                        print(
                            f"  [KG] BENEFITS_FROM MERGE | {rec['co']} -> {rec['theme']} | {sentiment} | {magnitude}"
                        )
                        benefit_count += 1

        # 3. Bridge telegram themes → curated KG themes via SUBTHEME_OF
        if not dry_run and all_theme_names:
            _bridge_to_curated(session, all_theme_names)

    if dry_run and all_theme_names:
        print(
            f"\n[DRY] Would bridge {len(all_theme_names)} themes to curated KG themes"
        )

    print(
        f"\n[KG] Done — Themes: {theme_count} | Edges: {benefit_count} | Skipped cos: {skipped_cos}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Load telegram themes into Neo4j KG")
    parser.add_argument(
        "--date",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Date to load (default: today, format YYYY-MM-DD)",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Print actions without writing to Neo4j"
    )
    args = parser.parse_args()

    if args.dry_run:
        print(f"[KG] DRY RUN — date={args.date}")
        load_themes(args.date, driver=None, dry_run=True)
        return

    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
        driver.verify_connectivity()
    except Exception as exc:
        print(f"[KG] ERROR: cannot connect to Neo4j at {NEO4J_URI}: {exc}")
        sys.exit(1)

    load_themes(args.date, driver, dry_run=False)
    driver.close()


if __name__ == "__main__":
    main()
