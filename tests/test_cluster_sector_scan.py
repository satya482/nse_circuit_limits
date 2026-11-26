import json

import pandas as pd

import sector_rotation_scanner as scanner


def setup_scan(monkeypatch, tmp_path, stale=False):
    group_path = tmp_path / 'groups.json'
    group_path.write_text(json.dumps({'version': '2026-11-26', 'groups': {
        'group_1': {'label': 'Test peers', 'size': 4, 'members': ['A', 'B', 'C', 'OUT']}}}))
    monkeypatch.setattr(scanner, 'GROUPS_FILE', group_path)
    monkeypatch.setattr(scanner, 'SCANS_DIR', tmp_path)
    monkeypatch.setattr(scanner, 'MD_FILE', tmp_path / 'latest.md')
    monkeypatch.setattr(scanner, 'COVERAGE_FILE', tmp_path / 'coverage.json')
    monkeypatch.setattr(scanner, 'STATE_FILE', tmp_path / 'state.json')
    universe = {'stocks': [{'symbol': s, 'name': s, 'price': 30, 'market_cap': 1000e7}
                           for s in ['A', 'B', 'C']]}
    monkeypatch.setattr(scanner, 'load_universe', lambda **kwargs: universe)
    monkeypatch.setattr(scanner, 'read_cache', lambda: {
        s: {'combined_description': 'Manufacturing business ' * 4} for s in ['A', 'B', 'C']})
    bars = pd.DataFrame({'date': pd.date_range('2026-10-01', periods=31),
                         'close': list(range(30, 61))})
    histories = {s: bars.copy() for s in ['A', 'B', 'C', 'OUT', scanner.BENCHMARK]}
    if stale:
        histories['C'] = bars.iloc[:-1]
    def load(symbols, **kwargs):
        assert 'OUT' not in symbols
        return {s: histories[s] for s in symbols}
    monkeypatch.setattr(scanner, 'load_ohlc_many', load)


def test_daily_sector_report_obeys_current_eligible_members(monkeypatch, tmp_path):
    setup_scan(monkeypatch, tmp_path)
    assert scanner.main() == 0
    report = scanner.MD_FILE.read_text(encoding='utf-8')
    assert '| Test peers | 3/3 |' in report
    assert 'OUT' not in report
    assert 'SEBI registered' in report


def test_stale_peer_is_pending_and_cannot_inflate_breadth(monkeypatch, tmp_path):
    setup_scan(monkeypatch, tmp_path, stale=True)
    assert scanner.main() == 0
    report = scanner.MD_FILE.read_text(encoding='utf-8')
    assert '| Test peers |' not in report
    coverage = json.loads(scanner.COVERAGE_FILE.read_text())
    reasons = {s['symbol']: s['reason'] for s in coverage['pending']}
    assert reasons['C'] == 'Stale price history'
    assert coverage['ready'] == 0


def test_report_expands_every_rising_member(monkeypatch, tmp_path):
    setup_scan(monkeypatch, tmp_path)
    symbols = [f'STOCK{i}' for i in range(12)]
    scanner.GROUPS_FILE.write_text(json.dumps({'version': '2026-11-26', 'groups': {
        'g': {'label': 'Large peers', 'size': 12, 'members': symbols}}}))
    bars = scanner.load_ohlc_many([scanner.BENCHMARK])[scanner.BENCHMARK]
    monkeypatch.setattr(scanner, 'load_universe', lambda **kwargs: {'stocks': [
        {'symbol': s, 'name': s, 'price': 30, 'market_cap': 1000e7} for s in symbols]})
    monkeypatch.setattr(scanner, 'load_ohlc_many', lambda members, **kwargs: {s: bars.copy() for s in members})
    assert scanner.main() == 0
    assert ', '.join(symbols) in scanner.MD_FILE.read_text(encoding='utf-8')
