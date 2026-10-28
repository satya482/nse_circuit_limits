"""Rolling NSE RS leadership rankings; run after the daily OHLC fetch."""

import json
import math
from datetime import datetime
from html import escape
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER, SEBI_HTML_BANNER, SEBI_HTML_FOOTER
from ohlc_db import load_ohlc_many, latest_date
from tv_watchlist import tv_csv

ROOT = Path(__file__).resolve().parent
PERIODS = {'1W': 5, '1M': 21, '3M': 63, '6M': 126}
BENCHMARK = 'NIFTY MIDSML 400'
MC_LOW = 1_000 * 10_000_000
MC_HIGH = 500_000 * 10_000_000
SCAN_DIR = ROOT / 'rs_leaders_scans'
STATE_PATH = SCAN_DIR / 'rs_leaders_latest.json'


def close_series(frame):
    if frame is None or frame.empty:
        raise ValueError('missing price history')
    dates = pd.to_datetime(frame['date'], errors='raise').dt.normalize()
    values = pd.to_numeric(frame['close'], errors='raise')
    if dates.isna().any() or dates.duplicated().any():
        raise ValueError('invalid or duplicate dates')
    if not values.map(lambda x: math.isfinite(x) and x > 0).all():
        raise ValueError('nonpositive or invalid close')
    return pd.Series(values.to_numpy(), index=dates).sort_index()


def calculate_periods(stock, benchmark):
    """Use benchmark session positions, never compress gaps in a stock's history."""
    bench = close_series(benchmark)
    close = close_series(stock).reindex(bench.index)
    result = {}
    for label, window in PERIODS.items():
        result[label] = None
        if len(bench) <= window:
            continue
        segment = close.iloc[-window - 1:]
        if segment.isna().any():
            continue
        stock_ratio = float(segment.iloc[-1] / segment.iloc[0])
        bench_ratio = float(bench.iloc[-1] / bench.iloc[-window - 1])
        result[label] = {'return': 100 * (stock_ratio - 1),
                         'rs': 100 * (stock_ratio / bench_ratio - 1)}
    return result


def build_rankings(stocks, benchmark):
    bench = close_series(benchmark)
    if len(bench) < 6:
        raise ValueError('benchmark needs at least six sessions')
    rows, excluded = [], {}
    for symbol, frame in sorted(stocks.items()):
        try:
            close = close_series(frame)
            if close.index[-1] != bench.index[-1]:
                raise ValueError('missing latest benchmark session')
            periods = calculate_periods(frame, benchmark)
            if not any(v is not None for v in periods.values()):
                raise ValueError('insufficient aligned history for every period')
            recent = frame.assign(date=pd.to_datetime(frame['date'])).sort_values('date').tail(30)
            turnover = None
            if len(recent) == 30 and 'volume' in recent:
                value = (pd.to_numeric(recent['close']) * pd.to_numeric(recent['volume'])).mean() / 10_000_000
                if math.isfinite(value):
                    turnover = float(value)
            rows.append({'symbol': symbol, 'close': float(close.iloc[-1]),
                         'turnover_cr': turnover, 'periods': periods})
        except (ValueError, TypeError, KeyError) as exc:
            excluded[symbol] = str(exc)
    for label in PERIODS:
        available = [r for r in rows if r['periods'][label] is not None]
        scores = pd.Series([r['periods'][label]['rs'] for r in available], dtype=float)
        ranks = scores.rank(method='min', ascending=False)
        ascending = scores.rank(method='average')
        for i, row in enumerate(available):
            p = row['periods'][label]
            p['rank'] = int(ranks.iloc[i])
            p['percentile'] = float(100 * (ascending.iloc[i] - 1) / (len(available) - 1)) if len(available) > 1 else 100.0
            p['leader'] = p['percentile'] >= 90 and p['rs'] > 0
            p['rank_change'] = None
    for row in rows:
        row['leader_count'] = sum(p['leader'] for p in row['periods'].values() if p is not None)
        row['available_periods'] = sum(p is not None for p in row['periods'].values())
    return sorted(rows, key=lambda r: (-r['leader_count'], r['symbol'])), excluded


