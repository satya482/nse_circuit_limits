import json
import inspect
import shutil
import subprocess
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


from union_chart_dashboard import build_chart_data, compute_rs_transition_kinds, compute_rs_pane_series


def _rs_pane_test_dfs():
    """2 full business weeks (Mon-Fri): week1 close=10 flat, week2 close=20
    flat, bench=100 flat throughout -- so rsLine steps cleanly 100 -> 200 at
    the week boundary, making the weekly-EMA broadcast easy to hand-verify."""
    dates = pd.bdate_range("2025-01-06", periods=10)
    closes = [10.0] * 5 + [20.0] * 5
    df = pd.DataFrame({
        "date": dates,
        "open": closes, "high": closes, "low": closes, "close": closes,
        "volume": [1000.0] * len(closes),
    })
    bench_df = pd.DataFrame({"date": dates, "close": [100.0] * len(closes)})
    return df, bench_df


def _rs_test_dfs():
    """12 flat bars (rsLine==rsEma9 exactly, no signal), then a big jump up
    (crossover), held flat (no re-fire), then a crash down (crossunder)."""
    closes = [100.0] * 12 + [300.0] * 5 + [50.0]
    dates = pd.date_range("2025-01-01", periods=len(closes), freq="D")
    df = pd.DataFrame({
        "date": dates,
        "open": closes, "high": closes, "low": closes, "close": closes,
        "volume": [1000.0] * len(closes),
    })
    bench_df = pd.DataFrame({
        "date": dates,
        "close": [100.0] * len(closes),
    })
    return df, bench_df


def test_compute_rs_transition_kinds_flags_crossover_and_crossunder():
    df, bench_df = _rs_test_dfs()
    kinds = compute_rs_transition_kinds(df, bench_df)
    assert len(kinds) == len(df)
    assert kinds[:12] == [None] * 12
    assert kinds[12] == "rs_weak_to_strong"
    assert kinds[13:17] == [None] * 4
    assert kinds[17] == "rs_strong_to_weak"


def test_compute_rs_transition_kinds_none_bench_returns_all_none():
    df, _ = _rs_test_dfs()
    kinds = compute_rs_transition_kinds(df, None)
    assert kinds == [None] * len(df)


def test_compute_rs_transition_kinds_short_bench_returns_all_none():
    df, bench_df = _rs_test_dfs()
    kinds = compute_rs_transition_kinds(df, bench_df.iloc[:3])
    assert kinds == [None] * len(df)


def test_compute_rs_pane_series_returns_four_parallel_arrays():
    df, bench_df = _rs_pane_test_dfs()
    pane = compute_rs_pane_series(df, bench_df)
    assert set(pane.keys()) == {"rs_line", "rs_ema9", "rs_ema21", "rs_weekly_ema9"}
    for key in pane:
        assert len(pane[key]) == len(df)


def test_compute_rs_pane_series_rs_line_matches_close_over_bench():
    df, bench_df = _rs_pane_test_dfs()
    pane = compute_rs_pane_series(df, bench_df)
    assert pane["rs_line"][:5] == pytest.approx([100.0] * 5)
    assert pane["rs_line"][5:] == pytest.approx([200.0] * 5)


def test_compute_rs_pane_series_ema9_seeds_at_first_value():
    df, bench_df = _rs_pane_test_dfs()
    pane = compute_rs_pane_series(df, bench_df)
    assert pane["rs_ema9"][0] == pytest.approx(100.0)
    assert pane["rs_ema9"][5] == pytest.approx(120.0)  # 0.2*200 + 0.8*100


def test_compute_rs_pane_series_ema21_seeds_at_first_value():
    df, bench_df = _rs_pane_test_dfs()
    pane = compute_rs_pane_series(df, bench_df)
    assert pane["rs_ema21"][0] == pytest.approx(100.0)


