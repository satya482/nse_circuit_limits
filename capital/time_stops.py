"""Entry trigger, time-stop ladder, opportunity-cost monitor (Sec 6). Pure
functions over explicit inputs -- no position tracking/persistence here;
callers (Task 4 / a future live-position tracker) own state."""

RISK_AMOUNT_DEFAULT = 15_000
STOP_ATR_MULT = 1.5
BREAKOUT_VOL_MULT = 2.0
BAR5_MIN_PNL_PCT = 4.0
OPPORTUNITY_COST_GAP_PCT = 3.0


def entry_trigger(
    close: float, range_high: float, volume: float, vol_ma50: float,
    deliv_today: float, deliv_baseline: float,
) -> bool:
    """Sec 6 breakout trigger: close above range high, volume >= 2x vol_ma50,
    delivery % >= baseline (churn filter -- rejects low-delivery breakouts)."""
    return (
        close > range_high
        and volume >= BREAKOUT_VOL_MULT * vol_ma50
        and deliv_today >= deliv_baseline
    )


def stop_price(breakout_low: float, entry_price: float, atr: float) -> float:
    """Stop = low of breakout bar, capped at 1.5x ATR from entry (spec: 'low of
    breakout bar, max 1.5x ATR'). Whichever is TIGHTER (higher) wins, since the
    ATR cap exists to stop losses from cutting too deep."""
    atr_floor = entry_price - STOP_ATR_MULT * atr
    return round(max(breakout_low, atr_floor), 4)


def position_size(entry_price: float, stop_price: float, risk_amount: float = RISK_AMOUNT_DEFAULT) -> int:
    """Fixed-rupee risk sizing (spec: 'Fixed Rs 15,000 risk sizing'). Floors to
    whole shares; 0 if there's no risk-per-share (degenerate stop == entry)."""
    risk_per_share = entry_price - stop_price
    if risk_per_share <= 0:
        return 0
    return int(risk_amount // risk_per_share)


def time_stop_check(
    bars_since_entry: int, close: float, range_high: float, entry_price: float,
    pnl_pct: float, ema_fanout: bool,
) -> str | None:
    """Sec 6 hard time-stop ladder, evaluated on the bar it applies to (bar 3,
    5, or 10 counted from entry). Returns the exit reason or None (hold)."""
    if bars_since_entry == 3:
        if close <= range_high:
            return "EXIT_FAILED_BREAKOUT"
    elif bars_since_entry == 5:
        if pnl_pct < BAR5_MIN_PNL_PCT:
            return "EXIT_LOW_PNL"
    elif bars_since_entry == 10:
        if not ema_fanout:
            return "EXIT_NO_TREND_HALF"
    return None


def opportunity_cost_flags(
    position_return: float, benchmark_return: float, tier1_hot_count: int, stalled: bool = False,
) -> list[str]:
    """Sec 6 opportunity-cost monitor. UNDERPERFORMING checked before
    ROTATE_CAPITAL -- a position lagging the benchmark by 3%+ is the more
    specific/urgent flag; ROTATE_CAPITAL only applies when it's merely stalled
    (not underperforming) while better candidates queue up."""
    if position_return < benchmark_return - OPPORTUNITY_COST_GAP_PCT:
        return ["UNDERPERFORMING"]
    if stalled and tier1_hot_count >= 2:
        return ["ROTATE_CAPITAL"]
    return []
