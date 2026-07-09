import pytest
import pandas as pd

from institutional_footprint_scanner import (
    absorption_day,
    analyse_symbol,
    assign_lifecycle,
    assign_rating,
    assign_trade_action,
    build_html,
    build_markdown,
    calculate_ics,
    consecutive_high_delivery_days,
    delivery_percentile,
    delivery_sparkline,
    delivery_zscore,
    failed_breakdown_reclaim,
    failed_breakout,
    resistance_touch_count,
    run,
    structure_tag,
)


def test_delivery_sparkline_returns_empty_when_insufficient_history():
    assert delivery_sparkline([10.0] * 19) == ""


def test_delivery_sparkline_uses_latest_20_values_and_middle_block_for_flat_series():
    assert delivery_sparkline([99.0] + [42.0] * 20) == "▄" * 20


def test_delivery_sparkline_scales_latest_20_values():
    sparkline = delivery_sparkline(list(range(1, 21)))

    assert len(sparkline) == 20
    assert sparkline[0] == "▁"
    assert sparkline[-1] == "█"


def test_delivery_percentile_excludes_latest_value():
    assert delivery_percentile(list(range(1, 62)), min_periods=60) == 100


def test_delivery_percentile_returns_none_until_min_periods_met():
    assert delivery_percentile(list(range(1, 61)), min_periods=60) is None


def test_delivery_zscore_positive_when_latest_above_prior_mean():
    values = list(range(1, 61)) + [100.0]
    assert delivery_zscore(values, min_periods=60) > 0


def test_delivery_zscore_none_when_prior_window_flat():
    assert delivery_zscore([10.0] * 61, min_periods=60) is None


def test_consecutive_high_delivery_days_counts_backward_against_prior_average():
    values = [20.0] * 20 + [40.0, 42.0]

    assert consecutive_high_delivery_days(values) == 2


def test_assign_rating_uses_spec_thresholds():
    assert assign_rating(95) == "ELITE"
    assert assign_rating(85) == "STRONG"
    assert assign_rating(70) == "BUILDING"
    assert assign_rating(55) == "WATCH"
    assert assign_rating(54.9) == "IGNORE"


def test_calculate_ics_caps_to_0_100_and_scores_all_components():
    row = {
        "latest_delivery_above_avg20": True,
        "delivery_ratio": 1.6,
        "delivery_percentile": 95,
        "consecutive_high_delivery_days": 3,
        "delivery_slope_positive": True,
        "volume_ratio": 1.6,
        "turnover_ratio": 1.6,
        "turnover_cr": 6,
        "up_day_volume_above_avg": True,
        "close_gt_ema20": True,
        "close_gt_ema50": True,
        "close_gt_ema200": True,
        "breakout20": True,
        "within_15pct_52w_high": True,
        "cmf20": 0.06,
        "cmf_rising": True,
        "rs_percentile": 95,
        "rs_trend": "UP",
        "outperform_benchmark_50d": True,
    }

    assert calculate_ics(row) == 100


@pytest.mark.parametrize(
    ("row", "stage"),
    [
        ({"price_down": True, "volume_ratio": 1.6, "cmf20": -0.1, "cmf_rising": False}, "DISTRIBUTION"),
        ({"breakout20": True, "delivery_percentile": 95, "volume_ratio": 1.6}, "BREAKOUT"),
        ({"close_gt_ema20": True, "close_gt_ema50": True, "rs_percentile": 95, "ics": 85}, "MARKUP"),
        ({"ics": 70, "delivery_slope_positive": True, "cmf20": 0.01, "breakout20": False}, "BUILDING"),
        ({"delivery_percentile": 85, "breakout20": False}, "SEED"),
    ],
)
def test_assign_lifecycle_uses_priority_order(row, stage):
    assert assign_lifecycle(row) == stage


def _ohlc(symbol_shift=0.0):
    n = 260
    close = [100 + i * 0.5 + symbol_shift for i in range(n)]
    return pd.DataFrame(
        {
            "date": pd.date_range("2025-01-01", periods=n, freq="D"),
            "open": [c - 0.5 for c in close],
            "high": [c + 1 for c in close],
            "low": [c - 1 for c in close],
            "close": close,
            "volume": [1_000_000] * 240 + [2_000_000] * 20,
        }
    )


