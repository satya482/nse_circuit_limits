import json
import inspect
import sys
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from union_chart_dashboard import (
    compute_coil_boxes,
    compute_pocket_pivot_flags,
    compute_signal_kinds,
    compute_wavetrend_kinds,
    fetch_tradingview_industries,
    load_todays_union,
    parse_union_tiers,
    resolve_industries,
)
from wavetrend_scanner import WaveTrendCalculator


def test_resolve_industries_merges_live_values_and_writes_cache(tmp_path):
    cache = tmp_path / "industries.json"
    cache.write_text(
        json.dumps({"as_of": "2026-08-25", "industries": {"OLD": "Banks"}}),
        encoding="utf-8",
    )
    result = resolve_industries(
        {"OLD", "NEW", "MISS"},
        str(cache),
        "2026-08-26",
        fetcher=lambda symbols: {"NEW": "Software"},
    )
    assert result == {"OLD": "Banks", "NEW": "Software", "MISS": "Unclassified"}
    saved = json.loads(cache.read_text(encoding="utf-8"))
    assert saved["as_of"] == "2026-08-26"
    assert saved["industries"] == {"NEW": "Software", "OLD": "Banks"}
    assert not (tmp_path / "industries.json.tmp").exists()


def test_resolve_industries_uses_cache_when_live_fetch_fails(tmp_path):
    cache = tmp_path / "industries.json"
    cache.write_text(
        json.dumps({"as_of": "2026-08-25", "industries": {"AAA": "Steel"}}),
        encoding="utf-8",
    )

    def fail(_symbols):
        raise RuntimeError("TradingView unavailable")

    assert resolve_industries({"AAA", "BBB"}, str(cache), "2026-08-26", fail) == {
        "AAA": "Steel",
        "BBB": "Unclassified",
    }


def test_resolve_industries_preserves_cache_after_empty_live_fetch(tmp_path):
    cache = tmp_path / "industries.json"
    original = json.dumps(
        {"as_of": "2026-08-25", "industries": {"AAA": "Steel"}}
    )
    cache.write_text(original, encoding="utf-8")
    result = resolve_industries(
        {"AAA", "BBB"},
        str(cache),
        "2026-08-26",
        fetcher=lambda symbols: {},
    )
    assert result == {"AAA": "Steel", "BBB": "Unclassified"}
    assert cache.read_text(encoding="utf-8") == original
    assert not (tmp_path / "industries.json.tmp").exists()


def test_resolve_industries_does_not_create_cache_for_unusable_live_mapping(tmp_path):
    cache = tmp_path / "industries.json"
    result = resolve_industries(
        {"AAA"},
        str(cache),
        "2026-08-26",
        fetcher=lambda symbols: {"AAA": pd.NA},
    )
    assert result == {"AAA": "Unclassified"}
    assert not cache.exists()


def test_fetch_tradingview_industries_rejects_nan_and_na_before_string_conversion(
    monkeypatch,
):
    class FakeColumn:
        def __eq__(self, _other):
            return self

        def has(self, _values):
            return self

    class FakeQuery:
        def set_markets(self, *_args):
            return self

        def select(self, *_args):
            return self

        def where(self, *_args):
            return self

        def limit(self, *_args):
            return self

        def get_scanner_data(self):
            return 4, pd.DataFrame(
                [
                    {"name": "GOOD", "industry": "Software"},
                    {"name": float("nan"), "industry": "Banks"},
                    {"name": "BAD_NAN", "industry": float("nan")},
                    {"name": "BAD_NA", "industry": pd.NA},
                ]
            )

    monkeypatch.setitem(
        sys.modules,
        "tradingview_screener",
        SimpleNamespace(Query=FakeQuery, col=lambda _name: FakeColumn()),
    )
    symbols = {"GOOD", "nan", "<NA>", "BAD_NAN", "BAD_NA"}
    assert fetch_tradingview_industries(symbols) == {"GOOD": "Software"}


def test_resolve_industries_handles_malformed_cache_shapes(tmp_path):
    for payload in ("not json", [], None, {"industries": None}, {"industries": {"AAA": None}}):
        cache = tmp_path / "industries.json"
        if isinstance(payload, str):
            cache.write_text(payload, encoding="utf-8")
        else:
            cache.write_text(json.dumps(payload), encoding="utf-8")
        result = resolve_industries(
            {"AAA", "BBB"},
            str(cache),
            "2026-08-26",
            fetcher=lambda symbols: {},
        )
        assert result == {"AAA": "Unclassified", "BBB": "Unclassified"}

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


