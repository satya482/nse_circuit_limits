import sqlite3
from datetime import date

from fetch_delivery import (
    backfill_delivery_range,
    parse_bhavcopy_csv,
    progress_stats,
    upsert_delivery,
)


_SAMPLE_CSV = """SYMBOL ,SERIES ,DATE1 ,PREV_CLOSE ,OPEN_PRICE ,HIGH_PRICE ,LOW_PRICE ,LAST_PRICE ,CLOSE_PRICE ,AVG_PRICE ,TTL_TRD_QNTY ,TURNOVER_LACS ,NO_OF_TRADES ,DELIV_QTY ,DELIV_PER
RELIANCE ,EQ ,04-JUL-2026 ,1500.00 ,1505.00 ,1520.00 ,1498.00 ,1510.00 ,1510.00 ,1508.50 ,1000000 ,15085.00 ,50000 ,650000 ,65.00
TATASTEEL ,EQ ,04-JUL-2026 ,140.00 ,141.00 ,143.00 ,139.00 ,142.00 ,142.00 ,141.50 ,5000000 ,7075.00 ,80000 ,1500000 ,30.00
IDEA ,BE ,04-JUL-2026 ,10.00 ,10.10 ,10.50 ,9.90 ,10.20 ,10.20 ,10.15 ,20000000 ,2030.00 ,10000 ,4000000 ,20.00
"""


def test_parse_bhavcopy_csv_filters_eq_series_only():
    df = parse_bhavcopy_csv(_SAMPLE_CSV)
    assert set(df["symbol"]) == {"RELIANCE", "TATASTEEL"}


def test_parse_bhavcopy_csv_strips_whitespace_and_parses_numeric():
    df = parse_bhavcopy_csv(_SAMPLE_CSV)
    row = df[df["symbol"] == "RELIANCE"].iloc[0]
    assert row["deliv_pct"] == 65.0
    assert row["ttl_trd_qty"] == 1000000
    assert row["deliv_qty"] == 650000


def test_upsert_delivery_writes_and_replaces(tmp_path):
    db_path = tmp_path / "test_market.db"
    df = parse_bhavcopy_csv(_SAMPLE_CSV)
    d = date(2026, 7, 4)

    n = upsert_delivery(df, d, db_path=db_path)
    assert n == 2

    con = sqlite3.connect(db_path)
    row = con.execute(
        "SELECT deliv_pct FROM delivery WHERE symbol=? AND date=?",
        ("RELIANCE", "2026-07-04"),
    ).fetchone()
    con.close()
    assert row == (65.0,)

    n2 = upsert_delivery(df, d, db_path=db_path)
    assert n2 == 2
    con = sqlite3.connect(db_path)
    count = con.execute("SELECT COUNT(*) FROM delivery").fetchone()[0]
    con.close()
    assert count == 2


def test_parse_bhavcopy_csv_drops_rows_with_missing_numeric_delivery_fields():
    """Verify that rows with non-numeric delivery% or delivery qty (NSE emits '-')
    are silently dropped, and other clean rows survive."""
    # Sample with one clean row (RELIANCE), one with missing DELIV_PER (HDFCBANK),
    # one with missing DELIV_QTY (INFY), and one with missing TTL_TRD_QNTY (BAJAJ)
    sample_csv = """SYMBOL ,SERIES ,DATE1 ,PREV_CLOSE ,OPEN_PRICE ,HIGH_PRICE ,LOW_PRICE ,LAST_PRICE ,CLOSE_PRICE ,AVG_PRICE ,TTL_TRD_QNTY ,TURNOVER_LACS ,NO_OF_TRADES ,DELIV_QTY ,DELIV_PER
RELIANCE ,EQ ,04-JUL-2026 ,1500.00 ,1505.00 ,1520.00 ,1498.00 ,1510.00 ,1510.00 ,1508.50 ,1000000 ,15085.00 ,50000 ,650000 ,65.00
HDFCBANK ,EQ ,04-JUL-2026 ,1800.00 ,1810.00 ,1820.00 ,1790.00 ,1815.00 ,1815.00 ,1808.00 ,2000000 ,36360.00 ,60000 ,1500000 ,-
INFY ,EQ ,04-JUL-2026 ,1200.00 ,1210.00 ,1220.00 ,1190.00 ,1215.00 ,1215.00 ,1208.00 ,500000 ,6075.00 ,30000 ,- ,25.00
BAJAJ ,EQ ,04-JUL-2026 ,3500.00 ,3510.00 ,3530.00 ,3480.00 ,3520.00 ,3520.00 ,3515.00 ,- ,12100.00 ,40000 ,2000000 ,55.00
"""
    df = parse_bhavcopy_csv(sample_csv)
    # Only RELIANCE should remain; others have missing numeric fields
    assert len(df) == 1
    assert df["symbol"].iloc[0] == "RELIANCE"
    assert df["deliv_pct"].iloc[0] == 65.0
    assert df["ttl_trd_qty"].iloc[0] == 1000000
    assert df["deliv_qty"].iloc[0] == 650000