def _delivery(latest=45.0):
    return pd.DataFrame(
        {
            "date": pd.date_range("2025-01-01", periods=82, freq="D"),
            "deliv_pct": [20.0] * 60 + [30.0] * 21 + [latest],
        }
    )


def test_structure_tag_joins_active_flags_only():
    row = {"absorption_day": True, "failed_breakdown_reclaim": False, "failed_breakout": True, "resistance_touches": 4}

    assert structure_tag(row) == "ABS TRAP R4"


def test_structure_tag_omits_resistance_below_threshold():
    row = {"resistance_touches": 2}

    assert structure_tag(row) == ""


def test_structure_tag_empty_when_no_flags():
    assert structure_tag({}) == ""


def test_build_markdown_includes_sector_and_structure_columns():
    rows = [
        {
            "symbol": "AAA", "ics": 91, "rating": "STRONG", "stage": "MARKUP", "delivery_tag": "",
            "rs_percentile": 100, "rs_trend": "UP", "cmf20": 0.1, "volume_ratio": 2.0, "turnover_cr": 12.3,
            "regime": "GREEN", "action_rank": "A", "action": "WATCH_FOR_ENTRY", "reason": "RS leader",
            "sector": "Banking and Finance", "sector_score": 67.0,
            "absorption_day": True, "resistance_touches": 3,
        },
    ]

    md = build_markdown(rows, "2026-07-07")

    assert "Sector" in md and "Structure" in md
    assert "Banking and Finance (67)" in md
    assert "ABS R3" in md


def test_build_html_includes_struct_div():
    rows = [
        {
            "symbol": "AAA", "ics": 91, "rating": "STRONG", "stage": "MARKUP", "delivery_tag": "",
            "action_rank": "A", "action": "WATCH_FOR_ENTRY", "reason": "Delivery P100",
            "sector": "IT", "sector_score": 80.0, "failed_breakdown_reclaim": True,
        },
    ]

    html = build_html(rows, "2026-07-07")

    assert 'class="struct"' in html
    assert "IT (80) · RECLAIM" in html


def test_absorption_day_true_on_narrow_range_high_delivery_upper_close():
    close = pd.Series([100.0] * 19 + [100.8])
    high = pd.Series([105.0] * 19 + [101.0])
    low = pd.Series([95.0] * 19 + [100.0])

    assert absorption_day(high, low, close, delivery_ratio=2.0) is True


def test_absorption_day_false_when_delivery_not_elevated():
    close = pd.Series([100.0] * 19 + [100.8])
    high = pd.Series([105.0] * 19 + [101.0])
    low = pd.Series([95.0] * 19 + [100.0])

    assert absorption_day(high, low, close, delivery_ratio=1.0) is False


def test_failed_breakdown_reclaim_true_when_support_broke_recovered_on_volume():
    close = pd.Series([100.0] * 20 + [100.0, 90.0, 105.0])
    low = pd.Series([99.0] * 20 + [99.0, 85.0, 104.0])

    assert failed_breakdown_reclaim(close, low, volume_ratio=1.5) is True


def test_failed_breakdown_reclaim_false_without_recovery():
    close = pd.Series([100.0] * 20 + [100.0, 90.0, 88.0])
    low = pd.Series([99.0] * 20 + [99.0, 85.0, 84.0])

    assert failed_breakdown_reclaim(close, low, volume_ratio=1.5) is False


def test_failed_breakdown_reclaim_false_without_volume_confirmation():
    close = pd.Series([100.0] * 20 + [100.0, 90.0, 105.0])
    low = pd.Series([99.0] * 20 + [99.0, 85.0, 104.0])

    assert failed_breakdown_reclaim(close, low, volume_ratio=1.0) is False


def test_failed_breakout_true_on_broken_resistance_with_long_wick():
    close = pd.Series([100.0] * 20 + [110.0, 108.0])
    high = pd.Series([101.0] * 20 + [111.0, 113.0])
    low = pd.Series([99.0] * 20 + [99.0, 104.0])

    assert failed_breakout(close, high, low, volume_ratio=2.0) is True


