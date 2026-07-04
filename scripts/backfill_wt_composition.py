#!/usr/bin/env python3
"""
scripts/backfill_wt_composition.py
====================================
One-off backfill of wt_total_cross / wt_os_frac / wt_sqz_frac / wt_source
into data/breadth_history.csv, so the dashboard.breadth.html composition
panel isn't blank on day one.

Two source segments, spliced (deliberate — see caveat in
research/wt_breadth_correlation.md "Extended backtest" section):

  2026-01-01 .. 2026-06-07  "raw_est"  from data/wt_breadth_backtest.csv
      (raw breadth_universe rescan — the only data that exists this far back;
       counts run ~3-5x higher than the live scanner, os_frac/sqz_frac ratios
       are the comparable quantities, not raw counts)

  2026-06-08 .. today        "live"     from wt_scans/wt_bullcross_YYYY-MM-DD.md
      (gated live scanner output — matches what you actually see day to day)

Idempotent: re-running overwrites the same date range with the same values.
Usage: python scripts/backfill_wt_composition.py
"""

from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

import pandas as pd

REPO_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_DIR))

from wt_squeeze_dashboard import parse_wt_rows, read_file  # noqa: E402

HISTORY_PATH = REPO_DIR / "data" / "breadth_history.csv"
BACKTEST_PATH = REPO_DIR / "data" / "wt_breadth_backtest.csv"
WT_SCANS_DIR = REPO_DIR / "wt_scans"

RAW_EST_START = "2026-01-01"
RAW_EST_END = "2026-06-07"
LIVE_START = "2026-06-08"

_WT_OS_RANKS = {2, 3, 5}


def raw_est_rows() -> dict[str, dict]:
    df = pd.read_csv(BACKTEST_PATH, dtype={"date": str})
    df = df[(df["date"] >= RAW_EST_START) & (df["date"] <= RAW_EST_END)]
    out = {}
    for _, r in df.iterrows():
        if r["total_cross"] <= 0:
            continue
        out[r["date"]] = {
            "wt_total_cross": int(r["total_cross"]),
            "wt_os_frac": round(r["os_cross"] / r["total_cross"], 4),
            "wt_sqz_frac": round(r["sqz_cross"] / r["total_cross"], 4),
            "wt_source": "raw_est",
        }
    return out


def live_rows() -> dict[str, dict]:
    out = {}
    pattern = str(WT_SCANS_DIR / "wt_bullcross_????-??-??.md")
    for path in sorted(glob.glob(pattern)):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", path)
        if not m:
            continue
        date_str = m.group(1)
        if date_str < LIVE_START:
            continue
        rows = parse_wt_rows(read_file(path))
        total = len(rows)
        if total == 0:
            continue
        os_count = sum(1 for r in rows if r["rank"] in _WT_OS_RANKS)
        sqz_count = sum(1 for r in rows if r["squeeze"])
        out[date_str] = {
            "wt_total_cross": total,
            "wt_os_frac": round(os_count / total, 4),
            "wt_sqz_frac": round(sqz_count / total, 4),
            "wt_source": "live",
        }
    return out


def main() -> None:
    history = pd.read_csv(HISTORY_PATH, dtype={"date": str})
    for col in ["wt_total_cross", "wt_os_frac", "wt_sqz_frac", "wt_source"]:
        if col not in history.columns:
            history[col] = None

    combined = raw_est_rows()
    combined.update(live_rows())  # live wins on any overlapping date

    n_matched = 0
    for date_str, vals in combined.items():
        mask = history["date"] == date_str
        if not mask.any():
            continue
        for k, v in vals.items():
            history.loc[mask, k] = v
        n_matched += 1

    history.to_csv(HISTORY_PATH, index=False)
    print(f"Backfilled {n_matched}/{len(combined)} dates into {HISTORY_PATH}")
    print(f"  raw_est: {sum(1 for v in combined.values() if v['wt_source']=='raw_est')}")
    print(f"  live:    {sum(1 for v in combined.values() if v['wt_source']=='live')}")
    unmatched = set(combined) - set(history.loc[history['wt_source'].notna(), 'date'])
    if unmatched:
        print(f"  WARNING: {len(unmatched)} dates had WT data but no matching breadth_history row: "
              f"{sorted(unmatched)[:5]}...")


if __name__ == "__main__":
    main()
