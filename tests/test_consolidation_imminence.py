import pandas as pd
from consolidation import imminence


def _df(n: int, closes, highs=None, opens=None) -> pd.DataFrame:
    closes = list(closes)
    highs = list(highs) if highs is not None else [c * 1.01 for c in closes]
    opens = list(opens) if opens is not None else closes
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": opens, "high": highs,
        "low": [c * 0.99 for c in closes], "close": closes,
        "volume": [1_000_000.0] * n,
    })


def test_spread_delta_crossover_true_on_boundary_cross():
    s = pd.Series([-0.002, -0.001, 0.0, 0.001])
    assert imminence.spread_delta_crossover(s) is True


def test_spread_delta_crossover_false_when_already_positive():
    s = pd.Series([0.001, 0.002, 0.003, 0.004])
    assert imminence.spread_delta_crossover(s) is False


def test_ema_stage3_flag_requires_ten_prior_negative_bars():
    """11 negative bars + the crossing bar = 12 elements, the function's own
    minimum length (len < 12 short-circuits to False before the streak count
    even runs) -- 10 negative bars alone (11 elements) would fail on length,
    not on streak count, and wouldn't test the intended branch."""
    s = pd.Series([-0.001] * 11 + [0.001])
    assert imminence.ema_stage3_flag(s) is True
    # long enough to pass the length gate, but the negative streak right before
    # the cross is only 5 bars -- exercises the "streak < 10" rejection, not
    # just the length gate
    s_short_streak = pd.Series([0.002] * 6 + [-0.001] * 5 + [0.001])
    assert imminence.ema_stage3_flag(s_short_streak) is False


def test_bb_breathing_true_on_two_bar_tick_up_from_low_percentile():
    s = pd.Series([10.0, 11.0, 13.0])
    assert imminence.bb_breathing(s) is True


def test_bb_breathing_false_when_starting_above_threshold():
    s = pd.Series([20.0, 25.0, 30.0])
    assert imminence.bb_breathing(s) is False


def test_range_position_top_third_flag():
    n = 30
    closes = [100.0] * (n - 1) + [109.0]  # near the top of a 100-110 range
    df = _df(n, closes, highs=[110.0] * n)
    df.loc[df.index[:-1], "low"] = 95.0
    pos = imminence.range_position(df, age_bars=20)
    assert pos >= 2 / 3


def test_higher_low_true_when_todays_low_exceeds_prior_window_low():
    n = 10
    df = _df(n, [100.0] * n)
    df.loc[df.index[-6:-1], "low"] = 95.0
    df.loc[df.index[-1], "low"] = 98.0
    assert imminence.higher_low(df, window=5) is True


def test_wick_rejection_absorbed_true_on_long_upper_wick_reclaimed():
    """Yesterday spiked to the range top with a long upper wick (rejected),
    today closes back above yesterday's body top (absorbed, not confirmed)."""
    n = 20
    rows = []
    for _ in range(n - 2):
        rows.append({"open": 100.0, "high": 105.0, "low": 99.0, "close": 100.0})
    # yesterday: body_top=101, wick=110-101=9, range=110-99=11, wick/range=0.82>0.3
    rows.append({"open": 100.0, "high": 110.0, "low": 99.0, "close": 101.0})
    # today: closes 101.5 >= yesterday's body_top (101) -> absorbed
    rows.append({"open": 101.0, "high": 102.0, "low": 100.5, "close": 101.5})
    df = pd.DataFrame(rows)
    df["date"] = pd.date_range("2024-01-01", periods=n, freq="B")
    assert imminence.wick_rejection_absorbed(df, age_bars=20) is True


def test_wick_rejection_absorbed_false_when_not_reclaimed():
    n = 20
    rows = []
    for _ in range(n - 2):
        rows.append({"open": 100.0, "high": 105.0, "low": 99.0, "close": 100.0})
    rows.append({"open": 100.0, "high": 110.0, "low": 99.0, "close": 101.0})
    # today closes well below yesterday's body_top (101) -- not absorbed
    rows.append({"open": 100.0, "high": 100.5, "low": 98.0, "close": 98.5})
    df = pd.DataFrame(rows)
    df["date"] = pd.date_range("2024-01-01", periods=n, freq="B")
    assert imminence.wick_rejection_absorbed(df, age_bars=20) is False


def test_signal3_weight_full_on_spike_half_without():
    assert imminence.signal3_weight(quiet_accum_today=True, deliv_spike_today=True) == 1.0
    assert imminence.signal3_weight(quiet_accum_today=True, deliv_spike_today=False) == 0.5
    assert imminence.signal3_weight(quiet_accum_today=False, deliv_spike_today=True) == 0.0


def test_imminence_score_all_signals_firing_scores_100():
    score, count = imminence.imminence_score(
        signal1=True, signal2=True, signal3_wt=1.0, signal4=True,
        signal5=True, signal6=True, stage3_flag=True,
        rs_breakout_flag=True, bb_breathing_flag=True, range_pos=0.9,
    )
    assert score == 100.0
    assert count == 6.0


def test_imminence_score_nothing_firing_scores_zero():
    score, count = imminence.imminence_score(
        signal1=False, signal2=False, signal3_wt=0.0, signal4=False,
        signal5=False, signal6=False, stage3_flag=False,
        rs_breakout_flag=False, bb_breathing_flag=False, range_pos=0.1,
    )
    assert score == 0.0
    assert count == 0.0
