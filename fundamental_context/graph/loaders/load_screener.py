"""
Load Screener.in fundamentals into existing Company nodes.

Supplements load_fundamentals.py (Trendlyne). Adds fields Trendlyne lacks:
  roe_3yr_avg          — Average ROE 3Yr (overwrites Trendlyne's "3yr ago" proxy)
  roce_current         — Current year ROCE (Trendlyne has 3yr avg; both kept)
  revenue_cagr_3yr     — Sales 3yr CAGR (overwrites)
  pat_cagr_3yr         — PAT 3yr CAGR (overwrites)
  piotroski_score      — Piotroski F-score 0-9 (new)
  interest_coverage    — Interest coverage ratio (new)
  ev_ebitda_current    — EV/EBITDA (new/overwrite)
  current_ratio        — Current ratio (new)
  cash_conversion_ratio — FCF / PAT; FCF = Mcap / P_to_FCF (was null from Trendlyne)

Source file : data/NSE_UNIVERSE_screener_in_fundamentals.csv
Run         : python load_screener.py
Re-run      : safe — MERGE overwrites properties idempotently
"""

from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from neo4j import GraphDatabase

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV = _HERE.parent.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

DATA_FILE = _HERE.parent.parent / "data" / "NSE_UNIVERSE_screener_in_fundamentals.csv"

# ── Column map: screener.in header -> internal name ───────────────────────────
_COL = {
    "NSE Code": "nse_code",
    "Average return on equity 3Years": "roe_3yr_avg",
    "Return on capital employed": "roce_current",
    "Sales growth 3Years": "revenue_cagr_3yr",
    "Profit growth 3Years": "pat_cagr_3yr",
    "Piotroski score": "piotroski_score",
    "Interest Coverage Ratio": "interest_coverage",
    "EVEBITDA": "ev_ebitda_current",
    "Current ratio": "current_ratio",
    "Market Capitalization": "mcap_scr",  # interim, used to derive FCF
    "Price to Free Cash Flow": "p_to_fcf",  # interim, used to derive FCF
    "Profit after tax": "pat_annual",  # interim, used to derive FCF
}

# ── Cypher ────────────────────────────────────────────────────────────────────
_MERGE_SCREENER = """
MATCH (c:Company {nse_code: $nse_code})
SET
  c.roe_3yr_avg           = CASE WHEN $roe_3yr_avg       IS NOT NULL THEN $roe_3yr_avg       ELSE c.roe_3yr_avg           END,
  c.roce_current          = CASE WHEN $roce_current      IS NOT NULL THEN $roce_current      ELSE c.roce_current          END,
  c.revenue_cagr_3yr      = CASE WHEN $revenue_cagr_3yr IS NOT NULL THEN $revenue_cagr_3yr ELSE c.revenue_cagr_3yr      END,
  c.pat_cagr_3yr          = CASE WHEN $pat_cagr_3yr     IS NOT NULL THEN $pat_cagr_3yr     ELSE c.pat_cagr_3yr          END,
  c.piotroski_score       = CASE WHEN $piotroski_score  IS NOT NULL THEN $piotroski_score  ELSE c.piotroski_score       END,
  c.interest_coverage     = CASE WHEN $interest_coverage IS NOT NULL THEN $interest_coverage ELSE c.interest_coverage   END,
  c.ev_ebitda_current     = CASE WHEN $ev_ebitda_current IS NOT NULL THEN $ev_ebitda_current ELSE c.ev_ebitda_current   END,
  c.current_ratio         = CASE WHEN $current_ratio    IS NOT NULL THEN $current_ratio    ELSE c.current_ratio         END,
  c.cash_conversion_ratio = CASE WHEN $cash_conv        IS NOT NULL THEN $cash_conv        ELSE c.cash_conversion_ratio END
"""


def _f(val) -> float | None:
    """Convert to float, returning None for NaN/inf."""
    try:
        v = float(val)
        return None if (v != v or abs(v) > 1e12) else v  # NaN check
    except (TypeError, ValueError):
        return None


def _cash_conv(
    mcap: float | None, p_to_fcf: float | None, pat: float | None
) -> float | None:
    """Derive cash_conversion_ratio = FCF / PAT. Clipped to [-3, 3]."""
    if mcap is None or p_to_fcf is None or pat is None:
        return None
    if p_to_fcf <= 0 or pat == 0:
        return None
    fcf = mcap / p_to_fcf
    ratio = fcf / pat
    return round(max(-3.0, min(3.0, ratio)), 3)


def load(session) -> int:
    """Read CSV, MERGE screener.in fields into existing Company nodes. Returns updated count."""
    df = pd.read_csv(DATA_FILE, dtype=str)
    df.columns = df.columns.str.strip()

    updated = 0
    skipped = 0

    for _, row in df.iterrows():
        nse_code = str(row.get("NSE Code", "") or "").strip()
        if not nse_code:
            skipped += 1
            continue

        roe_3yr = _f(row.get("Average return on equity 3Years"))
        roce_cur = _f(row.get("Return on capital employed"))
        rev_cagr = _f(row.get("Sales growth 3Years"))
        pat_cagr = _f(row.get("Profit growth 3Years"))
        piotroski = _f(row.get("Piotroski score"))
        int_cov = _f(row.get("Interest Coverage Ratio"))
        ev_ebitda = _f(row.get("EVEBITDA"))
        curr_ratio = _f(row.get("Current ratio"))

        mcap = _f(row.get("Market Capitalization"))
        p_to_fcf = _f(row.get("Price to Free Cash Flow"))
        pat_annual = _f(row.get("Profit after tax"))
        cash_conv = _cash_conv(mcap, p_to_fcf, pat_annual)

        result = session.run(
            _MERGE_SCREENER,
            nse_code=nse_code,
            roe_3yr_avg=roe_3yr,
            roce_current=roce_cur,
            revenue_cagr_3yr=rev_cagr,
            pat_cagr_3yr=pat_cagr,
            piotroski_score=piotroski,
            interest_coverage=int_cov,
            ev_ebitda_current=ev_ebitda,
            current_ratio=curr_ratio,
            cash_conv=cash_conv,
        )
        props = result.consume().counters.properties_set
        if props > 0:
            print(
                f"[GRAPH] Screener MERGE | Company | {nse_code} | "
                f"piotroski={piotroski} roe3y={roe_3yr} cash_conv={cash_conv}"
            )
            updated += 1
        else:
            skipped += 1

    return updated


def main() -> None:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    with driver.session() as session:
        n = load(session)
    driver.close()
    print(f"[GRAPH] Summary | {n} Company nodes enriched from screener.in")


if __name__ == "__main__":
    main()
