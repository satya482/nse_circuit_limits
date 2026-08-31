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
from html import escape as _escape

import pandas as pd

from ohlc_db import load_ohlc_many
from disclaimer import SEBI_HTML_BANNER, SEBI_HTML_FOOTER
from wavetrend_scanner import WaveTrendCalculator

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
EMA55_MD = os.path.join(REPO_DIR, "ema55_cross_scans", "ema55_cross_scans.md")
OUTPUT_PATH = os.path.join(REPO_DIR, "dashboard", "union_charts.html")
INDUSTRY_CACHE = os.path.join(REPO_DIR, ".union_chart_cache", "industries.json")
TODAY = datetime.now().strftime("%Y-%m-%d")
MIN_BARS = 130
LOOKBACK = 600  # >= 6mo default view (~126 bars) + HIGH52W_PERIOD (260) warmup, so the 52W High line covers the entire default view
BENCH_SYM = "NIFTY MIDSML 400"
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
        raw_symbol = row.get("name")
        raw_industry = row.get("industry")
        if pd.isna(raw_symbol) or pd.isna(raw_industry):
            continue
        symbol = str(raw_symbol).strip()
        industry = str(raw_industry).strip()
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
        if not live:
            raise ValueError("TradingView returned no usable industry classifications")
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


RS_EMA_PERIOD = 9


def compute_rs_transition_kinds(df, bench_df) -> list[str | None]:
    """Daily RS Line (close / NIFTY MIDSML 400 close * 1000) crossing its own
    9-EMA -- parity with pine_scripts/Satya EMAs.txt's transition/
    transitionToWeak. Fail-open: missing or too-short benchmark data returns
    all-None so the chart still renders without this overlay."""
    n = len(df)
    none_kinds: list[str | None] = [None] * n
    if bench_df is None or len(bench_df) < RS_EMA_PERIOD + 2:
        return none_kinds
    try:
        stock_close = df.set_index("date")["close"].astype(float)
        bench_close = bench_df.set_index("date")["close"].astype(float)
        rs_line = (stock_close / bench_close.reindex(stock_close.index).ffill()) * 1000
        rs_ema9 = rs_line.ewm(span=RS_EMA_PERIOD, adjust=False).mean()
        prev_rs = rs_line.shift(1)
        prev_ema = rs_ema9.shift(1)
        crossover = (rs_line > rs_ema9) & (prev_rs <= prev_ema)
        crossunder = (rs_line < rs_ema9) & (prev_rs >= prev_ema)
    except Exception:
        return none_kinds
    kinds: list[str | None] = list(none_kinds)
    for i in range(n):
        if bool(crossover.iloc[i]):
            kinds[i] = "rs_weak_to_strong"
        elif bool(crossunder.iloc[i]):
            kinds[i] = "rs_strong_to_weak"
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


def build_chart_data(
    ohlc_map: dict,
    tiers: dict[str, str],
    industries: dict[str, str] | None = None,
    min_bars: int = MIN_BARS,
    symbol_exchange: dict[str, str] | None = None,
    bench_df=None,
) -> tuple[list[dict], int]:
    """Returns (records, skipped_count), records sorted by symbol.
    Skips symbols missing from ohlc_map or with fewer than min_bars rows.
    symbol_exchange optionally maps symbol -> TV exchange prefix (defaults
    to NSE) for building exchange-qualified TradingView chart links.
    bench_df (NIFTY MIDSML 400 OHLC) optionally enables per-bar RS Line vs
    its 9-EMA crossover/crossunder tagging (rs_signals); omitted or None
    yields an all-None rs_signals array so the chart still renders."""
    industries = industries or {}
    symbol_exchange = symbol_exchange or {}
    records = []
    skipped = 0
    for symbol, tier in sorted(tiers.items()):
        df = ohlc_map.get(symbol)
        if df is None or len(df) < min_bars:
            skipped += 1
            continue
        try:
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
            previous_close = bars[-2][4]
            day_change = (bars[-1][4] / previous_close - 1) * 100
            records.append({
                "symbol": symbol,
                "tier": tier,
                "tv_symbol": f"{symbol_exchange.get(symbol, 'NSE')}:{symbol}",
                "industry": industries.get(symbol, "Unclassified"),
                "day_change": day_change,
                "bars": bars,
                "signals": compute_signal_kinds(df),
                "coil_boxes": compute_coil_boxes(df),
                "rs_signals": compute_rs_transition_kinds(
                    df, bench_df if symbol_exchange.get(symbol, "NSE") == "NSE" else None
                ),
            })
        except Exception as exc:
            skipped += 1
            print(f"[union_chart_dashboard] skip {symbol}: annotation failure: {exc}")
    return records, skipped


