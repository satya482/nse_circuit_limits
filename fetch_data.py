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
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
from tradingview_screener import Query, col

sys.path.insert(0, str(Path(__file__).parent / "ema-compression-scanner"))
from data_loader import load_env, get_kite

# ── Paths ──────────────────────────────────────────────────────────────────────
REPO_DIR = Path(__file__).parent
DB_PATH = REPO_DIR / ".ohlc_data" / "market.db"
MANIFEST_PATH = REPO_DIR / ".ohlc_data" / "data_manifest.csv"
ENV_PATH = REPO_DIR / "ema-compression-scanner" / ".env"

LOOKBACK_DAYS = 400  # calendar days for historical backfill (~280 trading bars)
MIN_ROWS = 200  # symbols below this trigger a backfill
BATCH_SIZE = 50  # max instruments per quote() call (larger batches trigger Cloudflare rate-limit)
BATCH_SLEEP = 3  # seconds between batches
BATCH_RETRY_WAIT = 30  # seconds to wait before retrying a failed batch
HIST_RATE = 0.35  # seconds between historical_data() calls

IST = timezone(timedelta(hours=5, minutes=30))

NIFTY50_SYM = "NIFTY 50"  # added for breadth dashboard price panel
BREADTH_UNIVERSE_PATH = REPO_DIR / "data" / "breadth_universe.csv"
BREADTH_LOOKBACK_DAYS = 3650  # ~10 years calendar days
BREADTH_MIN_ROWS = 2000  # re-backfill if SQLite has fewer rows

MC_LOW = 800 * 1_00_00_000  # ₹800 Cr
MC_HIGH = 1_00_000 * 1_00_00_000  # ₹1 Lakh Cr
BENCHMARK_SYM = "NIFTY MIDSML 400"  # Kite tradingsymbol; used by all RS scanners

