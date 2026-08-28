import sys
import math
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))

import ema25_zl_scanner as base
import ema55_cross_scanner as scanner
from ema55_cross_scanner import (
    average_traded_value_cr,
    filter_union_sources,
    ema55_cross_stats,
    ema55_trend_age,
    build_union,
    build_union_section,
    _symbols_from_tv_block,
    _load_union_source,
    TODAY,
)


def _liquidity_df(
    *,
    rows: int = 30,
    close: float = 100.0,
    volume: float = 1_000_000.0,
    end: str = TODAY,
) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "date": pd.bdate_range(end=end, periods=rows),
            "close": [close] * rows,
            "volume": [volume] * rows,
        }
    )


def test_average_traded_value_uses_30_session_sma_and_latest_close():
    df = _liquidity_df(close=200.0, volume=50_000.0)
    df.loc[df.index[0], "volume"] = 0.0

    expected = ((29 * 50_000.0) / 30) * 200.0 / 10_000_000
    assert math.isclose(average_traded_value_cr(df, TODAY), expected)


def test_filter_union_sources_includes_exact_ten_crore_and_excludes_below():
    sources = {"EMA55 Cross": {"EXACT", "LOW"}, "Trend": {"EXACT", "LOW"}}
    ohlc = {
        "EXACT": _liquidity_df(close=100.0, volume=1_000_000.0),
        "LOW": _liquidity_df(close=100.0, volume=999_999.0),
    }

    filtered, excluded, unverified = filter_union_sources(sources, ohlc, TODAY)

    assert filtered == {"EMA55 Cross": {"EXACT"}, "Trend": {"EXACT"}}
    assert excluded == ["LOW"]
    assert unverified == []


def test_filter_union_sources_retains_and_sorts_unverified_histories():
    stale = _liquidity_df(end="2000-01-31")
    invalid_close = _liquidity_df()
    invalid_close.loc[invalid_close.index[-1], "close"] = float("nan")
    negative_volume = _liquidity_df()
    negative_volume.loc[negative_volume.index[3], "volume"] = -1
    sources = {
        "EMA55 Cross": {"STALE", "MISSING", "SHORT"},
        "Trend": {"BAD_CLOSE", "BAD_VOLUME"},
    }
    ohlc = {
        "STALE": stale,
        "SHORT": _liquidity_df(rows=29),
        "BAD_CLOSE": invalid_close,
        "BAD_VOLUME": negative_volume,
    }

    filtered, excluded, unverified = filter_union_sources(sources, ohlc, TODAY)

    assert filtered == sources
    assert excluded == []
    assert unverified == ["BAD_CLOSE", "BAD_VOLUME", "MISSING", "SHORT", "STALE"]


def test_filter_union_sources_treats_nonpositive_close_and_nonnumeric_volume_as_unverified():
    zero_close = _liquidity_df(close=0.0)
    bad_volume = _liquidity_df()
    bad_volume["volume"] = bad_volume["volume"].astype(object)
    bad_volume.loc[bad_volume.index[0], "volume"] = "unknown"
    sources = {"EMA55 Cross": {"ZERO", "TEXT"}, "Trend": {"ZERO", "TEXT"}}

    filtered, excluded, unverified = filter_union_sources(
        sources, {"ZERO": zero_close, "TEXT": bad_volume}, TODAY
    )

    assert filtered == sources
    assert excluded == []
    assert unverified == ["TEXT", "ZERO"]


def test_filter_union_sources_does_not_mutate_inputs_and_recalculates_tiers():
    sources = {
        "EMA55 Cross": {"LIQUID", "LOW"},
        "EMA25 ZL": {"LIQUID", "LOW", "ONLY"},
        "Trend": {"LIQUID", "ONLY"},
    }
    original = {name: set(symbols) for name, symbols in sources.items()}
    ohlc = {
        "LIQUID": _liquidity_df(),
        "LOW": _liquidity_df(volume=50_000.0),
        "ONLY": _liquidity_df(),
    }

    filtered, excluded, unverified = filter_union_sources(sources, ohlc, TODAY)

    assert sources == original
    assert excluded == ["LOW"]
    assert unverified == []
    assert build_union(filtered) == [
        ("ALL 3", ["LIQUID"]),
        ("2 OF 3", ["ONLY"]),
    ]


def test_cross_up_detected_at_correct_age():
    # close crosses above ema on the 3rd-from-last bar -> age 3
    close = pd.Series([10, 10, 10, 10, 9, 11, 12, 13])
    ema = pd.Series([10, 10, 10, 10, 10, 10, 10, 10])
    days, pct = ema55_cross_stats(close, ema)
    assert days == 3
    assert pct == round((13 / 9 - 1) * 100, 2)