_JS_TEMPLATE = """
const CHART_DATA = __DATA_JSON__;
const chartsBySymbol = {};
const recordBySymbol = {};
const SIGNAL_COLORS = { ppv: "#2962ff", wt_bull: "#76ff03", wt_bear: "#fdd835" };
const EMA_COLORS = ["#00bcd4", "#ff9800", "#e040fb", "#8bc34a", "#ff5252"];
const uiState = {
  emaVisible: false,
  zlema25Visible: false,
  high52wVisible: __HIGH52W_DEFAULT__,
  rsVisible: false,
  volumeVisible: false,
  interactive: false,
};
CHART_DATA.forEach(function(r) { recordBySymbol[r.symbol] = r; });

const DEFAULT_VIEW_MONTHS = 6;

function fixedLogicalRange(record) {
  const last = record.bars[record.bars.length - 1][0];
  const cutoffText = monthsCutoff(last, DEFAULT_VIEW_MONTHS);
  const firstIndex = record.bars.findIndex(function(bar) { return bar[0] >= cutoffText; });
  return {
    from: firstIndex >= 0 ? firstIndex : 0,
    to: record.bars.length - 1 + 15,
  };
}

function monthsCutoff(last, months) {
  const current = new Date(last + "T00:00:00Z");
  const sourceDay = current.getUTCDate();
  const targetMonthIndex = current.getUTCMonth() - months;
  const targetYear = current.getUTCFullYear() + Math.floor(targetMonthIndex / 12);
  const targetMonth = ((targetMonthIndex % 12) + 12) % 12;
  const lastDay = new Date(Date.UTC(targetYear, targetMonth + 1, 0)).getUTCDate();
  return new Date(
    Date.UTC(targetYear, targetMonth, Math.min(sourceDay, lastDay))
  ).toISOString().slice(0, 10);
}

function applyChartMode(entry) {
  entry.chart.applyOptions({
    handleScroll: {
      mouseWheel: false,
      pressedMouseMove: uiState.interactive,
      horzTouchDrag: uiState.interactive,
      vertTouchDrag: false,
    },
    handleScale: {
      axisPressedMouseMove: false,
      mouseWheel: false,
      pinch: uiState.interactive,
    },
  });
  if (!uiState.interactive) {
    entry.chart.timeScale().setVisibleLogicalRange(fixedLogicalRange(entry.record));
  }
}

const RS_DOT_COLORS = { rs_weak_to_strong: "lime", rs_strong_to_weak: "red" };
const RS_DOT_WIDTH_FRACTION = 0.6; // dot diameter as a fraction of bar spacing -- reads no wider than the candle body

function rsDotGeometry(record, dotSize, xForIndex, yForPrice) {
  const dots = [];
  (record.rs_signals || []).forEach(function(kind, i) {
    if (!kind) return;
    const bar = record.bars[i];
    const x = xForIndex(i);
    const y = yForPrice(kind === "rs_weak_to_strong" ? bar[3] : bar[2]);
    if (x === null || y === null) return;
    dots.push({
      left: x - dotSize / 2,
      top: kind === "rs_weak_to_strong" ? y + 2 : y - dotSize - 2,
      width: dotSize,
      height: dotSize,
      color: RS_DOT_COLORS[kind],
    });
  });
  return dots;
}

function candleData(record) {
  return record.bars.map(function(b, i) {
    const point = { time: b[0], open: b[1], high: b[2], low: b[3], close: b[4] };
    const color = SIGNAL_COLORS[(record.signals || [])[i]];
    if (color) {
      point.color = color;
      point.borderColor = color;
      point.wickColor = color;
    }
    return point;
  });
}

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

function computeZlema25(closes) {
  const period = 25;
  const lag = Math.floor((period - 1) / 2);
  const alpha = 2 / (period + 1);
  const out = new Array(closes.length).fill(null);
  let previous = null;
  for (let i = lag; i < closes.length; i++) {
    const adjusted = closes[i] + (closes[i] - closes[i - lag]);
    previous = previous === null
      ? adjusted
      : alpha * adjusted + (1 - alpha) * previous;
    out[i] = previous;
  }
  return out;
}

function zlema25LineData(record) {
  const values = computeZlema25(record.bars.map(function(b) { return b[4]; }));
  return record.bars.map(function(bar, index) {
    if (values[index] === null) return null;
    const rising = index > 0 && values[index - 1] !== null
      && values[index] > values[index - 1];
    return {
      time: bar[0],
      value: values[index],
      color: rising ? "#ffffff" : "#ff0000",
    };
  }).filter(Boolean);
}

const HIGH52W_PERIOD = 260; // daily bars, matches pine_scripts/52w_full_history.pine's auto-bars daily=260

function computeHigh52w(highs, period) {
  const out = new Array(highs.length).fill(null);
  for (let i = period - 1; i < highs.length; i++) {
    out[i] = Math.max.apply(null, highs.slice(i - period + 1, i + 1));
  }
  return out;
}

function nextWeekday(dateStr) {
  const d = new Date(dateStr + "T00:00:00Z");
  d.setUTCDate(d.getUTCDate() + 1);
  while (d.getUTCDay() === 0 || d.getUTCDay() === 6) {
    d.setUTCDate(d.getUTCDate() + 1);
  }
  return d.toISOString().slice(0, 10);
}

const HIGH52W_EXTEND_DAYS = 15; // project the last known 52w-high flat this many weekdays forward

function extendFlatWeekdays(points, count) {
  if (points.length === 0) return points;
  const last = points[points.length - 1];
  const extended = points.slice();
  let cursor = last.time;
  for (let i = 0; i < count; i++) {
    cursor = nextWeekday(cursor);
    extended.push({ time: cursor, value: last.value });
  }
  return extended;
}

function high52wLineData(record) {
  const highs = record.bars.map(function(b) { return b[2]; });
  const values = computeHigh52w(highs, HIGH52W_PERIOD);
  const points = record.bars.map(function(bar, index) {
    return values[index] === null ? null : { time: bar[0], value: values[index] };
  }).filter(Boolean);
  return extendFlatWeekdays(points, HIGH52W_EXTEND_DAYS);
}

function addEmaSeries(entry, periods) {
  if (!uiState.emaVisible) return [];
  const closes = entry.record.bars.map(function(b) { return b[4]; });
  return periods.map(function(period, index) {
    const line = entry.chart.addLineSeries({
      color: EMA_COLORS[index % EMA_COLORS.length],
      lineWidth: 1,
      lastValueVisible: false,
      priceLineVisible: false,
    });
    line.setData(emaLineData(entry.record.bars, closes, period));
    return line;
  });
}

function rebuildEmas(entry) {
  entry.emaSeries.forEach(function(line) { entry.chart.removeSeries(line); });
  entry.emaSeries = addEmaSeries(entry, getEmaPeriods());
}

function rebuildZlema25(entry) {
  if (entry.zlema25Series !== null) {
    entry.chart.removeSeries(entry.zlema25Series);
    entry.zlema25Series = null;
  }
  if (!uiState.zlema25Visible) return;
  const line = entry.chart.addLineSeries({
    lineWidth: 1,
    lineType: LightweightCharts.LineType.WithSteps,
    lastValueVisible: false,
    priceLineVisible: false,
  });
  line.setData(zlema25LineData(entry.record));
  entry.zlema25Series = line;
}

function rebuildHigh52w(entry) {
  if (entry.high52wSeries !== null) {
    entry.chart.removeSeries(entry.high52wSeries);
    entry.high52wSeries = null;
  }
  if (!uiState.high52wVisible) return;
  const line = entry.chart.addLineSeries({
    color: "#2962ff",
    lineWidth: 1,
    lineType: LightweightCharts.LineType.WithSteps,
    lastValueVisible: false,
    priceLineVisible: false,
  });
  line.setData(high52wLineData(entry.record));
  entry.high52wSeries = line;
}

function applyVolumeState(entry) {
  entry.volumeSeries.applyOptions({ visible: uiState.volumeVisible });
  entry.chart.priceScale("right").applyOptions({
    scaleMargins: uiState.volumeVisible
      ? { top: 0.05, bottom: 0.25 }
      : { top: 0.05, bottom: 0.05 },
  });
  entry.chart.priceScale("").applyOptions({
    scaleMargins: { top: 0.78, bottom: 0.00 },
  });
}

function redrawCoils(entry) {
  entry.coilLayer.replaceChildren();
  (entry.record.coil_boxes || []).forEach(function(box) {
    const left = entry.chart.timeScale().logicalToCoordinate(box.start_index);
    const right = entry.chart.timeScale().logicalToCoordinate(box.end_index);
    const top = entry.candleSeries.priceToCoordinate(box.high);
    const bottom = entry.candleSeries.priceToCoordinate(box.low);
    if ([left, right, top, bottom].some(function(v) { return v === null; })) return;
    const rect = document.createElement("div");
    rect.className = "coil-box";
    rect.style.left = Math.min(left, right) + "px";
    rect.style.width = Math.abs(right - left) + "px";
    rect.style.top = Math.min(top, bottom) + "px";
    rect.style.height = Math.abs(bottom - top) + "px";
    entry.coilLayer.appendChild(rect);
  });
  redrawRsDots(entry);
}

function redrawRsDots(entry) {
  if (!uiState.rsVisible) return;
  const spacing = Math.abs(
    entry.chart.timeScale().logicalToCoordinate(1) - entry.chart.timeScale().logicalToCoordinate(0)
  );
  const dotSize = Math.max(2, spacing * RS_DOT_WIDTH_FRACTION);
  const dots = rsDotGeometry(
    entry.record,
    dotSize,
    function(i) { return entry.chart.timeScale().logicalToCoordinate(i); },
    function(p) { return entry.candleSeries.priceToCoordinate(p); }
  );
  dots.forEach(function(g) {
    const dot = document.createElement("div");
    dot.className = "rs-dot";
    dot.style.left = g.left + "px";
    dot.style.top = g.top + "px";
    dot.style.width = g.width + "px";
    dot.style.height = g.height + "px";
    dot.style.background = g.color;
    entry.coilLayer.appendChild(dot);
  });
}

function scheduleCoilRedraw(entry) {
  if (entry.coilFrame !== null) cancelAnimationFrame(entry.coilFrame);
  entry.coilFrame = requestAnimationFrame(function() {
    entry.coilFrame = requestAnimationFrame(function() {
      entry.coilFrame = null;
      redrawCoils(entry);
    });
  });
}

function buildChart(symbol) {
  const el = document.getElementById('chart-' + symbol);
  if (!el || chartsBySymbol[symbol]) return;
  const record = recordBySymbol[symbol];
  const bars = record.bars;
  const chart = LightweightCharts.createChart(el, {
    height: el.clientHeight,
    layout: { background: { color: '#161b22' }, textColor: '#8b949e' },
    grid: { vertLines: { color: '#21262d' }, horzLines: { color: '#21262d' } },
  });
  const upColor = document.getElementById('upColor').value;
  const downColor = document.getElementById('downColor').value;
  const candleSeries = chart.addCandlestickSeries({
    upColor: upColor, downColor: downColor, borderVisible: false,
    wickUpColor: upColor, wickDownColor: downColor,
  });
  candleSeries.setData(candleData(record));
  const volumeSeries = chart.addHistogramSeries({
    priceFormat: { type: 'volume' }, priceScaleId: '', color: '#30363d',
  });
  volumeSeries.setData(bars.map(function(b) { return { time: b[0], value: b[5] }; }));
  const entry = {
    chart: chart,
    candleSeries: candleSeries,
    volumeSeries: volumeSeries,
    emaSeries: [],
    zlema25Series: null,
    high52wSeries: null,
    coilFrame: null,
    coilLayer: el.parentElement.querySelector('.coil-layer'),
    record: record,
  };
  chartsBySymbol[symbol] = entry;
  entry.emaSeries = addEmaSeries(entry, getEmaPeriods());
  rebuildZlema25(entry);
  rebuildHigh52w(entry);
  applyVolumeState(entry);
  scheduleCoilRedraw(entry);
  chart.timeScale().subscribeVisibleLogicalRangeChange(function() { scheduleCoilRedraw(entry); });
  new ResizeObserver(function() {
    chart.applyOptions({ width: el.clientWidth, height: el.clientHeight });
    scheduleCoilRedraw(entry);
  }).observe(el);
  applyChartMode(entry);
}

function applyControls() {
  const upColor = document.getElementById('upColor').value;
  const downColor = document.getElementById('downColor').value;
  Object.keys(chartsBySymbol).forEach(function(symbol) {
    const entry = chartsBySymbol[symbol];
    entry.candleSeries.applyOptions({
      upColor: upColor, downColor: downColor, wickUpColor: upColor, wickDownColor: downColor,
    });
    rebuildEmas(entry);
    redrawCoils(entry);
  });
}

document.getElementById('upColor').addEventListener('input', applyControls);
document.getElementById('downColor').addEventListener('input', applyControls);
document.getElementById('emaPeriods').addEventListener('change', applyControls);
document.getElementById('emaVisible').addEventListener('change', function(e) {
  uiState.emaVisible = e.target.checked;
  Object.keys(chartsBySymbol).forEach(function(symbol) {
    const entry = chartsBySymbol[symbol];
    rebuildEmas(entry);
    redrawCoils(entry);
  });
});
document.getElementById('zlema25Visible').addEventListener('change', function(e) {
  uiState.zlema25Visible = e.target.checked;
  Object.keys(chartsBySymbol).forEach(function(symbol) {
    const entry = chartsBySymbol[symbol];
    rebuildZlema25(entry);
    scheduleCoilRedraw(entry);
  });
});
document.getElementById('rsVisible').addEventListener('change', function(e) {
  uiState.rsVisible = e.target.checked;
  Object.keys(chartsBySymbol).forEach(function(symbol) {
    const entry = chartsBySymbol[symbol];
    scheduleCoilRedraw(entry);
  });
});
document.getElementById('high52wVisible').addEventListener('change', function(e) {
  uiState.high52wVisible = e.target.checked;
  Object.keys(chartsBySymbol).forEach(function(symbol) {
    const entry = chartsBySymbol[symbol];
    rebuildHigh52w(entry);
    scheduleCoilRedraw(entry);
  });
});
document.getElementById('volumeVisible').addEventListener('change', function(e) {
  uiState.volumeVisible = e.target.checked;
  Object.keys(chartsBySymbol).forEach(function(symbol) {
    const entry = chartsBySymbol[symbol];
    applyVolumeState(entry);
    redrawCoils(entry);
  });
});
document.getElementById('chartMode').addEventListener('change', function(e) {
  uiState.interactive = e.target.checked;
  Object.keys(chartsBySymbol).forEach(function(symbol) {
    applyChartMode(chartsBySymbol[symbol]);
  });
});

function cardCompare(a, b, direction) {
  const delta = Number(a.dataset.dayChange) - Number(b.dataset.dayChange);
  if (delta !== 0) return direction * delta;
  return a.dataset.symbol.localeCompare(b.dataset.symbol);
}

const GROUP_SORT = "__GROUP_SORT__";

function applySortAndFilter() {
  const mode = document.getElementById("sortMode").value;
  const query = document.getElementById("q").value.toLowerCase();
  const cards = Array.from(document.querySelectorAll("#grid .card"));
  const fragment = document.createDocumentFragment();
  document.querySelectorAll("#grid .industry-heading").forEach(function(h) { h.remove(); });
  cards.forEach(function(card) {
    card.hidden = card.dataset.q.toLowerCase().indexOf(query) === -1;
  });
  if (mode === "industry") {
    const groups = {};
    cards.forEach(function(card) {
      (groups[card.dataset.industry] ||= []).push(card);
    });
    Object.keys(groups).sort(function(a, b) {
      if (a === "Unclassified") return 1;
      if (b === "Unclassified") return -1;
      return a.localeCompare(b);
    }).forEach(function(industry) {
      const heading = document.createElement("h2");
      heading.className = "industry-heading";
      heading.textContent = industry;
      const groupCards = groups[industry].sort(function(a, b) {
        return GROUP_SORT === "alpha"
          ? a.dataset.symbol.localeCompare(b.dataset.symbol)
          : cardCompare(a, b, -1);
      });
      heading.hidden = groupCards.every(function(card) { return card.hidden; });
      fragment.appendChild(heading);
      groupCards.forEach(function(card) { fragment.appendChild(card); });
    });
  } else {
    const direction = mode === "day-desc" ? -1 : 1;
    cards.sort(function(a, b) { return cardCompare(a, b, direction); })
      .forEach(function(card) { fragment.appendChild(card); });
  }
  document.getElementById("grid").appendChild(fragment);
}

document.getElementById('sortMode').addEventListener('change', applySortAndFilter);
document.getElementById('q').addEventListener('input', applySortAndFilter);
applySortAndFilter();

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


def build_html(
    records: list[dict],
    as_of: str,
    title: str = "Union Watchlist Charts",
    group_sort: str = "day-desc",
    high52w_default_visible: bool = False,
) -> str:
    data_json = (
        json.dumps(records)
        .replace("&", r"\u0026")
        .replace("<", r"\u003c")
        .replace(">", r"\u003e")
    )
    js = (
        _JS_TEMPLATE.replace("__DATA_JSON__", data_json)
        .replace("__GROUP_SORT__", group_sort)
        .replace("__HIGH52W_DEFAULT__", "true" if high52w_default_visible else "false")
    )

    if records:
        cards = []
        for r in records:
            change = float(r["day_change"])
            change_class = "gain" if change > 0 else "loss" if change < 0 else "flat"
            change_text = f"{change:+.2f}%" if change else "0.00%"
            tv_symbol = r.get("tv_symbol") or f"NSE:{r['symbol']}"
            cards.append(
                f'<div class="card" data-q="{_escape(r["symbol"])} {_escape(r["tier"])}" '
                f'data-symbol="{_escape(r["symbol"])}" '
                f'data-industry="{_escape(r["industry"])}" data-day-change="{change}">'
                f'<div class="hdr"><span class="day-change {change_class}">{change_text}</span>'
                f'<span class="tier">{_escape(r["tier"])}</span>'
                f'<a class="symbol-link" href="https://in.tradingview.com/chart/?symbol={_escape(tv_symbol)}" '
                f'target="_blank" rel="noopener noreferrer">{_escape(r["symbol"])}</a></div>'
                f'<div class="chart-wrap"><div class="chart" id="chart-{_escape(r["symbol"])}"></div>'
                f'<div class="coil-layer"></div></div></div>'
            )
        cards = "\n".join(cards)
    else:
        cards = '<p class="empty">No signals.</p>'

    return f"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} - {as_of}</title>
<script src="vendor/lightweight-charts.js"></script>
<style>
:root{{color-scheme:dark}}
body{{background:#0d1117;color:#e6edf3;font-family:system-ui,sans-serif;margin:0;padding:12px}}
h1{{font-size:1.1rem}}
#controls{{position:sticky;top:0;z-index:20;display:flex;flex-wrap:wrap;gap:12px;align-items:center;background:#161b22;border:1px solid #30363d;border-radius:6px;padding:10px;margin:8px 0}}
#controls label{{font-size:.85rem;color:#8b949e;display:flex;align-items:center;gap:4px}}
#controls input[type=text]{{background:#0d1117;color:#e6edf3;border:1px solid #30363d;border-radius:4px;padding:4px 6px;width:120px}}
#q{{width:100%;box-sizing:border-box;padding:8px;margin:8px 0;background:#161b22;color:#e6edf3;border:1px solid #30363d;border-radius:6px}}
#grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,520px),1fr));gap:10px}}
.industry-heading{{grid-column:1/-1;margin:14px 0 0}}
.card{{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:8px}}
.hdr{{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;font-weight:600;margin-bottom:6px}}
.symbol-link{{justify-self:end;min-height:44px;display:inline-flex;align-items:center;padding-left:12px;color:#58a6ff;text-decoration:none}}
.symbol-link:focus-visible{{outline:2px solid #58a6ff;outline-offset:2px}}
.tier{{justify-self:center;font-size:.7rem;color:#8b949e;border:1px solid #30363d;border-radius:4px;padding:1px 6px}}
.day-change{{justify-self:start;font-size:.8rem}}
.day-change.gain{{color:#3fb950}}.day-change.loss{{color:#f85149}}.day-change.flat{{color:#8b949e}}
.switch-row{{cursor:pointer}}
.switch-row input{{position:absolute;opacity:0}}
.switch{{width:30px;height:16px;border-radius:10px;background:#30363d;position:relative}}
.switch::after{{content:"";width:12px;height:12px;border-radius:50%;background:#8b949e;position:absolute;top:2px;left:2px;transition:left .15s}}
.switch-row input:checked + .switch{{background:#238636}}
.switch-row input:checked + .switch::after{{left:16px;background:#fff}}
.chart-wrap{{position:relative;overflow:hidden}}
.chart{{height:clamp(380px,44vw,520px)}}
.coil-layer{{position:absolute;inset:0;z-index:2;pointer-events:none}}
.coil-box{{position:absolute;box-sizing:border-box;border:1px solid #808080;background:rgba(128,128,128,.10)}}
.rs-dot{{position:absolute;border-radius:50%}}
.empty{{color:#8b949e}}
@media(max-width:600px){{#grid{{grid-template-columns:1fr}}.chart{{height:380px}}}}
</style></head>
<body>
{SEBI_HTML_BANNER}
<h1>{title} - {as_of}</h1>
<div id="controls">
  <label>Up color <input type="color" id="upColor" value="#26a69a"></label>
  <label>Down color <input type="color" id="downColor" value="#ef5350"></label>
  <label>EMAs <input type="text" id="emaPeriods" value="20,50,200"></label>
  <label class="switch-row"><span>EMAs</span><input type="checkbox" id="emaVisible"><span class="switch"></span></label>
  <label class="switch-row"><span>ZLEMA25</span><input type="checkbox" id="zlema25Visible"><span class="switch"></span></label>
  <label class="switch-row"><span>52W High</span><input type="checkbox" id="high52wVisible"{" checked" if high52w_default_visible else ""}><span class="switch"></span></label>
  <label class="switch-row"><span>RS Transitions</span><input type="checkbox" id="rsVisible"><span class="switch"></span></label>
  <label class="switch-row"><span>Volume</span><input type="checkbox" id="volumeVisible"><span class="switch"></span></label>
  <label class="switch-row"><span>Interactive</span><input type="checkbox" id="chartMode"><span class="switch"></span></label>
  <label>Sort <select id="sortMode">
    <option value="industry" selected>Industry groups</option>
    <option value="day-desc">Day change: highest first</option>
    <option value="day-asc">Day change: lowest first</option>
  </select></label>
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

    industries = resolve_industries(tiers.keys(), INDUSTRY_CACHE, TODAY)
    ohlc_map = load_ohlc_many(list(tiers.keys()), lookback=LOOKBACK)
    bench_df = load_ohlc_many([BENCH_SYM], lookback=LOOKBACK).get(BENCH_SYM)
    records, skipped = build_chart_data(ohlc_map, tiers, industries=industries, bench_df=bench_df)
    print(
        f"[union_chart_dashboard] {len(records)} charted, {skipped} skipped "
        f"(insufficient OHLCV or annotation failure)"
    )

    if tiers and not records:
        print("[union_chart_dashboard] SKIP: 0 symbols charted (OHLC data unavailable) -- not overwriting existing dashboard")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    html = build_html(records, TODAY)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
