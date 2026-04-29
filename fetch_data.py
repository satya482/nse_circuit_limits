#!/usr/bin/env python3
"""
Central OHLC data fetcher — run after 4:05 PM IST on every trading day.

Universe:
  - TVScreener-filtered NSE common stocks (MCap ₹800 Cr – ₹1 Lakh Cr, no EMA filter)
  - NIFTY MIDSML 400 index (for RS benchmarking)

Two-phase fetch:
  Phase 1 — Backfill:  historical_data() per symbol where DB has < 200 rows
  Phase 2 — Delta:     quote() in batches of 500 for today's bar (fast)

Output:
  .ohlc_data/market.db          SQLite, gitignored
  .ohlc_data/data_manifest.csv  symbol/last_date/rows audit, committed to git
"""

import sys
import time
import sqlite3
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
from tradingview_screener import Query, col

sys.path.insert(0, str(Path(__file__).parent / "ema-compression-scanner"))
from data_loader import load_env, get_kite

# ── Paths ──────────────────────────────────────────────────────────────────────
REPO_DIR      = Path(__file__).parent
DB_PATH       = REPO_DIR / ".ohlc_data" / "market.db"
MANIFEST_PATH = REPO_DIR / ".ohlc_data" / "data_manifest.csv"
ENV_PATH      = REPO_DIR / "ema-compression-scanner" / ".env"

LOOKBACK_DAYS  = 400        # calendar days for historical backfill (~280 trading bars)
MIN_ROWS       = 200        # symbols below this trigger a backfill
BATCH_SIZE     = 500        # max instruments per quote() call
HIST_RATE      = 0.35       # seconds between historical_data() calls

MC_LOW         = 800     * 1_00_00_000   # ₹800 Cr
MC_HIGH        = 1_00_000 * 1_00_00_000  # ₹1 Lakh Cr
BENCHMARK_SYM  = "NIFTY MIDSML 400"     # Kite tradingsymbol; used by all RS scanners