def make_state(rows, date, previous):
    """Keep prior price-session ranks across repeated runs of the same session."""
    if previous and previous['date'] > date:
        raise ValueError('refusing to replace newer rank state')
    baseline = previous.get('baseline', {}) if previous and previous['date'] == date else (previous or {}).get('ranks', {})
    baseline_date = previous.get('baseline_date') if previous and previous['date'] == date else (previous or {}).get('date')
    ranks = {label: {} for label in PERIODS}
    for row in rows:
        for label, p in row['periods'].items():
            if p is None:
                continue
            ranks[label][row['symbol']] = p['rank']
            old = baseline.get(label, {}).get(row['symbol'])
            p['rank_change'] = old - p['rank'] if old is not None else None
    return {'date': date, 'baseline_date': baseline_date, 'baseline': baseline, 'ranks': ranks}


def fmt(value):
    return 'N/A' if value is None else f'{value:.2f}'


def render_reports(rows, date, excluded, universe_count, baseline_date=None):
    note = (f'Price data: {date}. Universe: {universe_count}; ranked: {len(rows)}; '
            f'excluded: {len(excluded)}. NSE common equities; price > Rs50; market cap '
            'Rs1,000 crore to Rs5 lakh crore. Benchmark: NIFTY MIDSML 400. '
            'Windows: 5 / 21 / 63 / 126 benchmark trading sessions. '
            'RS% = 100 x [(stock end/start)/(benchmark end/start) - 1]. '
            'Leader: percentile >=90 and RS% >0. Percentiles use average ties on a '
            '0-100 scale (singleton=100); ranks use competition ties. '
            'Missing sessions/history show N/A per period; stale stocks are excluded. '
            'Rank change is previous available report rank minus current rank; '
            f'baseline price date: {baseline_date or "unavailable"}. '
            'Turnover is mean daily close x volume over 30 observed bars, in crore. '
            'No EMA or liquidity gate. Returns use local price history, not total returns; '
            'corporate-action adjustments have not been independently audited.')
    headers = ['Symbol', 'Industry', 'Close', 'Turnover30 Cr', 'Leaders', 'Available']
    for label in PERIODS:
        headers += [f'{label} Return%', f'{label} RS%', f'{label} Percentile', f'{label} Rank', f'{label} Change']

    def cells(row):
        values = [row['symbol'], row.get('industry', ''), fmt(row['close']), fmt(row['turnover_cr']),
                  str(row['leader_count']), str(row['available_periods'])]
        for label in PERIODS:
            p = row['periods'][label]
            values += ([fmt(p['return']), fmt(p['rs']), fmt(p['percentile']), str(p['rank']),
                        'N/A' if p['rank_change'] is None else f"{p['rank_change']:+d}"] if p else ['N/A'] * 5)
        return values

    def md_table(items):
        safe = lambda x: str(x).replace('|', '/').replace('\n', ' ')
        return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] +
                         ['| ' + ' | '.join(map(safe, cells(r))) + ' |' for r in items])

    md = [SEBI_MD_HEADER, f'# RS Leaders — {date}', note]
    for count in range(4, 0, -1):
        group = [r for r in rows if r['leader_count'] == count]
        md += [f'## {count}/4 leadership ({len(group)})', '```text',
               tv_csv(['NSE:' + r['symbol'] for r in group], label=f'RS {count} OF 4'), '```',
               md_table(group)]
    for label in PERIODS:
        ranked = sorted([r for r in rows if r['periods'][label]], key=lambda r: (r['periods'][label]['rank'], r['symbol']))
        leaders = [r for r in ranked if r['periods'][label]['leader']]
        md += [f'## {label} leaders ({len(leaders)}); eligible {len(ranked)}', '```text',
               tv_csv(['NSE:' + r['symbol'] for r in leaders], label=f'RS {label}'), '```',
               f'### {label} top 25 preview', md_table(ranked[:25])]
    md += ['## Full rankings', md_table(rows), '## Excluded symbols',
           '\n'.join(f'- {s}: {why}' for s, why in sorted(excluded.items())) or 'None.', SEBI_MD_FOOTER]

    html_rows = []
    for row in rows:
        tds = []
        for i, value in enumerate(cells(row)):
            content = escape(value)
            if i == 0:
                content = f'<a href="https://www.tradingview.com/chart/?symbol=NSE%3A{escape(row["symbol"], quote=True)}" target="_blank" rel="noopener">{content}</a>'
            tds.append(f'<td>{content}</td>')
        attrs = ' '.join(f'data-{k.lower()}="{int(bool(row["periods"][k] and row["periods"][k]["leader"]))}"' for k in PERIODS)
        html_rows.append(f'<tr data-count="{row["leader_count"]}" {attrs}>' + ''.join(tds) + '</tr>')
    watchlists = ''.join(f'<details><summary>{count}/4 TradingView watchlist</summary><textarea readonly>{escape(tv_csv(["NSE:" + r["symbol"] for r in rows if r["leader_count"] == count], label=f"RS {count} OF 4"))}</textarea></details>' for count in range(4, 0, -1))
    watchlists += ''.join(f'<details><summary>{label} leaders TradingView watchlist</summary><textarea readonly>{escape(tv_csv(["NSE:" + r["symbol"] for r in sorted(rows, key=lambda r: (r["periods"][label] or {}).get("rank", float("inf"))) if r["periods"][label] and r["periods"][label]["leader"]], label=f"RS {label}"))}</textarea></details>' for label in PERIODS)
    html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1"><title>RS Leaders</title>'
            '<style>body{font:15px system-ui;background:#111827;color:#e5e7eb;margin:20px}a{color:#67e8f9}'
            '.scroll{overflow:auto}table{border-collapse:collapse;width:100%}th,td{padding:9px;border-bottom:1px solid #374151;white-space:nowrap;text-align:right}'
            'th{background:#1f2937}th button{background:none;color:inherit;border:0;cursor:pointer;font:inherit}'
            'input,select{padding:9px;margin:8px}textarea{width:98%;height:75px}summary{cursor:pointer;padding:8px}</style></head><body>' +
            SEBI_HTML_BANNER + f'<h1>RS Leaders — {escape(date)}</h1><p>{escape(note)}</p>' + watchlists +
            '<label>Search <input id="search" oninput="filterRows()" placeholder="Symbol or industry"></label>'
            '<label>Leadership <select id="leaders" onchange="filterRows()"><option value="all">All stocks</option>' +
            ''.join(f'<option value="{n}">{n}/4</option>' for n in range(4, -1, -1)) +
            '</select></label><label>Period <select id="period" onchange="filterRows()"><option value="all">All periods</option>' +
            ''.join(f'<option value="{p.lower()}">{p} leaders</option>' for p in PERIODS) +
            '</select></label><p id="visible" aria-live="polite"></p><div class="scroll"><table><thead><tr>' +
            ''.join(f'<th><button onclick="sortTable({i})">{escape(h)}</button></th>' for i, h in enumerate(headers)) +
            '</tr></thead><tbody id="rankings">' + ''.join(html_rows) + '</tbody></table></div>' +
            '<details><summary>Excluded symbols</summary><pre>' + escape('\n'.join(f'{s}: {why}' for s, why in sorted(excluded.items())) or 'None') +
            '</pre></details>' + SEBI_HTML_FOOTER + '''<script>
let sortColumn=-1, ascending=true;
function filterRows(){
 const q=document.getElementById('search').value.toLowerCase();
 const count=document.getElementById('leaders').value;
 const period=document.getElementById('period').value;
 let shown=0;
 for(const r of document.querySelectorAll('#rankings tr')){
  r.hidden=!(r.textContent.toLowerCase().includes(q)&&(count==='all'||r.dataset.count===count)&&(period==='all'||r.dataset[period]==='1'));
  if(!r.hidden)shown++;
 }
 document.getElementById('visible').textContent=shown+' stocks shown';
}
function sortTable(column){
 ascending=sortColumn===column?!ascending:column<2;sortColumn=column;
 const body=document.getElementById('rankings');
 const rows=Array.from(body.rows);
 rows.sort((a,b)=>{
  const x=a.cells[column].textContent,y=b.cells[column].textContent;
  if(x==='N/A'||y==='N/A')return x===y?0:x==='N/A'?1:-1;
  const comparison=column<2?x.localeCompare(y):Number(x)-Number(y);
  return (ascending?1:-1)*comparison||a.cells[0].textContent.localeCompare(b.cells[0].textContent);
 });
 rows.forEach(r=>body.appendChild(r));
}
filterRows();
</script></body></html>''')
    return '\n\n'.join(md).rstrip() + '\n', html.rstrip() + '\n'


