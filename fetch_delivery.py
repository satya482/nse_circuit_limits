#!/usr/bin/env python3
"""Fetch NSE full bhavcopy delivery% (DELIV_PER) for EQ-series stocks.
Upserts into market.db `delivery` table. Run ~6:15 PM IST via
run_fetch_delivery.ps1, after NSE publishes the day's bhavcopy."""

import sqlite3
import sys
from datetime import date
from io import StringIO
from pathlib import Path

import pandas as pd
import requests

DB_PATH = Path(__file__).parent / ".ohlc_data" / "market.db"

_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"


def fetch_bhavcopy_csv(d: date) -> str:
    """Download raw bhavcopy CSV text for date d. Raises on non-200/network error."""
    url = (
        "https://nsearchives.nseindia.com/products/content/"
        f"sec_bhavdata_full_{d.strftime('%d%m%Y')}.csv"
    )
    session = requests.Session()
    session.headers.update({"User-Agent": _USER_AGENT})
    session.get("https://www.nseindia.com", timeout=10)  # cookie warm-up
    resp = session.get(url, timeout=15)
    resp.raise_for_status()
    return resp.text


def parse_bhavcopy_csv(csv_text: str) -> pd.DataFrame:
    """Parse bhavcopy CSV text -> DataFrame(symbol, ttl_trd_qty, deliv_qty, deliv_pct),
    EQ series only. NSE bhavcopy pads both header names and string values with
    whitespace -- strip both."""
    df = pd.read_csv(StringIO(csv_text))
    df.columns = [c.strip() for c in df.columns]
    df["SERIES"] = df["SERIES"].str.strip()
    df = df[df["SERIES"] == "EQ"].copy()
    df["SYMBOL"] = df["SYMBOL"].str.strip()
    out = pd.DataFrame(
        {
            "symbol": df["SYMBOL"],
            "ttl_trd_qty": pd.to_numeric(df["TTL_TRD_QNTY"], errors="coerce"),
            "deliv_qty": pd.to_numeric(df["DELIV_QTY"], errors="coerce"),
            "deliv_pct": pd.to_numeric(df["DELIV_PER"], errors="coerce"),
        }
    )
    return out.dropna(subset=["symbol", "ttl_trd_qty", "deliv_qty", "deliv_pct"]).reset_index(drop=True)


def upsert_delivery(rows: pd.DataFrame, d: date, db_path: Path = DB_PATH) -> int:
    """Upsert rows into the `delivery` table for date d. Creates the table on
    first run. Returns row count written."""
    con = sqlite3.connect(db_path)
    try:
        con.execute(
            "CREATE TABLE IF NOT EXISTS delivery ("
            "symbol TEXT, date DATE, ttl_trd_qty INTEGER, deliv_qty INTEGER, deliv_pct REAL, "
            "PRIMARY KEY (symbol, date))"
        )
        date_str = d.isoformat()
        con.executemany(
            "INSERT OR REPLACE INTO delivery (symbol, date, ttl_trd_qty, deliv_qty, deliv_pct) "
            "VALUES (?, ?, ?, ?, ?)",
            [
                (r.symbol, date_str, int(r.ttl_trd_qty), int(r.deliv_qty), float(r.deliv_pct))
                for r in rows.itertuples()
            ],
        )
        con.commit()
        return len(rows)
    finally:
        con.close()


def main() -> None:
    d = date.today()
    try:
        csv_text = fetch_bhavcopy_csv(d)
    except Exception as e:
        print(f"fetch_delivery: bhavcopy fetch failed for {d.isoformat()}: {e}", file=sys.stderr)
        sys.exit(1)
    rows = parse_bhavcopy_csv(csv_text)
    n = upsert_delivery(rows, d)
    print(f"fetch_delivery: wrote {n} EQ rows for {d.isoformat()}")


if __name__ == "__main__":
    main()
