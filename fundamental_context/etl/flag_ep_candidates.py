"""
Flag EP (Episodic Pivot) candidates.

Pulls companies from Neo4j that pass conviction + catalyst thresholds,
then checks technical EP conditions using existing ohlc_db.py SQLite.

EP preconditions (Qullamaggie NSE-adapted):
  1. conviction_score >= 70
  2. quality_score >= 7
  3. High/Medium ep_probability catalyst in last 30 days
  4. Volume on catalyst day > 5x 20D average (requires OHLC data)
  5. Stock sideways (ATR-range tight) for 3+ months before catalyst

Output: data/processed/ep_watchlist_YYYYMMDD.csv

Run: python flag_ep_candidates.py
"""
from __future__ import annotations

import csv
import os
import sys
from datetime import date, timedelta
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase

# Add parent project root to path so ohlc_db.py is importable
_PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_PROJECT_ROOT))

try:
    from ohlc_db import load_ohlc  # type: ignore[import]
    OHLC_AVAILABLE = True
except ImportError:
    OHLC_AVAILABLE = False
    print("[EP] WARNING: ohlc_db not found — technical EP conditions will be skipped")

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV  = _HERE.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI  = os.getenv("NEO4J_URI",      "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER",     "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

OUTPUT_DIR = _HERE.parent / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ── Neo4j query ───────────────────────────────────────────────────────────────
_EP_CANDIDATES = """
MATCH (c:Company)-[:TRIGGERED]->(cat:Catalyst)
WHERE cat.date >= date() - duration('P30D')
  AND cat.ep_probability IN ['High', 'Medium']
  AND c.conviction_score >= 70
  AND c.quality_score >= 7
OPTIONAL MATCH (c)-[:BENEFITS_FROM]->(t:Theme)
RETURN DISTINCT
  c.nse_code           AS nse_code,
  c.name               AS name,
  c.conviction_score   AS conviction,
  c.quality_score      AS quality,
  c.order_book_to_revenue_ratio AS ob_ratio,
  cat.type             AS catalyst_type,
  cat.date             AS catalyst_date,
  cat.ep_probability   AS ep_prob,
  collect(DISTINCT t.name) AS themes
ORDER BY c.conviction_score DESC
"""


# ── Technical checks (OHLC-based) ────────────────────────────────────────────
def _check_ep_technicals(nse_code: str, catalyst_date: date) -> tuple[bool, str]:
    """
    Returns (passes, reason) based on OHLC checks.
    catalyst_date is the date the catalyst was announced.
    """
    if not OHLC_AVAILABLE:
        return True, "OHLC unavailable — skipped"

    df = load_ohlc(nse_code, lookback=400)
    if df is None or df.empty:
        return False, "No OHLC data"

    df = df.copy()
    df["date"] = df["date"] if hasattr(df["date"], "dt") else df["date"]

    # Find catalyst day row
    cat_date_str = catalyst_date.isoformat()
    cat_rows = df[df["date"].astype(str) == cat_date_str]
    if cat_rows.empty:
        # Tolerate ±1 day for weekends/holidays
        tolerance = [
            (catalyst_date - timedelta(days=1)).isoformat(),
            (catalyst_date + timedelta(days=1)).isoformat(),
        ]
        cat_rows = df[df["date"].astype(str).isin(tolerance)]
    if cat_rows.empty:
        return False, "Catalyst date not in OHLC data"

    cat_idx = cat_rows.index[-1]

    # ── Volume check: catalyst day > 5x 20D avg ──────────────────────────
    window_end = cat_idx
    window_start = max(0, cat_idx - 20)
    avg_vol = df.iloc[window_start:window_end]["volume"].mean()
    cat_vol = df.loc[cat_idx, "volume"]
    if avg_vol > 0 and cat_vol < avg_vol * 5:
        return False, f"Volume {cat_vol:.0f} < 5x 20D avg {avg_vol:.0f}"

    # ── Sideways check: ATR tight for 3+ months (≈63 trading days) ───────
    lookback_end   = cat_idx
    lookback_start = max(0, cat_idx - 63)
    period         = df.iloc[lookback_start:lookback_end]
    if len(period) < 20:
        return True, "Insufficient history for sideways check"

    high_low_range_pct = (
        (period["high"].max() - period["low"].min()) / period["close"].mean() * 100
    )
    if high_low_range_pct > 35:
        return False, f"Not sideways — range {high_low_range_pct:.1f}% over 3M"

    return True, f"vol×{cat_vol/avg_vol:.1f} avg | range {high_low_range_pct:.1f}%"


# ── Main ──────────────────────────────────────────────────────────────────────
def run() -> list[dict]:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    with driver.session() as session:
        candidates = list(session.run(_EP_CANDIDATES))
    driver.close()

    print(f"[EP] {len(candidates)} candidates from Neo4j")
    ep_list: list[dict] = []

    for row in candidates:
        nse_code     = row["nse_code"]
        catalyst_date = row["catalyst_date"]

        if catalyst_date is None:
            continue

        passes, reason = _check_ep_technicals(nse_code, catalyst_date)
        status = "EP_WATCH" if passes else "FILTERED"

        record = {
            "symbol":         nse_code,
            "name":           row["name"],
            "conviction":     row["conviction"],
            "quality":        row["quality"],
            "ob_ratio":       row["ob_ratio"],
            "catalyst_type":  row["catalyst_type"],
            "catalyst_date":  str(catalyst_date),
            "ep_probability": row["ep_prob"],
            "themes":         "|".join(row["themes"] or []),
            "ep_status":      status,
            "technical_note": reason,
        }
        ep_list.append(record)
        print(f"[EP] {nse_code} | {status} | {reason}")

    # Write CSV
    today_str = date.today().isoformat()
    out_path  = OUTPUT_DIR / f"ep_watchlist_{today_str}.csv"
    if ep_list:
        fieldnames = list(ep_list[0].keys())
        with open(out_path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(ep_list)
        print(f"[EP] Watchlist written -> {out_path}")

    ep_watch = [r for r in ep_list if r["ep_status"] == "EP_WATCH"]
    print(f"[EP] Summary | {len(ep_watch)} EP candidates | {len(ep_list)} total screened")
    return ep_list


def main() -> None:
    run()


if __name__ == "__main__":
    main()
