"""Sector synchronization for the institutional footprint scanner.

Groups today's already-scored rows by sector (using the existing stock
universe CSV, not a new symbols table) and scores how broadly the sector is
participating: % above EMA20, % with RS trending up, % ICS >= 70.
"""

import csv
import os

import pandas as pd

_HERE = os.path.dirname(os.path.abspath(__file__))
UNIVERSE_CSV = os.path.join(_HERE, "NSE_500cr_15CrNotional10D_50rs_sector_industry.csv")


def load_sector_map(csv_path: str = UNIVERSE_CSV) -> dict[str, str]:
    if not os.path.exists(csv_path):
        return {}

    with open(csv_path, encoding="cp1252") as fh:
        reader = csv.DictReader(fh)
        return {
            row["NSE Code"].strip().upper(): (row.get("sector_name") or "").strip()
            for row in reader
            if row.get("NSE Code")
        }


def add_sector_scores(rows: pd.DataFrame, sector_map: dict[str, str] | None = None) -> pd.DataFrame:
    """Adds `sector` + `sector_score` (0-100) columns to an already-scored (has `ics`) rows frame."""
    if rows.empty:
        return rows

    sector_map = load_sector_map() if sector_map is None else sector_map
    rows = rows.copy()
    rows["sector"] = rows["symbol"].map(sector_map).fillna("UNKNOWN")

    grouped = rows.groupby("sector").agg(
        _pct_ema20=("close_gt_ema20", "mean"),
        _pct_rs_up=("rs_trend", lambda s: (s == "UP").mean()),
        _pct_ics70=("ics", lambda s: (s >= 70).mean()),
    )
    grouped["sector_score"] = (
        (grouped["_pct_ema20"] + grouped["_pct_rs_up"] + grouped["_pct_ics70"]) / 3 * 100
    ).round(1)

    return rows.merge(grouped[["sector_score"]], on="sector", how="left")