def test_build_chart_data_enriches_record_with_metadata_and_annotations(monkeypatch):
    ohlc_map = {"FOO": _fixture_df(200)}
    monkeypatch.setattr(
        "union_chart_dashboard.compute_signal_kinds",
        lambda df: [None] * 199 + ["ppv"],
    )
    monkeypatch.setattr(
        "union_chart_dashboard.compute_coil_boxes",
        lambda df: [{"start_index": 180, "end_index": 197, "high": 300.0, "low": 290.0}],
    )
    records, skipped = build_chart_data(
        ohlc_map,
        {"FOO": "ALL 4"},
        industries={"FOO": "Software"},
        min_bars=130,
    )
    record = records[0]
    assert skipped == 0
    assert record["industry"] == "Software"
    assert record["day_change"] == pytest.approx((299.5 / 298.5 - 1) * 100)
    assert record["signals"][-1] == "ppv"
    assert record["coil_boxes"][0]["end_index"] == 197


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
    records = [{
        "symbol": "FOO", "tier": "ALL 4", "industry": "Software",
        "day_change": 1.0,
        "bars": [["2025-01-01", 1.0, 2.0, 0.5, 1.5, 100.0]],
        "signals": [None], "coil_boxes": [],
    }]
    html = build_html(records, "2026-08-20")
    assert '"FOO"' in html
    assert '"ALL 4"' in html
    assert 'data-symbol="FOO"' in html
    assert 'id="chart-FOO"' in html


def test_build_html_escapes_script_context_json_and_preserves_data():
    hostile = "</script><script>alert(1)</script>&"
    records = [{
        "symbol": hostile, "tier": "1 ONLY", "industry": "Software",
        "day_change": 0.0,
        "bars": [["2026-08-25", 1, 2, 0.5, 1.5, 100]],
        "signals": [None], "coil_boxes": [],
    }]
    html = build_html(records, "2026-08-26")
    assert hostile not in html
    assert r"\u003c/script\u003e\u003cscript\u003ealert(1)" in html
    assert r"\u0026" in html
    payload = html.split("const CHART_DATA = ", 1)[1].split(
        ";\nconst chartsBySymbol", 1
    )[0]
    assert json.loads(payload)[0]["symbol"] == hostile


def test_build_html_renders_day_change_and_sort_metadata():
    records = [{
        "symbol": "FOO", "tier": "ALL 5", "industry": "Software",
        "day_change": 2.3456,
        "bars": [["2026-08-25", 1, 2, 0.5, 1.5, 100]],
        "signals": [None], "coil_boxes": [],
    }]
    html = build_html(records, "2026-08-26")
    assert 'data-industry="Software"' in html
    assert 'data-day-change="2.3456"' in html
    assert "+2.35%" in html
    assert 'id="sortMode"' in html
    assert '<option value="industry" selected>' in html
    assert '<option value="day-desc">' in html
    assert '<option value="day-asc">' in html


def test_build_html_has_fixed_mode_and_adaptive_touch_contract():
    html = build_html([], "2026-08-26")
    assert "repeat(auto-fit,minmax(min(100%,320px),1fr))" in html.replace(" ", "")
    assert "vertTouchDrag: false" in html
    assert "setVisibleLogicalRange" in html
    assert "setUTCMonth" not in html
    assert "Unclassified" in html


def test_fixed_range_clamps_month_end_six_calendar_months():
    html = build_html([], "2026-08-26")
    assert "function sixMonthCutoff(last)" in html
    assert "Math.min(sourceDay, lastDay)" in html
    assert "sixMonthCutoff(last)" in html

    def reference(last):
        year, month, day = map(int, last.split("-"))
        target = year * 12 + month - 1 - 6
        target_year, target_month_zero = divmod(target, 12)
        next_month = target_year * 12 + target_month_zero + 1
        next_year, next_month_zero = divmod(next_month, 12)
        from datetime import date, timedelta
        last_day = (date(next_year, next_month_zero + 1, 1) - timedelta(days=1)).day
        return date(target_year, target_month_zero + 1, min(day, last_day)).isoformat()

    assert reference("2025-08-31") == "2025-02-28"
    assert reference("2024-08-31") == "2024-02-29"
    assert reference("2026-03-31") == "2025-09-30"


