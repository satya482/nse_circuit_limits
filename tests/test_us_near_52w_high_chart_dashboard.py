import importlib
import re
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from union_chart_dashboard import build_chart_data, build_html


def module():
    return importlib.import_module('us_near_52w_high_chart_dashboard')


def history(n=65, last=95., high=100.):
    dates = pd.date_range('2025-01-06', periods=n, freq='W-MON')
    closes = np.linspace(60, last, n)
    return pd.DataFrame(dict(date=dates, open=closes, high=high,
                             low=closes - 1, close=closes, volume=1000))


def test_weekly_aggregation_retains_partial_week_and_holiday_week():
    df = pd.DataFrame(dict(
        date=pd.to_datetime(['2026-09-08', '2026-09-11', '2026-09-14', '2026-09-16']),
        open=[10, 12, 13, 14], high=[13, 15, 16, 18], low=[9, 11, 12, 13],
        close=[12, 14, 15, 17], volume=[10, 20, 30, 40]))
    weekly = module().to_weekly(df)
    assert weekly.date.dt.strftime('%Y-%m-%d').tolist() == ['2026-09-07', '2026-09-14']
    assert weekly[['open', 'high', 'low', 'close', 'volume']].values.tolist() == [
        [10, 15, 9, 14, 30], [13, 18, 12, 17, 70]]


@pytest.mark.parametrize('last,bucket', [(100, 'AT/NEW HIGH'), (95, '0-10%'),
    (90, '0-10%'), (80, '10-20%'), (70, '20-30%'), (69.9, None)])
def test_weekly_selection_band_and_buckets(last, bucket):
    df = history(last=last)
    frames, rows = module().select_weekly({'ABC': df}, df.date.iloc[-1])
    assert (rows[0]['tier'] if rows else None) == bucket
    assert ('ABC' in frames) == (bucket is not None)


def test_high_window_uses_52_weeks_not_all_history():
    df = history()
    df.loc[0, 'high'] = 1000
    _, rows = module().select_weekly({'ABC': df}, df.date.iloc[-1])
    assert rows[0]['high_52w'] == 100


def test_requires_52_weeks_and_strict_ema40_and_fresh_symbol():
    flat = history()
    flat['close'] = 95.
    good = history()
    _, rows = module().select_weekly({'FLAT': flat, 'SHORT': good.iloc[-51:],
                                     'STALE': good.iloc[:-1], 'GOOD': good}, good.date.iloc[-1])
    assert [r['symbol'] for r in rows] == ['GOOD']
    assert rows[0]['ema40'] == pytest.approx(good.close.ewm(span=40, adjust=False).mean().iloc[-1])


def test_weekly_us_records_have_spy_rs_and_week_change():
    stock = history()
    bench = history(last=110, high=120)
    records, skipped = build_chart_data({'ABC': stock}, {'ABC': '0-10%'},
        min_bars=52, symbol_exchange={'ABC': 'NASDAQ'}, bench_df=bench,
        rs_for_all_exchanges=True)
    assert skipped == 0
    record = records[0]
    assert record['tv_symbol'] == 'NASDAQ:ABC'
    assert record['rs_pane']['rs_line'][-1] == pytest.approx(95 / 110 * 1000)
    assert record['day_change'] == pytest.approx((95 / stock.close.iloc[-2] - 1) * 100)


def test_weekly_html_has_52_bar_high_and_weekly_labels():
    record = dict(symbol='ABC', tv_symbol='NYSE:ABC', tier='0-10%',
                  industry='Software', day_change=1, bars=[], signals=[])
    html = build_html([record], '2026-09-18', weekly=True,
                      subtitle='Weekly candles; RS vs SPY', high52w_default_visible=True)
    assert 'const HIGH52W_PERIOD = 52;' in html
    assert 'const DEFAULT_VIEW_MONTHS = 24;' in html
    assert 'Week change: highest first' in html
    assert 'Day change:' not in html
    assert 'interval=W' in html
    assert 'Weekly candles; RS vs SPY' in html
    assert '20,40,50,200' in html
    assert 'SEBI registered' in html
    assert not re.search(r'__[A-Z_]+__', html)


def test_daily_renderer_defaults_remain_daily():
    html = build_html([], '2026-09-18')
    assert 'const HIGH52W_PERIOD = 260;' in html
    assert 'const DEFAULT_VIEW_MONTHS = 6;' in html
    assert 'Day change: highest first' in html