def test_parse_and_upsert_with_missing_delivery_fields_full_pipeline(tmp_path):
    """Verify full pipeline (parse → upsert) doesn't raise when batch includes
    rows with missing delivery fields; only clean rows are written to DB."""
    sample_csv = """SYMBOL ,SERIES ,DATE1 ,PREV_CLOSE ,OPEN_PRICE ,HIGH_PRICE ,LOW_PRICE ,LAST_PRICE ,CLOSE_PRICE ,AVG_PRICE ,TTL_TRD_QNTY ,TURNOVER_LACS ,NO_OF_TRADES ,DELIV_QTY ,DELIV_PER
RELIANCE ,EQ ,04-JUL-2026 ,1500.00 ,1505.00 ,1520.00 ,1498.00 ,1510.00 ,1510.00 ,1508.50 ,1000000 ,15085.00 ,50000 ,650000 ,65.00
HDFCBANK ,EQ ,04-JUL-2026 ,1800.00 ,1810.00 ,1820.00 ,1790.00 ,1815.00 ,1815.00 ,1808.00 ,2000000 ,36360.00 ,60000 ,1500000 ,-
TATASTEEL ,EQ ,04-JUL-2026 ,140.00 ,141.00 ,143.00 ,139.00 ,142.00 ,142.00 ,141.50 ,5000000 ,7075.00 ,80000 ,1500000 ,30.00
"""
    db_path = tmp_path / "test_market.db"
    d = date(2026, 7, 4)

    df = parse_bhavcopy_csv(sample_csv)
    # Should have only 2 clean rows (RELIANCE, TATASTEEL); HDFCBANK dropped
    assert len(df) == 2
    assert set(df["symbol"]) == {"RELIANCE", "TATASTEEL"}

    # Upsert should not raise and should write the 2 clean rows
    n = upsert_delivery(df, d, db_path=db_path)
    assert n == 2

    # Verify DB has exactly 2 rows
    con = sqlite3.connect(db_path)
    count = con.execute("SELECT COUNT(*) FROM delivery").fetchone()[0]
    con.close()
    assert count == 2


def test_backfill_delivery_range_records_done_and_failed_dates(tmp_path):
    db_path = tmp_path / "test_market.db"

    def fetcher(d):
        if d == date(2026, 7, 6):
            return _SAMPLE_CSV
        raise RuntimeError("missing file")

    stats = backfill_delivery_range(
        date(2026, 7, 6),
        date(2026, 7, 7),
        db_path=db_path,
        fetcher=fetcher,
        emit=lambda _: None,
    )

    assert stats["total_dates"] == 2
    assert stats["done_dates"] == 1
    assert stats["failed_dates"] == 1
    assert stats["pending_dates"] == 0
    assert stats["rows_done"] == 2

    con = sqlite3.connect(db_path)
    rows = con.execute(
        "SELECT date, status, rows FROM delivery_backfill_progress ORDER BY date"
    ).fetchall()
    con.close()
    assert rows == [("2026-07-06", "done", 2), ("2026-07-07", "failed", 0)]


def test_backfill_delivery_range_skips_existing_done_date_on_resume(tmp_path):
    db_path = tmp_path / "test_market.db"
    calls = []

    def fetcher(d):
        calls.append(d)
        return _SAMPLE_CSV

    backfill_delivery_range(
        date(2026, 7, 6),
        date(2026, 7, 6),
        db_path=db_path,
        fetcher=fetcher,
        emit=lambda _: None,
    )
    stats = backfill_delivery_range(
        date(2026, 7, 6),
        date(2026, 7, 6),
        db_path=db_path,
        fetcher=fetcher,
        emit=lambda _: None,
    )

    assert calls == [date(2026, 7, 6)]
    assert stats["skipped_dates"] == 1
    assert stats["done_dates"] == 1
    assert stats["pending_dates"] == 0


def test_progress_stats_counts_existing_delivery_rows_without_progress_table(tmp_path):
    db_path = tmp_path / "test_market.db"
    upsert_delivery(parse_bhavcopy_csv(_SAMPLE_CSV), date(2026, 7, 6), db_path=db_path)

    stats = progress_stats(date(2026, 7, 6), date(2026, 7, 7), db_path=db_path)

    assert stats["total_dates"] == 2
    assert stats["done_dates"] == 1
    assert stats["pending_dates"] == 1
    assert stats["rows_done"] == 2