def test_build_html_has_interactive_controls():
    html = build_html([], "2026-08-20")
    assert 'id="upColor"' in html
    assert 'id="downColor"' in html
    assert 'id="emaPeriods"' in html
    assert "IntersectionObserver" in html
    assert "computeEMA" in html


def test_build_html_has_layer_switches_and_fixed_signal_colors():
    html = build_html([], "2026-08-26")
    assert 'id="emaVisible"' in html
    assert 'id="volumeVisible"' in html
    assert 'id="chartMode"' in html
    assert "volumeVisible: false" in html
    assert "interactive: false" in html
    assert 'ppv: "#2962ff"' in html
    assert 'wt_bull: "#ffffff"' in html
    assert 'wt_bear: "#fdd835"' in html
    assert "lastValueVisible: false" in html
    assert "priceLineVisible: false" in html


def test_build_html_separates_volume_and_price_scales():
    html = build_html([], "2026-08-26")
    assert "bottom: 0.05" in html
    assert "bottom: 0.25" in html
    assert "top: 0.78" in html


def test_build_html_ema_visibility_redraws_coils_after_rebuild():
    html = build_html([], "2026-08-26")
    ema_handler = html.split(
        "document.getElementById('emaVisible').addEventListener('change', function(e) {",
        1,
    )[1].split("document.getElementById('volumeVisible')", 1)[0]
    assert "rebuildEmas(entry);\n    redrawCoils(entry);" in ema_handler


def test_build_html_defers_coil_redraw_until_after_chrome_layout():
    html = build_html([], "2026-08-27")
    scheduler = html.split("function scheduleCoilRedraw(entry) {", 1)[1].split(
        "function buildChart(symbol)", 1
    )[0]
    assert scheduler.count("requestAnimationFrame") >= 2
    assert (
        "subscribeVisibleLogicalRangeChange(function() { scheduleCoilRedraw(entry); })"
        in html
    )
    resize_handler = html.split("new ResizeObserver(function() {", 1)[1].split(
        "}).observe(el);", 1
    )[0]
    assert "scheduleCoilRedraw(entry);" in resize_handler


def test_build_html_places_coil_overlay_above_chrome_chart_canvas():
    compact = "".join(build_html([], "2026-08-27").split())
    assert (
        ".coil-layer{position:absolute;inset:0;z-index:2;pointer-events:none}"
        in compact
    )


def test_build_html_disables_price_axis_drag_and_resizes_both_dimensions():
    html = build_html([], "2026-08-26")
    assert "axisPressedMouseMove: false" in html
    resize_handler = html.split("new ResizeObserver(function() {", 1)[1].split(
        "}).observe(el);", 1
    )[0]
    assert "width: el.clientWidth" in resize_handler
    assert "height: el.clientHeight" in resize_handler
    assert resize_handler.index("chart.applyOptions") < resize_handler.index(
        "scheduleCoilRedraw(entry)"
    )


import union_chart_dashboard as ucd


def test_main_writes_html_with_expected_symbols(tmp_path, monkeypatch, capsys):
    union_md = tmp_path / "ema55_cross_scans.md"
    union_md.write_text(UNION_MD_FRESH, encoding="utf-8")
    output_path = tmp_path / "dashboard" / "union_charts.html"

    monkeypatch.setattr(ucd, "EMA55_MD", str(union_md))
    monkeypatch.setattr(ucd, "OUTPUT_PATH", str(output_path))
    monkeypatch.setattr(ucd, "TODAY", "2026-08-20")
    monkeypatch.setattr(
        ucd,
        "resolve_industries",
        lambda symbols, cache_path, as_of: {sym: "Test Industry" for sym in symbols},
    )

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


def test_main_opens_temp_html_with_explicit_lf_newlines():
    assert 'newline="\\n"' in inspect.getsource(ucd.main)


