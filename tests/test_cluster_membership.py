import json
from datetime import date

import pandas as pd
import pytest

import cluster_membership as membership
from tools import company_fetcher as companies


def stock(symbol, price=26, mcap=1000 * 10_000_000):
    return {'symbol': symbol, 'name': symbol, 'price': price, 'market_cap': mcap}


@pytest.mark.parametrize('class_name', ['abt-desc-wrapper', 'FullStockInfo-module__abc__abt-desc-wrapper'])
def test_trendlyne_description_supports_current_and_legacy_layout(monkeypatch, class_name):
    description = 'Company manufactures industrial equipment and automation systems.'
    class Response:
        status_code = 200
        text = f'<span class="{class_name}">{description}</span>'
    monkeypatch.setattr(companies.requests, 'get', lambda *args, **kwargs: Response())
    result = companies.fetch_trendlyne('ABB', {'ABB': {'id': '17', 'slug': 'abb-india-ltd'}})
    assert result == description


def test_exact_universe_boundaries():
    assert membership.is_eligible(stock('LOW'))
    assert membership.is_eligible(stock('HIGH', mcap=500000 * 10_000_000))
    assert not membership.is_eligible(stock('PRICE', price=25))
    assert not membership.is_eligible(stock('SMALL', mcap=999 * 10_000_000))
    assert not membership.is_eligible(stock('BIG', mcap=500001 * 10_000_000))
    assert not membership.is_eligible(stock('NAN', price=float('nan')))


def test_paginated_common_equities_and_failure_preservation(monkeypatch, tmp_path):
    queries = []

    class Query:
        def __init__(self):
            self.start = 0
            queries.append(self)

        def __getattr__(self, name):
            def chain(*args, **kwargs):
                if name == 'where':
                    self.filters = list(args)
                if name == 'offset':
                    self.start = args[0]
                return self
            return chain

        def get_scanner_data(self, **kwargs):
            indices = range(self.start, min(self.start + 1000, 1205))
            return 1205, pd.DataFrame([
                {'name': f'S{i:04}', 'description': 'Business', 'close': 26,
                 'market_cap_basic': 1000 * 10_000_000} for i in indices
            ])

    target = tmp_path / 'universe.json'
    monkeypatch.setattr(companies, 'Query', Query)
    monkeypatch.setattr(companies, 'UNIVERSE_OUT', target)
    stocks = companies.fetch_universe()
    assert len(stocks) == 1205
    assert queries[-1].start == 1000
    assert any(f.get('left') == 'typespecs' for f in queries[0].filters)
    old = target.read_bytes()
    monkeypatch.setattr(Query, 'get_scanner_data', lambda self, **kwargs: (1205, pd.DataFrame()))
    with pytest.raises(ValueError):
        companies.fetch_universe()
    assert target.read_bytes() == old


def test_cadence_only_success_marks_period():
    today = date(2026, 11, 26)
    assert membership.due_periods({}, today) == (True, True)
    state = {'weekly': '2026-W48', 'monthly': '2026-11'}
    assert membership.due_periods(state, today) == (False, False)
    assert membership.due_periods(state, date(2026, 11, 30)) == (True, False)
    assert membership.due_periods(state, date(2026, 12, 1)) == (True, True)


def test_pending_coverage_and_daily_gate():
    universe = {'stocks': [stock(s) for s in ['A', 'B', 'C', 'IPO', 'EMPTY', 'SHORT', 'SOLO']]}
    groups = {'version': '2026-11-23', 'groups': {
        'g': {'label': 'Peers', 'members': ['A', 'B', 'C', 'SHORT', 'OUT'], 'size': 5},
        'single': {'label': 'Solo', 'members': ['SOLO'], 'size': 1}}}
    cache = {s['symbol']: {'combined_description': 'business description ' * 5} for s in universe['stocks']}
    cache['EMPTY']['combined_description'] = ''
    bars = pd.DataFrame({'date': pd.date_range('2026-10-01', periods=30), 'close': [30] * 30})
    ohlc = {s: bars for s in ['A', 'B', 'C', 'SOLO']}
    ohlc['SHORT'] = bars.iloc[:5]
    coverage = membership.build_coverage(universe, groups, cache, ohlc)
    pending = {row['symbol']: row['reason'] for row in coverage['pending']}
    assert coverage['eligible'] == 7
    assert coverage['ready'] == 3
    assert 'weekly' in pending['IPO']
    assert 'description' in pending['EMPTY']
    assert '30' in pending['SHORT']
    assert 'peer' in pending['SOLO']
    filtered = membership.eligible_groups(groups, universe)
    assert filtered['g']['members'] == ['A', 'B', 'C', 'SHORT']
    assert filtered['g']['size'] == 4


def test_stable_group_ids_and_manual_override():
    from tools.peer_group_builder import assemble_groups
    previous = {'groups': {'group_0042': {'label': 'Pumps', 'members': ['A', 'B'], 'size': 2}}}
    groups, mapping = assemble_groups(
        ['A', 'B', 'NEW', 'MANUAL'], ['pump manufacture'] * 4, ['Company'] * 4,
        [9, 9, 9, -1], {'MANUAL': 'group_0042'}, previous)
    assert groups['group_0042']['members'] == ['A', 'B', 'NEW', 'MANUAL']
    assert mapping['NEW'] == 'group_0042'