def test_failed_breakout_false_when_volume_not_elevated():
    close = pd.Series([100.0] * 20 + [110.0, 108.0])
    high = pd.Series([101.0] * 20 + [111.0, 113.0])
    low = pd.Series([99.0] * 20 + [99.0, 104.0])

    assert failed_breakout(close, high, low, volume_ratio=1.0) is False


def test_resistance_touch_count_counts_closes_near_60d_high():
    close = pd.Series([100.0] * 80)

    assert resistance_touch_count(close) == 20


def test_resistance_touch_count_zero_with_insufficient_history():
    close = pd.Series([100.0] * 40)

    assert resistance_touch_count(close) == 0


def test_analyse_symbol_exposes_todays_ohlc():
    df = _ohlc()
    row = analyse_symbol("AAA", df, _ohlc(-10), _delivery())

    assert row["open"] == pytest.approx(float(df["open"].iloc[-1]))
    assert row["high"] == pytest.approx(float(df["high"].iloc[-1]))
    assert row["low"] == pytest.approx(float(df["low"].iloc[-1]))


def test_run_scores_injected_universe_and_sorts_by_ics():
    universe = pd.DataFrame({"symbol": ["AAA", "BBB"]})
    rows = run(
        universe,
        "2026-07-07",
        ohlc_map={"AAA": _ohlc(10), "BBB": _ohlc(0)},
        delivery_map={"AAA": _delivery(60), "BBB": _delivery(25)},
        bench_df=_ohlc(-10),
        regime_info={"regime": "GREEN", "max_slots": 6, "time_stop_mode": "standard"},
    )

    assert rows["symbol"].tolist()[0] == "AAA"
    assert set(["ics", "rating", "stage", "delivery_tag", "regime", "action_rank", "action", "reason"]).issubset(rows.columns)
    assert rows["ics"].between(0, 100).all()
    assert rows.iloc[0]["delivery_tag"].startswith("DEL60%")
    assert rows.iloc[0]["regime"] == "GREEN"


def test_run_uses_sector_from_universe_df_when_present():
    universe = pd.DataFrame({"symbol": ["AAA", "BBB"], "sector": ["Banking", "IT"]})
    rows = run(
        universe,
        "2026-07-07",
        ohlc_map={"AAA": _ohlc(10), "BBB": _ohlc(0)},
        delivery_map={"AAA": _delivery(60), "BBB": _delivery(25)},
        bench_df=_ohlc(-10),
        regime_info={"regime": "GREEN", "max_slots": 6, "time_stop_mode": "standard"},
    )

    assert set(rows["sector"]) == {"Banking", "IT"}
    assert "UNKNOWN" not in rows["sector"].tolist()


def test_build_markdown_includes_disclaimer_and_ranked_rows():
    rows = [
        {"symbol": "AAA", "ics": 91, "rating": "STRONG", "stage": "MARKUP", "delivery_tag": "DEL60% P100", "rs_percentile": 100, "rs_trend": "UP", "cmf20": 0.1, "volume_ratio": 2.0, "turnover_cr": 12.3, "regime": "GREEN", "action_rank": "A", "action": "WATCH_FOR_ENTRY", "reason": "Delivery P100"},
    ]

    md = build_markdown(rows, "2026-07-07")

    assert "SEBI registered" in md
    assert "Institutional Footprint Scan" in md
    assert "AAA" in md
    assert "DEL60% P100" in md


def test_build_markdown_sorts_by_action_rank_before_ics():
    rows = [
        {"symbol": "BBB", "ics": 94, "rating": "STRONG", "stage": "MARKUP", "delivery_tag": "", "rs_percentile": 90, "rs_trend": "UP", "cmf20": 0.1, "volume_ratio": 1.5, "turnover_cr": 10, "regime": "GREEN", "action_rank": "B", "action": "WATCH_FOR_ENTRY", "reason": "RS leader"},
        {"symbol": "AAA", "ics": 86, "rating": "STRONG", "stage": "BREAKOUT", "delivery_tag": "", "rs_percentile": 91, "rs_trend": "UP", "cmf20": 0.1, "volume_ratio": 1.6, "turnover_cr": 10, "regime": "GREEN", "action_rank": "A", "action": "WATCH_FOR_ENTRY", "reason": "RS leader"},
    ]

    md = build_markdown(rows, "2026-07-07")

    assert md.index("AAA") < md.index("BBB")


