"""Imminence score (Sec 4): how close the spring is to releasing. Pre-break
signals ①-⑥ map to signal1..signal6 params in imminence_score()."""

import pandas as pd

_PREBREAK_MAX = 6.0


def spread_delta_crossover(spread_delta: pd.Series) -> bool:
    """Signal ②: spread_delta crosses positive (ta.crossover-equivalent, no float
    equality -- boundary via > / <=)."""
    if len(spread_delta) < 2:
        return False
    return bool(spread_delta.iloc[-1] > 0 and spread_delta.iloc[-2] <= 0)


def ema_stage3_flag(spread_delta: pd.Series) -> bool:
    """Sec 4 'EMA Stage 3 flag': spread_delta just crossed positive AFTER >= 10
    bars held negative (distinguishes a fresh, meaningful fanout from noise)."""
    if len(spread_delta) < 12:
        return False
    if not (spread_delta.iloc[-1] > 0 and spread_delta.iloc[-2] <= 0):
        return False
    count = 0
    for i in range(len(spread_delta) - 2, -1, -1):
        v = spread_delta.iloc[i]
        if pd.isna(v) or v > 0:
            break
        count += 1
    return count >= 10


def bb_breathing(bb_width_percentile: pd.Series) -> bool:
    """Sec 4 'BB breathing' / signal ④: bb_width_percentile ticks up 2 consecutive
    bars starting from below 15."""
    if len(bb_width_percentile) < 3:
        return False
    p0, p1, p2 = bb_width_percentile.iloc[-3:]
    if pd.isna(p0) or pd.isna(p1) or pd.isna(p2):
        return False
    return bool(p0 < 15 and p1 > p0 and p2 > p1)


def range_position(df: pd.DataFrame, age_bars: int) -> float:
    """0.0-1.0 position of today's close within the high/low range of the
    trailing max(age_bars, 10) bars."""
    window = df.iloc[-max(age_bars, 10):]
    hi, lo = window["high"].max(), window["low"].min()
    if hi == lo:
        return 0.0
    return float((df["close"].iloc[-1] - lo) / (hi - lo))


def higher_low(df: pd.DataFrame, window: int = 5) -> bool:
    """Signal ⑤: today's low exceeds the low of the prior `window` bars."""
    if len(df) < window + 1:
        return False
    low = df["low"].astype(float)
    today_low = low.iloc[-1]
    prior_low = low.iloc[-(window + 1):-1].min()
    return bool(today_low > prior_low)


def wick_rejection_absorbed(df: pd.DataFrame, age_bars: int) -> bool:
    """Signal ⑥: yesterday had a long upper wick near the range top, today closed
    back above/held yesterday's body top (rejection absorbed, not confirmed)."""
    if len(df) < 3:
        return False
    window = df.iloc[-max(age_bars, 10):]
    range_high = window["high"].max()
    prev = df.iloc[-2]
    today = df.iloc[-1]
    prev_body_top = max(prev["open"], prev["close"])
    prev_range = prev["high"] - prev["low"]
    if prev_range <= 0:
        return False
    prev_wick = prev["high"] - prev_body_top
    near_top = prev["high"] >= range_high * 0.98
    long_wick = prev_wick > prev_range * 0.3
    absorbed = today["close"] >= prev_body_top
    return bool(near_top and long_wick and absorbed)


def signal3_weight(quiet_accum_today: bool, deliv_spike_today: bool) -> float:
    """Signal ③: quiet accumulation bar, upgraded to full weight when delivery %
    also spiked that day (spec: 0.5 without delivery confirmation, 1.0 with)."""
    if not quiet_accum_today:
        return 0.0
    return 1.0 if deliv_spike_today else 0.5


def imminence_score(
    signal1: bool,
    signal2: bool,
    signal3_wt: float,
    signal4: bool,
    signal5: bool,
    signal6: bool,
    stage3_flag: bool,
    rs_breakout_flag: bool,
    bb_breathing_flag: bool,
    range_pos: float,
) -> tuple[float, float]:
    """Sec 4 table: pre-break count(30) + EMA stage3(25) + RS breakout(20) +
    BB breathing(15) + range position(10). Returns (score 0-100, prebreak_count 0-6)."""
    prebreak_count = (
        (1.0 if signal1 else 0.0)
        + (1.0 if signal2 else 0.0)
        + signal3_wt
        + (1.0 if signal4 else 0.0)
        + (1.0 if signal5 else 0.0)
        + (1.0 if signal6 else 0.0)
    )
    prebreak_pts = prebreak_count / _PREBREAK_MAX * 30
    stage3_pts = 25 if stage3_flag else 0
    rs_pts = 20 if rs_breakout_flag else 0
    bb_pts = 15 if bb_breathing_flag else 0
    range_pts = 10 if range_pos >= 2 / 3 else 0
    score = prebreak_pts + stage3_pts + rs_pts + bb_pts + range_pts
    return round(score, 1), round(prebreak_count, 1)