def test_failed_description_does_not_erase_good_cache(monkeypatch, tmp_path):
    monkeypatch.setattr(companies, 'CACHE_DIR', tmp_path)
    monkeypatch.setattr(companies, 'fetch_trendlyne', lambda *args: '')
    monkeypatch.setattr(companies, 'fetch_screener', lambda *args: ('', []))
    monkeypatch.setattr(companies.time, 'sleep', lambda *args: None)
    previous = {'symbol': 'A', 'combined_description': 'known business ' * 8}
    (tmp_path / 'A.json').write_text(json.dumps(previous))
    assert companies.fetch_and_cache('A', 'A', {}) == previous
    assert json.loads((tmp_path / 'A.json').read_text()) == previous


def test_failed_maintenance_does_not_advance_state(monkeypatch, tmp_path):
    monkeypatch.setattr(membership, 'STATE_FILE', tmp_path / 'state.json')
    monkeypatch.setattr(membership, 'SOURCE', tmp_path / 'universe.json')
    membership.SOURCE.write_text(json.dumps({'stocks': [stock('IPO')]}))
    monkeypatch.setattr(companies, 'ID_MAP_FILE', tmp_path / 'map.json')
    companies.ID_MAP_FILE.write_text('{}')
    monkeypatch.setattr(companies, 'fetch_and_cache', lambda *args: (_ for _ in ()).throw(RuntimeError('offline')))
    monkeypatch.setattr(membership, 'read_cache', lambda: {})
    with pytest.raises(RuntimeError):
        membership.maintain(date(2026, 11, 26))
    assert not membership.STATE_FILE.exists()


def test_successful_maintenance_is_idempotent_within_week_and_month(monkeypatch, tmp_path):
    from tools import peer_group_builder as builder
    monkeypatch.setattr(membership, 'STATE_FILE', tmp_path / 'state.json')
    monkeypatch.setattr(membership, 'SOURCE', tmp_path / 'universe.json')
    monkeypatch.setattr(membership, 'GROUPS_FILE', tmp_path / 'groups.json')
    membership.SOURCE.write_text(json.dumps({'stocks': [stock('A'), stock('B')]}))
    monkeypatch.setattr(membership, 'read_cache', lambda: {
        s: {'combined_description': 'business description ' * 5,
            'fetched_at': '2026-11-01T10:00:00+00:00'} for s in ['A', 'B']})
    monkeypatch.setattr(companies, '_is_fresh', lambda symbol: True)
    calls = []
    def rebuild(argv):
        calls.append(argv)
        membership.GROUPS_FILE.write_text(json.dumps({'groups': {'g': {
            'label': 'Peers', 'size': 2, 'members': ['A', 'B']}}}))
        return 0
    monkeypatch.setattr(builder, 'main', rebuild)
    first = membership.maintain(date(2026, 11, 26))
    second = membership.maintain(date(2026, 11, 27))
    assert first == second
    assert first['weekly'] == '2026-W48' and first['monthly'] == '2026-11'
    assert len(calls) == 1


def test_monthly_refresh_does_not_rebuild_groups_twice_in_same_week(monkeypatch, tmp_path):
    from tools import peer_group_builder as builder
    monkeypatch.setattr(membership, 'STATE_FILE', tmp_path / 'state.json')
    monkeypatch.setattr(membership, 'SOURCE', tmp_path / 'universe.json')
    membership.SOURCE.write_text(json.dumps({'stocks': [stock('A')]}))
    membership.STATE_FILE.write_text(json.dumps({'weekly': '2026-W49', 'monthly': '2026-11'}))
    monkeypatch.setattr(membership, 'read_cache', lambda: {'A': {'combined_description': 'Business ' * 20}})
    monkeypatch.setattr(companies, '_is_fresh', lambda symbol: False)
    fetched = []
    def fetch(*args):
        fetched.append(args[0])
        return {'combined_description': 'Business ' * 20, 'fetched_at': '2026-12-01T10:00:00+00:00'}
    monkeypatch.setattr(companies, 'fetch_and_cache', fetch)
    monkeypatch.setattr(builder, 'main', lambda argv: pytest.fail('Weekly group rebuild not due'))
    state = membership.maintain(date(2026, 12, 1))
    assert fetched == ['A']
    assert state['monthly'] == '2026-12'


def test_soft_failed_monthly_refresh_remains_due(monkeypatch, tmp_path):
    monkeypatch.setattr(membership, 'STATE_FILE', tmp_path / 'state.json')
    monkeypatch.setattr(membership, 'SOURCE', tmp_path / 'universe.json')
    membership.SOURCE.write_text(json.dumps({'stocks': [stock('A')]}))
    membership.STATE_FILE.write_text(json.dumps({'weekly': '2026-W49', 'monthly': '2026-11'}))
    stale = {'combined_description': 'Business ' * 20, 'fetched_at': '2026-11-26T10:00:00+00:00'}
    monkeypatch.setattr(membership, 'read_cache', lambda: {'A': stale})
    monkeypatch.setattr(companies, '_is_fresh', lambda symbol: True)
    attempts = []
    def failed_fetch(*args):
        attempts.append(args[0])
        return stale
    monkeypatch.setattr(companies, 'fetch_and_cache', failed_fetch)
    state = membership.maintain(date(2026, 12, 1))
    assert state['monthly'] == '2026-11'
    assert state['description_failures'] == ['A']
    membership.maintain(date(2026, 12, 2))
    assert attempts == ['A', 'A']