def test_compute_rs_pane_series_weekly_ema9_is_flat_within_each_week_and_steps_at_boundary():
    df, bench_df = _rs_pane_test_dfs()
    pane = compute_rs_pane_series(df, bench_df)
    week1 = pane["rs_weekly_ema9"][:5]
    week2 = pane["rs_weekly_ema9"][5:]
    assert week1 == pytest.approx([100.0] * 5)  # first week seeds the weekly EMA
    assert week2 == pytest.approx([120.0] * 5)  # 0.2*200 + 0.8*100, flat all of week 2


def test_compute_rs_pane_series_none_bench_returns_none():
    df, _ = _rs_pane_test_dfs()
    assert compute_rs_pane_series(df, None) is None


def test_compute_rs_pane_series_short_bench_returns_none():
    df, bench_df = _rs_pane_test_dfs()
    assert compute_rs_pane_series(df, bench_df.iloc[:3]) is None


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


def test_build_chart_data_includes_rs_signals_when_bench_df_given(monkeypatch):
    ohlc_map = {"FOO": _fixture_df(200)}
    monkeypatch.setattr(
        "union_chart_dashboard.compute_rs_transition_kinds",
        lambda df, bench_df: [None] * 199 + ["rs_weak_to_strong"],
    )
    records, _ = build_chart_data(
        ohlc_map, {"FOO": "ALL 4"}, min_bars=130, bench_df=_fixture_df(200),
    )
    assert records[0]["rs_signals"][-1] == "rs_weak_to_strong"


def test_build_chart_data_includes_rs_pane_when_bench_df_given(monkeypatch):
    ohlc_map = {"FOO": _fixture_df(200)}
    monkeypatch.setattr(
        "union_chart_dashboard.compute_rs_pane_series",
        lambda df, bench_df: {"rs_line": [1.0] * 200, "rs_ema9": [1.0] * 200,
                               "rs_ema21": [1.0] * 200, "rs_weekly_ema9": [1.0] * 200},
    )
    records, _ = build_chart_data(
        ohlc_map, {"FOO": "ALL 4"}, min_bars=130, bench_df=_fixture_df(200),
    )
    assert records[0]["rs_pane"]["rs_line"][0] == 1.0


def test_build_chart_data_rs_pane_none_for_non_nse_symbol(monkeypatch):
    ohlc_map = {"AAPL": _fixture_df(200)}
    monkeypatch.setattr(
        "union_chart_dashboard.compute_rs_pane_series",
        lambda df, bench_df: {"rs_line": [1.0] * 200} if bench_df is not None else None,
    )
    records, _ = build_chart_data(
        ohlc_map, {"AAPL": "ALL 4"}, min_bars=130,
        bench_df=_fixture_df(200), symbol_exchange={"AAPL": "NASDAQ"},
    )
    assert records[0]["rs_pane"] is None


def test_build_chart_data_rs_pane_none_without_bench_df():
    ohlc_map = {"FOO": _fixture_df(200)}
    records, _ = build_chart_data(ohlc_map, {"FOO": "ALL 4"}, min_bars=130)
    assert records[0]["rs_pane"] is None


def test_build_chart_data_skips_rs_signals_for_non_nse_symbol(monkeypatch):
    ohlc_map = {"AAPL": _fixture_df(200)}
    monkeypatch.setattr(
        "union_chart_dashboard.compute_rs_transition_kinds",
        lambda df, bench_df: [None] * 199 + ["rs_weak_to_strong"] if bench_df is not None else [None] * 200,
    )
    records, _ = build_chart_data(
        ohlc_map, {"AAPL": "ALL 4"}, min_bars=130,
        bench_df=_fixture_df(200), symbol_exchange={"AAPL": "NASDAQ"},
    )
    assert records[0]["rs_signals"] == [None] * 200


