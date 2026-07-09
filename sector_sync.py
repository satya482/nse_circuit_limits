"""Sector synchronization for the institutional footprint scanner.

Groups today's already-scored rows by sector (sector comes from the same
TradingView universe query used to build the scan, not a static CSV — that
gave 100% coverage vs ~69% from the old sector CSV join) and scores how
broadly the sector is participating: % above EMA20, % with RS trending up,
% ICS >= 70.
"""

import pandas as pd


def add_sector_scores(rows: pd.DataFrame, sector_map: dict[str, str] | None = None) -> pd.DataFrame:
    """Adds `sector` + `sector_score` (0-100) columns to an already-scored (has `ics`) rows frame."""
    if rows.empty:
        return rows

    sector_map = sector_map or {}
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