def test_build_markdown_merges_reason_and_delivery_after_symbol():
    rows = [
        {"symbol": "AAA", "ics": 91, "rating": "STRONG", "stage": "MARKUP", "delivery_tag": "DEL60% P100", "rs_percentile": 100, "rs_trend": "UP", "cmf20": 0.1, "volume_ratio": 2.0, "turnover_cr": 12.3, "regime": "GREEN", "action_rank": "A", "action": "WATCH_FOR_ENTRY", "reason": "Delivery P100"},
    ]

    md = build_markdown(rows, "2026-07-07")

    header = next(line for line in md.splitlines() if line.startswith("| Symbol"))
    assert header.split("|")[1:3] == [" Symbol ", " Reason / Delivery "]
    assert "Delivery P100 · DEL60% P100" in md


def test_build_markdown_handles_nan_delivery_tag_from_csv_reload():
    rows = pd.DataFrame(
        [
            {"symbol": "AAA", "ics": 91, "rating": "STRONG", "stage": "MARKUP", "delivery_tag": float("nan"), "rs_percentile": 100, "rs_trend": "UP", "cmf20": 0.1, "volume_ratio": 2.0, "turnover_cr": 12.3, "regime": "GREEN", "action_rank": "A", "action": "WATCH_FOR_ENTRY", "reason": "RS leader"},
        ]
    )

    md = build_markdown(rows, "2026-07-07")

    assert "RS leader |" in md
    assert "nan" not in md


def test_build_markdown_omits_ignore_rows_by_default():
    rows = [
        {"symbol": "AAA", "ics": 56, "rating": "WATCH", "stage": "NONE", "delivery_tag": "", "rs_percentile": 50, "rs_trend": "UP", "cmf20": 0.1, "volume_ratio": 1.2, "turnover_cr": 10, "regime": "GREEN", "action_rank": "C", "action": "WATCHLIST", "reason": "CMF positive"},
        {"symbol": "BBB", "ics": 20, "rating": "IGNORE", "stage": "NONE", "delivery_tag": "", "rs_percentile": 1, "rs_trend": "FLAT", "cmf20": -0.1, "volume_ratio": 0.5, "turnover_cr": 1, "regime": "GREEN", "action_rank": "C", "action": "IGNORE", "reason": "No standout factor"},
    ]

    md = build_markdown(rows, "2026-07-07")

    assert "AAA" in md
    assert "BBB" not in md


def test_build_html_includes_disclaimer_and_symbol():
    rows = [
        {"symbol": "AAA", "ics": 91, "rating": "STRONG", "stage": "MARKUP", "delivery_tag": "DEL60% P100", "action_rank": "A", "action": "WATCH_FOR_ENTRY", "reason": "Delivery P100"},
    ]

    html = build_html(rows, "2026-07-07")

    assert "SEBI registered" in html
    assert "AAA" in html
    assert "DEL60% P100" in html


def test_build_html_shows_no_signals_when_empty():
    html = build_html([], "2026-07-07")

    assert "No signals." in html


def test_assign_trade_action_blocks_deployment_in_red_regime():
    row = {"ics": 91, "rating": "STRONG", "stage": "BREAKOUT", "rs_percentile": 95, "delivery_ratio": 1.6, "volume_ratio": 2.0}

    assert assign_trade_action(row, "RED") == ("A", "NO_DEPLOY")


def test_assign_trade_action_green_promotes_strong_near_trigger():
    row = {"ics": 88, "rating": "STRONG", "stage": "BREAKOUT", "rs_percentile": 95, "delivery_ratio": 1.6, "volume_ratio": 2.0}

    assert assign_trade_action(row, "GREEN") == ("A", "WATCH_FOR_ENTRY")


def test_assign_trade_action_neutral_waits_for_non_a_setup():
    row = {"ics": 74, "rating": "BUILDING", "stage": "NONE", "rs_percentile": 80, "delivery_ratio": 1.1, "volume_ratio": 1.2}

    assert assign_trade_action(row, "NEUTRAL") == ("B", "WAIT")
