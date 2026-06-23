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
            con,
            params=(symbol, lookback),
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
                con,
                params=(sym, lookback),
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


def _fmt_name(raw: str) -> str:
    """Title-case a Kite instrument name and strip common legal suffixes."""
    s = raw.strip().title()
    for suffix in (
        " Private Limited",
        " Pvt. Ltd.",
        " Pvt Ltd",
        " Pvt. Ltd",
        " Limited",
        " Ltd.",
        " Ltd",
        " Llp",
        " Lp",
    ):
        if s.endswith(suffix):
            s = s[: -len(suffix)]
            break
    return s


def _fmt_mcap(cr: float) -> str:
    """Format market cap in crores to a short display string."""
    if cr >= 100_000:
        return f"₹{cr / 100_000:.1f}L Cr"
    elif cr >= 1_000:
        return f"₹{round(cr / 1_000):.0f}K Cr"
    else:
        return f"₹{cr:.0f} Cr"


def _ensure_mcap_col(con: sqlite3.Connection) -> None:
    """Add market_cap_cr column to instruments if not present (one-time migration)."""
    try:
        con.execute("ALTER TABLE instruments ADD COLUMN market_cap_cr REAL")
        con.commit()
    except Exception:
        pass


def get_names(
    symbols: list[str] | None = None,
    db_path: Path = DB_PATH,
) -> dict[str, str]:
    """Return {tradingsymbol: 'Name · ₹XK Cr'} from the instruments table.
    market_cap_cr is appended when available. Missing symbols are omitted."""
    con = _connect(db_path)
    if con is None:
        return {}
    try:
        if symbols is not None and len(symbols) == 0:
            return {}
        _ensure_mcap_col(con)
        if symbols is None:
            rows = con.execute(
                "SELECT tradingsymbol, name, market_cap_cr FROM instruments"
            ).fetchall()
        else:
            ph = ",".join("?" * len(symbols))
            rows = con.execute(
                f"SELECT tradingsymbol, name, market_cap_cr FROM instruments"
                f" WHERE tradingsymbol IN ({ph})",
                symbols,
            ).fetchall()
        result = {}
        for sym, name, mcap_cr in rows:
            label = _fmt_name(name) if name and name.strip() else ""
            if mcap_cr:
                mcap_str = _fmt_mcap(float(mcap_cr))
                label = f"{label} · {mcap_str}" if label else mcap_str
            if label:
                result[sym] = label
        return result
    except Exception:
        return {}
    finally:
        con.close()


def liq_tag(df: pd.DataFrame) -> str:
    """Compact traded-value label for scanner sub cells.
    Format: '{accel_arrow}{avg10_cr:.0f}Cr {ratio_arrow}{ratio:.1f}×'
    accel_arrow: ↗ avg10>avg20 by >10% | ↘ avg10<avg20 by >10% | → stable
    ratio_arrow: ↑ today>avg10 by >15% | ↓ today<avg10 by >25% | '' neutral
    Returns '' on insufficient data or error.
    """
    try:
        notional = df["close"].astype(float) * df["volume"].astype(float)
        avg10 = float(notional.rolling(10, min_periods=5).mean().iloc[-1]) / 1e7
        avg20 = float(notional.rolling(20, min_periods=10).mean().iloc[-1]) / 1e7
        today_val = float(notional.iloc[-1]) / 1e7
        if avg10 <= 0:
            return ""
        ratio = today_val / avg10
        accel = avg10 / avg20 if avg20 > 0 else 1.0
        ratio_arrow = "↑" if ratio > 1.15 else ("↓" if ratio < 0.75 else "")
        accel_arrow = "↗" if accel > 1.10 else ("↘" if accel < 0.90 else "→")
        cr_str = f"{avg10:.1f}Cr" if avg10 < 1 else f"{avg10:.0f}Cr"
        return f"{accel_arrow}{cr_str} {ratio_arrow}{ratio:.1f}×"
    except Exception:
        return ""


def get_liq_labels(
    symbols: list[str] | None = None,
    db_path: Path = DB_PATH,
) -> dict[str, str]:
    """Return {tradingsymbol: liq_tag_str} using the last 25 bars per symbol.
    Pass symbols=None to load for all symbols in the DB.
    """
    con = _connect(db_path)
    if con is None:
        return {}
    try:
        if symbols is None:
            syms = [
                r[0] for r in con.execute("SELECT DISTINCT symbol FROM ohlc").fetchall()
            ]
        else:
            syms = list(symbols)
        if not syms:
            return {}
        result = {}
        for sym in syms:
            df = pd.read_sql(
                "SELECT date, close, volume FROM ohlc"
                " WHERE symbol=? ORDER BY date DESC LIMIT 25",
                con,
                params=(sym,),
            )
            if len(df) >= 5:
                df = df.iloc[::-1].reset_index(drop=True)
                tag = liq_tag(df)
                if tag:
                    result[sym] = tag
        return result
    except Exception:
        return {}
    finally:
        con.close()