def test_build_chart_data_rs_signals_all_none_without_bench_df():
    ohlc_map = {"FOO": _fixture_df(200)}
    records, _ = build_chart_data(ohlc_map, {"FOO": "ALL 4"}, min_bars=130)
    assert records[0]["rs_signals"] == [None] * 200


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


def _chart_record(
    symbol="FOO", tier="ALL 5", industry="Software", day_change=2.3456
):
    return {
        "symbol": symbol,
        "tier": tier,
        "industry": industry,
        "day_change": day_change,
        "bars": [["2026-08-25", 1, 2, 0.5, 1.5, 100]],
        "signals": [None],
        "coil_boxes": [],
    }


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


def test_build_html_chart_background_pure_black_no_grid_lines():
    html = build_html([], "2026-08-27")
    build_chart_body = html.split("function buildChart(symbol) {", 1)[1].split(
        "const upColor", 1
    )[0]
    assert "background: { color: '#000000' }" in build_chart_body
    assert "vertLines: { visible: false }" in build_chart_body
    assert "horzLines: { visible: false }" in build_chart_body


def test_build_html_has_fixed_mode_and_adaptive_touch_contract():
    html = build_html([], "2026-08-27")
    compact = "".join(html.split())
    assert "repeat(auto-fit,minmax(min(100%,640px),1fr))" in compact
    assert ".chart,.rs-pane-wrap{height:clamp(380px,44vw,520px)}" in compact
    assert (
        "@media(max-width:600px){#grid{grid-template-columns:1fr}"
        ".chart,.rs-pane-wrap{height:380px}}" in compact
    )
    assert "vertTouchDrag:false" in compact
    assert "setVisibleLogicalRange" in html
    assert "fitContent(" not in html
    assert "setUTCMonth" not in html
    assert "Unclassified" in html


def test_build_html_starts_with_emas_hidden_and_switch_unchecked():
    html = build_html([], "2026-08-27")
    assert "emaVisible: false" in html
    label_start = html.index("<span>EMAs</span>")
    input_start = html.index("<input", label_start)
    ema_input = html[input_start : html.index(">", input_start) + 1]
    assert "checked" not in ema_input
    assert "localStorage" not in html
    assert "sessionStorage" not in html


def test_build_html_orders_change_tier_and_symbol_for_right_thumb_access():
    html = build_html([_chart_record()], "2026-08-27")
    header = html.split('<div class="hdr">', 1)[1].split("</div>", 1)[0]
    assert header.index('class="day-change gain"') < header.index('class="tier"')
    assert header.index('class="tier"') < header.index('class="symbol-link"')
    assert 'href="https://in.tradingview.com/chart/?symbol=NSE:FOO"' in header
    assert 'target="_blank"' in header


def test_build_html_has_centered_header_and_44px_symbol_target():
    compact = "".join(build_html([], "2026-08-27").split())
    assert (
        ".hdr{display:grid;grid-template-columns:1frauto1fr;align-items:center"
        in compact
    )
    assert ".day-change{justify-self:start" in compact
    assert ".tier{justify-self:center" in compact
    assert ".symbol-link{justify-self:end;min-height:44px" in compact


def test_fixed_range_clamps_month_end_generic_months_offset():
    html = build_html([], "2026-08-26")
    assert "function monthsCutoff(last, months)" in html
    assert "Math.min(sourceDay, lastDay)" in html
    assert "monthsCutoff(last, DEFAULT_VIEW_MONTHS)" in html

    def reference(last, months):
        year, month, day = map(int, last.split("-"))
        target = year * 12 + month - 1 - months
        target_year, target_month_zero = divmod(target, 12)
        next_month = target_year * 12 + target_month_zero + 1
        next_year, next_month_zero = divmod(next_month, 12)
        from datetime import date, timedelta
        last_day = (date(next_year, next_month_zero + 1, 1) - timedelta(days=1)).day
        return date(target_year, target_month_zero + 1, min(day, last_day)).isoformat()

    assert reference("2025-08-31", 12) == "2024-08-31"
    assert reference("2024-08-31", 12) == "2023-08-31"
    assert reference("2025-02-28", 9) == "2024-05-28"
    assert reference("2024-02-29", 9) == "2023-05-29"


