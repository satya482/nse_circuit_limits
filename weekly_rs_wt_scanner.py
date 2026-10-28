"""NSE weekly RS EMA21 and WaveTrend WT1 rising scan, including partial weeks."""

import math
from pathlib import Path

import numpy as np
import pandas as pd

from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from ohlc_db import load_ohlc_many, latest_date
from rs_leaders_scanner import get_universe
from tv_watchlist import tv_csv
from union_chart_dashboard import build_chart_data, build_html
from wavetrend_scanner import WaveTrendCalculator

ROOT = Path(__file__).resolve().parent
BENCHMARK = 'NIFTY MIDSML 400'
MIN_WEEKS = 22
LOOKBACK = 1500
REPORT_PATH = ROOT / 'weekly_rs_wt_scans' / 'weekly_rs_wt_scans.md'
DASHBOARD_PATH = ROOT / 'dashboard' / 'weekly_rs_wt.html'


def validated_daily(frame):
    if frame is None or frame.empty:
        raise ValueError('missing OHLC history')
    data = frame[['date', 'open', 'high', 'low', 'close', 'volume']].copy()
    data['date'] = pd.to_datetime(data['date'], errors='raise').dt.normalize()
    if data.date.isna().any() or data.date.duplicated().any():
        raise ValueError('invalid or duplicate dates')
    fields = ['open', 'high', 'low', 'close', 'volume']
    data[fields] = data[fields].apply(pd.to_numeric, errors='raise')
    if not np.isfinite(data[fields].to_numpy()).all():
        raise ValueError('nonfinite OHLCV')
    if (data[['open', 'high', 'low', 'close']] <= 0).any().any() or (data.volume < 0).any():
        raise ValueError('nonpositive price or negative volume')
    if ((data.high < data[['open', 'close', 'low']].max(axis=1)) |
            (data.low > data[['open', 'close', 'high']].min(axis=1))).any():
        raise ValueError('inconsistent OHLC prices')
    return data.sort_values('date').reset_index(drop=True)


def to_weekly(frame):
    """Aggregate first, then calculate indicators; candle dates are actual closes."""
    data = frame.copy().sort_values('date')
    data['date'] = pd.to_datetime(data.date)
    data['week'] = data.date.dt.to_period('W-SUN')
    return (data.groupby('week', sort=True)
            .agg(date=('date', 'last'), open=('open', 'first'), high=('high', 'max'),
                 low=('low', 'min'), close=('close', 'last'), volume=('volume', 'sum'))
            .reset_index(drop=True))


def passes_gate(rs_now, rs_before, wt_now, wt_before):
    return bool(all(math.isfinite(v) for v in (rs_now, rs_before, wt_now, wt_before))
                and rs_now > rs_before and wt_now > wt_before)


def weekly_indicators(weekly, benchmark):
    if len(weekly) < MIN_WEEKS:
        raise ValueError(f'insufficient history: need {MIN_WEEKS} weekly bars')
    bench = benchmark.set_index('date').close.reindex(weekly.date)
    if bench.isna().any():
        raise ValueError('weekly benchmark date mismatch')
    rs = pd.Series(weekly.close.to_numpy() / bench.to_numpy() * 1000)
    ema21 = rs.ewm(span=21, adjust=False).mean()
    wt1 = WaveTrendCalculator().calc_from_series((weekly.high + weekly.low + weekly.close) / 3)['wt1']
    values = [float(ema21.iloc[-1]), float(ema21.iloc[-2]), float(wt1.iloc[-1]), float(wt1.iloc[-2])]
    if not all(math.isfinite(v) for v in values):
        raise ValueError('indicator values unavailable')
    return {'rs_ema21': values[0], 'rs_previous': values[1], 'rs_slope': values[0] - values[1],
            'wt1': values[2], 'wt_previous': values[3], 'wt_slope': values[2] - values[3],
            'qualified': passes_gate(*values)}


def select_stocks(stocks, benchmark):
    bench = validated_daily(benchmark)
    weekly_bench = to_weekly(bench)
    if len(weekly_bench) < MIN_WEEKS:
        raise ValueError(f'benchmark needs {MIN_WEEKS} weekly bars')
    rows, frames, excluded, evaluated = [], {}, {}, 0
    for symbol, raw in sorted(stocks.items()):
        try:
            data = validated_daily(raw)
            if data.date.iloc[-1] != bench.date.iloc[-1]:
                raise ValueError('missing latest benchmark session')
            expected_dates = bench.loc[bench.date >= data.date.iloc[0], 'date']
            if not pd.Index(expected_dates).equals(pd.Index(data.date)):
                raise ValueError('missing sessions or benchmark history mismatch')
            weekly = to_weekly(data)
            indicators = weekly_indicators(weekly, weekly_bench)
            evaluated += 1
            if not indicators['qualified']:
                continue
            rows.append({'symbol': symbol, 'close': float(weekly.close.iloc[-1]),
                         'week_change': float((weekly.close.iloc[-1] / weekly.close.iloc[-2] - 1) * 100),
                         'weeks': len(weekly), **indicators})
            frames[symbol] = weekly
        except (ValueError, TypeError, KeyError) as exc:
            excluded[symbol] = str(exc)
    return rows, frames, excluded, evaluated


