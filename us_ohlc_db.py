#!/usr/bin/env python3
"""
SQLite reader for US OHLC data (yfinance-sourced).
Mirrors ohlc_db.py but points at .us_ohlc_data/us_market.db.

DB layout:
  ohlc(symbol TEXT, date DATE, open REAL, high REAL, low REAL, close REAL, volume INTEGER)
  PRIMARY KEY (symbol, date)

Columns returned: date (datetime64), open, high, low, close, volume — all lowercase.
Rows ordered oldest → newest.
"""

import sqlite3
from pathlib import Path

import pandas as pd

DB_PATH = Path(__file__).parent / ".us_ohlc_data" / "us_market.db"


def _connect(db_path: Path) -> sqlite3.Connection | None:
    if not db_path.exists():
        return None
    return sqlite3.connect(db_path)


def load_ohlc(
    symbol: str,
    lookback: int = 400,
    db_path: Path = DB_PATH,
) -> pd.DataFrame | None:
    con = _connect(db_path)
    if con is None:
        return None
    try:
        df = pd.read_sql(
            "SELECT date, open, high, low, close, volume FROM ohlc "
            "WHERE symbol=? ORDER BY date DESC LIMIT ?",
            con, params=(symbol, lookback),
        )
        if df.empty:
            return None
        df["date"] = pd.to_datetime(df["date"])
        return df.iloc[::-1].reset_index(drop=True)
    except Exception:
        return None
    finally:
        con.close()


def load_ohlc_many(
    symbols: list[str],
    lookback: int = 400,
    db_path: Path = DB_PATH,
) -> dict[str, pd.DataFrame]:
    con = _connect(db_path)
    if con is None:
        return {}
    results = {}
    try:
        for sym in symbols:
            df = pd.read_sql(
                "SELECT date, open, high, low, close, volume FROM ohlc "
                "WHERE symbol=? ORDER BY date DESC LIMIT ?",
                con, params=(sym, lookback),
            )
            if not df.empty:
                df["date"] = pd.to_datetime(df["date"])
                results[sym] = df.iloc[::-1].reset_index(drop=True)
    finally:
        con.close()
    return results


def latest_date(symbol: str | None = None, db_path: Path = DB_PATH) -> str | None:
    con = _connect(db_path)
    if con is None:
        return None
    try:
        if symbol:
            row = con.execute(
                "SELECT MAX(date) FROM ohlc WHERE symbol=?", (symbol,)
            ).fetchone()
        else:
            row = con.execute("SELECT MAX(date) FROM ohlc").fetchone()
        return row[0] if row else None
    finally:
        con.close()