# ── Schema ─────────────────────────────────────────────────────────────────────
_SCHEMA = """
CREATE TABLE IF NOT EXISTS instruments (
    instrument_token  INTEGER PRIMARY KEY,
    tradingsymbol     TEXT NOT NULL,
    name              TEXT,
    segment           TEXT,
    instrument_type   TEXT,
    last_updated      DATE,
    market_cap_cr     REAL
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
    # one-time migration: add market_cap_cr to existing DBs
    try:
        con.execute("ALTER TABLE instruments ADD COLUMN market_cap_cr REAL")
        con.commit()
    except Exception:
        pass


# ── TVScreener universe ────────────────────────────────────────────────────────
def get_tv_universe() -> tuple[set[str], dict[str, float]]:
    """Return (symbols, {symbol: market_cap_cr}) from TradingView screener."""
    print("  Fetching universe from TradingView screener...")
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "market_cap_basic")
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
    # market_cap_basic is in absolute INR; convert to Cr (1 Cr = 10,000,000)
    mcaps = {
        row["name"]: row["market_cap_basic"] / 10_000_000
        for _, row in df.iterrows()
        if row["market_cap_basic"] and row["market_cap_basic"] > 0
    }
    print(f"  TVScreener universe: {len(symbols)} stocks")
    return symbols, mcaps


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
        return pd.read_sql(
            "SELECT * FROM instruments WHERE last_updated=?", con, params=(today,)
        )

    tv_symbols, tv_mcaps = get_tv_universe()

    print("  Downloading instruments from Kite...")
    raw = pd.DataFrame(kite.instruments("NSE"))

    no_dash = ~raw["tradingsymbol"].str.contains("-", regex=False)

    # Stocks: EQ segment intersected with TV universe
    stocks = raw[
        (raw["exchange"] == "NSE")
        & (raw["segment"] == "NSE")
        & (raw["instrument_type"] == "EQ")
        & no_dash
        & raw["tradingsymbol"].isin(tv_symbols)
    ].copy()

    # Benchmark indices: MIDSML 400 (RS benchmark) and NIFTY 50 (dashboard price panel)
    benchmark = raw[
        (raw["segment"] == "INDICES")
        & raw["tradingsymbol"].isin([BENCHMARK_SYM, NIFTY50_SYM])
    ].copy()
    missing = {BENCHMARK_SYM, NIFTY50_SYM} - set(benchmark["tradingsymbol"])
    for sym in missing:
        print(f"  WARN: {sym!r} not found in Kite instruments list", file=sys.stderr)

    filtered = pd.concat([stocks, benchmark], ignore_index=True)
    filtered["last_updated"] = today

    con.execute("DELETE FROM instruments")
    for _, r in filtered.iterrows():
        mcap_cr = tv_mcaps.get(r["tradingsymbol"])  # None for benchmark index
        con.execute(
            "INSERT OR REPLACE INTO instruments VALUES (?,?,?,?,?,?,?)",
            (
                int(r["instrument_token"]),
                r["tradingsymbol"],
                str(r.get("name", "")),
                r["segment"],
                r["instrument_type"],
                today,
                mcap_cr,
            ),
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
def backfill(
    kite, tokens: dict[str, int], symbols: list[str], con: sqlite3.Connection
) -> None:
    today = date.today()
    from_date = today - timedelta(days=LOOKBACK_DAYS)
    total = len(symbols)
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
                    dt_str = (
                        dt.date().isoformat() if hasattr(dt, "date") else str(dt)[:10]
                    )
                    rows.append(
                        (
                            sym,
                            dt_str,
                            d["open"],
                            d["high"],
                            d["low"],
                            d["close"],
                            d["volume"],
                        )
                    )
                con.executemany(
                    "INSERT OR IGNORE INTO ohlc VALUES (?,?,?,?,?,?,?)", rows
                )
                con.commit()
        except Exception as e:
            print(f"    WARN {sym}: {e}", file=sys.stderr)

        if i % 100 == 0:
            print(f"    {i}/{total}...")
        time.sleep(HIST_RATE)

    print("  Phase 1 complete.")


# ── Breadth universe: 10yr backfill ───────────────────────────────────────────
def backfill_breadth(kite, con: sqlite3.Connection) -> None:
    """Extended 10yr backfill for broad breadth universe.

    Runs only for symbols below BREADTH_MIN_ROWS in SQLite.
    Skipped silently if breadth_universe.csv is absent.

    Kite API enforces a 2000-calendar-day limit per request for the "day"
    interval.  We paginate in 1800-day windows (oldest-first) so each call
    stays within the limit.
    """
    if not BREADTH_UNIVERSE_PATH.exists():
        print(
            "  breadth_universe.csv not found — skipping breadth backfill"
            " (run scripts/refresh_breadth_universe.py first)"
        )
        return

    breadth_df = pd.read_csv(BREADTH_UNIVERSE_PATH)
    symbols = breadth_df["symbol"].tolist()
    tokens: dict[str, int] = dict(
        zip(breadth_df["symbol"], breadth_df["instrument_token"].astype(int))
    )

    today = datetime.now(IST).date()
    target_from = today - timedelta(days=BREADTH_LOOKBACK_DAYS)

    # Build date windows of <= 1800 calendar days (safe below Kite's 2000-day limit)
    WINDOW = 1800
    windows: list[tuple[date, date]] = []
    win_end = today
    while win_end > target_from:
        win_start = max(win_end - timedelta(days=WINDOW), target_from)
        windows.append((win_start, win_end))
        win_end = win_start - timedelta(days=1)
    windows.reverse()  # oldest window first

    status = get_symbol_status(con)
    needs = [s for s in symbols if s not in status or status[s][1] < BREADTH_MIN_ROWS]
    if not needs:
        print(
            f"  Breadth universe: all {len(symbols)} symbols have"
            f" >=BREADTH_MIN_ROWS rows"
        )
        return

    print(
        f"\n  Breadth backfill: {len(needs)}/{len(symbols)} symbols"
        f" from {target_from} ({len(windows)} windows x ~{WINDOW}d)..."
    )
    for i, sym in enumerate(needs, 1):
        token = tokens.get(sym)
        if not token:
            continue
        for w_start, w_end in windows:
            try:
                data = kite.historical_data(token, w_start, w_end, "day")
                if data:
                    rows = []
                    for d in data:
                        dt = d["date"]
                        dt_str = (
                            dt.date().isoformat()
                            if hasattr(dt, "date")
                            else str(dt)[:10]
                        )
                        rows.append(
                            (
                                sym,
                                dt_str,
                                d["open"],
                                d["high"],
                                d["low"],
                                d["close"],
                                d["volume"],
                            )
                        )
                    con.executemany(
                        "INSERT OR IGNORE INTO ohlc VALUES (?,?,?,?,?,?,?)", rows
                    )
                    con.commit()
            except Exception as e:
                print(f"    WARN {sym} [{w_start}..{w_end}]: {e}", file=sys.stderr)
            time.sleep(HIST_RATE)

        if i % 100 == 0:
            print(f"    {i}/{len(needs)}...")

    print(f"  Breadth backfill complete: {len(needs)} symbols from {target_from}")


# ── Phase 2: Daily delta via quote() ──────────────────────────────────────────
def delta_update(
    kite, instruments_df: pd.DataFrame, symbols: list[str], con: sqlite3.Connection
) -> None:
    today = date.today().isoformat()
    total = len(symbols)
    print(f"\n  Phase 2 — Delta update via quote(): {total} symbols for {today}...")

    # Build "NSE:SYMBOL" strings; keep mapping back to plain symbol
    ex_syms = [f"NSE:{s}" for s in symbols]

    total_batches = -(-len(ex_syms) // BATCH_SIZE)
    inserted = 0
    for i in range(0, len(ex_syms), BATCH_SIZE):
        batch = ex_syms[i : i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        for attempt in (1, 2):
            try:
                quotes = kite.quote(batch)
                rows = []
                for ex_sym, q in quotes.items():
                    sym = ex_sym.split(":", 1)[1]  # "NSE:SBIN" -> "SBIN"
                    ltp = q.get("last_price", 0)
                    if not ltp:  # market closed / no data
                        continue
                    ohlc = q.get("ohlc", {})
                    rows.append(
                        (
                            sym,
                            today,
                            ohlc.get("open"),
                            ohlc.get("high"),
                            ohlc.get("low"),
                            ltp,  # close = LTP, NOT ohlc.close
                            q.get("volume", 0),
                        )
                    )
                con.executemany(
                    "INSERT OR IGNORE INTO ohlc VALUES (?,?,?,?,?,?,?)", rows
                )
                con.commit()
                inserted += len(rows)
                print(
                    f"    Batch {batch_num}/{total_batches}: {len(rows)} quotes inserted"
                )
                break
            except Exception as e:
                if attempt == 1:
                    print(
                        f"    WARN batch {batch_num} (attempt 1): {e} — retrying in {BATCH_RETRY_WAIT}s...",
                        file=sys.stderr,
                    )
                    time.sleep(BATCH_RETRY_WAIT)
                else:
                    print(
                        f"    WARN batch {batch_num} (attempt 2): {e} — skipping",
                        file=sys.stderr,
                    )
        time.sleep(BATCH_SLEEP)

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

    env = load_env(ENV_PATH)
    kite = get_kite(env)

    con = sqlite3.connect(DB_PATH)
    init_db(con)

    # 1. Instruments
    instruments_df = refresh_instruments(kite, con)
    all_symbols = instruments_df["tradingsymbol"].tolist()
    tokens: dict[str, int] = dict(
        zip(
            instruments_df["tradingsymbol"],
            instruments_df["instrument_token"].astype(int),
        )
    )
    print(f"  Total symbols to track: {len(all_symbols)}")

    # 2. Determine what each symbol needs
    status = get_symbol_status(con)
    today = date.today().isoformat()

    needs_backfill = [
        s for s in all_symbols if s not in status or status[s][1] < MIN_ROWS
    ]
    needs_delta = [
        s
        for s in all_symbols
        if s in status and status[s][1] >= MIN_ROWS and status[s][0] < today
    ]
    up_to_date = len(all_symbols) - len(needs_backfill) - len(needs_delta)

    print("\n  Symbol status:")
    print(f"    Needs backfill : {len(needs_backfill)}")
    print(f"    Needs delta    : {len(needs_delta)}")
    print(f"    Already today  : {up_to_date}")

    if needs_backfill:
        backfill(kite, tokens, needs_backfill, con)

    if needs_delta:
        delta_update(kite, instruments_df, needs_delta, con)

    write_manifest(con)

    # Breadth universe: 10yr extended backfill (runs after main manifest write)
    backfill_breadth(kite, con)

    con.close()

    total_rows = (
        sqlite3.connect(DB_PATH).execute("SELECT COUNT(*) FROM ohlc").fetchone()[0]
    )
    print(f"\nDone. DB: {DB_PATH}  ({total_rows:,} total rows)")


if __name__ == "__main__":
    main()