def test_default_view_months_is_six():
    html = build_html([], "2026-08-26")
    assert "const DEFAULT_VIEW_MONTHS = 6;" in html


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
    assert 'wt_bull: "#76ff03"' in html
    assert 'wt_bear: "#fdd835"' in html
    assert "lastValueVisible: false" in html
    assert "priceLineVisible: false" in html


def test_build_html_starts_with_zlema25_hidden_and_switch_unchecked():
    html = build_html([], "2026-08-27")
    assert "zlema25Visible: false" in html
    label_start = html.index("<span>ZLEMA25</span>")
    input_start = html.index("<input", label_start)
    zlema_input = html[input_start : html.index(">", input_start) + 1]
    assert 'id="zlema25Visible"' in zlema_input
    assert "checked" not in zlema_input


def test_build_html_configures_zlema25_as_hidden_label_step_line():
    html = build_html([], "2026-08-27")
    rebuild = html.split("function rebuildZlema25(entry) {", 1)[1].split(
        "function applyVolumeState(entry)", 1
    )[0]
    assert "LightweightCharts.LineType.WithSteps" in rebuild
    assert "lineWidth: 1" in rebuild
    assert "lastValueVisible: false" in rebuild
    assert "priceLineVisible: false" in rebuild
    assert "document.getElementById('zlema25Visible')" in html


