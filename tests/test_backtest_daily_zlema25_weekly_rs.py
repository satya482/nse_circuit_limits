import pandas as pd
import pytest
from pandas.testing import assert_series_equal

import backtest_daily_zlema25_weekly_rs as m


def _ohlc(closes, start="2024-01-01"):
    dates = pd.bdate_range(start, periods=len(closes))
    return pd.DataFrame({"date": dates, "close": closes})


def test_zlema_matches_double_ema_formula():
    close = pd.Series([100.0 + i for i in range(40)])
    ema = close.ewm(span=25, adjust=False).mean()
    expected = 2 * ema - ema.ewm(span=25, adjust=False).mean()
    assert_series_equal(m.zlema(close), expected)


def test_weekly_rs_ema_does_not_look_ahead_within_week():
    stock = _ohlc([100.0 + i for i in range(70)])
    bench = _ohlc([200.0 + i * 0.2 for i in range(70)])
    cutoff = stock.loc[62, "date"]
    early = m.build_indicator_frame(stock.iloc[:63], bench.iloc[:63])
    full = m.build_indicator_frame(stock, bench)
    cols = ["weekly_rs_ema9", "prior_week_rs_ema9", "rs_ema9_rising"]
    pd.testing.assert_frame_equal(
        early.set_index("date")[cols],
        full.loc[full["date"] <= cutoff].set_index("date")[cols],
    )


def test_entry_signal_requires_all_four_conditions():
    stock = _ohlc([100 + i * 0.2 + (2 if i % 9 == 0 else 0) for i in range(90)])
    bench = _ohlc([200 + i * 0.05 for i in range(90)])
    frame = m.build_indicator_frame(stock, bench)
    expected = (
        (frame["zlema25"] > frame["zlema25"].shift(1))
        & (frame["zlema25"].shift(1) <= frame["zlema25"].shift(2))
        & frame["rs_above_ema9"]
        & frame["rs_ema9_rising"]
        & (frame.index >= 24)
    )
    pd.testing.assert_series_equal(frame["entry_signal"], expected, check_names=False)


def _signal_frame():
    dates = pd.bdate_range("2024-03-01", periods=6)
    return pd.DataFrame(
        {
            "date": dates,
            "close": [100.0, 102.0, 105.0, 104.0, 103.0, 106.0],
            "zlema25": [100.0, 99.0, 100.0, 101.0, 100.5, 101.0],
            "rs_ema9_rising": [True, True, True, True, True, False],
            "entry_signal": [False, False, True, False, False, False],
        }
    )


def test_simulation_exits_on_first_zlema_down_close():
    completed, opened = m.simulate_stock(
        "TEST",
        _signal_frame(),
        pd.Timestamp("2024-03-01"),
        pd.Timestamp("2024-03-31"),
    )
    assert opened.empty
    trade = completed.iloc[0]
    assert trade["entry_close"] == 105.0
    assert trade["exit_close"] == 103.0
    assert trade["exit_reason"] == "ZLEMA_DOWN"
    assert trade["holding_trading_days"] == 2


def test_open_trade_is_not_in_completed_trades():
    frame = _signal_frame().iloc[:4].copy()
    completed, opened = m.simulate_stock(
        "TEST", frame, pd.Timestamp("2024-03-01"), pd.Timestamp("2024-03-31")
    )
    assert completed.empty
    assert len(opened) == 1


def test_simulation_records_rs_only_and_combined_exit_reasons():
    rs_only = _signal_frame()
    rs_only.loc[3, "rs_ema9_rising"] = False
    completed, _ = m.simulate_stock(
        "TEST", rs_only, pd.Timestamp("2024-03-01"), pd.Timestamp("2024-03-31")
    )
    assert completed.iloc[0]["exit_reason"] == "RS_NOT_RISING"

    combined = _signal_frame()
    combined.loc[3, "zlema25"] = 99.0
    combined.loc[3, "rs_ema9_rising"] = False
    completed, _ = m.simulate_stock(
        "TEST", combined, pd.Timestamp("2024-03-01"), pd.Timestamp("2024-03-31")
    )
    assert completed.iloc[0]["exit_reason"] == "ZLEMA_AND_RS"


def test_summary_counts_wins_zeros_and_compounds():
    trades = pd.DataFrame(
        {
            "symbol": ["A", "A", "A"],
            "return_pct": [10.0, -5.0, 0.0],
            "holding_trading_days": [2, 4, 3],
        }
    )
    row = m.summarize_trades(trades, ["A"]).set_index("symbol").loc["A"]
    assert row["wins"] == 1
    assert row["losses"] == 1
    assert row["zeros"] == 1
    assert row["win_rate_pct"] == pytest.approx(100 / 3)
    assert row["compounded_return_pct"] == pytest.approx(4.5)
