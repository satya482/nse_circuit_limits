#!/usr/bin/env python3
"""
NSE Breadth Monitor — regime/timing layer (not a candidate-selection scanner).

Answers: "is the market environment supportive right now?"
Accumulates a rolling time series; one row per (date, universe_tag) in breadth_history.csv.

Interface deviation from other scanners: this module accumulates a time series rather
than emitting per-day candidate lists. Deliberate — documented here and in CLAUDE.md.
"""

import sys
import argparse
from datetime import date, datetime, timezone, timedelta
from pathlib import Path

import pandas as pd

REPO_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_DIR))

from ohlc_db import load_ohlc, load_ohlc_many  # noqa: E402

IST = timezone(timedelta(hours=5, minutes=30))

UNIVERSE_TAG = "breadth_broad"
THRUST_THRESHOLD = (
    1.6  # TODO: validate against >=1yr NSE history before treating as production signal
)
CAPITULATION_THRESHOLD = (
    0.6  # TODO: validate against >=1yr NSE history before treating as production signal
)
HISTORY_PATH = REPO_DIR / "data" / "breadth_history.csv"
UNIVERSE_PATH = REPO_DIR / "data" / "breadth_universe.csv"
DASHBOARD_PATH = REPO_DIR / "dashboard" / "nse_breadth_monitor.html"
NIFTY50_SYM = "NIFTY 50"
OHLC_LOOKBACK = 2500  # ~10yr trading bars

_CSV_COLUMNS = [
    "date",
    "universe_tag",
    "total_eligible",
    "up4_count",
    "down4_count",
    "ratio_5d",
    "ratio_10d",
    "up25_quarter",
    "down25_quarter",
    "pct_above_sma200",
    "composite_score",
]


def compute_daily_breadth(
    universe_df: pd.DataFrame,
    as_of: date,
    ohlc_map: dict[str, pd.DataFrame],
) -> dict | None:
    """Single-day breadth snapshot. Pure function, no I/O.

    as_of strictly bounds all calculations — never reads closes after as_of.
    Returns None when as_of is not present as a trading date in ohlc_map.
    Circuit-frozen (v1): excluded if close == prev_close AND volume == 0.
    """
    as_of_str = as_of.strftime("%Y-%m-%d")

    # Filter ohlc_map to universe symbols only — prevents benchmark or other
    # non-universe symbols in SQLite from being silently counted in breadth metrics
    universe_syms = set(universe_df["symbol"].tolist())
    ohlc_map = {s: df for s, df in ohlc_map.items() if s in universe_syms}

    # Collect all trading dates up to as_of to build ratio window
    all_dates: set[str] = set()
    for df in ohlc_map.values():
        date_strs = df["date"].dt.strftime("%Y-%m-%d")
        all_dates.update(d for d in date_strs if d <= as_of_str)

    sorted_dates = sorted(all_dates)
    if not sorted_dates or as_of_str not in sorted_dates:
        return None  # as_of is not a trading day in this dataset

    # Window: last 10 trading dates (ratio_10d uses all 10; ratio_5d uses last 5)
    window_10 = sorted_dates[-10:]
    window_set = set(window_10)

    # Per-date accumulators for ratio computation
    up4: dict[str, int] = {d: 0 for d in window_10}
    dn4: dict[str, int] = {d: 0 for d in window_10}

    # as_of-specific accumulators
    total_eligible = 0
    up25 = 0
    dn25 = 0
    above_sma200 = 0
    elig_sma200 = 0

    for sym, df in ohlc_map.items():
        # Filter strictly to as_of and before
        mask = df["date"].dt.strftime("%Y-%m-%d") <= as_of_str
        df_s = df[mask].reset_index(drop=True)
        if len(df_s) < 2:
            continue

        closes = df_s["close"].astype(float).values
        volumes = df_s["volume"].astype(float).values
        dates_arr = df_s["date"].dt.strftime("%Y-%m-%d").values

        # Stock must have a row on as_of
        if dates_arr[-1] != as_of_str:
            continue

        date_to_pos = {d: i for i, d in enumerate(dates_arr)}

        # Per-date up4/dn4 for the ratio window
        for target_d in window_set:
            if target_d not in date_to_pos:
                continue
            pos = date_to_pos[target_d]
            if pos == 0:
                continue
            c, pc, v = closes[pos], closes[pos - 1], volumes[pos]
            if c == pc and v == 0:  # circuit-frozen: skip
                continue
            pct = c / pc - 1
            if pct >= 0.04:
                up4[target_d] += 1
            if pct <= -0.04:
                dn4[target_d] += 1

        # as_of row metrics
        today_close = closes[-1]
        today_vol = volumes[-1]
        prev_close = closes[-2]

        if today_close == prev_close and today_vol == 0:  # circuit-frozen
            continue

        total_eligible += 1

        # pct_63d — exclude stocks with <64 bars from quarterly calc only
        if len(df_s) >= 64:
            pct_63d = today_close / closes[-64] - 1
            if pct_63d >= 0.25:
                up25 += 1
            if pct_63d <= -0.25:
                dn25 += 1

        # SMA200 — plain SMA, min_periods=200
        # Known limitation: circuit-gap days distort plain SMA. Flagged, deferred to v1.1.
        if len(df_s) >= 200:
            elig_sma200 += 1
            if today_close > closes[-200:].mean():
                above_sma200 += 1

    up4_today = up4.get(as_of_str, 0)
    dn4_today = dn4.get(as_of_str, 0)

    def _ratio(n: int) -> float | None:
        last_n = window_10[-n:]
        if len(last_n) < n:
            return None
        up_sum = sum(up4.get(d, 0) for d in last_n)
        dn_sum = sum(dn4.get(d, 0) for d in last_n)
        return round(up_sum / max(1, dn_sum), 4)

    pct_sma200 = round(above_sma200 / elig_sma200 * 100, 2) if elig_sma200 > 0 else None

    return {
        "date": as_of_str,
        "universe_tag": UNIVERSE_TAG,
        "total_eligible": total_eligible,
        "up4_count": up4_today,
        "down4_count": dn4_today,
        "ratio_5d": _ratio(5),
        "ratio_10d": _ratio(10),
        "up25_quarter": up25,
        "down25_quarter": dn25,
        "pct_above_sma200": pct_sma200,
        "composite_score": None,  # v1.1: backtest normalization bounds before enabling
    }