def build_report(rows, date, universe_count, evaluated, excluded):
    note = (f'Price data: {date}. Current developing week included; signals can change before '
            'the week closes. NSE common equities; price > Rs50; market cap Rs1,000 crore '
            'to Rs5 lakh crore. Weekly RS = stock close / NIFTY MIDSML 400 close x 1000; '
            'EMA21 uses adjust=False. Weekly WT1 uses HLC3, EMA10 channel and EMA21 '
            'smoothing, matching the existing WaveTrend calculator. Both latest weekly '
            'values must be strictly greater than their previous weekly values. '
            f'Minimum {MIN_WEEKS} weekly bars; all available history up to {LOOKBACK} daily bars. '
            'Flat slopes do not qualify. No daily EMA200, 52-week-high, float, liquidity, '
            'WT1 zero-line or WT2 gate. No manual-list bypass. All qualifiers are shown.')
    lines = [SEBI_MD_HEADER, f'# Weekly RS EMA21 + WT1 Uptrend — {date}', '', note, '',
             f'Universe: {universe_count} | Evaluated: {evaluated} | Qualified: {len(rows)} | Excluded: {len(excluded)}',
             '', '[Weekly chart dashboard](../dashboard/weekly_rs_wt.html)', '',
             '## TradingView watchlist', '', '```text',
             tv_csv(['NSE:' + r['symbol'] for r in rows], label='WEEKLY RS21 WT1 UP'), '```',
             '', '## All qualifying stocks', '',
             '| Symbol | Close | Week % | RS EMA21 | Previous | RS slope | WT1 | Previous WT1 | WT1 slope | Weeks |',
             '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in rows:
        lines.append(f"| [NSE:{r['symbol']}](https://in.tradingview.com/chart/?symbol=NSE:{r['symbol']}&interval=W) | "
                     f"{r['close']:.2f} | {r['week_change']:+.2f} | {r['rs_ema21']:.4f} | "
                     f"{r['rs_previous']:.4f} | {r['rs_slope']:+.4f} | {r['wt1']:.4f} | "
                     f"{r['wt_previous']:.4f} | {r['wt_slope']:+.4f} | {r['weeks']} |")
    if not rows:
        lines.append('No stocks meet both weekly uptrend conditions.')
    lines += ['', '## Excluded data', '', '\n'.join(f'- {s}: {reason}' for s, reason in sorted(excluded.items())) or 'None.', '', SEBI_MD_FOOTER]
    return '\n'.join(lines).rstrip() + '\n'


def write_outputs(universe, ohlc_map, report_path=REPORT_PATH, dashboard_path=DASHBOARD_PATH, now=None):
    if not universe:
        raise ValueError('empty universe; preserving outputs')
    bench = validated_daily(ohlc_map.get(BENCHMARK))
    as_of = bench.date.iloc[-1]
    today = pd.Timestamp(now) if now is not None else pd.Timestamp.now(tz='Asia/Kolkata').tz_localize(None)
    age = (today.normalize() - as_of).days
    if age < 0 or age > 4:
        raise ValueError(f'benchmark stale or future dated: {as_of.date()}; preserving outputs')
    rows, weekly, excluded, evaluated = select_stocks({s: ohlc_map.get(s) for s in universe}, bench)
    if not evaluated:
        raise ValueError('no stocks have usable aligned indicator history; preserving outputs')
    records, skipped = build_chart_data(weekly, {r['symbol']: 'WEEKLY RS21 + WT1 UP' for r in rows},
        industries=universe, min_bars=MIN_WEEKS, bench_df=to_weekly(bench), include_wt_pane=True)
    if skipped or len(records) != len(rows):
        raise ValueError('qualifying chart generation failed; preserving outputs')
    date = str(as_of.date())
    subtitle = (f'Weekly candles, developing week included | Price data: {date} | '
                f'Qualified {len(rows)} / evaluated {evaluated} / universe {len(universe)} | '
                'Weekly RS EMA21 rising vs NIFTY MIDSML 400 AND weekly WT1 rising (10,21). '
                'RS EMA21 is the blue/red line in the RS pane; WT1 is aqua. '
                f'Minimum {MIN_WEEKS} weeks; no price EMA, 52W-high, WT zero-line or WT2 gate.')
    html = build_html(records, date, title='Weekly RS EMA21 + WT1 Uptrend', group_sort='alpha',
                      weekly=True, subtitle=subtitle, wt_pane_enabled=True, darvas_enabled=True)
    md = build_report(rows, date, len(universe), evaluated, excluded)
    # Render both first; each file replacement is atomic.
    outputs = [(Path(report_path), md), (Path(dashboard_path), html)]
    for path, content in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
        temp = path.with_suffix(path.suffix + '.tmp')
        with temp.open('w', encoding='utf-8', newline='\n') as fh:
            fh.write(content.rstrip() + '\n')
    for path, _ in outputs:
        path.with_suffix(path.suffix + '.tmp').replace(path)
    print(f'Weekly RS21 + WT1: prices {date}; universe {len(universe)}; evaluated {evaluated}; qualified {len(rows)}; excluded {len(excluded)}')
    return records


def main():
    universe = get_universe()
    prices = load_ohlc_many(list(universe) + [BENCHMARK], lookback=LOOKBACK)
    bench = validated_daily(prices.get(BENCHMARK))
    if str(bench.date.iloc[-1].date()) != latest_date():
        raise ValueError('benchmark behind latest local DB date; preserving outputs')
    write_outputs(universe, prices)


if __name__ == '__main__':
    main()
