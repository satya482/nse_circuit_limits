import json
import re
import shutil
import subprocess

import pandas as pd
import pytest

import rs_leaders_scanner as rs


def prices(values, dates=None):
    return pd.DataFrame({'date': dates if dates is not None else pd.bdate_range('2026-04-01', periods=len(values)), 'close': values, 'volume': 1000000})


def test_ratio_relative_return_and_window_endpoints():
    b = prices([100] * 5 + [105])
    s = prices([100] * 5 + [112])
    row = rs.calculate_periods(s, b)
    assert row['1W']['return'] == pytest.approx(12)
    assert row['1W']['rs'] == pytest.approx(100 * (1.12 / 1.05 - 1))
    assert row['1M'] is None


def test_missing_session_does_not_shorten_window():
    b = prices([100] * 22)
    s = b.drop(index=10)
    row = rs.calculate_periods(s, b)
    assert row['1M'] is None
    assert row['1W']['rs'] == 0


def test_stale_stock_is_excluded_and_short_history_kept():
    b = prices([100] * 127)
    rows, excluded = rs.build_rankings({'OLD': b.iloc[:-1], 'IPO': b.iloc[-6:]}, b)
    assert [r['symbol'] for r in rows] == ['IPO']
    assert excluded == {'OLD': 'missing latest benchmark session'}
    assert rows[0]['periods']['1M'] is None


def test_percentiles_ties_and_positive_rs_gate():
    b = prices([100] * 127)
    stocks = {f'S{i:02}': prices([100] * 126 + [100 + i]) for i in range(11)}
    rows, _ = rs.build_rankings(stocks, b)
    by = {r['symbol']: r for r in rows}
    assert by['S10']['periods']['1W']['percentile'] == 100
    assert by['S09']['leader_count'] == 4
    assert by['S08']['leader_count'] == 0
    tied, _ = rs.build_rankings({'A': b, 'B': b}, b)
    assert all(r['periods']['1W']['percentile'] == 50 for r in tied)
    assert all(r['leader_count'] == 0 for r in tied)


def test_nonpositive_and_duplicate_prices_rejected():
    b = prices([100] * 127)
    bad = b.copy()
    bad.loc[126, 'close'] = 0
    rows, excluded = rs.build_rankings({'BAD': bad, 'DUP': pd.concat([b, b.tail(1)])}, b)
    assert not rows
    assert set(excluded) == {'BAD', 'DUP'}


def test_previous_session_rank_changes_survive_same_date_rerun():
    rows = [{'symbol': 'A', 'periods': {'1W': {'rank': 2}}}]
    old = {'date': '2026-10-27', 'ranks': {'1W': {'A': 5}}}
    state = rs.make_state(rows, '2026-10-28', old)
    assert rows[0]['periods']['1W']['rank_change'] == 3
    rerun = rs.make_state(rows, '2026-10-28', state)
    assert rows[0]['periods']['1W']['rank_change'] == 3
    assert rerun == state


def test_reports_include_full_rankings_na_and_disclaimers():
    b = prices([100] * 6)
    rows, excluded = rs.build_rankings({'A': prices([100] * 5 + [110])}, b)
    md, html = rs.render_reports(rows, str(b.date.iloc[-1].date()), excluded, 1)
    assert 'SEBI registered' in md and 'SEBI registered' in html
    assert 'N/A' in md and 'N/A' in html
    assert 'NSE:A' in md
    assert 'Full rankings' in md
    assert 'sortTable' in html and 'filterRows' in html
    assert '126' in md and 'corporate' in md
    assert json.loads(json.dumps(rows, allow_nan=False)) == rows


def test_invalid_benchmark_fails_instead_of_empty_success():
    with pytest.raises(ValueError):
        rs.build_rankings({}, prices([100, 0, 100]))


