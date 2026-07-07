#!/usr/bin/env python3
"""Fetch NSE full bhavcopy delivery% (DELIV_PER) for EQ-series stocks.
Upserts into market.db `delivery` table. Run ~6:15 PM IST via
run_fetch_delivery.ps1, after NSE publishes the day's bhavcopy."""

import sqlite3
import sys
from argparse import ArgumentParser
from datetime import date, datetime, timedelta
from io import StringIO
from pathlib import Path
from typing import Callable

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
        con.execute("CREATE INDEX IF NOT EXISTS idx_delivery_date ON delivery(date)")
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


def ensure_progress_table(con: sqlite3.Connection) -> None:
    con.execute(
        "CREATE TABLE IF NOT EXISTS delivery_backfill_progress ("
        "date TEXT PRIMARY KEY, "
        "status TEXT NOT NULL, "
        "rows INTEGER NOT NULL DEFAULT 0, "
        "error TEXT, "
        "updated_at TEXT NOT NULL)"
    )
    con.commit()


def record_progress(
    d: date,
    status: str,
    rows: int,
    error: str | None = None,
    db_path: Path = DB_PATH,
) -> None:
    con = sqlite3.connect(db_path)
    try:
        ensure_progress_table(con)
        con.execute(
            "INSERT OR REPLACE INTO delivery_backfill_progress "
            "(date, status, rows, error, updated_at) VALUES (?, ?, ?, ?, ?)",
            (d.isoformat(), status, int(rows), error, datetime.now().isoformat(timespec="seconds")),
        )
        con.commit()
    finally:
        con.close()


def existing_delivery_rows(d: date, db_path: Path = DB_PATH) -> int:
    con = sqlite3.connect(db_path)
    try:
        row = con.execute(
            "SELECT COUNT(*) FROM delivery WHERE date=?",
            (d.isoformat(),),
        ).fetchone()
        return int(row[0]) if row else 0
    except sqlite3.Error:
        return 0
    finally:
        con.close()


def completed_progress_dates(db_path: Path = DB_PATH) -> dict[str, int]:
    con = sqlite3.connect(db_path)
    try:
        ensure_progress_table(con)
        rows = con.execute(
            "SELECT date, rows FROM delivery_backfill_progress WHERE status='done'"
        ).fetchall()
        return {d: int(n) for d, n in rows}
    finally:
        con.close()


def trading_dates(start: date, end: date) -> list[date]:
    if end < start:
        raise ValueError("--to must be on or after --from")
    days = []
    d = start
    while d <= end:
        if d.weekday() < 5:
            days.append(d)
        d += timedelta(days=1)
    return days


def progress_stats(start: date, end: date, db_path: Path = DB_PATH) -> dict[str, int]:
    dates = trading_dates(start, end)
    done = 0
    failed = 0
    rows_done = 0

    con = sqlite3.connect(db_path)
    try:
        has_progress = con.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='delivery_backfill_progress'"
        ).fetchone()
        progress = {}
        if has_progress:
            progress = {
                d: (status, int(rows))
                for d, status, rows in con.execute(
                    "SELECT date, status, rows FROM delivery_backfill_progress"
                ).fetchall()
            }

        for d in dates:
            iso = d.isoformat()
            if iso in progress:
                status, rows = progress[iso]
                if status == "done":
                    done += 1
                    rows_done += rows
                elif status == "failed":
                    failed += 1
                continue
            try:
                row_count = con.execute(
                    "SELECT COUNT(*) FROM delivery WHERE date=?",
                    (iso,),
                ).fetchone()[0]
            except sqlite3.Error:
                row_count = 0
            if row_count:
                done += 1
                rows_done += int(row_count)

        pending = max(0, len(dates) - done - failed)
        return {
            "total_dates": len(dates),
            "done_dates": done,
            "failed_dates": failed,
            "pending_dates": pending,
            "rows_done": rows_done,
            "skipped_dates": 0,
        }
    finally:
        con.close()


def backfill_delivery_range(
    start: date,
    end: date,
    db_path: Path = DB_PATH,
    force: bool = False,
    fetcher: Callable[[date], str] = fetch_bhavcopy_csv,
    emit: Callable[[str], None] = print,
) -> dict[str, int]:
    dates = trading_dates(start, end)
    done_progress = completed_progress_dates(db_path)
    skipped = 0

    for d in dates:
        iso = d.isoformat()
        existing_rows = existing_delivery_rows(d, db_path)
        if not force and (iso in done_progress or existing_rows > 0):
            rows = done_progress.get(iso, existing_rows)
            record_progress(d, "done", rows, db_path=db_path)
            skipped += 1
            stats = progress_stats(start, end, db_path)
            emit(_format_progress_line("skip", d, rows, stats | {"skipped_dates": skipped}))
            continue

        try:
            csv_text = fetcher(d)
            rows = parse_bhavcopy_csv(csv_text)
            count = upsert_delivery(rows, d, db_path=db_path)
            record_progress(d, "done", count, db_path=db_path)
            stats = progress_stats(start, end, db_path)
            emit(_format_progress_line("done", d, count, stats | {"skipped_dates": skipped}))
        except Exception as e:
            record_progress(d, "failed", 0, str(e)[:500], db_path=db_path)
            stats = progress_stats(start, end, db_path)
            emit(_format_progress_line("failed", d, 0, stats | {"skipped_dates": skipped}))

    stats = progress_stats(start, end, db_path)
    stats["skipped_dates"] = skipped
    emit(
        "summary: "
        f"done={stats['done_dates']}/{stats['total_dates']} "
        f"pending={stats['pending_dates']} failed={stats['failed_dates']} "
        f"skipped={stats['skipped_dates']} rows={stats['rows_done']}"
    )
    return stats


def _format_progress_line(action: str, d: date, rows: int, stats: dict[str, int]) -> str:
    return (
        f"{action}: {d.isoformat()} rows={rows} "
        f"done={stats['done_dates']}/{stats['total_dates']} "
        f"pending={stats['pending_dates']} failed={stats['failed_dates']} "
        f"rows_done={stats['rows_done']}"
    )


def _parse_date(raw: str) -> date:
    return date.fromisoformat(raw)


def _parser() -> ArgumentParser:
    parser = ArgumentParser(description="Fetch NSE full bhavcopy delivery percentage.")
    parser.add_argument("--date", type=_parse_date, help="Fetch one date, YYYY-MM-DD.")
    parser.add_argument("--from", dest="start", type=_parse_date, help="Backfill start date, YYYY-MM-DD.")
    parser.add_argument("--to", dest="end", type=_parse_date, help="Backfill end date, YYYY-MM-DD.")
    parser.add_argument("--force", action="store_true", help="Refetch dates already marked done.")
    parser.add_argument("--stats", action="store_true", help="Print backfill stats for the requested range.")
    return parser


def main() -> None:
    args = _parser().parse_args()
    if args.start or args.end:
        if not args.start or not args.end:
            print("fetch_delivery: --from and --to must be passed together", file=sys.stderr)
            sys.exit(2)
        if args.stats:
            stats = progress_stats(args.start, args.end)
            print(
                "summary: "
                f"done={stats['done_dates']}/{stats['total_dates']} "
                f"pending={stats['pending_dates']} failed={stats['failed_dates']} "
                f"rows={stats['rows_done']}"
            )
            return
        backfill_delivery_range(args.start, args.end, force=args.force)
        return

    d = args.date or date.today()
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
