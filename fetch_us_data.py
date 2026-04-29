#!/usr/bin/env python3
"""
US OHLC data fetcher — run at 4:40 PM IST on every trading day.
Fetches from yfinance; no broker auth required.

Universe:
  NYSE + NASDAQ common stocks, MCap $300M–$10B, price > $5, avg 10d vol > 300K
  SPY (S&P 500 ETF, benchmark for RS calculations)

Two-phase fetch per symbol:
  Phase 1 — Backfill : yf.download(batch, period="2y") where DB has < MIN_ROWS bars
  Phase 2 — Delta    : yf.download(batch, period="5d") for symbols behind today

Output:
  .us_ohlc_data/us_market.db      SQLite, gitignored
  us_data_manifest.csv            symbol/last_date/rows audit, committed to git
"""

import sys
import time
import sqlite3
from datetime import date
from pathlib import Path

import pandas as pd
import yfinance as yf
from tradingview_screener import Query, col

sys.stdout.reconfigure(encoding="utf-8")

# ── Paths ──────────────────────────────────────────────────────────────────────
REPO_DIR      = Path(__file__).parent
DB_PATH       = REPO_DIR / ".us_ohlc_data" / "us_market.db"
MANIFEST_PATH = REPO_DIR / "us_data_manifest.csv"

# ── Config ─────────────────────────────────────────────────────────────────────
BENCHMARK_SYM  = "SPY"
MIN_ROWS       = 200          # symbols below this trigger a 2y backfill
BATCH_SIZE     = 100          # tickers per yf.download() call
BATCH_SLEEP    = 2            # seconds between batches
MC_LOW         = 300_000_000  # $300M
MC_HIGH        = 10_000_000_000  # $10B

# ── Schema ─────────────────────────────────────────────────────────────────────
_SCHEMA = """
CREATE TABLE IF NOT EXISTS ohlc (
    symbol   TEXT NOT NULL,
    date     DATE NOT NULL,
    open     REAL,
    high     REAL,
    low      REAL,
    close    REAL,
    volume   INTEGER,
    PRIMARY KEY (symbol, date)
);
CREATE INDEX IF NOT EXISTS idx_ohlc_symbol_date ON ohlc (symbol, date);
"""


def init_db(con: sqlite3.Connection) -> None:
    con.executescript(_SCHEMA)
    con.commit()


# ── Universe ───────────────────────────────────────────────────────────────────
def get_tv_universe() -> list[str]:
    print("  Fetching universe from TradingView screener (US)...")
    _, df = (
        Query()
        .set_markets("america")
        .select("name", "close", "market_cap_basic", "average_volume_10d_calc")
        .where(
            col("exchange").isin(["NASDAQ", "NYSE"]),
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 5,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
            col("average_volume_10d_calc") > 300_000,
        )
        .limit(3000)
        .get_scanner_data()
    )
    symbols = df["name"].tolist()
    print(f"  TVScreener universe: {len(symbols)} US stocks")
    return symbols


# ── yfinance download ──────────────────────────────────────────────────────────
def _download_batch(tickers: list[str], period: str) -> dict[str, pd.DataFrame]:
    """Download OHLCV for a list of tickers. Returns {ticker: df} oldest-first."""
    if not tickers:
        return {}

    raw = yf.download(
        tickers if len(tickers) > 1 else tickers[0],
        period=period,
        auto_adjust=True,
        progress=False,
        group_by="ticker",
    )

    results = {}
    for sym in tickers:
        try:
            # Single-ticker download returns flat columns; multi returns MultiIndex
            df = raw if len(tickers) == 1 else raw[sym]
            df = df.copy()
            df.columns = [c.lower() for c in df.columns]
            needed = ["open", "high", "low", "close", "volume"]
            if not all(c in df.columns for c in needed):
                continue
            df = df[needed].dropna()
            if df.empty:
                continue
            # Normalise index: strip timezone, keep date only
            idx = pd.to_datetime(df.index)
            if idx.tz is not None:
                idx = idx.tz_convert("UTC").tz_localize(None)
            df.index = idx.normalize()
            results[sym] = df
        except (KeyError, TypeError):
            continue

    return results


# ── DB helpers ─────────────────────────────────────────────────────────────────
def get_symbol_status(con: sqlite3.Connection) -> dict[str, tuple[str, int]]:
    rows = con.execute(
        "SELECT symbol, MAX(date), COUNT(*) FROM ohlc GROUP BY symbol"
    ).fetchall()
    return {r[0]: (r[1], r[2]) for r in rows}


