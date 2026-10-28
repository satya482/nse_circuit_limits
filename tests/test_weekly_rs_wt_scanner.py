import json
import re

import numpy as np
import pandas as pd
import pytest

import weekly_rs_wt_scanner as scan


def daily(values, dates=None):
    values = np.asarray(values, dtype=float)
    return pd.DataFrame({'date': pd.bdate_range('2026-01-05', periods=len(values)) if dates is None else dates,
                         'open': values, 'high': values + 2, 'low': values - 2,
                         'close': values, 'volume': 1000})


def frames():
    stock = daily(np.linspace(100, 140, 200) + np.sin(np.arange(200) / 4) * 5)
    bench = daily(np.full(200, 1000))
    return stock, bench


def test_weekly_aggregation_includes_partial_week_and_actual_price_date():
    frame = daily(np.arange(1, 9) + 100)
    weekly = scan.to_weekly(frame)
    assert len(weekly) == 2
    assert weekly.iloc[0].open == 101
    assert weekly.iloc[0].close == 105
    assert weekly.iloc[0].high == 107
    assert weekly.iloc[0].volume == 5000
    assert weekly.iloc[-1].date == pd.Timestamp('2026-01-14')
    assert weekly.iloc[-1].close == 108
    assert weekly.iloc[-1].volume == 3000


def test_indicators_match_independent_weekly_formulas():
    stock, bench = frames()
    w, b = scan.to_weekly(stock), scan.to_weekly(bench)
    result = scan.weekly_indicators(w, b)
    rs = (w.close / b.close * 1000).ewm(span=21, adjust=False).mean()
    hlc3 = (w.high + w.low + w.close) / 3
    esa = hlc3.ewm(span=10, adjust=False).mean()
    deviation = (hlc3 - esa).abs().ewm(span=10, adjust=False).mean()
    wt = ((hlc3 - esa) / (0.015 * deviation)).mask(deviation.eq(0), 0).ewm(span=21, adjust=False).mean()
    assert result['rs_ema21'] == pytest.approx(rs.iloc[-1])
    assert result['rs_slope'] == pytest.approx(rs.iloc[-1] - rs.iloc[-2])
    assert result['wt1'] == pytest.approx(wt.iloc[-1])
    assert result['wt_slope'] == pytest.approx(wt.iloc[-1] - wt.iloc[-2])


@pytest.mark.parametrize('rs_now,rs_before,wt_now,wt_before,expected', [
    (10, 9, -38, -45, True), (10, 10, 1, 0, False),
    (10, 9, 1, 1, False), (10, 11, 3, 2, False),
    (10, 9, 1, 2, False), (float('nan'), 9, 1, 0, False)])
def test_gate_is_strict_slope_only(rs_now, rs_before, wt_now, wt_before, expected):
    assert scan.passes_gate(rs_now, rs_before, wt_now, wt_before) is expected


def test_short_history_and_stale_stocks_are_named():
    stock, bench = frames()
    selected, weekly, excluded, evaluated = scan.select_stocks(
        {'STALE': stock.iloc[:-1], 'SHORT': stock.tail(20), 'GAP': stock.drop(index=50), 'MISSING': None}, bench)
    assert not selected and not weekly and evaluated == 0
    assert 'latest' in excluded['STALE']
    assert '22' in excluded['SHORT']
    assert 'missing sessions' in excluded['GAP']
    assert 'missing' in excluded['MISSING']


def test_flat_history_is_valid_no_signal_not_total_data_failure():
    bench = daily([100] * 150)
    rows, weekly, excluded, evaluated = scan.select_stocks({'FLAT': bench}, bench)
    assert rows == [] and weekly == {} and excluded == {} and evaluated == 1


def test_below_high_below_daily_ema_and_negative_wt_recovery_can_qualify():
    values = np.r_[np.linspace(1000, 80, 120), np.linspace(80, 120, 30)]
    stock = daily(values)
    bench = daily(np.linspace(1000, 10, 150))
    rows, _, excluded, evaluated = scan.select_stocks({'RECOVERY': stock}, bench)
    assert evaluated == 1 and not excluded and len(rows) == 1
    assert rows[0]['wt1'] < 0 and rows[0]['wt_slope'] > 0
    assert stock.close.iloc[-1] < stock.close.ewm(span=200, adjust=False).mean().iloc[-1]
    assert stock.close.iloc[-1] < stock.high.max() * 0.7


