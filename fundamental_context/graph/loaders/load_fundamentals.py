"""
Load fundamental data from Trendlyne CSV export into Neo4j Company nodes.

Source  : fundamental_context/data/NSE_UNIVERSE_trendlyne_fundamentals.csv
Run     : python load_fundamentals.py
Re-run  : safe — idempotent via MERGE (quarterly refresh: overwrite CSV, re-run)

Column notes
------------
- 'ROE Annual 3Yr Ago %'  -> roe_3yr_avg (proxy; closest available from Trendlyne export)
- 'ROCE Annual 3Yr Avg %' -> roce_3yr_avg (true 3yr average)
- pat_ttm derived: revenue_ttm × (net_profit_margin_ttm / 100)
- ebitda_margin_ttm derived: ebitda_ttm / revenue_ttm × 100
- cash_conversion_ratio, order_book_crore, working_capital_days -> null in this export
"""
from __future__ import annotations

import csv
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV  = _HERE.parent.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI  = os.getenv("NEO4J_URI",      "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER",     "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

CSV_PATH = _HERE.parent.parent / "data" / "NSE_UNIVERSE_trendlyne_fundamentals.csv"


# ── Quality score thresholds (from CLAUDE.md) ────────────────────────────────
def _quality_score(roe: float | None, roce: float | None,
                   ob_ratio: float | None, pledge: float | None,
                   promoter: float | None) -> int:
    """0–10 composite quality score based on CLAUDE.md thresholds."""
    pts = 0
    if roe      is not None and roe      > 25:  pts += 2
    if roce     is not None and roce     > 30:  pts += 2
    if ob_ratio is not None and ob_ratio > 2:   pts += 3
    if pledge   is not None and pledge   == 0:  pts += 2
    if promoter is not None and promoter > 50:  pts += 1
    return pts


def _conviction_business_quality(roe: float | None, roce: float | None,
                                  ob_ratio: float | None, pledge: float | None,
                                  promoter: float | None,
                                  debt_eq: float | None) -> int:
    """Business Quality layer only (max 35). No catalyst/theme data yet."""
    score = 0
    if roe      is not None and roe      > 25:  score += 8
    if roce     is not None and roce     > 30:  score += 8
    if ob_ratio is not None and ob_ratio > 2:   score += 10
    if pledge   is not None and pledge   == 0:  score += 5
    if promoter is not None and promoter > 50:  score += 4

    # Negative adjustments
    if pledge   is not None and pledge   >  0:  score -= 10
    if ob_ratio is not None and ob_ratio <  1:  score -= 8
    if debt_eq  is not None and debt_eq  > 1.5: score -= 5

    return max(0, min(100, score))


# ── CSV parsing ───────────────────────────────────────────────────────────────
def _safe_float(val: str) -> float | None:
    """Parse a numeric string; return None on empty / non-numeric."""
    v = val.strip()
    if not v or v == "-":
        return None
    try:
        return float(v.replace(",", ""))
    except ValueError:
        return None


def parse_csv(path: Path) -> list[dict]:
    """Read Trendlyne CSV; return list of dicts with typed fields."""
    records: list[dict] = []
    with open(path, encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        for raw in reader:
            nse_code = raw.get("NSE Code", "").strip()
            if not nse_code:
                continue  # BSE-only stock, skip

            revenue_ttm        = _safe_float(raw.get("Operating Revenue TTM", ""))
            net_profit_margin  = _safe_float(raw.get("Net Profit Margin TTM %", ""))
            ebitda_ttm         = _safe_float(raw.get("EBITDA TTM", ""))
            roe                = _safe_float(raw.get("ROE Annual 3Yr Ago %", ""))
            roce               = _safe_float(raw.get("ROCE Annual 3Yr Avg %", ""))
            promoter           = _safe_float(raw.get("Promoter holding latest %", ""))
            pledge             = _safe_float(raw.get("Promoter holding pledge percentage % Qtr", ""))
            debt_eq            = _safe_float(raw.get("Total Debt to Total Equity Annual", ""))
            pe                 = _safe_float(raw.get("PE TTM Price to Earnings", ""))
            revenue_cagr       = _safe_float(raw.get("Revenue Annual 3Yr Growth %", ""))
            pat_cagr           = _safe_float(raw.get("Net Profit 3Yr Growth %", ""))
            mcap               = _safe_float(raw.get("Market Capitalization", ""))

            # Derived fields
            pat_ttm: float | None = None
            if revenue_ttm is not None and net_profit_margin is not None:
                pat_ttm = round(revenue_ttm * net_profit_margin / 100, 2)

            ebitda_margin: float | None = None
            if ebitda_ttm is not None and revenue_ttm and revenue_ttm > 0:
                ebitda_margin = round(ebitda_ttm / revenue_ttm * 100, 2)

            ob_ratio: float | None = None  # not in this export

            quality   = _quality_score(roe, roce, ob_ratio, pledge, promoter)
            conv_init = _conviction_business_quality(roe, roce, ob_ratio, pledge, promoter, debt_eq)

            records.append({
                "nse_code":           nse_code,
                "name":               raw.get("Stock Name", "").strip() or None,
                "roe_3yr_avg":        roe,
                "roce_3yr_avg":       roce,
                "promoter_pct":       promoter,
                "pledge_pct":         pledge,
                "debt_to_equity":     debt_eq,
                "revenue_ttm":        revenue_ttm,
                "pat_ttm":            pat_ttm,
                "ebitda_margin_ttm":  ebitda_margin,
                "pe_current":         pe,
                "revenue_cagr_3yr":   revenue_cagr,
                "pat_cagr_3yr":       pat_cagr,
                "mcap":               mcap,
                # fields not in export — will remain null
                "cash_conversion_ratio":       None,
                "order_book_crore":            None,
                "order_book_to_revenue_ratio": None,
                "working_capital_days":        None,
                "ev_ebitda_current":           None,
                # computed
                "quality_score":    quality,
                "conviction_score": conv_init,
            })
    return records


# ── Cypher ────────────────────────────────────────────────────────────────────
_MERGE_FUNDAMENTALS = """
MATCH (c:Company {nse_code: $nse_code})
SET
  c.name                        = coalesce($name, c.name),
  c.roe_3yr_avg                 = $roe_3yr_avg,
  c.roce_3yr_avg                = $roce_3yr_avg,
  c.promoter_pct                = $promoter_pct,
  c.pledge_pct                  = $pledge_pct,
  c.debt_to_equity              = $debt_to_equity,
  c.revenue_ttm                 = $revenue_ttm,
  c.pat_ttm                     = $pat_ttm,
  c.ebitda_margin_ttm           = $ebitda_margin_ttm,
  c.pe_current                  = $pe_current,
  c.revenue_cagr_3yr            = $revenue_cagr_3yr,
  c.pat_cagr_3yr                = $pat_cagr_3yr,
  c.mcap                        = coalesce($mcap, c.mcap),
  c.cash_conversion_ratio       = $cash_conversion_ratio,
  c.order_book_crore            = $order_book_crore,
  c.order_book_to_revenue_ratio = $order_book_to_revenue_ratio,
  c.working_capital_days        = $working_capital_days,
  c.ev_ebitda_current           = $ev_ebitda_current,
  c.quality_score               = $quality_score,
  c.conviction_score            = $conviction_score,
  c.updated_at                  = date()
RETURN c.nse_code AS code
"""


# ── Loader ────────────────────────────────────────────────────────────────────
def load(records: list[dict]) -> tuple[int, int]:
    """Write fundamentals to Neo4j. Returns (merged, skipped_not_in_graph)."""
    driver  = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    merged  = 0
    skipped = 0

    with driver.session() as session:
        for r in records:
            result = session.run(_MERGE_FUNDAMENTALS, **r)
            if result.single():
                print(
                    f"[GRAPH] Fundamentals MERGE | Company | {r['nse_code']} | "
                    f"quality={r['quality_score']} conviction={r['conviction_score']}"
                )
                merged += 1
            else:
                skipped += 1  # company not in graph yet (not in universe)

    driver.close()
    return merged, skipped


def main() -> None:
    if not CSV_PATH.exists():
        print(f"ERROR: CSV not found at {CSV_PATH}")
        sys.exit(1)

    print(f"[GRAPH] Fundamentals load starting... ({CSV_PATH.name})")
    records = parse_csv(CSV_PATH)
    print(f"[GRAPH] CSV parsed | {len(records)} NSE-coded rows")

    merged, skipped = load(records)
    print(
        f"[GRAPH] Summary | {merged} companies updated | "
        f"{skipped} skipped (not in universe graph)"
    )


if __name__ == "__main__":
    main()
