import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scanners.sma200_context import (
    sma200_band,
    sma200_roc_10d,
    sma200_slope_label,
    confirm_or_diverge,
    breadth_cross_tier,
    enrich_bull_crosses,
)


# ── sma200_band tests ────────────────────────────────────────────────────────


def test_sma200_band_overbought_peak_risk():
    """> 80% → overbought_peak_risk."""
    assert sma200_band(81.0) == "overbought_peak_risk"
    assert sma200_band(95.0) == "overbought_peak_risk"
    assert sma200_band(100.0) == "overbought_peak_risk"


def test_sma200_band_boundary_80_is_healthy_bull():
    """80% exactly → healthy_bull (not overbought, since boundary is > 80, not >= 80)."""
    assert sma200_band(80.0) == "healthy_bull"


def test_sma200_band_healthy_bull():
    """[50%, 80%] → healthy_bull."""
    assert sma200_band(50.0) == "healthy_bull"
    assert sma200_band(65.0) == "healthy_bull"
    assert sma200_band(79.9) == "healthy_bull"


def test_sma200_band_boundary_50_is_healthy_bull():
    """50% exactly → healthy_bull."""
    assert sma200_band(50.0) == "healthy_bull"


def test_sma200_band_weakening():
    """[20%, 50%) → weakening."""
    assert sma200_band(20.0) == "weakening"
    assert sma200_band(35.0) == "weakening"
    assert sma200_band(49.9) == "weakening"


def test_sma200_band_boundary_20_is_weakening():
    """20% exactly → weakening."""
    assert sma200_band(20.0) == "weakening"


def test_sma200_band_washout():
    """[15%, 20%) → washout."""
    assert sma200_band(15.0) == "washout"
    assert sma200_band(17.5) == "washout"
    assert sma200_band(19.9) == "washout"


def test_sma200_band_boundary_15_is_washout():
    """15% exactly → washout."""
    assert sma200_band(15.0) == "washout"


def test_sma200_band_extreme_bottom():
    """< 15% → extreme_bottom."""
    assert sma200_band(14.9) == "extreme_bottom"
    assert sma200_band(10.0) == "extreme_bottom"
    assert sma200_band(0.0) == "extreme_bottom"


def test_sma200_band_nan():
    """NaN input → NaN output."""
    result = sma200_band(float("nan"))
    assert pd.isna(result)


# ── sma200_roc_10d tests ─────────────────────────────────────────────────────


