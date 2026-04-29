#!/usr/bin/env python3
"""
Shared SQLite reader for OHLC data.
All scanners and backtests import load_ohlc() / load_ohlc_many() from here.

DB layout:
  ohlc(symbol TEXT, date DATE, open REAL, high REAL, low REAL, close REAL, volume INTEGER)
  PRIMARY KEY (symbol, date)

Columns returned: date (datetime), open, high, low, close, volume  — all lowercase.
Rows are ordered oldest → newest.
"""

import sqlite3
from pathlib import Path

import pandas as pd

DB_PATH = Path(__file__).parent / ".ohlc_data" / "market.db"


def _connect(db_path: Path) -> sqlite3.Connection | None:
    if not db_path.exists():
        return None
    return sqlite3.connect(db_path)


def load_ohlc(
    symbol: str,
    lookback: int = 400,
    db_path: Path = DB_PATH,
) -> pd.DataFrame | None:
    """Return OHLC DataFrame for one symbol, oldest first, up to lookback rows.

    Columns: date (datetime64), open, high, low, close, volume.
    'date' is a plain column (not index) — call .set_index('date') if needed.
    Returns None if symbol not found or DB missing.
    """
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
    """Return {symbol: df} for a list of symbols in a single DB connection.

    Same column format as load_ohlc(). Symbols missing from DB are omitted.
    """
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


def latest_date(db_path: Path = DB_PATH) -> str | None:
    """Return the most recent date present in the ohlc table (ISO string)."""
    con = _connect(db_path)
    if con is None:
        return None
    try:
        row = con.execute("SELECT MAX(date) FROM ohlc").fetchone()
        return row[0] if row else None
    finally:
        con.close()