def test_orchestrator_runs_weekly_page_after_successful_us_refresh():
    root = Path(__file__).resolve().parents[1]
    runner = (root / 'run_all_scanners.ps1').read_text()
    assert runner.index('"US_FetchData"') < runner.index('"US_Near52WWeekly"')
    assert '$results[-1].Status -eq "PASS"' in runner


def universe():
    return pd.DataFrame(dict(name=['ABC'], exchange=['NASDAQ'], industry=['Software'])).set_index('name')


@pytest.mark.parametrize('case', ['missing_spy', 'stale_spy', 'missing_stocks', 'empty_universe'])
def test_unusable_inputs_preserve_existing_output(tmp_path, case):
    m = module()
    prices = {'ABC': history(), 'SPY': history(last=110, high=120)}
    members = universe()
    today = prices['SPY'].date.iloc[-1]
    if case == 'missing_spy':
        del prices['SPY']
    elif case == 'stale_spy':
        today += pd.Timedelta(days=6)
    elif case == 'missing_stocks':
        del prices['ABC']
    else:
        members = members.iloc[:0]
    page = tmp_path / 'charts.html'
    page.write_text('original')
    with pytest.raises(RuntimeError):
        m.write_outputs(members, prices, today=today, output_path=page, report_path=tmp_path / 'report.md')
    assert page.read_text() == 'original'


def test_valid_empty_selection_replaces_old_page(tmp_path):
    stock = history(last=60)
    prices = {'ABC': stock, 'SPY': history(last=110, high=120)}
    page = tmp_path / 'charts.html'
    page.write_text('old')
    records = module().write_outputs(universe(), prices, today=stock.date.iloc[-1],
        output_path=page, report_path=tmp_path / 'report.md')
    assert records == []
    assert 'No signals.' in page.read_text(encoding='utf-8')
    assert 'SEBI registered' in (tmp_path / 'report.md').read_text(encoding='utf-8')


def test_weekly_ema40_overlay_matches_selection_calculation():
    import shutil
    import subprocess
    import json
    if not shutil.which('node'):
        pytest.skip('Node unavailable')
    html = build_html([], '2026-09-18', weekly=True)
    function = html.split('function computeEMA(', 1)[1].split('function getEmaPeriods', 1)[0]
    closes = history().close.tolist()
    source = 'function computeEMA(' + function + '\nconsole.log(JSON.stringify(computeEMA(' + json.dumps(closes) + ',40)));'
    result = subprocess.run(['node', '-e', source], capture_output=True, text=True, check=True)
    values = json.loads(result.stdout)
    assert values[-1] == pytest.approx(pd.Series(closes).ewm(span=40, adjust=False).mean().iloc[-1])


def test_weekly_high_projection_uses_three_weekly_dates():
    import shutil
    import subprocess
    import json
    if not shutil.which('node'):
        pytest.skip('Node unavailable')
    html = build_html([], '2026-09-18', weekly=True)
    source = html.split('function nextWeekday(', 1)[1].split('function high52wLineData', 1)[0]
    source = 'function nextWeekday(' + source + '\nconsole.log(JSON.stringify(extendFlatWeekdays([{time:"2026-09-14", value:100}], HIGH52W_EXTEND_DAYS)));'
    result = subprocess.run(['node', '-e', source], capture_output=True, text=True, check=True)
    assert [p['time'] for p in json.loads(result.stdout)] == [
        '2026-09-14', '2026-09-21', '2026-09-28', '2026-10-05']


@pytest.mark.parametrize('now,expected', [
    ('2026-09-18 15:35:00+05:30', '2026-09-17'),
    ('2026-09-19 06:00:00+05:30', '2026-09-18'),
    ('2026-09-08 15:35:00+05:30', '2026-09-04'),
    ('2026-11-27 13:30:00-05:00', '2026-11-27'),
])
def test_expected_session_handles_us_time_holidays_and_early_close(now, expected):
    assert str(module().expected_us_session(pd.Timestamp(now)).date()) == expected


def test_missed_midweek_session_rejects_old_prices(tmp_path):
    stock = history()
    # Shift the last observation to Monday Sept 14, then run Thursday Sept 17.
    stock.date += pd.Timestamp('2026-09-14') - stock.date.iloc[-1]
    with pytest.raises(RuntimeError, match='stale'):
        module().write_outputs(universe(), {'ABC': stock, 'SPY': stock},
            today='2026-09-17', output_path=tmp_path / 'page.html', report_path=tmp_path / 'report.md')
