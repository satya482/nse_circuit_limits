import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from near_52w_high_chart_dashboard import (
    parse_near_52w_buckets,
    load_todays_near_52w,
    split_buckets_by_kind,
)
from near_52w_high_scanner import NEW_LISTING_LABEL

MD_FRESH = """> disclaimer

# NSE Near-52W-High Watchlist - 2026-08-20
*Generated 2026-08-20 16:20 IST*

**On watch: 3**

**TradingView watchlist** *(sectioned by distance from 52w high - paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###AT/NEW HIGH,NSE:FOO,###0-10%,NSE:BAR,###20-30%,NSE:BAZ
```
"""

MD_STALE = MD_FRESH.replace("2026-08-20", "2026-08-19")


def test_parse_near_52w_buckets_skips_index_and_commodity_anchors():
    buckets = parse_near_52w_buckets(MD_FRESH)
    assert buckets == {"FOO": "AT/NEW HIGH", "BAR": "0-10%", "BAZ": "20-30%"}


def test_parse_near_52w_buckets_no_fenced_block_returns_empty():
    assert parse_near_52w_buckets("# nothing here") == {}


def test_parse_near_52w_buckets_recognizes_new_listing_label():
    md = MD_FRESH.replace(
        "###20-30%,NSE:BAZ",
        f"###20-30%,NSE:BAZ,###{NEW_LISTING_LABEL},NSE:FRESHIPO",
    )
    buckets = parse_near_52w_buckets(md)
    assert buckets["FRESHIPO"] == NEW_LISTING_LABEL


def test_split_buckets_by_kind_separates_new_listings():
    buckets = {"FOO": "AT/NEW HIGH", "BAR": "0-10%", "FRESHIPO": NEW_LISTING_LABEL}
    normal, new_listing = split_buckets_by_kind(buckets)
    assert normal == {"FOO": "AT/NEW HIGH", "BAR": "0-10%"}
    assert new_listing == {"FRESHIPO": NEW_LISTING_LABEL}


def test_split_buckets_by_kind_empty_new_listings():
    buckets = {"FOO": "AT/NEW HIGH"}
    normal, new_listing = split_buckets_by_kind(buckets)
    assert normal == {"FOO": "AT/NEW HIGH"}
    assert new_listing == {}


def test_load_todays_near_52w_missing_file(tmp_path):
    buckets, err = load_todays_near_52w(str(tmp_path / "nope.md"), "2026-08-20")
    assert buckets is None
    assert "not found" in err


def test_load_todays_near_52w_stale_date(tmp_path):
    p = tmp_path / "near_52w_high_scans.md"
    p.write_text(MD_STALE, encoding="utf-8")
    buckets, err = load_todays_near_52w(str(p), "2026-08-20")
    assert buckets is None
    assert "stale" in err


def test_load_todays_near_52w_fresh_returns_buckets():
    p_content = MD_FRESH
    import tempfile, os
    fd, path = tempfile.mkstemp(suffix=".md")
    os.close(fd)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(p_content)
    try:
        buckets, err = load_todays_near_52w(path, "2026-08-20")
        assert err is None
        assert buckets == {"FOO": "AT/NEW HIGH", "BAR": "0-10%", "BAZ": "20-30%"}
    finally:
        os.remove(path)


def test_load_todays_near_52w_no_signals_reports_no_data():
    md = MD_FRESH.split("```\n", 1)[0] + "*No signals.*\n"
    import tempfile, os
    fd, path = tempfile.mkstemp(suffix=".md")
    os.close(fd)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(md)
    try:
        buckets, err = load_todays_near_52w(path, "2026-08-20")
        assert buckets is None
        assert "no" in err.lower()
    finally:
        os.remove(path)
