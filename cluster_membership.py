"""Daily cluster discovery, weekly membership maintenance and coverage reporting."""

import argparse
import json
import math
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "tools" / "sector_rotation_universe.json"
GROUPS_FILE = ROOT / "peer_groups.json"
STATE_FILE = ROOT / "data" / "cluster_membership_state.json"
COVERAGE_FILE = ROOT / "sector_rotation_scans" / "cluster_coverage.json"
IST = timezone(timedelta(hours=5, minutes=30))


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + '\n', encoding='utf-8')
    temporary.replace(path)


def read_json(path, default=None):
    return json.loads(Path(path).read_text(encoding='utf-8')) if Path(path).exists() else default


def is_eligible(stock):
    try:
        price, mcap = float(stock['price']), float(stock['market_cap'])
        return math.isfinite(price) and math.isfinite(mcap) and price > 25 and 1000e7 <= mcap <= 500000e7
    except (KeyError, TypeError, ValueError):
        return False


def load_universe(path=SOURCE, require_today=False):
    universe = read_json(path)
    if not universe or not universe.get('stocks') or any(not is_eligible(s) for s in universe['stocks']):
        raise ValueError('Cluster universe is missing, empty or invalid; run daily discovery')
    symbols = [s['symbol'] for s in universe['stocks']]
    if len(set(symbols)) != len(symbols):
        raise ValueError('Duplicate cluster universe symbols')
    if require_today:
        discovered = datetime.fromisoformat(universe['fetched_at']).astimezone(IST).date()
        if discovered != datetime.now(IST).date():
            raise ValueError('Cluster universe is stale; run daily discovery')
    return universe


def read_cache():
    from tools.company_fetcher import CACHE_DIR
    cache = {}
    for path in CACHE_DIR.glob('*.json'):
        try:
            cache[path.stem] = read_json(path)
        except (ValueError, OSError):
            continue
    return cache


def eligible_groups(groups, universe):
    allowed = {s['symbol'] for s in universe['stocks'] if is_eligible(s)}
    return {gid: {**g, 'members': [s for s in g['members'] if s in allowed],
                  'size': sum(s in allowed for s in g['members'])}
            for gid, g in groups['groups'].items()}


def due_periods(state, today):
    year, week, _ = today.isocalendar()
    return state.get('weekly') != f'{year}-W{week:02}', state.get('monthly') != today.strftime('%Y-%m')


def description_current(entry, today):
    if len(entry.get('combined_description', '').strip()) < 40:
        return False
    try:
        fetched = datetime.fromisoformat(entry['fetched_at']).astimezone(IST)
        return fetched.strftime('%Y-%m') == today.strftime('%Y-%m')
    except (KeyError, TypeError, ValueError):
        return False


def membership_changes(previous, current):
    def assignments(data):
        return {s: gid for gid, g in data.get('groups', {}).items() for s in g['members']}
    before, after = assignments(previous), assignments(current)
    return {'added': sorted(after.keys() - before.keys()), 'removed': sorted(before.keys() - after.keys()),
            'moved': [{'symbol': s, 'from': before[s], 'to': after[s]}
                      for s in sorted(before.keys() & after.keys()) if before[s] != after[s]]}


def maintain(today=None):
    from tools import company_fetcher as companies
    today = today or datetime.now(IST).date()
    universe = load_universe(SOURCE)
    state = read_json(STATE_FILE, {})
    weekly, monthly = due_periods(state, today)
    if not weekly and not monthly:
        print('Cluster memberships and descriptions already maintained this period')
        return state
    cache = read_cache()
    id_map = read_json(companies.ID_MAP_FILE, {})
    eligible = {s['symbol'] for s in universe['stocks']}
    failures = set(state.get('description_failures', [])) & eligible
    monthly_failed = []
    for stock in universe['stocks']:
        symbol = stock['symbol']
        entry = cache.get(symbol, {})
        missing = len(entry.get('combined_description', '').strip()) < 40
        refresh_existing = monthly and not missing and not description_current(entry, today)
        if (weekly and missing) or refresh_existing:
            result = companies.fetch_and_cache(symbol, stock['name'], id_map)
            if not description_current(result or {}, today):
                failures.add(symbol)
                if refresh_existing:
                    monthly_failed.append(symbol)
            else:
                failures.discard(symbol)
    if weekly:
        from tools import peer_group_builder as builder
        previous = read_json(GROUPS_FILE, {})
        if builder.main(['--universe', str(SOURCE)]) != 0:
            raise RuntimeError('Peer group rebuild failed; cadence state not advanced')
        current = read_json(GROUPS_FILE)
        state['changes'] = membership_changes(previous, current)
        state['group_updated'] = today.isoformat()
        year, week, _ = today.isocalendar()
        state['weekly'] = f'{year}-W{week:02}'
    state['description_failures'] = sorted(failures)
    if monthly and not monthly_failed:
        state['monthly'] = today.strftime('%Y-%m')
        state['descriptions_updated'] = today.isoformat()
    atomic_json(STATE_FILE, state)
    return state


def build_coverage(universe, groups, cache, ohlc):
    filtered = eligible_groups(groups, universe)
    assignments = {s: gid for gid, g in filtered.items() for s in g['members']}
    benchmark = ohlc.get('NIFTY MIDSML 400')
    latest = None if benchmark is None or benchmark.empty else benchmark['date'].max()

    def history_reason(symbol):
        bars = ohlc.get(symbol)
        if bars is None or bars.empty:
            return 'Missing price history'
        if len(bars) < 30:
            return 'Insufficient price history (minimum 30 trading bars)'
        if latest is not None and bars['date'].max() != latest:
            return 'Stale price history'
        if not bars['close'].gt(0).all() or not bars['close'].map(math.isfinite).all():
            return 'Invalid price history'
        return None

    usable = {gid: sum(history_reason(s) is None for s in g['members']) for gid, g in filtered.items()}
    pending = []
    for stock in universe['stocks']:
        symbol = stock['symbol']
        gid = assignments.get(symbol)
        if len(cache.get(symbol, {}).get('combined_description', '').strip()) < 40:
            reason = 'Awaiting company description'
        elif gid is None:
            reason = 'Awaiting weekly group assignment'
        elif filtered[gid]['size'] < 3 or gid.startswith('singleton_'):
            reason = 'No suitable peer group (minimum 3 members)'
        else:
            reason = history_reason(symbol)
            if reason is None and usable[gid] < 3:
                reason = 'Peer group needs 3 members with usable price history'
        if reason:
            pending.append({'symbol': symbol, 'name': stock['name'], 'reason': reason})
    return {'discovered_at': universe.get('fetched_at', ''), 'groups_updated': groups.get('version', ''),
            'price_date': str(latest.date()) if latest is not None else '',
            'eligible': len(universe['stocks']), 'ready': len(universe['stocks']) - len(pending),
            'pending': pending}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--discover', action='store_true')
    args = parser.parse_args()
    if args.discover:
        from tools.company_fetcher import fetch_universe
        fetch_universe()
    else:
        load_universe(SOURCE, require_today=True)
        maintain()


if __name__ == '__main__':
    main()
