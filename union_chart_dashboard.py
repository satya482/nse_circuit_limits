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
from wavetrend_scanner import WaveTrendCalculator

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
EMA55_MD = os.path.join(REPO_DIR, "ema55_cross_scans", "ema55_cross_scans.md")
OUTPUT_PATH = os.path.join(REPO_DIR, "dashboard", "union_charts.html")
INDUSTRY_CACHE = os.path.join(REPO_DIR, ".union_chart_cache", "industries.json")
TODAY = datetime.now().strftime("%Y-%m-%d")
MIN_BARS = 130
LOOKBACK = 250
SKIP_LABELS = {"INDICES", "COMMODITIES"}
INDEX_ANCHORS = {"NIFTYSMLCAP250", "NIFTYMIDSML400"}
TIER_LABEL_RE = re.compile(r"^(ALL \d+|\d+ OF \d+|1 ONLY)$")


def fetch_tradingview_industries(symbols: set[str]) -> dict[str, str]:
    from tradingview_screener import Query, col

    _, df = (
        Query()
        .set_markets("india")
        .select("name", "industry")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
        )
        .limit(5000)
        .get_scanner_data()
    )
    result = {}
    for row in df.to_dict("records"):
        symbol = str(row.get("name") or "").strip()
        industry = str(row.get("industry") or "").strip()
        if symbol in symbols and industry:
            result[symbol] = industry
    return result


def resolve_industries(symbols, cache_path, as_of, fetcher=fetch_tradingview_industries):
    cached = {}
    try:
        with open(cache_path, encoding="utf-8") as fh:
            payload = json.load(fh)
        raw_cached = payload.get("industries", {}) if isinstance(payload, dict) else {}
        if isinstance(raw_cached, dict):
            cached = {
                key.strip(): value.strip()
                for key, value in raw_cached.items()
                if isinstance(key, str)
                and key.strip()
                and isinstance(value, str)
                and value.strip()
            }
    except (FileNotFoundError, OSError, ValueError, TypeError):
        cached = {}
    try:
        live = {
            key.strip(): value.strip()
            for key, value in fetcher(set(symbols)).items()
            if isinstance(key, str)
            and key.strip()
            and isinstance(value, str)
            and value.strip()
        }
        merged = {**cached, **live}
        cache_dir = os.path.dirname(cache_path)
        if cache_dir:
            os.makedirs(cache_dir, exist_ok=True)
        tmp = cache_path + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"as_of": as_of, "industries": dict(sorted(merged.items()))}, fh)
            fh.write("\n")
        os.replace(tmp, cache_path)
        cached = merged
    except Exception as exc:
        print(f"[union_chart_dashboard] industry refresh fallback: {exc}")
    return {symbol: cached.get(symbol, "Unclassified") for symbol in sorted(symbols)}


def compute_pocket_pivot_flags(df, pp_len: int = 10) -> list[bool]:
    close = df["close"].astype(float).tolist()
    volume = df["volume"].astype(float).tolist()
    flags = [False] * len(df)
    for i in range(1, len(df)):
        if close[i] <= close[i - 1]:
            continue
        down_volumes = []
        for j in range(i - 1, 0, -1):
            if close[j] < close[j - 1]:
                down_volumes.append(volume[j])
                if len(down_volumes) == pp_len:
                    break
        flags[i] = (
            len(down_volumes) == pp_len
            and volume[i] > max(down_volumes)
        )
    return flags


def compute_wavetrend_kinds(df) -> list[str | None]:
    hlc3 = (
        df["high"].astype(float)
        + df["low"].astype(float)
        + df["close"].astype(float)
    ) / 3
    cross_type = WaveTrendCalculator().calc_from_series(hlc3)["cross_type"]
    mapping = {"BULL_CROSS": "wt_bull", "BEAR_CROSS": "wt_bear", "NONE": None}
    return cross_type.map(mapping).tolist()


def compute_signal_kinds(df) -> list[str | None]:
    kinds = ["ppv" if flag else None for flag in compute_pocket_pivot_flags(df)]
    for i, wt_kind in enumerate(compute_wavetrend_kinds(df)):
        if wt_kind is not None:
            kinds[i] = wt_kind
    return kinds


def compute_coil_boxes(
    df,
    min_inside: int = 2,
    extend_bars: int = 15,
) -> list[dict]:
    high = df["high"].astype(float).tolist()
    low = df["low"].astype(float).tolist()
    boxes = []
    for confirm in range(min_inside, len(df)):
        mother = confirm - min_inside
        contained = all(
            high[i] <= high[mother] and low[i] >= low[mother]
            for i in range(mother + 1, confirm + 1)
        )
        if not contained:
            continue
        box = {
            "start_index": mother,
            "end_index": confirm + extend_bars,
            "high": high[mother],
            "low": low[mother],
        }
        if boxes and box["start_index"] <= boxes[-1]["end_index"]:
            boxes.pop()
        boxes.append(box)
    return boxes


def parse_union_tiers(md_text: str) -> dict[str, str]:
    """Symbol -> confluence tier label, from the first fenced TV-paste block
    in ema55_cross_scans.md (the Union Watchlist block, at the top of the
    file). Mirrors ema55_cross_scanner._symbols_from_tv_block's section-split
    and anchor-exclusion logic, but keeps the tier label per symbol instead
    of discarding it into a flat set. Sections whose label isn't a real
    confluence tier (ALL n / n OF n / 1 ONLY) are dropped -- this guards
    against silently harvesting the wrong fenced block (e.g. EMA55's own
    cross-age TV block) on days the union section renders no fence at all."""
    m = re.search(r"```\n(.*?)\n```", md_text, re.S)
    if not m:
        return {}
    tiers: dict[str, str] = {}
    for section in m.group(1).split("###")[1:]:
        label, _, rest = section.partition(",")
        label = label.strip()
        if label.upper() in SKIP_LABELS or not TIER_LABEL_RE.match(label):
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

    if tiers and not records:
        print("[union_chart_dashboard] SKIP: 0 symbols charted (OHLC data unavailable) -- not overwriting existing dashboard")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    html = build_html(records, TODAY)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as fh:
        fh.write(html)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
