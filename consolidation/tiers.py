"""Tier labelling (Sec 5) + stateless consolidation_age / quality-peak-drawdown /
abandonment checks -- no persisted state, no DB. Age and peak are derived by
backward-scanning the historical OHLCV already loaded for today's indicator
calcs, the same 'bars-ago scan' idiom ohlc_db.cmf_days()/zl25_stats() use."""

import pandas as pd

from consolidation import indicators, quality

MAX_AGE_STALE = 120


def tier(quality: float, imminence: float) -> str:
    if quality < 70:
        return "NONE"
    if imminence >= 60:
        return "TIER_1_HOT"
    if imminence >= 30:
        return "TIER_2_WARM"
    return "TIER_3_COLD"


def consolidation_age(df: pd.DataFrame) -> int:
    """Consecutive tail bars where EMA dual gate AND squeeze gate both held
    (2-gate definition per user decision -- not the spec's ambiguous '4 gates').
    df must already have spread_atr_ratio, spread_pct, squeeze_on,
    bb_width_percentile columns (ema_compression() + bollinger_keltner() applied)."""
    ema_ok = (df["spread_atr_ratio"] < indicators.EMA_ATR_GATE) & (
        df["spread_pct"] < indicators.EMA_PCT_GATE
    )
    sq_ok = df["squeeze_on"] & (df["bb_width_percentile"] <= indicators.BB_WIDTH_PCT_MAX)
    combined = (ema_ok & sq_ok).fillna(False)
    count = 0
    for i in range(len(combined) - 1, -1, -1):
        if bool(combined.iloc[i]):
            count += 1
        else:
            break
    return count


def cmf_negative_streak(cmf_vals: pd.Series, threshold: float = -0.05) -> int:
    count = 0
    for i in range(len(cmf_vals) - 1, -1, -1):
        if cmf_vals.iloc[i] < threshold:
            count += 1
        else:
            break
    return count


def quality_peak_drawdown(
    df: pd.DataFrame,
    age_bars: int,
    rs_char: str,
    cmf: float,
    deliv_trend_label: str | None,
) -> float:
    """Points quality has fallen from its peak over the trailing
    min(age_bars, MAX_AGE_STALE) window.
    ponytail: rs_char / cmf / deliv_trend are held constant at today's value
    across the window -- only BB/EMA/vol components vary bar-to-bar (those are
    already full per-bar Series; re-classifying RS/CMF/delivery at every
    historical bar would need a much heavier per-bar resample loop for an
    abandonment check only). Revisit if this misfires in the Phase 7 backtest."""
    window = min(age_bars, MAX_AGE_STALE, len(df))
    if window < 2:
        return 0.0
    tail = df.iloc[-window:]
    scores = []
    for i in range(len(tail)):
        row = tail.iloc[i]
        bb_pct = row.get("bb_width_percentile")
        vol_pct = row.get("vol_percentile")
        if pd.isna(bb_pct) or pd.isna(vol_pct):
            continue
        stage = indicators.ema_stage(row.get("spread_delta"))
        scores.append(
            quality.quality_score(
                float(bb_pct), stage, float(vol_pct), rs_char, cmf, deliv_trend_label
            )
        )
    if not scores:
        return 0.0
    return round(max(scores) - scores[-1], 1)


def abandonment_reasons(
    rs_char: str,
    age_bars: int,
    volume_rising: bool,
    cmf: float,
    cmf_days_negative: int,
    quality_drawdown: float,
) -> list[str]:
    """Sec 5 abandonment triggers. Sector RS breakdown is not implemented here
    (needs a sector universe this scanner doesn't have) -- out of scope for v1."""
    reasons = []
    if rs_char in ("CHAR_1_DECLINING", "CHAR_2_FLAT"):
        reasons.append("RS_CHARACTER_DROPPED")
    if age_bars > MAX_AGE_STALE:
        reasons.append("STALE_AGE")
    if volume_rising:
        reasons.append("VOLUME_PHASE_REVERSED")
    if cmf < -0.05 and cmf_days_negative >= 5:
        reasons.append("CMF_DISTRIBUTION")
    if quality_drawdown >= 15:
        reasons.append("QUALITY_DRAWDOWN")
    return reasons