def test_no_cross_within_cap_returns_cap_sentinel():
    # always above ema, never crosses -> capped age, pct measured from cap bar
    close = pd.Series([20.0] * 70)
    ema = pd.Series([10.0] * 70)
    days, pct = ema55_cross_stats(close, ema)
    assert days == 60
    assert pct == 0.0


def test_trend_age_diverges_from_cross_age_on_a_whipsaw():
    # long steady uptrend interrupted by one sharp one-day dip below EMA55,
    # then resumes: cross age should reset low (fresh recross) but the
    # 5-bar-smoothed trend age should stay high (still an established
    # uptrend) -- proves trend age isn't just a copy of cross age (a raw
    # per-bar EMA slope-turn always equals the crossover, see
    # ema55_cross_stats docstring).
    close = pd.Series([100.0 + i for i in range(100)])
    close.iloc[-3] -= 40
    close.iloc[-2] = close.iloc[-4] + 1
    close.iloc[-1] = close.iloc[-2] + 1
    ema55 = base.ema(close, 55)

    cross_days, _ = ema55_cross_stats(close, ema55)
    trend_days, _ = ema55_trend_age(ema55, close)

    assert cross_days <= 3
    assert trend_days > cross_days


def test_build_union_groups_by_confluence_descending():
    source_sets = {
        "EMA55 Cross": {"A", "B", "C"},
        "EMA25 ZL": {"A", "B", "D"},
        "Minervini": {"A", "E"},
    }
    groups = build_union(source_sets)
    assert groups[0] == ("ALL 3", ["A"])
    assert groups[1] == ("2 OF 3", ["B"])
    assert groups[2] == ("1 ONLY", ["C", "D", "E"])


def test_build_union_omits_empty_groups():
    # nothing appears in all 3 -> no "ALL 3" group emitted
    source_sets = {
        "EMA55 Cross": {"A"},
        "EMA25 ZL": {"B"},
        "Minervini": {"C"},
    }
    groups = build_union(source_sets)
    labels = [label for label, _ in groups]
    assert "ALL 3" not in labels
    assert groups == [("1 ONLY", ["A", "B", "C"])]


def test_build_union_degrades_with_fewer_sources():
    # one upstream source missing -> relabel to 2-way confluence, not 3-way
    source_sets = {"EMA55 Cross": {"A", "B"}, "EMA25 ZL": {"A", "C"}}
    groups = build_union(source_sets)
    assert groups == [("ALL 2", ["A"]), ("1 ONLY", ["B", "C"])]


def test_build_union_uses_five_source_tiers():
    source_sets = {
        "EMA55 Cross": {"ALL5", "FOUR"},
        "EMA25 ZL": {"ALL5", "FOUR"},
        "Minervini": {"ALL5", "FOUR"},
        "Trend": {"ALL5", "FOUR"},
        "Weekly RS EMA9": {"ALL5", "WEEKLY_ONLY"},
    }
    assert build_union(source_sets) == [
        ("ALL 5", ["ALL5"]),
        ("4 OF 5", ["FOUR"]),
        ("1 ONLY", ["WEEKLY_ONLY"]),
    ]


def test_union_section_names_weekly_rs_ema9_as_fifth_source():
    section = "\n".join(build_union_section([("ALL 5", ["FOO"])], []))
    assert "EMA25 ZL + EMA55 Cross + Minervini Trend Template + Trend Scanner + Weekly RS EMA9" in section


def test_build_markdown_loads_weekly_rs_ema9_source(monkeypatch):
    loaded_names = []

    def fake_load(path, skip_labels, name):
        loaded_names.append(name)
        return {"FOO"}, None

    monkeypatch.setattr(scanner, "_load_union_source", fake_load)
    report = scanner.build_markdown([], {})

    assert "Weekly RS EMA9" in loaded_names
    assert "Weekly RS EMA9" in report
    assert "4 OF 5" in report


def test_build_union_returns_empty_for_single_source():
    assert build_union({"EMA55 Cross": {"A", "B"}}) == []


def test_symbols_from_tv_block_skips_anchors_and_labelled_sections():
    md = (
        "intro text\n"
        "```\n"
        "###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,"
        "###1 DAY,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:FOO,NSE:BAR,"
        "###WATCH,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:BAZ\n"
        "```\n"
        "outro text\n"
    )
    syms = _symbols_from_tv_block(md, {"INDICES", "COMMODITIES", "WATCH"})
    assert syms == {"FOO", "BAR"}


def test_load_union_source_missing_file(tmp_path):
    missing = tmp_path / "does_not_exist.md"
    syms, note = _load_union_source(str(missing), set(), "Test Source")
    assert syms is None
    assert "not found" in note


def test_load_union_source_stale_date(tmp_path):
    stale = tmp_path / "stale.md"
    stale.write_text("# Some Scan - 2000-01-01\n```\n###1 DAY,NSE:FOO\n```\n", encoding="utf-8")
    syms, note = _load_union_source(str(stale), set(), "Test Source")
    assert syms is None
    assert "stale" in note