def test_invalid_stock_prices_are_excluded():
    stock, bench = frames()
    stock.loc[20, 'high'] = float('inf')
    rows, _, excluded, evaluated = scan.select_stocks({'BAD': stock}, bench)
    assert not rows and evaluated == 0 and 'nonfinite' in excluded['BAD']


def test_chart_failure_preserves_both_outputs(tmp_path, monkeypatch):
    stock, bench = frames()
    stock.loc[195:, ['open', 'high', 'low', 'close']] += 40
    report, dashboard = tmp_path / 'report.md', tmp_path / 'dashboard.html'
    report.write_text('old report')
    dashboard.write_text('old html')
    monkeypatch.setattr(scan, 'build_chart_data', lambda *args, **kwargs: ([], 1))
    with pytest.raises(ValueError, match='chart generation'):
        scan.write_outputs({'A': ''}, {'A': stock, scan.BENCHMARK: bench},
                           report, dashboard, now=bench.date.iloc[-1])
    assert report.read_text() == 'old report' and dashboard.read_text() == 'old html'


def test_new_report_and_dashboard_include_same_qualifiers(tmp_path):
    stock, bench = frames()
    stock.loc[195:, ['open', 'high', 'low', 'close']] += 40
    report = tmp_path / 'report.md'
    dashboard = tmp_path / 'dashboard.html'
    records = scan.write_outputs({'UP': 'Test Industry'}, {'UP': stock, scan.BENCHMARK: bench},
                                 report, dashboard, now=bench.date.iloc[-1])
    assert len(records) == 1
    md, html = report.read_text(encoding='utf-8'), dashboard.read_text(encoding='utf-8')
    assert 'NSE:UP' in md
    assert 'SEBI registered' in md and 'SEBI registered' in html
    assert 'Test Industry' in html
    assert records[0]['rs_pane']['rs_ema21'][-1] > records[0]['rs_pane']['rs_ema21'][-2]
    assert records[0]['wt_pane']['wt1'][-1] > records[0]['wt_pane']['wt1'][-2]
    assert records[0]['bars'][-1][0] == str(stock.date.iloc[-1].date())
    assert 'interval=W' in html and 'wtPaneVisible' in html
    assert 'Price data: ' + str(stock.date.iloc[-1].date()) in html
    assert json.loads(re.search(r'const CHART_DATA = (.*?);', html).group(1)) == records


def test_valid_zero_signals_overwrites_old_outputs(tmp_path):
    bench = daily([100] * 150)
    report, dashboard = tmp_path / 'report.md', tmp_path / 'dashboard.html'
    report.write_text('old')
    records = scan.write_outputs({'FLAT': ''}, {'FLAT': bench, scan.BENCHMARK: bench},
                                 report, dashboard, now=bench.date.iloc[-1])
    assert not records
    assert 'Qualified: 0' in report.read_text(encoding='utf-8')
    assert 'const CHART_DATA = [];' in dashboard.read_text(encoding='utf-8')


@pytest.mark.parametrize('scenario', ['missing_benchmark', 'stale_benchmark', 'missing_stocks', 'empty_universe'])
def test_failure_preserves_outputs(tmp_path, scenario):
    stock, bench = frames()
    report, dashboard = tmp_path / 'report.md', tmp_path / 'dashboard.html'
    report.write_text('old report')
    dashboard.write_text('old html')
    universe, data = {'A': ''}, {'A': stock, scan.BENCHMARK: bench}
    if scenario == 'missing_benchmark': data.pop(scan.BENCHMARK)
    if scenario == 'missing_stocks': data.pop('A')
    if scenario == 'empty_universe': universe = {}
    now = bench.date.iloc[-1] + pd.Timedelta(days=10 if scenario == 'stale_benchmark' else 0)
    with pytest.raises(ValueError):
        scan.write_outputs(universe, data, report, dashboard, now=now)
    assert report.read_text() == 'old report'
    assert dashboard.read_text() == 'old html'
