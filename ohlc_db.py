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
from datetime import date
from pathlib import Path

import numpy as np
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
    Format: '{accel_arrow}{avg10_cr}Cr · {today_cr}Cr'
    accel_arrow: ↗ avg10>avg20 by >10% | ↘ avg10<avg20 by >10% | → stable
    avg10_cr  = price × avg_volume(10d) / 1e7  — avg daily notional
    today_cr  = price × today_volume / 1e7     — today's notional
    Returns '' on insufficient data or error.
    """
    try:
        vol = df["volume"].astype(float)
        close = df["close"].astype(float)
        today_close = float(close.iloc[-1])
        today_vol = float(vol.iloc[-1])
        avg10_vol = float(vol.rolling(10, min_periods=5).mean().iloc[-1])
        avg20_vol = float(vol.rolling(20, min_periods=10).mean().iloc[-1])
        if avg10_vol <= 0:
            return ""
        avg10 = today_close * avg10_vol / 1e7
        today_cr = today_close * today_vol / 1e7
        accel = avg10_vol / avg20_vol if avg20_vol > 0 else 1.0
        accel_arrow = "↗" if accel > 1.10 else ("↘" if accel < 0.90 else "→")
        avg_str = f"{avg10:.1f}Cr" if avg10 < 1 else f"{avg10:.0f}Cr"
        today_str = f"{today_cr:.1f}Cr" if today_cr < 1 else f"{today_cr:.0f}Cr"
        return f"{accel_arrow}{avg_str} · {today_str}"
    except Exception:
        return ""


def cmf_series(df: pd.DataFrame, n: int = 20) -> pd.Series:
    """Raw Chaikin Money Flow series (rolling n-bar sum of money-flow-volume over
    rolling n-bar sum of volume), index-reset, NaNs dropped. Empty if fewer than
    n bars available. Factored out of cmf_days() so quality scoring (which needs
    the raw value, not just sign+days-since-cross) shares one source of truth."""
    high = df["high"].astype(float)
    low = df["low"].astype(float)
    close = df["close"].astype(float)
    volume = df["volume"].astype(float)

    range_ = high - low
    mfm = np.where(range_ > 0, ((close - low) - (high - close)) / range_, 0.0)
    mfv = pd.Series(mfm, index=df.index) * volume

    return (
        mfv.rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum()
    ).dropna().reset_index(drop=True)


def cmf_days(df: pd.DataFrame, n: int = 20, cap: int = 30) -> tuple[bool, int] | None:
    """Chaikin Money Flow zero-line-cross recency.
    Returns (cmf_positive, bars_since_zero_cross), bars_ago capped at `cap`.
    None if fewer than n + 2 bars.
    No float equality: cross = sign flip via > / <= boundary, mirrors
    zl25_stats()'s bars-ago scan pattern.
    """
    if len(df) < n + 2:
        return None

    cmf = cmf_series(df, n=n)
    m = len(cmf)
    if m < 2:
        return None

    cmf_positive = bool(cmf.iloc[-1] > 0)

    limit = max(1, m - cap)
    for i in range(m - 1, limit - 1, -1):
        curr, prev = cmf.iloc[i], cmf.iloc[i - 1]
        if cmf_positive and curr > 0 and prev <= 0:
            return True, (m - 1) - i
        if not cmf_positive and curr <= 0 and prev > 0:
            return False, (m - 1) - i

    return cmf_positive, cap


def cmf_tag(df: pd.DataFrame, n: int = 20, cap: int = 30) -> str:
    """Formats cmf_days() -> '↑CMF{d}d' / '↓CMF{d}d'. '' on None or error."""
    try:
        result = cmf_days(df, n=n, cap=cap)
        if result is None:
            return ""
        positive, days = result
        arrow = "↑" if positive else "↓"
        return f"{arrow}CMF{days}d"
    except Exception:
        return ""


DELIV_SPIKE_N = 20  # baseline window, trading days
DELIV_SPIKE_MULT = 1.5  # today must exceed baseline * mult to count as spike


def load_delivery(symbol: str, lookback: int = 60, db_path: Path = DB_PATH) -> pd.DataFrame | None:
    """Return (date, deliv_pct) for one symbol from the `delivery` table, oldest-first.
    None if symbol/table missing or DB error -- delivery data lags scanner runs by
    design, so 'no data yet' is expected, not an error state."""
    con = _connect(db_path)
    if con is None:
        return None
    try:
        df = pd.read_sql(
            "SELECT date, deliv_pct FROM delivery WHERE symbol=? ORDER BY date DESC LIMIT ?",
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


def deliv_spike(
    df: pd.DataFrame, n: int = DELIV_SPIKE_N, mult: float = DELIV_SPIKE_MULT
) -> tuple[float, float] | None:
    """Returns (today_pct, baseline_pct) when today's deliv_pct exceeds the rolling
    mean of the PRIOR n days by `mult`. Baseline strictly excludes today's row --
    no look-ahead. None if no spike or fewer than n+1 rows."""
    if df is None or len(df) < n + 1:
        return None
    pct = df["deliv_pct"].astype(float)
    today_pct = float(pct.iloc[-1])
    baseline_pct = float(pct.iloc[-(n + 1) : -1].mean())
    if today_pct <= baseline_pct * mult:
        return None
    return today_pct, baseline_pct


def deliv_tag(
    symbol: str,
    n: int = DELIV_SPIKE_N,
    mult: float = DELIV_SPIKE_MULT,
    db_path: Path = DB_PATH,
) -> str:
    """'' if no spike / insufficient data. 'DEL{today_pct:.0f}%' if spike.
    Binary flag, NOT always-on (unlike cmf_tag) -- only appears on genuine spike
    days. The '(T-1)' suffix is appended only when the latest row in `delivery`
    is older than today (the normal 4:xx PM scanner-run case, where bhavcopy for
    day T hasn't published yet and delivery data lags by one session). When
    `backfill_delivery_markers.py` runs later the same evening right after
    fetch_delivery.py has written today's own row, the latest date IS today --
    no lag -- so the suffix is omitted."""
    try:
        df = load_delivery(symbol, lookback=n + 1, db_path=db_path)
        result = deliv_spike(df, n=n, mult=mult)
        if result is None:
            return ""
        today_pct, _ = result
        latest_date = df["date"].iloc[-1]
        if pd.Timestamp(latest_date).normalize() == pd.Timestamp(date.today()):
            return f"DEL{today_pct:.0f}%"
        return f"DEL{today_pct:.0f}%(T-1)"
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