def update_breadth_history(history_path: str, new_row: dict) -> None:
    """Upsert new_row into breadth_history.csv keyed on (date, universe_tag). Idempotent."""
    path = Path(history_path)
    if path.exists():
        df = pd.read_csv(path)
        # Ensure all expected columns present (handles schema evolution)
        for col in _CSV_COLUMNS:
            if col not in df.columns:
                df[col] = None
        df = df[_CSV_COLUMNS]
    else:
        df = pd.DataFrame(columns=_CSV_COLUMNS)

    # Remove existing row for this (date, universe_tag) — idempotent upsert
    mask = (df["date"] == new_row["date"]) & (
        df["universe_tag"] == new_row["universe_tag"]
    )
    df = df[~mask]

    new_df = pd.DataFrame([{c: new_row.get(c) for c in _CSV_COLUMNS}])
    df = pd.concat([df, new_df], ignore_index=True)
    df = df.sort_values("date").reset_index(drop=True)

    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def build_dashboard_html(
    history_df: pd.DataFrame,
    nifty_df: "pd.DataFrame | None",
) -> str:
    """Build static NSE Breadth Monitor dashboard HTML.
    Data embedded as JSON. Returns HTML string; caller writes file.
    6 panels: stat strip, Nifty price+markers, mirrored bars, ratio oscillator,
    %above SMA200, calendar heatmap.
    """
    from datetime import datetime

    def _to_js(series) -> str:
        import json

        vals = [None if pd.isna(v) else float(v) for v in series]
        return json.dumps(vals)

    def _to_js_int(series) -> str:
        import json

        vals = [None if pd.isna(v) else int(v) for v in series]
        return json.dumps(vals)

    dates = history_df["date"].tolist()
    dates_json = __import__("json").dumps(dates)

    up4_js = _to_js_int(history_df["up4_count"])
    dn4_js = _to_js_int(history_df["down4_count"])
    dn4_neg_js = __import__("json").dumps(
        [None if pd.isna(v) else -int(v) for v in history_df["down4_count"]]
    )
    r5_js = _to_js(history_df["ratio_5d"])
    r10_js = _to_js(history_df["ratio_10d"])
    sma200_js = _to_js(history_df["pct_above_sma200"])

    # Nifty 50 price — normalized 0-100 for overlay
    nifty_js = "[]"
    if nifty_df is not None and not nifty_df.empty:
        date_col = pd.to_datetime(nifty_df["date"])
        nifty_dates = date_col.dt.strftime("%Y-%m-%d").tolist()
        nifty_close = nifty_df["close"].astype(float).tolist()
        mn, mx = min(nifty_close), max(nifty_close)
        rng = mx - mn if mx != mn else 1.0
        nifty_map = {
            d: round((c - mn) / rng * 100, 2) for d, c in zip(nifty_dates, nifty_close)
        }
        nifty_vals = [nifty_map.get(d) for d in dates]
        nifty_js = __import__("json").dumps(nifty_vals)

    generated = datetime.now(IST).strftime("%Y-%m-%d %H:%M IST")
    n_stocks = int(history_df["total_eligible"].max()) if not history_df.empty else 0

    # Latest stats for stat strip
    if not history_df.empty:
        last = history_df.iloc[-1]
        stat_r5 = f"{last['ratio_5d']:.2f}" if pd.notna(last.get("ratio_5d")) else "—"
        stat_up4 = (
            str(int(last["up4_count"])) if pd.notna(last.get("up4_count")) else "—"
        )
        stat_dn4 = (
            str(int(last["down4_count"])) if pd.notna(last.get("down4_count")) else "—"
        )
        stat_sma = (
            f"{last['pct_above_sma200']:.1f}%"
            if pd.notna(last.get("pct_above_sma200"))
            else "—"
        )
    else:
        stat_r5 = stat_up4 = stat_dn4 = stat_sma = "—"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NSE Breadth Monitor</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@3.0.1/dist/chartjs-plugin-annotation.min.js"></script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0a0e14;color:#e8edf3;font-family:'Space Grotesk',system-ui,sans-serif;padding:20px;line-height:1.4}}