def test_sma200_roc_10d_basic():
    """Diff(10) produces NaN for first 10 values, then computes diff."""
    series = pd.Series(
        [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
    )
    roc = sma200_roc_10d(series)
    # First 10 should be NaN
    assert roc.iloc[:10].isna().all()
    # At index 10: 20.0 - 10.0 = 10.0
    assert roc.iloc[10] == 10.0


def test_sma200_roc_10d_negative_change():
    """Declining series produces negative ROC."""
    series = pd.Series([20.0] * 10 + [15.0])
    roc = sma200_roc_10d(series)
    # At index 10: 15.0 - 20.0 = -5.0
    assert roc.iloc[10] == -5.0


def test_sma200_roc_10d_empty_series():
    """Empty series returns empty result."""
    series = pd.Series([], dtype=float)
    roc = sma200_roc_10d(series)
    assert len(roc) == 0


def test_sma200_roc_10d_all_nan():
    """Series with all NaN produces all NaN."""
    series = pd.Series([float("nan")] * 15)
    roc = sma200_roc_10d(series)
    assert roc.isna().all()


# ── sma200_slope_label tests ────────────────────────────────────────────────


def test_sma200_slope_label_rising():
    """ROC > 1.0 → 'rising'."""
    assert sma200_slope_label(1.1) == "rising"
    assert sma200_slope_label(5.0) == "rising"
    assert sma200_slope_label(100.0) == "rising"


def test_sma200_slope_label_boundary_1_is_flat():
    """ROC = 1.0 exactly → 'flat' (not rising, since boundary is > 1.0)."""
    assert sma200_slope_label(1.0) == "flat"


def test_sma200_slope_label_flat():
    """ROC in [-1.0, +1.0] → 'flat'."""
    assert sma200_slope_label(0.0) == "flat"
    assert sma200_slope_label(0.5) == "flat"
    assert sma200_slope_label(-0.5) == "flat"
    assert sma200_slope_label(-1.0) == "flat"


def test_sma200_slope_label_falling():
    """ROC < -1.0 → 'falling'."""
    assert sma200_slope_label(-1.1) == "falling"
    assert sma200_slope_label(-5.0) == "falling"
    assert sma200_slope_label(-100.0) == "falling"


# ── confirm_or_diverge tests ─────────────────────────────────────────────────


def test_confirm_or_diverge_confirmed():
    """ROC > 1.0 → 'CONFIRMED'."""
    assert confirm_or_diverge(1.1) == "CONFIRMED"
    assert confirm_or_diverge(5.0) == "CONFIRMED"


def test_confirm_or_diverge_boundary_1_is_neutral():
    """ROC = 1.0 exactly → 'NEUTRAL'."""
    assert confirm_or_diverge(1.0) == "NEUTRAL"


def test_confirm_or_diverge_neutral():
    """ROC in [-1.0, +1.0] → 'NEUTRAL'."""
    assert confirm_or_diverge(0.0) == "NEUTRAL"
    assert confirm_or_diverge(0.5) == "NEUTRAL"
    assert confirm_or_diverge(-0.5) == "NEUTRAL"
    assert confirm_or_diverge(-1.0) == "NEUTRAL"


def test_confirm_or_diverge_divergent():
    """ROC < -1.0 → 'DIVERGENT'."""
    assert confirm_or_diverge(-1.1) == "DIVERGENT"
    assert confirm_or_diverge(-5.0) == "DIVERGENT"


def test_confirm_or_diverge_nan():
    """ROC = NaN → 'NEUTRAL' (NaN comparisons are all False)."""
    result = confirm_or_diverge(float("nan"))
    assert result == "NEUTRAL"


# ── breadth_cross_tier tests ─────────────────────────────────────────────────


def test_breadth_cross_tier_extreme_bottom_with_rising_roc():
    """extreme_bottom + ROC > 1.0 → Tier 1."""
    assert breadth_cross_tier("extreme_bottom", 1.5) == 1
    assert breadth_cross_tier("extreme_bottom", 5.0) == 1


def test_breadth_cross_tier_washout_with_rising_roc():
    """washout + ROC > 1.0 → Tier 1."""
    assert breadth_cross_tier("washout", 1.5) == 1
    assert breadth_cross_tier("washout", 10.0) == 1


def test_breadth_cross_tier_extreme_bottom_flat_or_falling():
    """extreme_bottom + ROC <= 1.0 → Tier 3 (default)."""
    assert breadth_cross_tier("extreme_bottom", 0.5) == 3
    assert breadth_cross_tier("extreme_bottom", -2.0) == 3


def test_breadth_cross_tier_washout_flat_or_falling():
    """washout + ROC <= 1.0 → Tier 3 (default)."""
    assert breadth_cross_tier("washout", 0.5) == 3
    assert breadth_cross_tier("washout", -5.0) == 3


def test_breadth_cross_tier_weakening_with_rising_roc():
    """weakening + ROC > 1.0 → Tier 2."""
    assert breadth_cross_tier("weakening", 1.5) == 2
    assert breadth_cross_tier("weakening", 10.0) == 2


def test_breadth_cross_tier_weakening_flat_or_falling():
    """weakening + ROC <= 1.0 → Tier 3 (default)."""
    assert breadth_cross_tier("weakening", 0.5) == 3
    assert breadth_cross_tier("weakening", -5.0) == 3


def test_breadth_cross_tier_healthy_bull_any_roc():
    """healthy_bull + any ROC → Tier 3 (default)."""
    assert breadth_cross_tier("healthy_bull", 5.0) == 3
    assert breadth_cross_tier("healthy_bull", 0.0) == 3
    assert breadth_cross_tier("healthy_bull", -5.0) == 3


def test_breadth_cross_tier_overbought_peak_risk_any_roc():
    """overbought_peak_risk + any ROC → Tier 4 (caution)."""
    assert breadth_cross_tier("overbought_peak_risk", 5.0) == 4
    assert breadth_cross_tier("overbought_peak_risk", 0.0) == 4
    assert breadth_cross_tier("overbought_peak_risk", -5.0) == 4


def test_breadth_cross_tier_nan_band():
    """NaN band → NaN tier."""
    result = breadth_cross_tier(float("nan"), 5.0)
    assert pd.isna(result)


def test_breadth_cross_tier_nan_roc():
    """NaN ROC → NaN tier."""
    result = breadth_cross_tier("healthy_bull", float("nan"))
    assert pd.isna(result)


# ── enrich_bull_crosses tests ────────────────────────────────────────────────


def test_enrich_bull_crosses_basic():
    """Enrich BULL_CROSS rows with SMA200 context columns."""
    wt_df = pd.DataFrame(
        {
            "date": ["2026-06-20", "2026-06-21", "2026-06-22"],
            "channel": ["fast", "fast", "slow"],
            "cross_type": ["BULL_CROSS", "NONE", "BULL_CROSS"],
            "wt1": [1.0, 2.0, 3.0],
            "wt2": [0.5, 1.5, 2.5],
        }
    )

    history_df = pd.DataFrame(
        {
            "date": [
                "2026-06-10",
                "2026-06-11",
                "2026-06-12",
                "2026-06-13",
                "2026-06-14",
                "2026-06-15",
                "2026-06-16",
                "2026-06-17",
                "2026-06-18",
                "2026-06-19",
                "2026-06-20",
                "2026-06-21",
                "2026-06-22",
            ],
            "pct_above_sma200": [
                50.0,
                51.0,
                52.0,
                53.0,
                54.0,
                55.0,
                56.0,
                57.0,
                58.0,
                59.0,
                60.0,
                65.0,
                70.0,
            ],
        }
    )

    result = enrich_bull_crosses(wt_df, history_df)

    # Only BULL_CROSS rows should be returned
    assert len(result) == 2
    assert list(result["cross_type"]) == ["BULL_CROSS", "BULL_CROSS"]
    assert list(result["date"]) == ["2026-06-20", "2026-06-22"]

    # Check for added columns
    assert "sma200_band" in result.columns
    assert "sma200_roc_10d" in result.columns
    assert "confirm_or_diverge" in result.columns
    assert "breadth_cross_tier" in result.columns

    # Check values for 2026-06-20: pct_above_sma200=60.0, ROC = 60.0 - 50.0 = 10.0
    row_20 = result[result["date"] == "2026-06-20"].iloc[0]
    assert row_20["sma200_band"] == "healthy_bull"  # 60% → [50,80]
    assert row_20["sma200_roc_10d"] == 10.0
    assert row_20["confirm_or_diverge"] == "CONFIRMED"  # ROC > 1.0
    assert row_20["breadth_cross_tier"] == 3  # healthy_bull → Tier 3

    # Check values for 2026-06-22: pct_above_sma200=70.0
    # ROC = diff(10) at index 12 = 70.0 - 52.0 (value at index 2) = 18.0
    row_22 = result[result["date"] == "2026-06-22"].iloc[0]
    assert row_22["sma200_band"] == "healthy_bull"  # 70% → [50,80]
    assert row_22["sma200_roc_10d"] == 18.0
    assert row_22["confirm_or_diverge"] == "CONFIRMED"
    assert row_22["breadth_cross_tier"] == 3


def test_enrich_bull_crosses_no_matching_rows():
    """No BULL_CROSS rows → return empty DataFrame with expected columns."""
    wt_df = pd.DataFrame(
        {
            "date": ["2026-06-20", "2026-06-21"],
            "channel": ["fast", "fast"],
            "cross_type": ["NONE", "BEAR_CROSS"],
            "wt1": [1.0, 2.0],
            "wt2": [0.5, 1.5],
        }
    )

    history_df = pd.DataFrame(
        {
            "date": ["2026-06-20", "2026-06-21"],
            "pct_above_sma200": [50.0, 55.0],
        }
    )

    result = enrich_bull_crosses(wt_df, history_df)

    assert len(result) == 0
    expected_cols = [
        "date",
        "channel",
        "cross_type",
        "wt1",
        "wt2",
        "sma200_band",
        "sma200_roc_10d",
        "confirm_or_diverge",
        "breadth_cross_tier",
    ]
    for col in expected_cols:
        assert col in result.columns


def test_enrich_bull_crosses_missing_history_date():
    """BULL_CROSS with missing date in history → NaN for context columns."""
    wt_df = pd.DataFrame(
        {
            "date": ["2026-06-20"],
            "channel": ["fast"],
            "cross_type": ["BULL_CROSS"],
            "wt1": [1.0],
            "wt2": [0.5],
        }
    )

    # history_df does not have 2026-06-20
    history_df = pd.DataFrame(
        {
            "date": ["2026-06-19", "2026-06-21"],
            "pct_above_sma200": [50.0, 55.0],
        }
    )

    result = enrich_bull_crosses(wt_df, history_df)

    assert len(result) == 1
    row = result.iloc[0]
    assert pd.isna(row["sma200_roc_10d"])
    assert pd.isna(row["sma200_band"])
    assert pd.isna(row["breadth_cross_tier"])
    # NaN comparisons are False, so confirm_or_diverge(NaN) → "NEUTRAL"
    assert row["confirm_or_diverge"] == "NEUTRAL"


def test_enrich_bull_crosses_multiple_channels():
    """Multiple channels on same date → both rows returned, sorted by channel."""
    wt_df = pd.DataFrame(
        {
            "date": ["2026-06-20", "2026-06-20"],
            "channel": ["slow", "fast"],  # reversed order
            "cross_type": ["BULL_CROSS", "BULL_CROSS"],
            "wt1": [1.0, 2.0],
            "wt2": [0.5, 1.5],
        }
    )

    history_df = pd.DataFrame(
        {
            "date": list(f"2026-06-{i:02d}" for i in range(10, 21)),
            "pct_above_sma200": list(range(50, 61)),
        }
    )

    result = enrich_bull_crosses(wt_df, history_df)

    assert len(result) == 2
    # Sorted by date, then channel
    assert result.iloc[0]["channel"] == "fast"
    assert result.iloc[1]["channel"] == "slow"


def test_enrich_bull_crosses_tier_1_signal():
    """Test a Tier 1 (extreme_bottom + rising) signal."""
    wt_df = pd.DataFrame(
        {
            "date": ["2026-06-20"],
            "channel": ["fast"],
            "cross_type": ["BULL_CROSS"],
            "wt1": [1.0],
            "wt2": [0.5],
        }
    )

    history_df = pd.DataFrame(
        {
            "date": list(f"2026-06-{i:02d}" for i in range(10, 21)),
            "pct_above_sma200": [
                12.0,
                12.5,
                13.0,
                13.5,
                14.0,
                14.5,
                15.0,
                18.0,
                22.0,
                25.0,
                28.0,
            ],
        }
    )

    result = enrich_bull_crosses(wt_df, history_df)

    row = result.iloc[0]
    # pct at 2026-06-20 is 28.0; ROC (diff from 2026-06-10) = 28.0 - 12.0 = 16.0
    assert row["sma200_band"] == "weakening"  # 28% → [20, 50)
    assert row["sma200_roc_10d"] == 16.0
    assert row["confirm_or_diverge"] == "CONFIRMED"
    # weakening + roc > 1.0 → Tier 2
    assert row["breadth_cross_tier"] == 2


def test_enrich_bull_crosses_tier_4_signal():
    """Test a Tier 4 (overbought_peak_risk) signal."""
    wt_df = pd.DataFrame(
        {
            "date": ["2026-06-20"],
            "channel": ["fast"],
            "cross_type": ["BULL_CROSS"],
            "wt1": [1.0],
            "wt2": [0.5],
        }
    )

    history_df = pd.DataFrame(
        {
            "date": list(f"2026-06-{i:02d}" for i in range(10, 21)),
            "pct_above_sma200": [
                90.0,
                91.0,
                92.0,
                93.0,
                94.0,
                95.0,
                96.0,
                97.0,
                98.0,
                99.0,
                99.5,
            ],
        }
    )

    result = enrich_bull_crosses(wt_df, history_df)

    row = result.iloc[0]
    # pct at 2026-06-20 is 99.5; ROC (diff from 2026-06-10) = 99.5 - 90.0 = 9.5
    assert row["sma200_band"] == "overbought_peak_risk"  # 99.5% > 80
    assert row["sma200_roc_10d"] == 9.5
    assert row["confirm_or_diverge"] == "CONFIRMED"
    # overbought_peak_risk → Tier 4 (regardless of ROC)
    assert row["breadth_cross_tier"] == 4


def test_enrich_bull_crosses_pct_above_sma200_column_removed():
    """The pct_above_sma200 column added during join should be removed from output."""
    wt_df = pd.DataFrame(
        {
            "date": ["2026-06-20"],
            "channel": ["fast"],
            "cross_type": ["BULL_CROSS"],
            "wt1": [1.0],
        }
    )

    history_df = pd.DataFrame(
        {
            "date": list(f"2026-06-{i:02d}" for i in range(10, 21)),
            "pct_above_sma200": list(range(50, 61)),
        }
    )

    result = enrich_bull_crosses(wt_df, history_df)

    # pct_above_sma200 should NOT be in output
    assert "pct_above_sma200" not in result.columns
