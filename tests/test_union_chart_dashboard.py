import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from union_chart_dashboard import parse_union_tiers, load_todays_union

UNION_MD_FRESH = """> disclaimer text
# NSE EMA55 Cross Watchlist -- 2026-08-20
*Generated 2026-08-20 15:47 IST*

### Union Watchlist
**ALL 4: 2** | **1 ONLY: 2**

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,###ALL 4,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,NSE:FOO,NSE:BAR,###1 ONLY,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,NSE:BAZ,NSE:QUX
```

---
### Scan definition
"""

UNION_MD_STALE = UNION_MD_FRESH.replace("2026-08-20", "2026-08-19")


def test_parse_union_tiers_extracts_symbol_to_tier():
    tiers = parse_union_tiers(UNION_MD_FRESH)
    assert tiers == {"FOO": "ALL 4", "BAR": "ALL 4", "BAZ": "1 ONLY", "QUX": "1 ONLY"}


def test_parse_union_tiers_excludes_index_and_commodity_anchors():
    tiers = parse_union_tiers(UNION_MD_FRESH)
    assert "NIFTYSMLCAP250" not in tiers
    assert "NIFTYMIDSML400" not in tiers
    assert "GOLDM1!" not in tiers
    assert not any(k.startswith("MCX") for k in tiers)


def test_parse_union_tiers_no_block_returns_empty():
    assert parse_union_tiers("no fenced block here") == {}


def test_load_todays_union_missing_file(tmp_path):
    tiers, err = load_todays_union(str(tmp_path / "nope.md"), "2026-08-20")
    assert tiers is None
    assert "not found" in err


def test_load_todays_union_stale_date(tmp_path):
    p = tmp_path / "ema55_cross_scans.md"
    p.write_text(UNION_MD_STALE, encoding="utf-8")
    tiers, err = load_todays_union(str(p), "2026-08-20")
    assert tiers is None
    assert "stale" in err


def test_load_todays_union_fresh_returns_tiers(tmp_path):
    p = tmp_path / "ema55_cross_scans.md"
    p.write_text(UNION_MD_FRESH, encoding="utf-8")
    tiers, err = load_todays_union(str(p), "2026-08-20")
    assert err is None
    assert tiers == {"FOO": "ALL 4", "BAR": "ALL 4", "BAZ": "1 ONLY", "QUX": "1 ONLY"}


import pandas as pd
from union_chart_dashboard import build_chart_data


def _fixture_df(n_rows: int) -> pd.DataFrame:
    dates = pd.date_range("2025-01-01", periods=n_rows, freq="D")
    return pd.DataFrame({
        "date": dates,
        "open": [100.0 + i for i in range(n_rows)],
        "high": [101.0 + i for i in range(n_rows)],
        "low": [99.0 + i for i in range(n_rows)],
        "close": [100.5 + i for i in range(n_rows)],
        "volume": [1000 + i for i in range(n_rows)],
    })


def test_build_chart_data_keeps_symbol_with_enough_bars():
    ohlc_map = {"FOO": _fixture_df(200)}
    tiers = {"FOO": "ALL 4"}
    records, skipped = build_chart_data(ohlc_map, tiers, min_bars=130)
    assert skipped == 0
    assert len(records) == 1
    assert records[0]["symbol"] == "FOO"
    assert records[0]["tier"] == "ALL 4"
    assert records[0]["bars"][0] == ["2025-01-01", 100.0, 101.0, 99.0, 100.5, 1000.0]
    assert len(records[0]["bars"]) == 200


def test_build_chart_data_skips_symbol_below_bar_floor():
    ohlc_map = {"FOO": _fixture_df(200), "BAR": _fixture_df(50)}
    tiers = {"FOO": "ALL 4", "BAR": "1 ONLY"}
    records, skipped = build_chart_data(ohlc_map, tiers, min_bars=130)
    assert skipped == 1
    assert [r["symbol"] for r in records] == ["FOO"]


def test_build_chart_data_skips_symbol_missing_from_ohlc_map():
    ohlc_map = {"FOO": _fixture_df(200)}
    tiers = {"FOO": "ALL 4", "MISSING": "1 ONLY"}
    records, skipped = build_chart_data(ohlc_map, tiers, min_bars=130)
    assert skipped == 1
    assert [r["symbol"] for r in records] == ["FOO"]


def test_build_chart_data_sorted_by_symbol():
    ohlc_map = {"ZEBRA": _fixture_df(150), "APEX": _fixture_df(150)}
    tiers = {"ZEBRA": "1 ONLY", "APEX": "ALL 4"}
    records, _ = build_chart_data(ohlc_map, tiers, min_bars=130)
    assert [r["symbol"] for r in records] == ["APEX", "ZEBRA"]


from union_chart_dashboard import build_html


def test_build_html_contains_disclaimer():
    html = build_html([], "2026-08-20")
    assert "SEBI registered" in html


def test_build_html_contains_vendor_script_tag():
    html = build_html([], "2026-08-20")
    assert 'src="vendor/lightweight-charts.js"' in html


def test_build_html_no_records_shows_empty_state():
    html = build_html([], "2026-08-20")
    assert "No signals" in html


