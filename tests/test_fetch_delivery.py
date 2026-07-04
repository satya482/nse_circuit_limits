import sqlite3
from datetime import date

from fetch_delivery import parse_bhavcopy_csv, upsert_delivery


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