def test_main_preserves_outputs_when_no_usable_history(tmp_path, monkeypatch):
    dates = pd.bdate_range(end=pd.Timestamp.now(tz='Asia/Kolkata').date(), periods=127)
    b = prices([100] * 127, dates)
    monkeypatch.setattr(rs, 'ROOT', tmp_path)
    monkeypatch.setattr(rs, 'SCAN_DIR', tmp_path / 'scans')
    monkeypatch.setattr(rs, 'get_universe', lambda: {'MISSING': 'Industry'})
    monkeypatch.setattr(rs, 'load_ohlc_many', lambda *a, **k: {rs.BENCHMARK: b})
    monkeypatch.setattr(rs, 'latest_date', lambda: dates[-1].strftime('%Y-%m-%d'))
    with pytest.raises(ValueError, match='no usable'):
        rs.main()
    assert not (tmp_path / 'scans').exists()


def test_main_writes_current_outputs_and_state(tmp_path, monkeypatch):
    dates = pd.bdate_range(end=pd.Timestamp.now(tz='Asia/Kolkata').date(), periods=127)
    b = prices([100] * 127, dates)
    monkeypatch.setattr(rs, 'ROOT', tmp_path)
    monkeypatch.setattr(rs, 'SCAN_DIR', tmp_path / 'scans')
    monkeypatch.setattr(rs, 'STATE_PATH', tmp_path / 'scans' / 'rs_leaders_latest.json')
    monkeypatch.setattr(rs, 'get_universe', lambda: {'A': 'Test & Industry'})
    monkeypatch.setattr(rs, 'load_ohlc_many', lambda *a, **k: {rs.BENCHMARK: b, 'A': prices([100] * 126 + [110], dates)})
    monkeypatch.setattr(rs, 'latest_date', lambda: dates[-1].strftime('%Y-%m-%d'))
    rs.main()
    state = json.loads(rs.STATE_PATH.read_text())
    assert state['ranks']['6M'] == {'A': 1}
    assert 'Test &amp; Industry' in (tmp_path / 'dashboard' / 'rs_leaders.html').read_text(encoding='utf-8')


def test_main_rejects_stale_benchmark(tmp_path, monkeypatch):
    monkeypatch.setattr(rs, 'get_universe', lambda: {'A': ''})
    monkeypatch.setattr(rs, 'load_ohlc_many', lambda *a, **k: {rs.BENCHMARK: prices([100] * 127)})
    monkeypatch.setattr(rs, 'latest_date', lambda: '2099-01-01')
    with pytest.raises(ValueError, match='benchmark stale'):
        rs.main()


def test_dashboard_javascript_filters_and_numeric_sorting():
    if not shutil.which('node'):
        pytest.skip('Node required for generated JavaScript checks')
    b = prices([100] * 127)
    rows, excluded = rs.build_rankings({'A': prices([100] * 126 + [110]), 'B': b}, b)
    _, html = rs.render_reports(rows, '2026-09-25', excluded, 2)
    script = re.search(r'<script>(.*?)</script>', html, re.S).group(1)
    harness = '''
const assert=require('node:assert/strict');
function row(symbol,price,count,leader){return {
 cells:[{textContent:symbol},{textContent:'Industry'},{textContent:price}],
 textContent:symbol+' Industry '+price,dataset:{count:count,'1w':leader},hidden:false};}
const body={rows:[row('A','100','1','1'),row('B','20','0','0'),row('C','N/A','0','0')],
 appendChild(r){this.rows.splice(this.rows.indexOf(r),1);this.rows.push(r);}};
const elements={rankings:body,search:{value:''},leaders:{value:'all'},period:{value:'all'},visible:{textContent:''}};
global.document={getElementById(id){return elements[id];},querySelectorAll(){return body.rows;}};
'''
    checks = '''
assert.equal(elements.visible.textContent,'3 stocks shown');
sortTable(2);assert.deepEqual(body.rows.map(r=>r.cells[0].textContent),['A','B','C']);
sortTable(2);assert.deepEqual(body.rows.map(r=>r.cells[0].textContent),['B','A','C']);
elements.leaders.value='1';filterRows();assert.equal(elements.visible.textContent,'1 stocks shown');
elements.leaders.value='all';elements.period.value='1w';filterRows();assert.equal(elements.visible.textContent,'1 stocks shown');
elements.search.value='B';filterRows();assert.equal(elements.visible.textContent,'0 stocks shown');
elements.period.value='all';filterRows();assert.equal(elements.visible.textContent,'1 stocks shown');
'''
    result = subprocess.run(['node', '-e', harness + script + checks], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
