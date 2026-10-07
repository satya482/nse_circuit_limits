from pathlib import Path

import pytest

import ipo_watchlist_updater as updater


def test_only_eq_symbols_are_normalized_and_deduplicated():
    rows = [
        {'series': 'EQ', 'symbol': ' nse:abc '},
        {'series': ' eq ', 'symbol': 'ABC', 'status': 'Forthcoming'},
        {'series': 'EQ', 'symbol': 'M&M', 'status': 'Active'},
        {'series': 'SME', 'symbol': 'SMESTOCK'},
        {'series': 'DEBT', 'symbol': 'BOND'},
    ]
    assert updater.parse_eq_symbols(rows) == ['ABC', 'M&M']


@pytest.mark.parametrize('payload', [{}, [None], [{'series': 'EQ'}],
                                     [{'series': 'EQ', 'symbol': 'BAD,SYM'}]])
def test_malformed_response_is_rejected(payload):
    with pytest.raises(ValueError):
        updater.parse_eq_symbols(payload)


def test_no_eq_is_a_valid_noop():
    assert updater.parse_eq_symbols([]) == []
    assert updater.parse_eq_symbols([{'series': 'DEBT', 'symbol': 'BOND'}]) == []


def test_append_preserves_existing_bytes_and_is_idempotent(tmp_path):
    path = tmp_path / 'ipo_listings.txt'
    original = b'# Keep header\r\n\r\nabc\r\nLAST'
    path.write_bytes(original)
    assert updater.append_missing(path, ['ABC', 'NEW', 'NEW']) == ['NEW']
    assert path.read_bytes() == original + b'\nNEW\n'
    assert updater.append_missing(path, ['ABC', 'NEW']) == []
    assert path.read_bytes() == original + b'\nNEW\n'


def test_main_updates_both_lists(tmp_path, monkeypatch):
    paths = [tmp_path / 'new_listings.txt', tmp_path / 'ipo_listings.txt']
    for path in paths:
        path.write_text('# existing\nOLD', encoding='utf-8')
    monkeypatch.setattr(updater, 'WATCHLIST_PATHS', paths)
    monkeypatch.setattr(updater, 'fetch_eq_symbols', lambda: ['NEW'])
    assert updater.main() == 0
    assert all(path.read_text().endswith('OLD\nNEW\n') for path in paths)


def test_fetch_failure_leaves_both_lists_untouched(tmp_path, monkeypatch):
    paths = [tmp_path / 'new_listings.txt', tmp_path / 'ipo_listings.txt']
    for path in paths:
        path.write_bytes(b'OLD')
    monkeypatch.setattr(updater, 'WATCHLIST_PATHS', paths)
    def fail():
        raise ValueError('Unexpected NSE payload')
    monkeypatch.setattr(updater, 'fetch_eq_symbols', fail)
    assert updater.main() == 1
    assert all(path.read_bytes() == b'OLD' for path in paths)


def test_daily_updater_runs_before_data_fetch():
    root = Path(__file__).resolve().parents[1]
    runner = (root / 'run_all_scanners.ps1').read_text()
    assert runner.index('Run-Scanner "IPOWatchlistUpdate"') < runner.index('Run-Scanner "FetchData"')
