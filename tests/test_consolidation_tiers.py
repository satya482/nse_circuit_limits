import pandas as pd
from consolidation import tiers, indicators


def _gated_df(n: int) -> pd.DataFrame:
    """Flat series that passes both gates for its full length -- gives a
    predictable consolidation_age == n (or n-1 accounting for warmup NaNs)."""
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": [100.0] * n, "high": [100.5] * n,
        "low": [99.5] * n, "close": [100.0] * n,
        "volume": [1_000_000.0] * n,
    })
    df = indicators.ema_compression(df)
    df = indicators.bollinger_keltner(df)
    df = indicators.volume_exhaustion(df)
    return df


def test_tier_hot_on_high_quality_high_imminence():
    assert tiers.tier(quality=75, imminence=65) == "TIER_1_HOT"


def test_tier_warm_on_high_quality_mid_imminence():
    assert tiers.tier(quality=80, imminence=45) == "TIER_2_WARM"


def test_tier_cold_on_high_quality_low_imminence():
    assert tiers.tier(quality=90, imminence=10) == "TIER_3_COLD"


def test_tier_none_below_quality_floor():
    assert tiers.tier(quality=50, imminence=90) == "NONE"


def test_consolidation_age_counts_consecutive_gated_bars():
    df = _gated_df(300)
    age = tiers.consolidation_age(df)
    assert age > indicators.EMA_MIN_BARS


def test_consolidation_age_zero_when_gate_breaks_today():
    df = _gated_df(300)
    df.loc[df.index[-1], "squeeze_on"] = False
    assert tiers.consolidation_age(df) == 0


def test_cmf_negative_streak_counts_tail_bars_below_threshold():
    s = pd.Series([0.1, 0.1, -0.06, -0.07, -0.08])
    assert tiers.cmf_negative_streak(s, threshold=-0.05) == 3


def test_quality_peak_drawdown_zero_on_stable_flat_series():
    """A perfectly flat series has the same quality score at every bar in the
    window -- peak equals today's score, drawdown is 0."""
    df = _gated_df(300)
    drawdown = tiers.quality_peak_drawdown(
        df, age_bars=100, rs_char="CHAR_4_RISING", cmf=0.15, deliv_trend_label="RISING",
    )
    assert drawdown == 0.0


def test_quality_peak_drawdown_positive_when_recent_bars_diverge():
    """Widen bb_width_percentile on the last 5 bars only (simulating a recent
    quality decline from an earlier peak) -- drawdown must be positive."""
    df = _gated_df(300)
    df.loc[df.index[-5:], "bb_width_percentile"] = 50.0
    drawdown = tiers.quality_peak_drawdown(
        df, age_bars=100, rs_char="CHAR_4_RISING", cmf=0.15, deliv_trend_label="RISING",
    )
    assert drawdown > 0.0


def test_abandonment_reasons_flags_declining_rs_and_stale_age():
    reasons = tiers.abandonment_reasons(
        rs_char="CHAR_1_DECLINING", age_bars=130, volume_rising=False,
        cmf=0.02, cmf_days_negative=0, quality_drawdown=5.0,
    )
    assert "RS_CHARACTER_DROPPED" in reasons
    assert "STALE_AGE" in reasons


def test_abandonment_reasons_empty_on_healthy_setup():
    reasons = tiers.abandonment_reasons(
        rs_char="CHAR_4_RISING", age_bars=30, volume_rising=False,
        cmf=0.08, cmf_days_negative=0, quality_drawdown=2.0,
    )
    assert reasons == []
