from capital import time_stops as ts


def test_entry_trigger_all_conditions_met():
    assert ts.entry_trigger(
        close=105.0, range_high=100.0, volume=2_000_000, vol_ma50=1_000_000,
        deliv_today=18.0, deliv_baseline=15.0,
    ) is True


def test_entry_trigger_fails_below_range_high():
    assert ts.entry_trigger(
        close=99.0, range_high=100.0, volume=2_000_000, vol_ma50=1_000_000,
        deliv_today=18.0, deliv_baseline=15.0,
    ) is False


def test_entry_trigger_fails_low_volume():
    assert ts.entry_trigger(
        close=105.0, range_high=100.0, volume=1_500_000, vol_ma50=1_000_000,
        deliv_today=18.0, deliv_baseline=15.0,
    ) is False


def test_entry_trigger_fails_low_delivery_churn_filter():
    assert ts.entry_trigger(
        close=105.0, range_high=100.0, volume=2_000_000, vol_ma50=1_000_000,
        deliv_today=10.0, deliv_baseline=15.0,
    ) is False


def test_stop_price_uses_breakout_low_when_within_atr_cap():
    # breakout_low=98, entry=105, atr=3 -> max distance = 1.5*3=4.5 -> floor=100.5
    # breakout_low (98) is below the floor, so stop clamps to the floor
    assert ts.stop_price(breakout_low=98.0, entry_price=105.0, atr=3.0) == 100.5


def test_stop_price_uses_breakout_low_when_inside_atr_cap():
    # breakout_low=103, floor=100.5 -> breakout_low is above floor, use it directly
    assert ts.stop_price(breakout_low=103.0, entry_price=105.0, atr=3.0) == 103.0


def test_position_size_standard_risk():
    # risk 15000, entry 105, stop 100.5 -> risk/share=4.5 -> 3333 shares (floor)
    assert ts.position_size(entry_price=105.0, stop_price=100.5, risk_amount=15_000) == 3333


def test_position_size_zero_risk_per_share_returns_zero():
    assert ts.position_size(entry_price=105.0, stop_price=105.0, risk_amount=15_000) == 0


def test_time_stop_check_bar3_failed_breakout():
    assert ts.time_stop_check(
        bars_since_entry=3, close=99.0, range_high=100.0, entry_price=100.0,
        pnl_pct=-1.0, ema_fanout=True,
    ) == "EXIT_FAILED_BREAKOUT"


def test_time_stop_check_bar3_holds_inside_range_ok():
    assert ts.time_stop_check(
        bars_since_entry=3, close=101.0, range_high=100.0, entry_price=100.0,
        pnl_pct=1.0, ema_fanout=True,
    ) is None


def test_time_stop_check_bar5_low_pnl():
    assert ts.time_stop_check(
        bars_since_entry=5, close=102.0, range_high=100.0, entry_price=100.0,
        pnl_pct=2.0, ema_fanout=True,
    ) == "EXIT_LOW_PNL"


def test_time_stop_check_bar5_pnl_ok():
    assert ts.time_stop_check(
        bars_since_entry=5, close=105.0, range_high=100.0, entry_price=100.0,
        pnl_pct=5.0, ema_fanout=True,
    ) is None


def test_time_stop_check_bar10_no_fanout():
    assert ts.time_stop_check(
        bars_since_entry=10, close=106.0, range_high=100.0, entry_price=100.0,
        pnl_pct=6.0, ema_fanout=False,
    ) == "EXIT_NO_TREND_HALF"


def test_time_stop_check_bar10_fanout_ok():
    assert ts.time_stop_check(
        bars_since_entry=10, close=106.0, range_high=100.0, entry_price=100.0,
        pnl_pct=6.0, ema_fanout=True,
    ) is None


def test_time_stop_check_other_bar_no_rule():
    assert ts.time_stop_check(
        bars_since_entry=7, close=106.0, range_high=100.0, entry_price=100.0,
        pnl_pct=6.0, ema_fanout=False,
    ) is None


def test_opportunity_cost_flags_underperforming():
    flags = ts.opportunity_cost_flags(
        position_return=1.0, benchmark_return=5.0, tier1_hot_count=0,
    )
    assert flags == ["UNDERPERFORMING"]


def test_opportunity_cost_flags_rotate_capital():
    flags = ts.opportunity_cost_flags(
        position_return=4.0, benchmark_return=5.0, stalled=True, tier1_hot_count=2,
    )
    assert flags == ["ROTATE_CAPITAL"]


def test_opportunity_cost_flags_none():
    flags = ts.opportunity_cost_flags(
        position_return=6.0, benchmark_return=5.0, stalled=False, tier1_hot_count=0,
    )
    assert flags == []