# ── Schema ─────────────────────────────────────────────────────────────────────
_SCHEMA = """
CREATE TABLE IF NOT EXISTS instruments (
    instrument_token  INTEGER PRIMARY KEY,
    tradingsymbol     TEXT NOT NULL,
    name              TEXT,
    segment           TEXT,
    instrument_type   TEXT,
    last_updated      DATE
);

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


# ── TVScreener universe ────────────────────────────────────────────────────────
def get_tv_universe() -> set[str]:
    """Return NSE common-stock symbols passing MCap filter (no EMA condition)."""
    print("  Fetching universe from TradingView screener...")
    _, df = (
        Query()
        .set_markets("india")
        .select("name")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(2000)
        .get_scanner_data()
    )
    symbols = set(df["name"].tolist())
    print(f"  TVScreener universe: {len(symbols)} stocks")
    return symbols


# ── Instruments ────────────────────────────────────────────────────────────────
def refresh_instruments(kite, con: sqlite3.Connection) -> pd.DataFrame:
    """Build instrument list from TV universe + benchmark index, store in DB."""
    today = date.today().isoformat()

    # Skip if already fetched today
    row = con.execute(
        "SELECT COUNT(*) FROM instruments WHERE last_updated=?", (today,)
    ).fetchone()
    if row[0] > 0:
        print("  Instruments already fetched today, loading from DB...")
        return pd.read_sql("SELECT * FROM instruments WHERE last_updated=?",
                           con, params=(today,))

    tv_symbols = get_tv_universe()

    print("  Downloading instruments from Kite...")
    raw = pd.DataFrame(kite.instruments("NSE"))

    no_dash = ~raw["tradingsymbol"].str.contains("-", regex=False)

    # Stocks: EQ segment intersected with TV universe
    stocks = raw[
        (raw["exchange"] == "NSE") &
        (raw["segment"] == "NSE") &
        (raw["instrument_type"] == "EQ") &
        no_dash &
        raw["tradingsymbol"].isin(tv_symbols)
    ].copy()

    # Benchmark index: exactly one row
    benchmark = raw[
        (raw["segment"] == "INDICES") &
        (raw["tradingsymbol"] == BENCHMARK_SYM)
    ].copy()
    if benchmark.empty:
        print(f"  WARN: {BENCHMARK_SYM!r} not found in Kite instruments list",
              file=sys.stderr)

    filtered = pd.concat([stocks, benchmark], ignore_index=True)
    filtered["last_updated"] = today

    con.execute("DELETE FROM instruments")
    for _, r in filtered.iterrows():
        con.execute(
            "INSERT OR REPLACE INTO instruments VALUES (?,?,?,?,?,?)",
            (int(r["instrument_token"]), r["tradingsymbol"],
             str(r.get("name", "")), r["segment"], r["instrument_type"], today),
        )
    con.commit()
    print(f"  Instruments: {len(stocks)} EQ stocks + {len(benchmark)} benchmark index")
    return filtered


# ── Symbol status ──────────────────────────────────────────────────────────────
def get_symbol_status(con: sqlite3.Connection) -> dict[str, tuple[str, int]]:
    """Return {symbol: (last_date_iso, row_count)} for every symbol in ohlc table."""
    rows = con.execute(
        "SELECT symbol, MAX(date), COUNT(*) FROM ohlc GROUP BY symbol"
    ).fetchall()
    return {r[0]: (r[1], r[2]) for r in rows}


# ── Phase 1: Backfill ──────────────────────────────────────────────────────────
def backfill(kite, tokens: dict[str, int], symbols: list[str],
             con: sqlite3.Connection) -> None:
    today     = date.today()
    from_date = today - timedelta(days=LOOKBACK_DAYS)
    total     = len(symbols)
    print(f"\n  Phase 1 — Backfill: {total} symbols (from {from_date})...")

    for i, sym in enumerate(symbols, 1):
        token = tokens.get(sym)
        if not token:
            continue
        try:
            data = kite.historical_data(token, from_date, today, "day")
            if data:
                rows = []
                for d in data:
                    dt = d["date"]
                    dt_str = dt.date().isoformat() if hasattr(dt, "date") else str(dt)[:10]
                    rows.append((sym, dt_str, d["open"], d["high"],
                                 d["low"], d["close"], d["volume"]))
                con.executemany(
                    "INSERT OR IGNORE INTO ohlc VALUES (?,?,?,?,?,?,?)", rows
                )
                con.commit()
        except Exception as e:
            print(f"    WARN {sym}: {e}", file=sys.stderr)

        if i % 100 == 0:
            print(f"    {i}/{total}...")
        time.sleep(HIST_RATE)

    print(f"  Phase 1 complete.")


# ── Phase 2: Daily delta via quote() ──────────────────────────────────────────
def delta_update(kite, instruments_df: pd.DataFrame,
                 symbols: list[str], con: sqlite3.Connection) -> None:
    today   = date.today().isoformat()
    total   = len(symbols)
    print(f"\n  Phase 2 — Delta update via quote(): {total} symbols for {today}...")

    # Build "NSE:SYMBOL" strings; keep mapping back to plain symbol
    ex_syms = [f"NSE:{s}" for s in symbols]

    inserted = 0
    for i in range(0, len(ex_syms), BATCH_SIZE):
        batch = ex_syms[i : i + BATCH_SIZE]
        try:
            quotes = kite.quote(batch)
            rows = []
            for ex_sym, q in quotes.items():
                sym  = ex_sym.split(":", 1)[1]            # "NSE:SBIN" → "SBIN"
                ltp  = q.get("last_price", 0)
                if not ltp:                                # market closed / no data
                    continue
                ohlc = q.get("ohlc", {})
                rows.append((
                    sym, today,
                    ohlc.get("open"),
                    ohlc.get("high"),
                    ohlc.get("low"),
                    ltp,                                   # close = LTP, NOT ohlc.close
                    q.get("volume", 0),
                ))
            con.executemany(
                "INSERT OR IGNORE INTO ohlc VALUES (?,?,?,?,?,?,?)", rows
            )
            con.commit()
            inserted += len(rows)
            print(f"    Batch {i // BATCH_SIZE + 1}/{-(-len(ex_syms)//BATCH_SIZE)}: "
                  f"{len(rows)} quotes inserted")
        except Exception as e:
            print(f"    WARN batch {i // BATCH_SIZE + 1}: {e}", file=sys.stderr)
        time.sleep(0.1)

    print(f"  Phase 2 complete: {inserted} symbols updated for {today}")


# ── Manifest ───────────────────────────────────────────────────────────────────
def write_manifest(con: sqlite3.Connection) -> None:
    df = pd.read_sql(
        "SELECT symbol, MAX(date) AS last_date, COUNT(*) AS rows "
        "FROM ohlc GROUP BY symbol ORDER BY symbol",
        con,
    )
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(MANIFEST_PATH, index=False)
    print(f"\n  Manifest written: {len(df)} symbols -> {MANIFEST_PATH.name}")


# ── Main ───────────────────────────────────────────────────────────────────────
def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    env  = load_env(ENV_PATH)
    kite = get_kite(env)

    con = sqlite3.connect(DB_PATH)
    init_db(con)

    # 1. Instruments
    instruments_df = refresh_instruments(kite, con)
    all_symbols    = instruments_df["tradingsymbol"].tolist()
    tokens: dict[str, int] = dict(zip(
        instruments_df["tradingsymbol"],
        instruments_df["instrument_token"].astype(int),
    ))
    print(f"  Total symbols to track: {len(all_symbols)}")

    # 2. Determine what each symbol needs
    status  = get_symbol_status(con)
    today   = date.today().isoformat()

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
        backfill(kite, tokens, needs_backfill, con)

    if needs_delta:
        delta_update(kite, instruments_df, needs_delta, con)

    write_manifest(con)
    con.close()

    total_rows = sqlite3.connect(DB_PATH).execute(
        "SELECT COUNT(*) FROM ohlc"
    ).fetchone()[0]
    print(f"\nDone. DB: {DB_PATH}  ({total_rows:,} total rows)")


if __name__ == "__main__":
    main()