#!/usr/bin/env python3
"""
Union Watchlist Chart Dashboard
Run after run_ema55_cross_scanner.ps1 (needs today's union watchlist written).

Plots every symbol in the EMA55 union watchlist (ema55_cross_scans.md) as an
interactive candlestick+volume chart, with live client-side controls for
candle color and EMA overlay periods.

Data source: .ohlc_data/market.db (via ohlc_db.load_ohlc_many)
Symbol source: ema55_cross_scans/ema55_cross_scans.md (union tv-paste block)
Output: dashboard/union_charts.html
"""

import json
import os
import re
from datetime import datetime

from ohlc_db import load_ohlc_many
from disclaimer import SEBI_HTML_BANNER, SEBI_HTML_FOOTER

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
EMA55_MD = os.path.join(REPO_DIR, "ema55_cross_scans", "ema55_cross_scans.md")
OUTPUT_PATH = os.path.join(REPO_DIR, "dashboard", "union_charts.html")
TODAY = datetime.now().strftime("%Y-%m-%d")
MIN_BARS = 130
LOOKBACK = 250
SKIP_LABELS = {"INDICES", "COMMODITIES"}
INDEX_ANCHORS = {"NIFTYSMLCAP250", "NIFTYMIDSML400"}


def parse_union_tiers(md_text: str) -> dict[str, str]:
    """Symbol -> confluence tier label, from the first fenced TV-paste block
    in ema55_cross_scans.md (the Union Watchlist block, at the top of the
    file). Mirrors ema55_cross_scanner._symbols_from_tv_block's section-split
    and anchor-exclusion logic, but keeps the tier label per symbol instead
    of discarding it into a flat set."""
    m = re.search(r"```\n(.*?)\n```", md_text, re.S)
    if not m:
        return {}
    tiers: dict[str, str] = {}
    for section in m.group(1).split("###")[1:]:
        label, _, rest = section.partition(",")
        label = label.strip()
        if label.upper() in SKIP_LABELS:
            continue
        for tok in rest.split(","):
            tok = tok.strip()
            if tok.startswith("NSE:") and tok[4:] not in INDEX_ANCHORS:
                tiers[tok[4:]] = label
    return tiers


def load_todays_union(md_path: str, today: str) -> tuple[dict[str, str] | None, str | None]:
    """Returns (tiers, None) if today's union data is present and fresh,
    else (None, reason)."""
    if not os.path.exists(md_path):
        return None, f"{md_path} not found"
    with open(md_path, encoding="utf-8") as fh:
        md = fh.read()
    if not re.search(rf"^#\s.*{re.escape(today)}", md, re.MULTILINE):
        return None, f"{md_path} stale (not today's date)"
    tiers = parse_union_tiers(md)
    if not tiers:
        return None, f"{md_path} has no union watchlist data"
    return tiers, None


def build_chart_data(ohlc_map: dict, tiers: dict[str, str], min_bars: int = MIN_BARS) -> tuple[list[dict], int]:
    """Returns (records, skipped_count), records sorted by symbol.
    Skips symbols missing from ohlc_map or with fewer than min_bars rows."""
    records = []
    skipped = 0
    for symbol, tier in sorted(tiers.items()):
        df = ohlc_map.get(symbol)
        if df is None or len(df) < min_bars:
            skipped += 1
            continue
        bars = [
            [
                row.date.strftime("%Y-%m-%d"),
                float(row.open),
                float(row.high),
                float(row.low),
                float(row.close),
                float(row.volume),
            ]
            for row in df.itertuples(index=False)
        ]
        records.append({"symbol": symbol, "tier": tier, "bars": bars})
    return records, skipped


