import pandas as pd
import sqlite3

import fetch_data


def test_cluster_symbols_above_old_market_cap_ceiling_are_fetched(monkeypatch):
    class Query:
        def __getattr__(self, name):
            if name == 'get_scanner_data':
                return lambda: (1, pd.DataFrame([{'name': 'OLD', 'market_cap_basic': 1000e7}]))
            return lambda *args, **kwargs: self
    monkeypatch.setattr(fetch_data, 'Query', Query)
    monkeypatch.setattr(fetch_data, 'get_cluster_universe', lambda: ({'IPO', 'LARGE'}, {'IPO': 1500, 'LARGE': 400000}), raising=False)
    symbols, caps = fetch_data.get_tv_universe()
    assert {'OLD', 'IPO', 'LARGE'} == symbols
    assert caps['LARGE'] == 400000


def test_new_cluster_member_invalidates_same_day_instrument_cache(monkeypatch):
    con = sqlite3.connect(':memory:')
    fetch_data.init_db(con)
    today = fetch_data.date.today().isoformat()
    con.execute('INSERT INTO instruments VALUES (1, ?, ?, ?, ?, ?, ?)',
                ('OLD', 'Old', 'NSE', 'EQ', today, 1000))
    monkeypatch.setattr(fetch_data, 'get_cluster_universe', lambda: ({'NEW-IPO'}, {'NEW-IPO': 1500}))
    monkeypatch.setattr(fetch_data, 'get_tv_universe', lambda: ({'OLD', 'NEW-IPO'}, {'OLD': 1000, 'NEW-IPO': 1500}))
    class Kite:
        def instruments(self, exchange):
            return [{'instrument_token': i, 'tradingsymbol': symbol, 'name': symbol,
                     'segment': 'NSE', 'exchange': 'NSE', 'instrument_type': 'EQ'}
                    for i, symbol in enumerate(['OLD', 'NEW-IPO'], 1)]
    result = fetch_data.refresh_instruments(Kite(), con)
    assert 'NEW-IPO' in set(result['tradingsymbol'])
    con.close()