def test_union_dashboard_runner_checks_python_exit_before_git_add():
    runner = (Path(__file__).parent.parent / "run_union_chart_dashboard.ps1").read_text(
        encoding="utf-8"
    )
    pipeline = runner.index("ForEach-Object", runner.index("union_chart_dashboard.py"))
    capture = runner.index("$pythonExit = $LASTEXITCODE", pipeline)
    check = runner.index("if ($pythonExit -ne 0)", capture)
    exit_native = runner.index("exit $pythonExit", check)
    git_add = runner.index(" add dashboard/union_charts.html")
    assert pipeline < capture < check < exit_native < git_add
    assert "try {" not in runner[runner.index("union_chart_dashboard.py"):git_add]


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
    monkeypatch.setattr(
        ucd,
        "resolve_industries",
        lambda symbols, cache_path, as_of: {sym: "Test Industry" for sym in symbols},
    )
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
    monkeypatch.setattr(
        ucd,
        "resolve_industries",
        lambda symbols, cache_path, as_of: {sym: "Test Industry" for sym in symbols},
    )
    monkeypatch.setattr(ucd, "load_ohlc_many", lambda symbols, lookback=250: {})

    ucd.main()

    assert output_path.read_text(encoding="utf-8") == "PREVIOUS GOOD DASHBOARD"


def _ohlcv(closes, volumes, highs=None, lows=None):
    n = len(closes)
    highs = highs or [c + 1.0 for c in closes]
    lows = lows or [c - 1.0 for c in closes]
    return pd.DataFrame({
        "date": pd.date_range("2026-01-01", periods=n, freq="D"),
        "open": closes,
        "high": highs,
        "low": lows,
        "close": closes,
        "volume": volumes,
    })


def test_pocket_pivot_uses_most_recent_ten_down_days_not_ten_bars():
    closes = [100.0]
    volumes = [100.0]
    for i in range(1, 22):
        closes.append(closes[-1] - 1 if i % 2 else closes[-1] + 2)
        volumes.append(100.0 + i)
    closes.append(closes[-1] + 1)
    volumes.append(1000.0)
    flags = compute_pocket_pivot_flags(_ohlcv(closes, volumes))
    assert flags[-1] is True


def test_pocket_pivot_requires_ten_prior_down_days_and_strictly_higher_volume():
    few = _ohlcv([10, 9, 10, 9, 10, 11], [1, 10, 1, 20, 1, 100])
    assert compute_pocket_pivot_flags(few)[-1] is False

    closes = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 11]
    volumes = [1, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100]
    assert compute_pocket_pivot_flags(_ohlcv(closes, volumes))[-1] is False


def test_wavetrend_kinds_match_existing_calculator_for_all_bars():
    closes = [100 + ((i % 14) - 7) * 2 + i * 0.05 for i in range(100)]
    df = _ohlcv(closes, [1000.0] * len(closes))
    expected = WaveTrendCalculator().calc_from_series(
        (df["high"] + df["low"] + df["close"]) / 3
    )["cross_type"].map({
        "BULL_CROSS": "wt_bull",
        "BEAR_CROSS": "wt_bear",
        "NONE": None,
    }).tolist()
    assert compute_wavetrend_kinds(df) == expected


def test_wavetrend_flat_startup_matches_zero_deviation_pine_golden():
    result = WaveTrendCalculator(n1=2, n2=2).calc_from_series(
        pd.Series([100.0] * 8)
    )
    assert result["wt1"].tolist() == [0.0] * 8
    assert result["wt2"].iloc[:3].isna().all()
    assert result["wt2"].iloc[3:].tolist() == [0.0] * 5
    assert result["cross_type"].tolist() == ["NONE"] * 8


def test_wavetrend_kind_overrides_pocket_pivot(monkeypatch):
    df = _ohlcv([10, 11, 12], [10, 20, 30])
    monkeypatch.setattr(
        "union_chart_dashboard.compute_pocket_pivot_flags",
        lambda frame: [False, False, True],
    )
    monkeypatch.setattr(
        "union_chart_dashboard.compute_wavetrend_kinds",
        lambda frame: [None, None, "wt_bull"],
    )
    assert compute_signal_kinds(df) == [None, None, "wt_bull"]


def test_coil_box_uses_mother_range_and_fifteen_bars_after_confirmation():
    df = _ohlcv(
        [10, 10, 10],
        [100, 100, 100],
        highs=[12, 11, 11.5],
        lows=[8, 9, 8.5],
    )
    assert compute_coil_boxes(df) == [
        {"start_index": 0, "end_index": 17, "high": 12.0, "low": 8.0}
    ]


def test_new_overlapping_coil_replaces_previous_box():
    df = _ohlcv(
        [10, 10, 10, 10],
        [100] * 4,
        highs=[12, 11.5, 11, 10.5],
        lows=[8, 8.5, 9, 9.5],
    )
    assert compute_coil_boxes(df) == [
        {"start_index": 1, "end_index": 18, "high": 11.5, "low": 8.5}
    ]