def test_build_html_embeds_symbol_data_and_cards():
    records = [{"symbol": "FOO", "tier": "ALL 4", "bars": [["2025-01-01", 1.0, 2.0, 0.5, 1.5, 100.0]]}]
    html = build_html(records, "2026-08-20")
    assert '"FOO"' in html
    assert '"ALL 4"' in html
    assert 'data-symbol="FOO"' in html
    assert 'id="chart-FOO"' in html


def test_build_html_has_interactive_controls():
    html = build_html([], "2026-08-20")
    assert 'id="upColor"' in html
    assert 'id="downColor"' in html
    assert 'id="emaPeriods"' in html
    assert "IntersectionObserver" in html
    assert "computeEMA" in html


import union_chart_dashboard as ucd


def test_main_writes_html_with_expected_symbols(tmp_path, monkeypatch, capsys):
    union_md = tmp_path / "ema55_cross_scans.md"
    union_md.write_text(UNION_MD_FRESH, encoding="utf-8")
    output_path = tmp_path / "dashboard" / "union_charts.html"

    monkeypatch.setattr(ucd, "EMA55_MD", str(union_md))
    monkeypatch.setattr(ucd, "OUTPUT_PATH", str(output_path))
    monkeypatch.setattr(ucd, "TODAY", "2026-08-20")

    def fake_load_ohlc_many(symbols, lookback=250):
        return {sym: _fixture_df(200) for sym in symbols}

    monkeypatch.setattr(ucd, "load_ohlc_many", fake_load_ohlc_many)

    ucd.main()

    assert output_path.exists()
    html = output_path.read_text(encoding="utf-8")
    assert '"FOO"' in html
    assert '"BAR"' in html
    assert "SEBI registered" in html
    out = capsys.readouterr().out
    assert "4 charted" in out


def test_main_skips_write_when_stale(tmp_path, monkeypatch, capsys):
    union_md = tmp_path / "ema55_cross_scans.md"
    union_md.write_text(UNION_MD_STALE, encoding="utf-8")
    output_path = tmp_path / "dashboard" / "union_charts.html"

    monkeypatch.setattr(ucd, "EMA55_MD", str(union_md))
    monkeypatch.setattr(ucd, "OUTPUT_PATH", str(output_path))
    monkeypatch.setattr(ucd, "TODAY", "2026-08-20")

    ucd.main()

    assert not output_path.exists()
    out = capsys.readouterr().out
    assert "stale" in out


EMA55_CROSS_AGE_MD_NO_UNION = """> disclaimer text
# NSE EMA55 Cross Watchlist -- 2026-08-20
*Generated 2026-08-20 15:47 IST*

### Union Watchlist
*No union data available today.*

---
### Scan definition
...

**On watch: 3**

**TradingView watchlist**
```
###1 DAY,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:FOO,###2 DAYS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:BAR
```
"""


def test_parse_union_tiers_ignores_non_tier_labels():
    tiers = parse_union_tiers(EMA55_CROSS_AGE_MD_NO_UNION)
    assert tiers == {}


def test_load_todays_union_no_union_section_reports_no_data(tmp_path):
    p = tmp_path / "ema55_cross_scans.md"
    p.write_text(EMA55_CROSS_AGE_MD_NO_UNION, encoding="utf-8")
    tiers, err = load_todays_union(str(p), "2026-08-20")
    assert tiers is None
    assert "no union watchlist data" in err


def test_main_skips_write_when_all_ohlc_missing(tmp_path, monkeypatch, capsys):
    union_md = tmp_path / "ema55_cross_scans.md"
    union_md.write_text(UNION_MD_FRESH, encoding="utf-8")
    output_path = tmp_path / "dashboard" / "union_charts.html"

    monkeypatch.setattr(ucd, "EMA55_MD", str(union_md))
    monkeypatch.setattr(ucd, "OUTPUT_PATH", str(output_path))
    monkeypatch.setattr(ucd, "TODAY", "2026-08-20")
    monkeypatch.setattr(ucd, "load_ohlc_many", lambda symbols, lookback=250: {})

    ucd.main()

    assert not output_path.exists()
    out = capsys.readouterr().out
    assert "0 charted" in out
    assert "not overwriting" in out


def test_main_does_not_clobber_existing_dashboard_when_ohlc_missing(tmp_path, monkeypatch):
    union_md = tmp_path / "ema55_cross_scans.md"
    union_md.write_text(UNION_MD_FRESH, encoding="utf-8")
    output_path = tmp_path / "dashboard" / "union_charts.html"
    output_path.parent.mkdir(parents=True)
    output_path.write_text("PREVIOUS GOOD DASHBOARD", encoding="utf-8")

    monkeypatch.setattr(ucd, "EMA55_MD", str(union_md))
    monkeypatch.setattr(ucd, "OUTPUT_PATH", str(output_path))
    monkeypatch.setattr(ucd, "TODAY", "2026-08-20")
    monkeypatch.setattr(ucd, "load_ohlc_many", lambda symbols, lookback=250: {})

    ucd.main()

    assert output_path.read_text(encoding="utf-8") == "PREVIOUS GOOD DASHBOARD"
