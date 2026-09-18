#!/usr/bin/env python3
"""US near-52-week-high selection and charts, entirely on weekly candles."""
from pathlib import Path

import pandas as pd
import exchange_calendars as xcals
from tradingview_screener import Query, col

from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from us_ohlc_db import load_ohlc_many
from union_chart_dashboard import build_chart_data, build_html

ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT / 'dashboard' / 'us_near_52w_high_charts.html'
REPORT_PATH = ROOT / 'us_near_52w_high_scans' / 'us_near_52w_high_scans.md'
LOOKBACK = 3000
BUCKETS = ('AT/NEW HIGH', '0-10%', '10-20%', '20-30%')


def get_universe():
    """Same eligibility as fetch_us_data and US ZL; include chart metadata."""
    _, frame = (Query().set_markets('america')
        .select('name', 'exchange', 'industry')
        .where(col('exchange').isin(['NASDAQ', 'NYSE']),
               col('type') == 'stock', col('typespecs').has(['common']),
               col('close') > 5,
               col('market_cap_basic').between(300_000_000, 10_000_000_000),
               col('average_volume_10d_calc') > 300_000)
        .limit(3000).get_scanner_data(timeout=30))
    if frame.empty:
        raise RuntimeError('US universe is empty; preserving existing dashboard')
    return frame.drop_duplicates('name').set_index('name')


def to_weekly(df):
    """Monday-labelled trading weeks, including the current unfinished week."""
    data = df.copy().sort_values('date')
    data['date'] = pd.to_datetime(data['date'])
    data['week'] = data['date'].dt.to_period('W-SUN').dt.start_time
    return (data.groupby('week', sort=True)
        .agg(open=('open', 'first'), high=('high', 'max'), low=('low', 'min'),
             close=('close', 'last'), volume=('volume', 'sum'))
        .dropna().rename_axis('date').reset_index())


def select_weekly(ohlc_map, as_of):
    """Return qualifying weekly frames and audit rows at the benchmark date."""
    frames, rows = {}, []
    as_of = pd.Timestamp(as_of)
    for symbol, raw in sorted(ohlc_map.items()):
        data = raw.loc[pd.to_datetime(raw['date']) <= as_of]
        if data.empty or pd.Timestamp(data['date'].max()) != as_of:
            continue
        weekly = to_weekly(data)
        if len(weekly) < 52:
            continue
        close = float(weekly.close.iloc[-1])
        high = float(weekly.high.tail(52).max())
        ema40 = float(weekly.close.ewm(span=40, adjust=False).mean().iloc[-1])
        if high <= 0 or not (0.7 * high <= close <= high and close > ema40):
            continue
        distance = (close - high) / high * 100
        tier = ('AT/NEW HIGH' if abs(distance) < .01 else
                '0-10%' if distance >= -10 else
                '10-20%' if distance >= -20 else '20-30%')
        frames[symbol] = weekly
        rows.append(dict(symbol=symbol, tier=tier, close=close, high_52w=high,
                         pct_from_high=distance, ema40=ema40, weeks=len(weekly)))
    return frames, rows


def expected_us_session(now):
    """Latest completed NYSE session, including US holidays and early closes."""
    now = pd.Timestamp(now)
    if now.tzinfo is None:
        now = now.tz_localize('Asia/Kolkata')
    calendar = xcals.get_calendar('XNYS')
    session = calendar.date_to_session(now.tz_convert('America/New_York').date(), direction='previous')
    if calendar.session_close(session) > now.tz_convert('UTC'):
        session = calendar.previous_session(session)
    return pd.Timestamp(session).tz_localize(None)


def write_outputs(universe, ohlc_map, today=None, output_path=OUTPUT_PATH, report_path=REPORT_PATH):
    """Validate prices, generate both outputs, then atomically replace each file."""
    now = pd.Timestamp(today) if today is not None else pd.Timestamp.now(tz='Asia/Kolkata')
    expected = expected_us_session(now)
    today = now.tz_localize(None).normalize()
    if universe.empty:
        raise RuntimeError('US universe is empty; preserving existing dashboard')
    bench = ohlc_map.get('SPY')
    if bench is None or len(bench) < 2:
        raise RuntimeError('SPY data missing; preserving existing dashboard')
    bench = bench.loc[pd.to_datetime(bench.date) <= today].sort_values('date')
    if bench.empty:
        raise RuntimeError('SPY has no usable dated data')
    as_of = pd.Timestamp(bench.date.max())
    if as_of < expected:
        raise RuntimeError(f'SPY data is stale ({as_of.date()}); expected session {expected.date()}')
    weekly_bench = to_weekly(bench)
    if len(weekly_bench) < 52:
        raise RuntimeError('SPY requires at least 52 weeks of history')
    prices = {s: ohlc_map[s] for s in universe.index if s != 'SPY' and s in ohlc_map}
    if not any(pd.Timestamp(df.date.max()) == as_of for df in prices.values() if not df.empty):
        raise RuntimeError('No US stocks have current OHLC data; preserving existing dashboard')
    frames, rows = select_weekly(prices, as_of)
    records, skipped = build_chart_data(frames, {r['symbol']: r['tier'] for r in rows},
        industries=universe.industry.fillna('Unclassified').to_dict(), min_bars=52,
        symbol_exchange=universe.exchange.to_dict(), bench_df=weekly_bench,
        rs_for_all_exchanges=True)
    if skipped:
        raise RuntimeError(f'{skipped} qualifying charts failed; preserving existing dashboard')
    data_date = str(as_of.date())
    generated = str(today.date())
    subtitle = (f'Weekly candles (unfinished week included) | US prices through {data_date} | '
                f'Generated {generated} | RS vs SPY | Close > weekly EMA40; within 30% of '
                '52-week high. Indicators use available history; EMA200 needs 200 weeks.')
    html = build_html(records, data_date, title='US Near 52W High - Weekly Charts',
        high52w_default_visible=True, weekly=True, subtitle=subtitle)
    lines = [SEBI_MD_HEADER, f'# US Weekly Near-52W-High - {generated}', '', subtitle, '',
        f'Universe: {len(universe)} | Charted: {len(records)}', '',
        '[Weekly charts](../dashboard/us_near_52w_high_charts.html)', '',
        '| Symbol | Bucket | Close | 52W High | From High % | Weekly EMA40 | Weeks |',
        '|---|---|---:|---:|---:|---:|---:|']
    for row in rows:
        lines.append(f"| {row['symbol']} | {row['tier']} | {row['close']:.2f} | "
            f"{row['high_52w']:.2f} | {row['pct_from_high']:.2f} | {row['ema40']:.2f} | {row['weeks']} |")
    for bucket in BUCKETS:
        symbols = [f"{universe.loc[r['symbol'], 'exchange']}:{r['symbol']}"
                   for r in rows if r['tier'] == bucket]
        lines.extend(['', f'## {bucket}', '', '```', ','.join(symbols), '```'])
    lines.append(SEBI_MD_FOOTER)
    for path, content in ((Path(report_path), '\n'.join(lines)), (Path(output_path), html)):
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + '.tmp')
        temporary.write_text(content, encoding='utf-8', newline='\n')
        temporary.replace(path)
    print(f'US weekly near-high: {len(universe)} universe, {len(records)} charted; prices {data_date}')
    return records


def main():
    universe = get_universe()
    prices = load_ohlc_many(list(dict.fromkeys(['SPY', *universe.index])), lookback=LOOKBACK)
    write_outputs(universe, prices)


if __name__ == '__main__':
    main()