def _run_generated_js_function(html, start_marker, end_marker, expression):
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for generated JavaScript parity tests")
    function_source = start_marker + html.split(start_marker, 1)[1].split(
        end_marker, 1
    )[0]
    completed = subprocess.run(
        [
            node,
            "-e",
            function_source + "\nconsole.log(JSON.stringify(" + expression + "));",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def test_generated_zlema25_matches_pine_recursive_ema_seed():
    html = build_html([], "2026-08-27")
    closes = list(range(1, 41))
    values = _run_generated_js_function(
        html,
        "function computeZlema25(closes) {",
        "function zlema25LineData(record)",
        f"computeZlema25({json.dumps(closes)})",
    )
    assert values[:12] == [None] * 12
    assert values[12] == pytest.approx(25.0)
    assert values[13] == pytest.approx(25.076923076923077)
    assert values[-1] == pytest.approx(41.38230658545096)


def test_zlema25_toggle_is_independent_and_schedules_coil_redraw():
    html = build_html([], "2026-08-27")
    ema_handler = html.split(
        "document.getElementById('emaVisible').addEventListener('change', function(e) {",
        1,
    )[1].split("document.getElementById('zlema25Visible')", 1)[0]
    zlema_handler = html.split(
        "document.getElementById('zlema25Visible').addEventListener('change', function(e) {",
        1,
    )[1].split("document.getElementById('volumeVisible')", 1)[0]
    assert "rebuildZlema25" not in ema_handler
    assert "rebuildEmas" not in zlema_handler
    assert "rebuildZlema25(entry);" in zlema_handler
    assert "scheduleCoilRedraw(entry);" in zlema_handler


def test_build_html_starts_with_high52w_hidden_and_switch_unchecked():
    html = build_html([], "2026-08-27")
    assert "high52wVisible: false" in html
    label_start = html.index("<span>52W High</span>")
    input_start = html.index("<input", label_start)
    high52w_input = html[input_start : html.index(">", input_start) + 1]
    assert 'id="high52wVisible"' in high52w_input
    assert "checked" not in high52w_input


def test_build_html_high52w_default_visible_true_starts_checked_and_shown():
    html = build_html([], "2026-08-27", high52w_default_visible=True)
    assert "high52wVisible: true" in html
    label_start = html.index("<span>52W High</span>")
    input_start = html.index("<input", label_start)
    high52w_input = html[input_start : html.index(">", input_start) + 1]
    assert 'id="high52wVisible"' in high52w_input
    assert "checked" in high52w_input


def test_build_html_configures_high52w_as_blue_step_line():
    html = build_html([], "2026-08-27")
    rebuild = html.split("function rebuildHigh52w(entry) {", 1)[1].split(
        "function applyVolumeState(entry)", 1
    )[0]
    assert "LightweightCharts.LineType.WithSteps" in rebuild
    assert "lastValueVisible: false" in rebuild
    assert "priceLineVisible: false" in rebuild
    assert "document.getElementById('high52wVisible')" in html


def test_next_weekday_skips_saturday_and_sunday():
    html = build_html([], "2026-08-27")
    result = _run_generated_js_function(
        html,
        "function nextWeekday(dateStr) {",
        "function extendFlatWeekdays",
        'nextWeekday("2024-01-05")',
    )
    assert result == "2024-01-08"


def test_next_weekday_plain_weekday_increments_by_one():
    html = build_html([], "2026-08-27")
    result = _run_generated_js_function(
        html,
        "function nextWeekday(dateStr) {",
        "function extendFlatWeekdays",
        'nextWeekday("2024-01-08")',
    )
    assert result == "2024-01-09"


def test_extend_flat_weekdays_appends_15_points_holding_last_value():
    html = build_html([], "2026-08-27")
    points = _run_generated_js_function(
        html,
        "function nextWeekday(dateStr) {",
        "function high52wLineData(record)",
        'extendFlatWeekdays([{"time": "2024-01-05", "value": 42}], 15)',
    )
    assert len(points) == 16
    assert all(p["value"] == 42 for p in points[1:])
    assert points[1]["time"] == "2024-01-08"
    assert points[-1]["time"] == "2024-01-26"
    assert all(
        pd_to_weekday(p["time"]) not in ("Saturday", "Sunday") for p in points[1:]
    )


def pd_to_weekday(date_str):
    import datetime
    return datetime.date.fromisoformat(date_str).strftime("%A")


def test_high52wlinedata_extends_15_weekdays_flat_at_last_value():
    html = build_html([], "2026-08-27")
    dates = list(pd.bdate_range("2025-01-06", periods=260).strftime("%Y-%m-%d"))
    bars = [[d, 100.0, 100.0 + i, 99.0, 100.0, 1000.0] for i, d in enumerate(dates)]
    record = {"bars": bars}
    points = _run_generated_js_function(
        html,
        "const HIGH52W_PERIOD = 260;",
        "function addEmaSeries(entry, periods)",
        f"high52wLineData({json.dumps(record)})",
    )
    assert len(points) == (260 - 259) + 15  # 1 real rolling-max point + 15 extension
    last_real_value = points[0]["value"]
    assert all(p["value"] == last_real_value for p in points[1:])


def test_rs_dot_geometry_sizes_below_low_and_above_high():
    html = build_html([], "2026-08-27")
    record = {
        "bars": [
            ["2026-01-01", 1, 2, 0.5, 1.5, 100],
            ["2026-01-02", 1, 2, 0.5, 1.5, 100],
            ["2026-01-03", 1, 2, 0.5, 1.5, 100],
        ],
        "rs_signals": [None, "rs_weak_to_strong", "rs_strong_to_weak"],
    }
    dots = _run_generated_js_function(
        html,
        "const RS_DOT_COLORS",
        "function redrawRsDots(entry)",
        "rsDotGeometry("
        f"{json.dumps(record)}, 6, "
        "function(i) { return i * 10; }, "
        "function(p) { return 100 - p; }"
        ")",
    )
    assert dots == [
        {"left": 7, "top": 101.5, "width": 6, "height": 6, "color": "lime"},
        {"left": 17, "top": 90, "width": 6, "height": 6, "color": "red"},
    ]


def test_rs_dot_geometry_skips_off_chart_coordinates():
    html = build_html([], "2026-08-27")
    record = {
        "bars": [["2026-01-01", 1, 2, 0.5, 1.5, 100]],
        "rs_signals": ["rs_weak_to_strong"],
    }
    dots = _run_generated_js_function(
        html,
        "const RS_DOT_COLORS",
        "function redrawRsDots(entry)",
        f"rsDotGeometry({json.dumps(record)}, 6, function(i) {{ return null; }}, function(p) {{ return 1; }})",
    )
    assert dots == []


def test_rs_dot_geometry_skips_missing_rs_signals_field():
    html = build_html([], "2026-08-27")
    record = {"bars": [["2026-01-01", 1, 2, 0.5, 1.5, 100]]}
    dots = _run_generated_js_function(
        html,
        "const RS_DOT_COLORS",
        "function redrawRsDots(entry)",
        f"rsDotGeometry({json.dumps(record)}, 6, function(i) {{ return 0; }}, function(p) {{ return 0; }})",
    )
    assert dots == []


def test_build_html_starts_with_rs_dots_hidden_and_switch_unchecked():
    html = build_html([], "2026-08-27")
    assert "rsVisible: false" in html
    label_start = html.index("<span>RS Transitions</span>")
    input_start = html.index("<input", label_start)
    rs_input = html[input_start : html.index(">", input_start) + 1]
    assert 'id="rsVisible"' in rs_input
    assert "checked" not in rs_input


def test_rs_dots_toggle_schedules_redraw():
    html = build_html([], "2026-08-27")
    rs_handler = html.split(
        "document.getElementById('rsVisible').addEventListener('change', function(e) {",
        1,
    )[1].split("document.getElementById('volumeVisible')", 1)[0]
    assert "uiState.rsVisible = e.target.checked;" in rs_handler
    assert "scheduleCoilRedraw(entry);" in rs_handler


def test_redraw_rs_dots_returns_without_drawing_when_hidden():
    html = build_html([], "2026-08-27")
    redraw_rs_dots_body = html.split("function redrawRsDots(entry) {", 1)[1].split(
        "function scheduleCoilRedraw(entry)", 1
    )[0]
    assert "if (!uiState.rsVisible) return;" in redraw_rs_dots_body


def test_redraw_coils_draws_rs_dots_sized_to_bar_spacing():
    html = build_html([], "2026-08-27")
    redraw_coils_body = html.split("function redrawCoils(entry) {", 1)[1].split(
        "function scheduleCoilRedraw(entry)", 1
    )[0]
    assert "redrawRsDots(entry);" in redraw_coils_body
    assert "RS_DOT_WIDTH_FRACTION" in html
    assert ".rs-dot{" in "".join(html.split())


def test_build_html_rs_pane_switch_checked_by_default():
    html = build_html([], "2026-08-27")
    assert "rsPaneVisible: true" in html
    label_start = html.index("<span>RS Pane</span>")
    input_start = html.index("<input", label_start)
    rs_pane_input = html[input_start : html.index(">", input_start) + 1]
    assert 'id="rsPaneVisible"' in rs_pane_input
    assert "checked" in rs_pane_input


def test_rs_line_directional_data_colors_by_direction_and_skips_nulls():
    html = build_html([], "2026-08-27")
    bars = [
        ["2026-01-01", 1, 2, 0.5, 1.5, 100],
        ["2026-01-02", 1, 2, 0.5, 1.5, 100],
        ["2026-01-03", 1, 2, 0.5, 1.5, 100],
        ["2026-01-04", 1, 2, 0.5, 1.5, 100],
    ]
    values = [10, None, 15, 12]
    points = _run_generated_js_function(
        html,
        "function rsLineDirectionalData(bars, values, upColor, downColor) {",
        "function buildRsPane(entry)",
        f'rsLineDirectionalData({json.dumps(bars)}, {json.dumps(values)}, "up", "down")',
    )
    assert points == [
        {"time": "2026-01-01", "value": 10, "color": "down"},
        {"time": "2026-01-03", "value": 15, "color": "down"},
        {"time": "2026-01-04", "value": 12, "color": "down"},
    ]


def test_rs_line_directional_data_marks_rising_point_up_colored():
    html = build_html([], "2026-08-27")
    bars = [["2026-01-01", 1, 2, 0.5, 1.5, 100], ["2026-01-02", 1, 2, 0.5, 1.5, 100]]
    values = [10, 20]
    points = _run_generated_js_function(
        html,
        "function rsLineDirectionalData(bars, values, upColor, downColor) {",
        "function buildRsPane(entry)",
        f'rsLineDirectionalData({json.dumps(bars)}, {json.dumps(values)}, "up", "down")',
    )
    assert points[1]["color"] == "up"


def test_build_rs_pane_colors_weekly_ema9_lime_in_uptrend():
    html = build_html([], "2026-08-27")
    build_rs_pane_body = html.split("function buildRsPane(entry) {", 1)[1].split(
        "\nfunction applyControls()", 1
    )[0]
    assert (
        'rsLineDirectionalData(bars, pane.rs_weekly_ema9, "lime", "#787b86")'
        in build_rs_pane_body
    )


def test_build_chart_wires_rs_pane_build_and_sync():
    html = build_html([], "2026-08-27")
    build_chart_body = html.split("function buildChart(symbol) {", 1)[1].split(
        "\nfunction applyControls()", 1
    )[0]
    assert "buildRsPane(entry);" in build_chart_body


def test_build_rs_pane_returns_early_without_rs_pane_data():
    html = build_html([], "2026-08-27")
    build_rs_pane_body = html.split("function buildRsPane(entry) {", 1)[1].split(
        "\nfunction applyControls()", 1
    )[0]
    assert "if (!entry.record.rs_pane) return;" in build_rs_pane_body
    assert "subscribeVisibleLogicalRangeChange" in build_rs_pane_body
    assert "ResizeObserver" in build_rs_pane_body


def test_rs_pane_toggle_hides_wrap_without_rebuilding():
    html = build_html([], "2026-08-27")
    handler = html.split(
        "document.getElementById('rsPaneVisible').addEventListener('change', function(e) {",
        1,
    )[1].split("</script>", 1)[0]
    assert "uiState.rsPaneVisible = e.target.checked;" in handler
    assert "entry.rsPaneWrap.hidden = !uiState.rsPaneVisible;" in handler


def test_generated_high52w_matches_rolling_max_of_high():
    html = build_html([], "2026-08-27")
    highs = [10, 20, 15, 12, 11, 25, 24]
    values = _run_generated_js_function(
        html,
        "function computeHigh52w(highs, period) {",
        "function high52wLineData(record)",
        f"computeHigh52w({json.dumps(highs)}, 3)",
    )
    assert values[:2] == [None, None]
    assert values[2] == 20
    assert values[3] == 20
    assert values[4] == 15
    assert values[5] == 25
    assert values[6] == 25


def test_high52w_toggle_is_independent_and_schedules_coil_redraw():
    html = build_html([], "2026-08-27")
    zlema_handler = html.split(
        "document.getElementById('zlema25Visible').addEventListener('change', function(e) {",
        1,
    )[1].split("document.getElementById('high52wVisible')", 1)[0]
    high52w_handler = html.split(
        "document.getElementById('high52wVisible').addEventListener('change', function(e) {",
        1,
    )[1].split("document.getElementById('volumeVisible')", 1)[0]
    assert "rebuildHigh52w" not in zlema_handler
    assert "rebuildZlema25" not in high52w_handler
    assert "rebuildHigh52w(entry);" in high52w_handler
    assert "scheduleCoilRedraw(entry);" in high52w_handler


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