_JS_TEMPLATE = """
const CHART_DATA = __DATA_JSON__;
const chartsBySymbol = {};
const dataBySymbol = {};
CHART_DATA.forEach(function(r) { dataBySymbol[r.symbol] = r.bars; });

function computeEMA(closes, period) {
  const k = 2 / (period + 1);
  const out = new Array(closes.length).fill(null);
  if (closes.length < period) return out;
  let sma = 0;
  for (let i = 0; i < period; i++) sma += closes[i];
  sma /= period;
  out[period - 1] = sma;
  let prev = sma;
  for (let i = period; i < closes.length; i++) {
    prev = closes[i] * k + prev * (1 - k);
    out[i] = prev;
  }
  return out;
}

function getEmaPeriods() {
  return document.getElementById('emaPeriods').value
    .split(',').map(function(s) { return parseInt(s.trim(), 10); })
    .filter(function(n) { return n > 0; });
}

function emaLineData(bars, closes, period) {
  const ema = computeEMA(closes, period);
  return bars.map(function(b, i) {
    return ema[i] === null ? null : { time: b[0], value: ema[i] };
  }).filter(Boolean);
}

function buildChart(symbol) {
  const el = document.getElementById('chart-' + symbol);
  if (!el || chartsBySymbol[symbol]) return;
  const bars = dataBySymbol[symbol];
  const chart = LightweightCharts.createChart(el, {
    height: 220,
    layout: { background: { color: '#161b22' }, textColor: '#8b949e' },
    grid: { vertLines: { color: '#21262d' }, horzLines: { color: '#21262d' } },
  });
  const upColor = document.getElementById('upColor').value;
  const downColor = document.getElementById('downColor').value;
  const candleSeries = chart.addCandlestickSeries({
    upColor: upColor, downColor: downColor, borderVisible: false,
    wickUpColor: upColor, wickDownColor: downColor,
  });
  candleSeries.setData(bars.map(function(b) {
    return { time: b[0], open: b[1], high: b[2], low: b[3], close: b[4] };
  }));
  const volumeSeries = chart.addHistogramSeries({
    priceFormat: { type: 'volume' }, priceScaleId: '', color: '#30363d',
  });
  volumeSeries.setData(bars.map(function(b) { return { time: b[0], value: b[5] }; }));
  const closes = bars.map(function(b) { return b[4]; });
  const emaSeries = getEmaPeriods().map(function(period) {
    const line = chart.addLineSeries({ lineWidth: 1 });
    line.setData(emaLineData(bars, closes, period));
    return line;
  });
  chartsBySymbol[symbol] = { chart: chart, candleSeries: candleSeries, volumeSeries: volumeSeries, emaSeries: emaSeries };
}

function applyControls() {
  const upColor = document.getElementById('upColor').value;
  const downColor = document.getElementById('downColor').value;
  const periods = getEmaPeriods();
  Object.keys(chartsBySymbol).forEach(function(symbol) {
    const entry = chartsBySymbol[symbol];
    entry.candleSeries.applyOptions({
      upColor: upColor, downColor: downColor, wickUpColor: upColor, wickDownColor: downColor,
    });
    entry.emaSeries.forEach(function(line) { entry.chart.removeSeries(line); });
    const bars = dataBySymbol[symbol];
    const closes = bars.map(function(b) { return b[4]; });
    entry.emaSeries = periods.map(function(period) {
      const line = entry.chart.addLineSeries({ lineWidth: 1 });
      line.setData(emaLineData(bars, closes, period));
      return line;
    });
  });
}

document.getElementById('upColor').addEventListener('input', applyControls);
document.getElementById('downColor').addEventListener('input', applyControls);
document.getElementById('emaPeriods').addEventListener('change', applyControls);

document.getElementById('q').addEventListener('input', function(e) {
  const q = e.target.value.toLowerCase();
  document.querySelectorAll('#grid .card').forEach(function(c) {
    c.style.display = c.dataset.q.toLowerCase().indexOf(q) !== -1 ? '' : 'none';
  });
});

const observer = new IntersectionObserver(function(entries) {
  entries.forEach(function(entry) {
    if (entry.isIntersecting) {
      buildChart(entry.target.dataset.symbol);
      observer.unobserve(entry.target);
    }
  });
}, { rootMargin: '200px' });

document.querySelectorAll('#grid .card').forEach(function(c) { observer.observe(c); });
"""


def build_html(records: list[dict], as_of: str) -> str:
    data_json = json.dumps(records)
    js = _JS_TEMPLATE.replace("__DATA_JSON__", data_json)

    if records:
        cards = "\n".join(
            f'<div class="card" data-q="{r["symbol"]} {r["tier"]}" data-symbol="{r["symbol"]}">'
            f'<div class="hdr"><a href="https://in.tradingview.com/chart/?symbol=NSE:{r["symbol"]}" '
            f'target="_blank">{r["symbol"]}</a><span class="tier">{r["tier"]}</span></div>'
            f'<div class="chart" id="chart-{r["symbol"]}"></div>'
            f"</div>"
            for r in records
        )
    else:
        cards = '<p class="empty">No signals.</p>'

    return f"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Union Watchlist Charts - {as_of}</title>
<script src="vendor/lightweight-charts.js"></script>
<style>
:root{{color-scheme:dark}}
body{{background:#0d1117;color:#e6edf3;font-family:system-ui,sans-serif;margin:0;padding:12px}}
h1{{font-size:1.1rem}}
#controls{{display:flex;flex-wrap:wrap;gap:12px;align-items:center;background:#161b22;border:1px solid #30363d;border-radius:6px;padding:10px;margin:8px 0}}
#controls label{{font-size:.85rem;color:#8b949e;display:flex;align-items:center;gap:4px}}
#controls input[type=text]{{background:#0d1117;color:#e6edf3;border:1px solid #30363d;border-radius:4px;padding:4px 6px;width:120px}}
#q{{width:100%;box-sizing:border-box;padding:8px;margin:8px 0;background:#161b22;color:#e6edf3;border:1px solid #30363d;border-radius:6px}}
#grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:10px}}
.card{{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:8px}}
.hdr{{display:flex;justify-content:space-between;align-items:center;font-weight:600;margin-bottom:6px}}
.hdr a{{color:#58a6ff;text-decoration:none}}
.tier{{font-size:.7rem;color:#8b949e;border:1px solid #30363d;border-radius:4px;padding:1px 6px}}
.chart{{height:220px}}
.empty{{color:#8b949e}}
</style></head>
<body>
{SEBI_HTML_BANNER}
<h1>Union Watchlist Charts - {as_of}</h1>
<div id="controls">
  <label>Up color <input type="color" id="upColor" value="#26a69a"></label>
  <label>Down color <input type="color" id="downColor" value="#ef5350"></label>
  <label>EMAs <input type="text" id="emaPeriods" value="20,50,200"></label>
</div>
<input id="q" placeholder="Filter by symbol / tier">
<div id="grid">
{cards}
</div>
{SEBI_HTML_FOOTER}
<script>
{js}
</script>
</body></html>
"""


def main() -> None:
    tiers, err = load_todays_union(EMA55_MD, TODAY)
    if err:
        print(f"[union_chart_dashboard] SKIP: {err}")
        return

    ohlc_map = load_ohlc_many(list(tiers.keys()), lookback=LOOKBACK)
    records, skipped = build_chart_data(ohlc_map, tiers)
    print(f"[union_chart_dashboard] {len(records)} charted, {skipped} skipped (< {MIN_BARS} bars)")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    html = build_html(records, TODAY)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(html)


if __name__ == "__main__":
    main()
