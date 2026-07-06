"""Market regime throttle (Sec 8). GREEN/NEUTRAL/RED classification off
data/breadth_history.csv (already written daily by scanners/breadth_monitor.py)
-- this module never touches ohlc_db or the Kite API, it only reads the
existing history CSV. No new persistence."""

import os

import pandas as pd

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_PATH = os.path.join(REPO_DIR, "data", "breadth_history.csv")

GREEN_RATIO_MIN = 1.6
GREEN_SMA200_LOW = 50.0
GREEN_SMA200_HIGH = 80.0
RED_RATIO_MAX = 0.6
RED_SMA200_LOW = 20.0

_REGIME_PARAMS = {
    "GREEN": {"max_slots": 6, "time_stop_mode": "standard"},
    "NEUTRAL": {"max_slots": 3, "time_stop_mode": "bar3_only"},
    "RED": {"max_slots": 0, "time_stop_mode": "halted"},
}


def classify_regime(ratio_5d: float, pct_above_sma200: float, sma200_falling: bool) -> str:
    """Sec 8 bands. GREEN checked first (healthy band), then RED (either low
    ratio_5d alone, or SMA200 below 20% AND falling), else NEUTRAL."""
    if ratio_5d >= GREEN_RATIO_MIN and GREEN_SMA200_LOW <= pct_above_sma200 <= GREEN_SMA200_HIGH:
        return "GREEN"
    if ratio_5d <= RED_RATIO_MAX or (pct_above_sma200 < RED_SMA200_LOW and sma200_falling):
        return "RED"
    return "NEUTRAL"


def sma200_falling(history_df: pd.DataFrame, universe_tag: str, as_of: str, lookback: int = 5) -> bool:
    """True if today's pct_above_sma200 is lower than it was `lookback` rows
    earlier for this universe_tag. False (not falling) if there isn't enough
    history -- the conservative default, same idiom as indicators.ema_stage's
    NaN handling."""
    rows = history_df[history_df["universe_tag"] == universe_tag].sort_values("date")
    rows = rows[rows["date"] <= as_of]
    if len(rows) <= lookback:
        return False
    today = float(rows["pct_above_sma200"].iloc[-1])
    earlier = float(rows["pct_above_sma200"].iloc[-1 - lookback])
    return today < earlier


def regime_for_date(as_of: str, universe_tag: str = "breadth_broad", history_path: str = HISTORY_PATH) -> dict:
    """Reads history_path, classifies as_of's regime. Defaults to NEUTRAL (the
    conservative middle band, not GREEN) if as_of has no row -- fail toward
    caution, not toward full deployment."""
    history_df = pd.read_csv(history_path, dtype={"date": str})
    rows = history_df[(history_df["universe_tag"] == universe_tag) & (history_df["date"] == as_of)]
    if rows.empty:
        regime = "NEUTRAL"
    else:
        row = rows.iloc[-1]
        falling = sma200_falling(history_df, universe_tag, as_of)
        regime = classify_regime(float(row["ratio_5d"]), float(row["pct_above_sma200"]), falling)
    return {"regime": regime, **_REGIME_PARAMS[regime]}
