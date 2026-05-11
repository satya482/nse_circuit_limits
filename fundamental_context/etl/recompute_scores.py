"""
Recompute conviction scores for all Company nodes in Neo4j.

Runs nightly after NSE RSS parse. Implements the full 4-layer formula:
  Business Quality (max 35) + Earnings Quality (max 20)
  + Thematic Alignment (max 20) + Catalyst Layer (max 25, decayed 20%/quarter)
  − Negative adjustments

Run     : python recompute_scores.py
Re-run  : safe — always overwrites conviction_score
"""
from __future__ import annotations

import os
from datetime import date, timedelta
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV  = _HERE.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI  = os.getenv("NEO4J_URI",      "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER",     "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

# Optionally compute for a single company only
SINGLE_SYMBOL: str | None = None


# ── Fetch context for each company ───────────────────────────────────────────
_FETCH_COMPANIES = """
MATCH (c:Company)
WHERE c.roe_3yr_avg IS NOT NULL OR c.roce_3yr_avg IS NOT NULL
RETURN
  c.nse_code                   AS nse_code,
  c.roe_3yr_avg                AS roe,
  c.roce_3yr_avg               AS roce,
  c.promoter_pct               AS promoter,
  c.pledge_pct                 AS pledge,
  c.order_book_to_revenue_ratio AS ob_ratio,
  c.cash_conversion_ratio      AS cash_conv,
  c.debt_to_equity             AS debt_eq,
  c.working_capital_days       AS wc_days,
  c.piotroski_score            AS piotroski,
  c.interest_coverage          AS int_cov,
  c.current_ratio              AS curr_ratio
"""

_FETCH_COMPANIES_SINGLE = """
MATCH (c:Company {nse_code: $nse_code})
RETURN
  c.nse_code                   AS nse_code,
  c.roe_3yr_avg                AS roe,
  c.roce_3yr_avg               AS roce,
  c.promoter_pct               AS promoter,
  c.pledge_pct                 AS pledge,
  c.order_book_to_revenue_ratio AS ob_ratio,
  c.cash_conversion_ratio      AS cash_conv,
  c.debt_to_equity             AS debt_eq,
  c.working_capital_days       AS wc_days,
  c.piotroski_score            AS piotroski,
  c.interest_coverage          AS int_cov,
  c.current_ratio              AS curr_ratio
"""

_FETCH_GRAPH_CONTEXT = """
MATCH (c:Company {nse_code: $nse_code})

// Theme count (direct or via SUBTHEME_OF*)
OPTIONAL MATCH (c)-[:BENEFITS_FROM]->(t:Theme)
WITH c, count(DISTINCT t) AS theme_count

// Scheme approval
OPTIONAL MATCH (c)-[e:ELIGIBLE_FOR]->(g:GovernmentScheme)
WHERE e.approval_status = 'Approved'
WITH c, theme_count, count(g) > 0 AS scheme_approved

// Beat streak: quarters with beat_pct > 0 in last 4
OPTIONAL MATCH (c)-[:REPORTED]->(q:Quarter)
WHERE q.beat_pct > 0
WITH c, theme_count, scheme_approved, count(q) AS beat_streak

// Governance flag
OPTIONAL MATCH (c)-[:RISK_EXPOSED_TO]->(r:Risk)
WHERE r.type = 'Governance' AND r.severity IN ['High','Critical']
WITH c, theme_count, scheme_approved, beat_streak, count(r) > 0 AS governance_flag

// Industry growth
OPTIONAL MATCH (c)-[:BELONGS_TO]->(i:Industry)
WITH c, theme_count, scheme_approved, beat_streak, governance_flag,
     coalesce(i.industry_growth_rate_pct, 0) AS industry_growth

// Recent catalysts (last 4 quarters = ~365 days)
OPTIONAL MATCH (c)-[:TRIGGERED]->(cat:Catalyst)
WHERE cat.date >= date() - duration('P365D')
WITH c, theme_count, scheme_approved, beat_streak, governance_flag,
     industry_growth, collect({
       conviction_delta: coalesce(cat.conviction_delta, 3),
       age_quarters: toFloat(
         duration.between(cat.date, date()).months / 3
       )
     }) AS recent_catalysts

RETURN
  theme_count, scheme_approved, beat_streak,
  governance_flag, industry_growth, recent_catalysts
"""

_UPDATE_SCORE = """
MATCH (c:Company {nse_code: $nse_code})
SET c.conviction_score = $score, c.updated_at = date()
"""


# ── Score formula (mirrors 02_daily_pipeline.md) ─────────────────────────────
def _f(v) -> float:
    return float(v) if v is not None else 0.0


def compute_conviction(company: dict, ctx: dict) -> int:
    score = 0.0

    roe       = _f(company.get("roe"))
    roce      = _f(company.get("roce"))
    ob_ratio  = company.get("ob_ratio")
    pledge    = company.get("pledge")
    promoter  = _f(company.get("promoter"))
    cash_conv = _f(company.get("cash_conv"))
    debt_eq   = _f(company.get("debt_eq"))
    wc_days   = company.get("wc_days")
    piotroski = company.get("piotroski")
    int_cov   = company.get("int_cov")
    curr_ratio= company.get("curr_ratio")

    # ── Business Quality (max 35) ──────────────────────────────────────────
    if roe  > 25:                  score += 8
    if roce > 30:                  score += 8
    if ob_ratio and ob_ratio > 2:  score += 10
    if pledge is not None and pledge == 0: score += 5
    if promoter > 50:              score += 4

    # ── Earnings Quality (max 25) ──────────────────────────────────────────
    # cash_conv now populated from screener.in (FCF/PAT)
    if cash_conv > 0.85:           score += 8
    if _f(ctx.get("beat_streak")) >= 3: score += 7
    if wc_days is not None and wc_days < 90: score += 5
    # Piotroski score > 7 = strong balance sheet health across 9 criteria
    if piotroski is not None and _f(piotroski) >= 7: score += 5

    # ── Thematic Alignment (max 20) ────────────────────────────────────────
    if _f(ctx.get("theme_count")) > 0:      score += 8
    if ctx.get("scheme_approved"):          score += 7
    if _f(ctx.get("industry_growth")) > 15: score += 5

    # ── Catalyst Layer (max 25, decayed 20%/quarter) ───────────────────────
    catalyst_score = 0.0
    for cat in ctx.get("recent_catalysts") or []:
        delta        = _f(cat.get("conviction_delta"))
        age_quarters = max(0.0, _f(cat.get("age_quarters")))
        catalyst_score += delta * (0.8 ** age_quarters)
    score += min(25, catalyst_score)

    # ── Negative adjustments ──────────────────────────────────────────────
    if pledge is not None and pledge > 0:      score -= 10
    if ctx.get("governance_flag"):             score -= 20
    if ob_ratio is not None and ob_ratio < 1:  score -= 8
    if debt_eq  > 1.5:                         score -= 5
    # Poor debt serviceability (interest coverage < 1.5x = danger zone)
    if int_cov is not None and _f(int_cov) < 1.5: score -= 5

    return max(0, min(100, round(score)))


# ── Main ──────────────────────────────────────────────────────────────────────
def run(nse_code: str | None = None) -> int:
    """Recompute scores. Returns count of updated companies."""
    driver  = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    updated = 0

    with driver.session() as session:
        if nse_code:
            companies = list(session.run(_FETCH_COMPANIES_SINGLE, nse_code=nse_code))
        else:
            companies = list(session.run(_FETCH_COMPANIES))

        print(f"[SCORES] Computing for {len(companies)} companies...")

        for row in companies:
            code = row["nse_code"]
            ctx_row = session.run(_FETCH_GRAPH_CONTEXT, nse_code=code).single()
            ctx = dict(ctx_row) if ctx_row else {}

            score = compute_conviction(dict(row), ctx)
            session.run(_UPDATE_SCORE, nse_code=code, score=score)
            print(f"[GRAPH] Score MERGE | Company | {code} | conviction={score}")
            updated += 1

    driver.close()
    return updated


def main() -> None:
    updated = run(SINGLE_SYMBOL)
    print(f"[SCORES] Summary | {updated} companies updated")


if __name__ == "__main__":
    main()