def get_universe():
    from tradingview_screener import Query, col
    count, frame = (Query().set_markets('india').select('name', 'industry', 'close')
                    .where(col('exchange') == 'NSE', col('type') == 'stock',
                           col('typespecs').has(['common']), col('close') > 50,
                           col('market_cap_basic').between(MC_LOW, MC_HIGH))
                    .limit(10000).get_scanner_data(timeout=45))
    if frame.empty or len(frame) < count:
        raise ValueError('empty or truncated TradingView universe; outputs preserved')
    return {str(r['name']): str(r['industry']) if pd.notna(r['industry']) else '' for _, r in frame.iterrows()}


def main():
    universe = get_universe()
    data = load_ohlc_many(list(universe) + [BENCHMARK], lookback=160)
    benchmark = data.pop(BENCHMARK, None)
    bench = close_series(benchmark)
    date = bench.index[-1].strftime('%Y-%m-%d')
    today = datetime.now(ZoneInfo('Asia/Kolkata')).date()
    if date != latest_date() or (today - bench.index[-1].date()).days > 4 or bench.index[-1].date() > today:
        raise ValueError(f'benchmark stale or inconsistent with local DB: {date}; outputs preserved')
    if len(bench) < 127:
        raise ValueError('benchmark needs 127 sessions for production rankings')
    rows, excluded = build_rankings({s: data.get(s) for s in universe}, benchmark)
    if not rows:
        raise ValueError('no usable stock histories; outputs preserved')
    for row in rows:
        row['industry'] = universe[row['symbol']]
    previous = json.loads(STATE_PATH.read_text(encoding='utf-8')) if STATE_PATH.exists() else None
    state = make_state(rows, date, previous)
    md, html = render_reports(rows, date, excluded, len(universe), state['baseline_date'])
    SCAN_DIR.mkdir(exist_ok=True)
    (ROOT / 'dashboard').mkdir(exist_ok=True)
    for path, content in [(SCAN_DIR / 'rs_leaders_latest.md', md),
                          (ROOT / 'dashboard' / 'rs_leaders.html', html),
                          (STATE_PATH, json.dumps(state, indent=2, allow_nan=False) + '\n')]:
        temp = path.with_suffix(path.suffix + '.tmp')
        with temp.open('w', encoding='utf-8', newline='\n') as fh:
            fh.write(content)
        temp.replace(path)
    print(f'RS Leaders: price data {date}; universe {len(universe)}; ranked {len(rows)}; excluded {len(excluded)}')
    for label in PERIODS:
        eligible = [r for r in rows if r['periods'][label] is not None]
        print(f'{label}: eligible {len(eligible)}, leaders {sum(r["periods"][label]["leader"] for r in eligible)}')


if __name__ == '__main__':
    main()
