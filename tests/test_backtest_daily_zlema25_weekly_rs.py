import pandas as pd
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
