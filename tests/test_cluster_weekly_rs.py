import pandas as pd
import pytest

import sector_rotation_scanner as scanner


def bars(values, start='2026-08-07'):
    return pd.DataFrame({'date': pd.date_range(start, periods=len(values), freq='W-FRI'), 'close': values})


def test_weekly_rs_uses_ratio_ema_and_developing_week():
    stock = bars([100] * 9 + [120])
    bench = bars([1000] * 10)
    stock.loc[9, 'date'] -= pd.Timedelta(days=1)
    bench.loc[9, 'date'] -= pd.Timedelta(days=1)
    assert scanner.weekly_rs_above_ema9(stock, bench) is True
    assert scanner.weekly_rs_above_ema9(stock.iloc[:-1], bench.iloc[:-1]) is False
    expected = (stock['close'] / bench['close'] * 1000).ewm(span=9, adjust=False).mean().iloc[-1]
    assert expected == pytest.approx(104)
    assert scanner.weekly_rs_above_ema9(bars([120] * 9 + [100]), bars([1000] * 10)) is False


def test_rising_price_with_faster_benchmark_is_below_ema():
    assert scanner.weekly_rs_above_ema9(bars([100] * 9 + [110]), bars([1000] * 9 + [1300])) is False


def test_unavailable_weekly_histories():
    stock, bench = bars([100] * 10), bars([1000] * 10)
    assert scanner.weekly_rs_above_ema9(None, bench) is None
    assert scanner.weekly_rs_above_ema9(stock.iloc[:8], bench.iloc[:8]) is None
    assert scanner.weekly_rs_above_ema9(stock.iloc[:-1], bench) is None
    stock.loc[9, 'close'] = 0
    assert scanner.weekly_rs_above_ema9(stock, bench) is None


def test_mismatched_weekly_session_breaks_ema_history():
    stock, bench = bars([100] * 10), bars([1000] * 10)
    stock.loc[5, 'date'] -= pd.Timedelta(days=1)
    assert scanner.weekly_rs_above_ema9(stock, bench) is None


def test_invalid_last_daily_close_cannot_fall_back_to_previous_session():
    stock, bench = bars([100] * 10), bars([1000] * 10)
    earlier = stock.iloc[[-1]].copy()
    earlier['date'] -= pd.Timedelta(days=1)
    stock.loc[9, 'close'] = float('nan')
    stock = pd.concat([stock, earlier]).sort_values('date')
    assert scanner.weekly_rs_above_ema9(stock, bench) is None


def test_group_weekly_rs_evaluates_all_members_with_separate_unavailable():
    states = {'RISING': True, 'FALLING': True, 'BELOW': False, 'SHORT': None}
    summary = scanner.group_weekly_rs(['RISING', 'FALLING', 'BELOW', 'SHORT', 'MISSING'], states)
    assert summary == {'above': 2, 'evaluated': 3, 'unavailable': 2, 'pct': pytest.approx(200 / 3)}
