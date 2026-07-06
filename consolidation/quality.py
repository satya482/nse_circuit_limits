"""Quality score (Sec 3): how good a spring this consolidation is. Fixed weights
against absolute thresholds -- NOT normalized across today's candidate set, so a
score is comparable day-over-day (needed for stable tier thresholds)."""

import pandas as pd

import ohlc_db

DELIV_MA_WINDOW = 20
DELIV_BASELINE_WINDOW = 120
DELIV_RISING_MULT = 1.15
DELIV_BELOW_MULT = 0.85

_EMA_STAGE_PTS = {"STAGE_1_CONVERGING": 8, "STAGE_2_COMPRESSED": 20, "STAGE_3_DIVERGING": 0}
_RS_CHAR_PTS = {
    "CHAR_1_DECLINING": 0, "CHAR_2_FLAT": 5, "CHAR_3_HOLDING": 12,
    "CHAR_4_RISING": 20, "CHAR_5_RS_BREAKOUT": 20,
}
_DELIV_TREND_PTS = {"RISING": 10, "AT_BASELINE": 5, "BELOW": 0}


def deliv_trend(symbol: str, db_path=ohlc_db.DB_PATH) -> str | None:
    """RISING / AT_BASELINE / BELOW per spec Sec 2.6. None if insufficient delivery
    history (< DELIV_BASELINE_WINDOW days). The AT_BASELINE band (0.85x-1.15x) is a
    first-pass interpretation -- spec only defines the RISING threshold explicitly;
    unvalidated, Sec 14 backtest territory."""
    df = ohlc_db.load_delivery(symbol, lookback=DELIV_BASELINE_WINDOW, db_path=db_path)
    if df is None or len(df) < DELIV_BASELINE_WINDOW:
        return None
    pct = df["deliv_pct"].astype(float)
    deliv_ma20 = pct.iloc[-DELIV_MA_WINDOW:].mean()
    deliv_baseline = pct.median()
    if deliv_baseline == 0:
        return None
    ratio = deliv_ma20 / deliv_baseline
    if ratio > DELIV_RISING_MULT:
        return "RISING"
    if ratio < DELIV_BELOW_MULT:
        return "BELOW"
    return "AT_BASELINE"


def quality_score(
    bb_width_percentile: float,
    ema_stage: str,
    vol_percentile: float,
    rs_char: str,
    cmf: float,
    deliv_trend_label: str | None,
) -> float:
    """Sec 3 table, full 100 pts: BB depth(20) + EMA stage(20) + vol exhaustion(15)
    + RS character(20) + CMF(15) + delivery trend(10)."""
    bb_pts = max(0.0, (20 - bb_width_percentile) * 1.0)
    stage_pts = _EMA_STAGE_PTS[ema_stage]
    vol_pts = max(0.0, (20 - vol_percentile) * 0.75)
    rs_pts = _RS_CHAR_PTS[rs_char]
    cmf_pts = 15 if cmf > 0.10 else (10 if cmf > 0.05 else (6 if cmf > 0 else 0))
    deliv_pts = _DELIV_TREND_PTS.get(deliv_trend_label, 0)
    return round(bb_pts + stage_pts + vol_pts + rs_pts + cmf_pts + deliv_pts, 1)