def _upsert(con: sqlite3.Connection, symbol: str, df: pd.DataFrame) -> int:
    rows = [
        (symbol, str(dt.date()), row.open, row.high, row.low, row.close, int(row.volume))
        for dt, row in df.iterrows()
    ]
    con.executemany(
        "INSERT OR IGNORE INTO ohlc VALUES (?,?,?,?,?,?,?)", rows
    )
    con.commit()
    return len(rows)


# ── Phase 1: Backfill ──────────────────────────────────────────────────────────
def backfill(symbols: list[str], con: sqlite3.Connection) -> None:
    total = len(symbols)
    print(f"\n  Phase 1 — Backfill: {total} symbols (period=2y)...")
    inserted = 0
    for batch_start in range(0, total, BATCH_SIZE):
        batch = symbols[batch_start: batch_start + BATCH_SIZE]
        batch_num = batch_start // BATCH_SIZE + 1
        n_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
        print(f"    Batch {batch_num}/{n_batches} ({len(batch)} tickers)...")
        data = _download_batch(batch, period="2y")
        for sym, df in data.items():
            inserted += _upsert(con, sym, df)
        time.sleep(BATCH_SLEEP)
    print(f"  Phase 1 complete. {inserted} rows inserted.")


# ── Phase 2: Delta ─────────────────────────────────────────────────────────────
def delta_update(symbols: list[str], con: sqlite3.Connection) -> None:
    today = date.today().isoformat()
    total = len(symbols)
    print(f"\n  Phase 2 — Delta: {total} symbols (period=5d)...")
    updated = 0
    for batch_start in range(0, total, BATCH_SIZE):
        batch = symbols[batch_start: batch_start + BATCH_SIZE]
        batch_num = batch_start // BATCH_SIZE + 1
        n_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
        data = _download_batch(batch, period="5d")
        for sym, df in data.items():
            # Only insert rows newer than what's in DB
            sym_last = con.execute(
                "SELECT MAX(date) FROM ohlc WHERE symbol=?", (sym,)
            ).fetchone()[0]
            if sym_last:
                df = df[df.index > pd.Timestamp(sym_last)]
            if not df.empty:
                _upsert(con, sym, df)
                updated += 1
        if batch_num % 5 == 0:
            print(f"    {batch_num}/{n_batches}...")
        time.sleep(BATCH_SLEEP)
    print(f"  Phase 2 complete. {updated} symbols received new bars.")


# ── Manifest ───────────────────────────────────────────────────────────────────
def write_manifest(con: sqlite3.Connection) -> None:
    df = pd.read_sql(
        "SELECT symbol, MAX(date) AS last_date, COUNT(*) AS rows "
        "FROM ohlc GROUP BY symbol ORDER BY symbol",
        con,
    )
    df.to_csv(MANIFEST_PATH, index=False)
    print(f"\n  Manifest written: {len(df)} symbols → {MANIFEST_PATH.name}")


# ── Main ───────────────────────────────────────────────────────────────────────
def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    init_db(con)

    print("\n=== US OHLC Fetcher ===")
    today = date.today().isoformat()

    # 1. Build universe (TV screener + SPY)
    tv_symbols = get_tv_universe()
    all_symbols = list(dict.fromkeys([BENCHMARK_SYM] + tv_symbols))  # SPY first, deduped
    print(f"  Total symbols to track: {len(all_symbols)}  (incl. {BENCHMARK_SYM})")

    # 2. Classify each symbol
    status = get_symbol_status(con)
    needs_backfill = [s for s in all_symbols
                      if s not in status or status[s][1] < MIN_ROWS]
    needs_delta    = [s for s in all_symbols
                      if s in status and status[s][1] >= MIN_ROWS
                      and status[s][0] < today]
    up_to_date     = len(all_symbols) - len(needs_backfill) - len(needs_delta)

    print(f"\n  Symbol status:")
    print(f"    Needs backfill : {len(needs_backfill)}")
    print(f"    Needs delta    : {len(needs_delta)}")
    print(f"    Already today  : {up_to_date}")

    if needs_backfill:
        backfill(needs_backfill, con)

    if needs_delta:
        delta_update(needs_delta, con)

    write_manifest(con)
    con.close()

    total_rows = sqlite3.connect(DB_PATH).execute(
        "SELECT COUNT(*) FROM ohlc"
    ).fetchone()[0]
    print(f"\nDone. DB: {DB_PATH}  ({total_rows:,} total rows)")


if __name__ == "__main__":
    main()