h1{{font-size:1.1rem;font-weight:600;color:#e8edf3}}
.meta{{font-size:0.72rem;color:#6b7785;margin:4px 0 20px}}
.card{{background:#10151d;border:1px solid #1c2530;border-radius:8px;padding:16px;margin-bottom:14px}}
.card h2{{font-size:0.78rem;font-weight:600;color:#6b7785;text-transform:uppercase;letter-spacing:.05em;margin-bottom:12px}}
canvas{{width:100%!important}}

/* Stat strip */
.stats{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:14px}}
.stat{{background:#10151d;border:1px solid #1c2530;border-radius:8px;padding:12px 18px;flex:1;min-width:120px}}
.stat-label{{font-size:0.68rem;color:#6b7785;margin-bottom:4px;font-family:'JetBrains Mono',monospace}}
.stat-val{{font-size:1.5rem;font-weight:600;font-family:'JetBrains Mono',monospace}}
.bull{{color:#1fd980}}.bear{{color:#ff5577}}.cyan{{color:#4dd9e8}}.amber{{color:#ffb454}}.muted{{color:#6b7785}}

/* Range controls */
.controls{{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap}}
button{{background:#1c2530;color:#6b7785;border:1px solid #1c2530;border-radius:4px;
        padding:4px 12px;cursor:pointer;font-size:0.75rem;font-family:'Space Grotesk',sans-serif;transition:all .15s}}
button:hover{{background:#2a3545;color:#e8edf3}}
button.active{{background:#1fd98022;color:#1fd980;border-color:#1fd980}}

/* Calendar heatmap */
#heatmap-canvas{{display:block}}
</style>
</head>
<body>
<h1>NSE Breadth Monitor</h1>
<p class="meta">Universe: NSE broad EQ (~{n_stocks} stocks) · Regime/timing layer · Generated: {generated}</p>

<!-- Panel 1: Stat strip -->
<div class="stats">
  <div class="stat"><div class="stat-label">Composite Score</div><div class="stat-val muted">— v1.1</div></div>
  <div class="stat"><div class="stat-label">Ratio 5D</div><div class="stat-val cyan" id="s-r5">{stat_r5}</div></div>
  <div class="stat"><div class="stat-label">Up 4% Today</div><div class="stat-val bull" id="s-up4">{stat_up4}</div></div>
  <div class="stat"><div class="stat-label">Down 4% Today</div><div class="stat-val bear" id="s-dn4">{stat_dn4}</div></div>
  <div class="stat"><div class="stat-label">% Above SMA200</div><div class="stat-val amber" id="s-sma">{stat_sma}</div></div>
</div>

<div class="controls">
  <span style="font-size:0.72rem;color:#6b7785;align-self:center">Range:</span>
  <button onclick="setRange(90)"  id="btn-90"  class="active">90D</button>
  <button onclick="setRange(180)" id="btn-180">180D</button>
  <button onclick="setRange(252)" id="btn-252">1Y</button>
  <button onclick="setRange(504)" id="btn-504">2Y</button>
  <button onclick="setRange(0)"   id="btn-all">All</button>
</div>

<!-- Panel 2: Nifty 50 price + thrust/cap markers -->
<div class="card">
  <h2>NIFTY 50 (normalised) — ▲ Thrust / ▼ Capitulation crossings</h2>
  <canvas id="c-nifty" height="160"></canvas>
</div>

<!-- Panel 3: Mirrored thrust bars -->
<div class="card">
  <h2>Daily 4% Movers — Up (green) vs Down (red)</h2>
  <canvas id="c-bars" height="160"></canvas>
</div>

<!-- Panel 4: Ratio oscillator -->
<div class="card">
  <h2>Ratio Oscillator — 5D (solid) · 10D (dashed) | Thrust ≥1.6 · Cap ≤0.6</h2>
  <canvas id="c-ratio" height="160"></canvas>
</div>

<!-- Panel 5: % above SMA200 -->
<div class="card">
  <h2>% Stocks Above SMA200</h2>
  <canvas id="c-sma200" height="140"></canvas>
</div>

<!-- Panel 6: Calendar heatmap -->
<div class="card">
  <h2>Net Thrust Heatmap (Up4 − Down4) · Last 2 years</h2>
  <canvas id="heatmap-canvas"></canvas>
</div>

<script>
Chart.register(window['chartjs-plugin-annotation']);

const DATA = {{
  dates:  {dates_json},
  up4:    {up4_js},
  dn4:    {dn4_js},
  dn4neg: {dn4_neg_js},
  r5:     {r5_js},
  r10:    {r10_js},
  sma200: {sma200_js},
  nifty:  {nifty_js},
}};

const THRUST = {THRUST_THRESHOLD};
const CAPITU = {CAPITULATION_THRESHOLD};

// --- shared x-axis range ---
let _range = 90;
function sl(arr, n) {{ return n > 0 ? arr.slice(-n) : [...arr]; }}

function setRange(n) {{
  _range = n;
  ['90','180','252','504','all'].forEach(k => document.getElementById('btn-' + k)?.classList.remove('active'));
  document.getElementById(n === 0 ? 'btn-all' : 'btn-' + n)?.classList.add('active');
  [chartNifty, chartBars, chartRatio, chartSma200].forEach(ch => {{
    ch.data.labels = sl(DATA.dates, n);
    ch.data.datasets.forEach((ds, i) => {{
      const key = ds._dataKey;
      if (key) ds.data = sl(DATA[key], n);
    }});
    ch.options.plugins.annotation.annotations = buildAnnotations(ch._type, n);
    ch.update('none');
  }});
  drawHeatmap();
}}

function buildAnnotations(type, n) {{
  if (type === 'ratio') {{
    return {{
      thrustZone: {{
        type: 'box', yMin: THRUST, yMax: 4,
        backgroundColor: 'rgba(31,217,128,0.08)', borderWidth: 0,
      }},
      capZone: {{
        type: 'box', yMin: 0, yMax: CAPITU,
        backgroundColor: 'rgba(255,85,119,0.08)', borderWidth: 0,
      }},
      thrustLine: {{
        type: 'line', yMin: THRUST, yMax: THRUST,
        borderColor: 'rgba(31,217,128,0.4)', borderWidth: 1, borderDash: [4, 3],
      }},
      capLine: {{
        type: 'line', yMin: CAPITU, yMax: CAPITU,
        borderColor: 'rgba(255,85,119,0.4)', borderWidth: 1, borderDash: [4, 3],
      }},
    }};
  }}
  if (type === 'nifty') {{
    const dates = sl(DATA.dates, n);
    const r5    = sl(DATA.r5, n);
    const nifty = sl(DATA.nifty, n);
    const annotations = {{}};
    for (let i = 1; i < r5.length; i++) {{
      if (r5[i] == null || r5[i-1] == null) continue;
      if (r5[i] >= THRUST && r5[i-1] < THRUST) {{
        annotations['t' + i] = {{
          type: 'point', xValue: dates[i], yValue: nifty[i] ?? 50,
          pointStyle: 'triangle', radius: 8,
          backgroundColor: '#1fd980', borderColor: '#1fd980',
        }};
      }}
      if (r5[i] <= CAPITU && r5[i-1] > CAPITU) {{
        annotations['c' + i] = {{
          type: 'point', xValue: dates[i], yValue: nifty[i] ?? 50,
          pointStyle: 'triangle', rotation: 180, radius: 8,
          backgroundColor: '#ff5577', borderColor: '#ff5577',
        }};
      }}
    }}
    return annotations;
  }}
  return {{}};
}}

const CHART_OPTS = (type) => ({{
  responsive: true, animation: false,
  interaction: {{ mode: 'index', intersect: false }},
  plugins: {{
    legend: {{ display: false }},
    tooltip: {{
      backgroundColor: '#10151d', titleColor: '#e8edf3',
      bodyColor: '#6b7785', borderColor: '#1c2530', borderWidth: 1,
    }},
    annotation: {{ annotations: buildAnnotations(type, _range) }},
  }},
  scales: {{
    x: {{ grid: {{ color: '#1a222d' }}, ticks: {{ color: '#6b7785', maxTicksLimit: 10, maxRotation: 0 }} }},
    y: {{ grid: {{ color: '#1a222d' }}, ticks: {{ color: '#6b7785' }} }},
  }},
}});

// Panel 2: Nifty price
const chartNifty = new Chart(document.getElementById('c-nifty'), {{
  type: 'line',
  data: {{
    labels: sl(DATA.dates, 90),
    datasets: [{{
      data: sl(DATA.nifty, 90), _dataKey: 'nifty',
      borderColor: '#4dd9e8', borderWidth: 1.5, pointRadius: 0,
      fill: false, spanGaps: true,
    }}],
  }},
  options: {{ ...CHART_OPTS('nifty'), scales: {{ ...CHART_OPTS('nifty').scales, y: {{ min: 0, max: 100, grid: {{ color: '#1a222d' }}, ticks: {{ color: '#6b7785', callback: v => v + '%' }} }} }} }},
}});
chartNifty._type = 'nifty';

// Panel 3: Mirrored bars
const chartBars = new Chart(document.getElementById('c-bars'), {{
  type: 'bar',
  data: {{
    labels: sl(DATA.dates, 90),
    datasets: [
      {{ data: sl(DATA.up4, 90),    _dataKey: 'up4',    backgroundColor: 'rgba(31,217,128,0.7)', label: 'Up 4%'   }},
      {{ data: sl(DATA.dn4neg, 90), _dataKey: 'dn4neg', backgroundColor: 'rgba(255,85,119,0.7)', label: 'Down 4%' }},
    ],
  }},
  options: {{ ...CHART_OPTS('bars'),
    plugins: {{ ...CHART_OPTS('bars').plugins, tooltip: {{ ...CHART_OPTS('bars').plugins.tooltip,
      callbacks: {{ label: ctx => ` ${{ctx.dataset.label}}: ${{Math.abs(ctx.parsed.y)}}` }} }} }},
    scales: {{ ...CHART_OPTS('bars').scales, x: {{ ...CHART_OPTS('bars').scales.x, stacked: false }} }},
  }},
}});
chartBars._type = 'bars';

// Panel 4: Ratio oscillator
const chartRatio = new Chart(document.getElementById('c-ratio'), {{
  type: 'line',
  data: {{
    labels: sl(DATA.dates, 90),
    datasets: [
      {{ data: sl(DATA.r5,  90), _dataKey: 'r5',  borderColor: '#4dd9e8', borderWidth: 2, pointRadius: 0, fill: false, spanGaps: true, label: 'Ratio 5D' }},
      {{ data: sl(DATA.r10, 90), _dataKey: 'r10', borderColor: '#ffb454', borderWidth: 1.5, borderDash: [5,3], pointRadius: 0, fill: false, spanGaps: true, label: 'Ratio 10D' }},
    ],
  }},
  options: {{ ...CHART_OPTS('ratio'), scales: {{ ...CHART_OPTS('ratio').scales, y: {{ min: 0, suggestedMax: 4, grid: {{ color: '#1a222d' }}, ticks: {{ color: '#6b7785' }} }} }} }},
}});
chartRatio._type = 'ratio';

// Panel 5: % above SMA200
const chartSma200 = new Chart(document.getElementById('c-sma200'), {{
  type: 'line',
  data: {{
    labels: sl(DATA.dates, 90),
    datasets: [{{
      data: sl(DATA.sma200, 90), _dataKey: 'sma200',
      borderColor: '#1fd980', borderWidth: 2, pointRadius: 0,
      fill: false, spanGaps: true, label: '% Above SMA200',
    }}],
  }},
  options: {{
    ...CHART_OPTS('sma200'),
    plugins: {{
      ...CHART_OPTS('sma200').plugins,
      annotation: {{ annotations: {{
        ref50: {{ type: 'line', yMin: 50, yMax: 50, borderColor: 'rgba(107,119,133,0.5)', borderWidth: 1, borderDash: [4,3] }},
      }} }},
    }},
    scales: {{ ...CHART_OPTS('sma200').scales, y: {{ min: 0, max: 100, grid: {{ color: '#1a222d' }}, ticks: {{ color: '#6b7785', callback: v => v + '%' }} }} }},
  }},
}});
chartSma200._type = 'sma200';

// Panel 6: Calendar heatmap (custom canvas — net = up4 - dn4)
function drawHeatmap() {{
  const canvas = document.getElementById('heatmap-canvas');
  const LOOKBACK = 504; // ~2yr
  const dates = sl(DATA.dates, LOOKBACK);
  const up4   = sl(DATA.up4, LOOKBACK);
  const dn4   = sl(DATA.dn4, LOOKBACK);
  if (!dates.length) return;

  const CELL = 13, GAP = 2, STEP = CELL + GAP;
  const DAYS = ['M','T','W','T','F','S','S'];

  // Compute net for each date
  const netMap = {{}};
  for (let i = 0; i < dates.length; i++) {{
    netMap[dates[i]] = (up4[i] ?? 0) - (dn4[i] ?? 0);
  }}

  // Find first Monday on or before earliest date
  const firstDate = new Date(dates[0] + 'T00:00:00');
  const dow = firstDate.getDay(); // 0=Sun
  const mondayOffset = dow === 0 ? 6 : dow - 1;
  const startDate = new Date(firstDate);
  startDate.setDate(startDate.getDate() - mondayOffset);

  // Count weeks
  const lastDate = new Date(dates[dates.length - 1] + 'T00:00:00');
  const totalDays = Math.ceil((lastDate - startDate) / 86400000) + 1;
  const numWeeks = Math.ceil(totalDays / 7);

  const LABEL_W = 20;
  const W = LABEL_W + numWeeks * STEP + GAP;
  const H = 7 * STEP + 30; // 30px for month labels

  canvas.width  = W;
  canvas.height = H;
  canvas.style.width  = Math.min(W, canvas.parentElement.clientWidth) + 'px';
  canvas.style.height = (H * Math.min(W, canvas.parentElement.clientWidth) / W) + 'px';

  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, W, H);

  // Color scale: net → red/neutral/green
  function netColor(net) {{
    const MAX = 300;
    const t = Math.max(-1, Math.min(1, net / MAX));
    if (t >= 0) {{
      // 0 → neutral, 1 → bull
      const r = Math.round(0x1c + (0x1f - 0x1c) * t);
      const g = Math.round(0x25 + (0xd9 - 0x25) * t);
      const b = Math.round(0x30 + (0x80 - 0x30) * t);
      return `rgb(${{r}},${{g}},${{b}})`;
    }} else {{
      const u = -t; // 0→1
      const r = Math.round(0x1c + (0xff - 0x1c) * u);
      const g = Math.round(0x25 + (0x55 - 0x25) * u);
      const b = Math.round(0x30 + (0x77 - 0x30) * u);
      return `rgb(${{r}},${{g}},${{b}})`;
    }}
  }}

  // Day labels
  ctx.fillStyle = '#6b7785';
  ctx.font = '10px JetBrains Mono, monospace';
  for (let d = 0; d < 7; d++) {{
    ctx.fillText(DAYS[d], 2, 30 + d * STEP + CELL - 2);
  }}

  // Draw cells
  let cur = new Date(startDate);
  let lastMonth = -1;
  for (let w = 0; w < numWeeks; w++) {{
    const x = LABEL_W + w * STEP;
    for (let d = 0; d < 7; d++) {{
      const y = 30 + d * STEP;
      const iso = cur.toISOString().slice(0, 10);
      const net = netMap[iso];

      if (net !== undefined) {{
        ctx.fillStyle = netColor(net);
      }} else {{
        ctx.fillStyle = '#1c2530'; // no data / weekend
      }}
      ctx.fillRect(x, y, CELL, CELL);

      // Month label on first cell of month
      const month = cur.getMonth();
      if (d === 0 && month !== lastMonth && net !== undefined) {{
        const MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
        ctx.fillStyle = '#6b7785';
        ctx.font = '9px Space Grotesk, sans-serif';
        ctx.fillText(MONTHS[month], x, 22);
        lastMonth = month;
      }}

      cur.setDate(cur.getDate() + 1);
    }}
  }}
}}

// Initial draw
drawHeatmap();
window.addEventListener('resize', drawHeatmap);
</script>
</body>
</html>"""


def main() -> None:
    parser = argparse.ArgumentParser(description="NSE Breadth Monitor")
    parser.add_argument(
        "--backfill",
        action="store_true",
        help="Iterate all trading dates in SQLite and compute breadth for each. "
        "Use for one-time historical backfill. Idempotent.",
    )
    args = parser.parse_args()

    if not UNIVERSE_PATH.exists():
        print(
            f"ERROR: {UNIVERSE_PATH} not found. Run scripts/refresh_breadth_universe.py first."
        )
        raise SystemExit(1)

    universe_df = pd.read_csv(UNIVERSE_PATH)
    symbols = universe_df["symbol"].tolist()
    print(f"Universe: {len(symbols)} symbols from {UNIVERSE_PATH.name}")

    print("Loading OHLCV from SQLite (lookback=2500)...")
    ohlc_map = load_ohlc_many(symbols, lookback=OHLC_LOOKBACK)
    print(f"Loaded: {len(ohlc_map)} symbols with data")

    if args.backfill:
        # Collect all trading dates across all symbols
        all_dates = sorted(
            set(
                d
                for df in ohlc_map.values()
                for d in df["date"].dt.strftime("%Y-%m-%d")
            )
        )
        print(f"Backfilling {len(all_dates)} trading dates...")
        for i, date_str in enumerate(all_dates):
            as_of = date.fromisoformat(date_str)
            row = compute_daily_breadth(universe_df, as_of, ohlc_map)
            if row:
                update_breadth_history(str(HISTORY_PATH), row)
            if (i + 1) % 100 == 0:
                print(f"  {i + 1}/{len(all_dates)} dates processed...")
        print("Backfill complete.")
    else:
        today = datetime.now(IST).date()
        print(f"Computing breadth for {today}...")
        row = compute_daily_breadth(universe_df, today, ohlc_map)
        if row is None:
            print(f"  {today} is not a trading day in SQLite — no row written.")
        else:
            update_breadth_history(str(HISTORY_PATH), row)
            print(
                f"  up4={row['up4_count']} down4={row['down4_count']} ratio5d={row['ratio_5d']}"
            )

    # Build dashboard from full history
    print("Building dashboard HTML...")
    history_df = pd.read_csv(HISTORY_PATH)
    nifty_df = load_ohlc(NIFTY50_SYM, lookback=OHLC_LOOKBACK)
    html = build_dashboard_html(history_df, nifty_df)
    DASHBOARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    DASHBOARD_PATH.write_text(html, encoding="utf-8")
    print(f"Dashboard -> {DASHBOARD_PATH}")


if __name__ == "__main__":
    main()