def test_load_union_source_fresh_file(tmp_path):
    fresh = tmp_path / "fresh.md"
    fresh.write_text(f"# Some Scan - {TODAY}\n```\n###1 DAY,NSE:FOO\n```\n", encoding="utf-8")
    syms, note = _load_union_source(str(fresh), set(), "Test Source")
    assert syms == {"FOO"}
    assert note is None


def test_union_section_reports_liquidity_exclusions_and_unverified_symbols():
    section = "\n".join(
        build_union_section(
            [("ALL 2", ["LIQUID"])],
            [],
            excluded_symbols=["LOW"],
            unverified_symbols=["BETA", "ALPHA"],
        )
    )

    assert "Avg Volume 30D × latest close ≥ ₹10 Cr" in section
    assert "Excluded below threshold: 1" in section
    assert "Liquidity unverified (retained): ALPHA, BETA" in section
    assert section.index("Liquidity unverified") < section.index("```")


def test_build_markdown_filters_union_with_one_sorted_batch_load(monkeypatch):
    def fake_source(path, skip_labels, name):
        return {"LIQUID", "LOW", "MISSING"}, None

    calls = []

    def fake_many(symbols, lookback):
        calls.append((symbols, lookback))
        return {
            "LIQUID": _liquidity_df(),
            "LOW": _liquidity_df(volume=50_000.0),
        }

    monkeypatch.setattr(scanner, "_load_union_source", fake_source)
    monkeypatch.setattr(scanner, "load_ohlc_many", fake_many)

    report = scanner.build_markdown([], {})

    assert calls == [(["LIQUID", "LOW", "MISSING"], 30)]
    union_block = report.split("### Scan definition", 1)[0]
    assert "NSE:LIQUID" in union_block
    assert "NSE:MISSING" in union_block
    assert "NSE:LOW" not in union_block
    assert "Excluded below threshold: 1" in union_block
    assert "Liquidity unverified (retained): MISSING" in union_block


def test_build_markdown_skips_liquidity_load_with_only_ema55_source(monkeypatch):
    monkeypatch.setattr(scanner, "_load_union_source", lambda *args: (None, "stale"))

    def unexpected_load(*args, **kwargs):
        raise AssertionError("load_ohlc_many must not run for one source")

    monkeypatch.setattr(scanner, "load_ohlc_many", unexpected_load)
    monkeypatch.setattr(scanner, "_table_rows", lambda *args: ["| EMA55ONLY |"])

    report = scanner.build_markdown([{"symbol": "EMA55ONLY", "cross_days": 1}], {})

    assert "No union data available today" in report


def test_build_markdown_retains_candidates_when_batch_load_fails(monkeypatch):
    monkeypatch.setattr(
        scanner, "_load_union_source", lambda *args: ({"EMA55SYM", "UPSTREAM"}, None)
    )
    monkeypatch.setattr(
        scanner,
        "load_ohlc_many",
        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("db down")),
    )
    monkeypatch.setattr(scanner, "_table_rows", lambda *args: ["| EMA55SYM |"])
    finding = {"symbol": "EMA55SYM", "cross_days": 1}

    report = scanner.build_markdown([finding], {})
    union_block, standalone = report.split("### Scan definition", 1)

    assert "NSE:EMA55SYM" in union_block
    assert "NSE:UPSTREAM" in union_block
    assert "Liquidity unverified (retained): EMA55SYM, UPSTREAM" in union_block
    assert "EMA55SYM" in standalone


def test_low_liquidity_symbol_is_removed_only_from_union(monkeypatch):
    monkeypatch.setattr(scanner, "_load_union_source", lambda *args: ({"LOW"}, None))
    monkeypatch.setattr(
        scanner,
        "load_ohlc_many",
        lambda *args, **kwargs: {"LOW": _liquidity_df(volume=50_000.0)},
    )
    monkeypatch.setattr(scanner, "_table_rows", lambda *args: ["| LOW |"])
    finding = {"symbol": "LOW", "cross_days": 1}

    report = scanner.build_markdown([finding], {})
    union_block, standalone = report.split("### Scan definition", 1)

    assert "NSE:LOW" not in union_block
    assert "Excluded below threshold: 1" in union_block
    assert "| LOW |" in standalone
    assert "NSE:LOW" in standalone


if __name__ == "__main__":
    test_cross_up_detected_at_correct_age()
    test_no_cross_within_cap_returns_cap_sentinel()
    test_trend_age_diverges_from_cross_age_on_a_whipsaw()
    test_build_union_groups_by_confluence_descending()
    test_build_union_omits_empty_groups()
    test_build_union_degrades_with_fewer_sources()
    test_build_union_returns_empty_for_single_source()
    test_symbols_from_tv_block_skips_anchors_and_labelled_sections()
    print("ok")
