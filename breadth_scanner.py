#!/usr/bin/env python3
"""
Market Breadth Scanner — % of NSE stocks above SMA10/20/50/200

Universe: NSE common equity, MCap Rs.500 Cr - Rs.5 Lakh Cr (filtered set, ~900 stocks).

First run: backfills all available history from SQLite (up to 400 bars).
Subsequent runs: appends only new dates since the last CSV entry.

Output:
  breadth_scans/breadth_history.csv   — date, pct_above_10/20/50/200, n_10/20/50/200
  breadth_chart.html                  — Chart.js interactive chart (repo root → GitHub Pages)
"""

import os
import sys
import json
from datetime import datetime, timezone, timedelta

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc_many, load_ohlc

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(REPO_DIR, "breadth_scans")
CSV_PATH = os.path.join(OUT_DIR, "breadth_history.csv")
HTML_PATH = os.path.join(REPO_DIR, "breadth_chart.html")  # root → GitHub Pages

MC_LOW = 500 * 1_00_00_000  # Rs.500 Cr
MC_HIGH = 5_00_000 * 1_00_00_000  # Rs.5 Lakh Cr
BENCH_SYM = "NIFTY MIDSML 400"
LOOKBACK = 400
MIN_STOCKS = 10  # minimum valid stocks for a date to be reported

IST = timezone(timedelta(hours=5, minutes=30))


# ── Universe ──────────────────────────────────────────────────────────────────


def get_universe() -> list[str]:
    """TradingView screener -> NSE equity symbols, MCap Rs.500 Cr - Rs.5 Lakh Cr."""
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "market_cap_basic")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(5000)
        .get_scanner_data()
    )
    return df["name"].tolist()


# ── Breadth computation ───────────────────────────────────────────────────────


def compute_breadth(ohlc_map: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    For each trading date, count stocks with valid SMAx and stocks where close > SMAx.
    Returns DataFrame: date, pct_above_10/20/50/200, n_10/20/50/200.
    """
    parts = []
    for sym, df in ohlc_map.items():
        c = df["close"].astype(float)
        dates = df["date"].dt.strftime("%Y-%m-%d")
        chunk = pd.DataFrame({"date": dates})
        for period in [10, 20, 50, 200]:
            sma = c.rolling(period, min_periods=period).mean()
            valid = sma.notna()
            chunk[f"above_{period}"] = ((c > sma) & valid).astype(int)
            chunk[f"valid_{period}"] = valid.astype(int)
        parts.append(chunk)

    all_df = pd.concat(parts, ignore_index=True)
    grouped = all_df.groupby("date", sort=True).sum()

    result = pd.DataFrame({"date": grouped.index})
    for period in [10, 20, 50, 200]:
        n = grouped[f"valid_{period}"]
        above = grouped[f"above_{period}"]
        result[f"n_{period}"] = n.values
        pct = (above / n * 100).where(n >= MIN_STOCKS).round(2)
        result[f"pct_above_{period}"] = pct.values

    return result.reset_index(drop=True)


# ── HTML chart ────────────────────────────────────────────────────────────────


def build_html(breadth_df: pd.DataFrame, bench_df: "pd.DataFrame | None") -> str:
    dates = breadth_df["date"].tolist()

    def to_js(col_name):
        return [None if pd.isna(v) else float(v) for v in breadth_df[col_name]]

    p10 = to_js("pct_above_10")
    p20 = to_js("pct_above_20")
    p50 = to_js("pct_above_50")
    p200 = to_js("pct_above_200")

    # Benchmark: normalize to 0-100 range for overlay
    bench_series = [None] * len(dates)
    if bench_df is not None and not bench_df.empty:
        bench_map_raw = dict(
            zip(
                bench_df["date"].dt.strftime("%Y-%m-%d").tolist(),
                bench_df["close"].tolist(),
            )
        )
        raw_vals = [v for v in bench_map_raw.values() if v is not None]
        if raw_vals:
            mn, mx = min(raw_vals), max(raw_vals)
            rng = mx - mn if mx > mn else 1.0
            bench_series = [
                (
                    round((bench_map_raw[d] - mn) / rng * 100, 2)
                    if d in bench_map_raw
                    else None
                )
                for d in dates
            ]

    data_json = json.dumps(
        {
            "dates": dates,
            "p10": p10,
            "p20": p20,
            "p50": p50,
            "p200": p200,
            "bench": bench_series,
        }
    )

    generated = datetime.now(IST).strftime("%Y-%m-%d %H:%M IST")
    n_stocks = int(breadth_df["n_10"].max()) if not breadth_df.empty else 0

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NSE Market Breadth</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #0f1117; color: #e0e0e0; font-family: 'Segoe UI', system-ui, sans-serif; padding: 20px; }}
  h1 {{ font-size: 1.15rem; color: #fff; font-weight: 600; }}
  .meta {{ font-size: 0.73rem; color: #666; margin: 4px 0 20px; }}
  .card {{ background: #1a1d27; border: 1px solid #2a2d3e; border-radius: 8px; padding: 16px; margin-bottom: 16px; }}
  .controls {{ display: flex; gap: 6px; margin-bottom: 14px; flex-wrap: wrap; align-items: center; }}
  .controls label {{ font-size: 0.75rem; color: #666; margin-right: 4px; }}
  button {{ background: #252836; color: #aaa; border: 1px solid #3a3d4e; border-radius: 4px;
            padding: 4px 14px; cursor: pointer; font-size: 0.78rem; transition: all 0.15s; }}
  button:hover {{ background: #2e3148; color: #ddd; }}
  button.active {{ background: #3b5bdb; color: #fff; border-color: #3b5bdb; }}
  .legend {{ display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 10px; }}
  .li {{ display: flex; align-items: center; gap: 6px; font-size: 0.75rem; color: #999; }}
  .li span {{ cursor: pointer; }}
  .li span:hover {{ color: #ddd; }}
  .li.dim {{ opacity: 0.35; }}
  .style-btn {{ padding: 1px 7px !important; font-size: 0.67rem !important; margin-left: 2px; }}
  .swatch {{ width: 24px; height: 3px; border-radius: 2px; flex-shrink: 0; }}
  .swatch.dashed {{ background: repeating-linear-gradient(90deg, #a78bfa 0 5px, transparent 5px 9px); }}
  canvas {{ width: 100% !important; }}
  .stats {{ display: flex; gap: 16px; flex-wrap: wrap; margin-top: 16px; }}
  .stat {{ background: #252836; border-radius: 6px; padding: 10px 16px; min-width: 130px; }}
  .stat-label {{ font-size: 0.7rem; color: #666; margin-bottom: 4px; }}
  .stat-val {{ font-size: 1.25rem; font-weight: 600; }}
  .green {{ color: #34d399; }} .orange {{ color: #fb923c; }} .red {{ color: #f87171; }} .blue {{ color: #60a5fa; }} .purple {{ color: #a78bfa; }}
</style>
</head>
<body>
<h1>NSE Market Breadth — % Stocks Above Moving Average</h1>
<p class="meta">Universe: NSE equity Rs.500 Cr–Rs.5 Lakh Cr &nbsp;(~{n_stocks} stocks) &nbsp;|&nbsp; Benchmark: NIFTY MidSmallcap 400 &nbsp;|&nbsp; Generated: {generated}</p>

<div class="card">
  <div class="controls">
    <label>Range:</label>
    <button onclick="setRange(60)"  id="btn-60">60D</button>
    <button onclick="setRange(90)"  id="btn-90" class="active">90D</button>
    <button onclick="setRange(180)" id="btn-180">180D</button>
    <button onclick="setRange(252)" id="btn-252">1Y</button>
    <button onclick="setRange(0)"   id="btn-all">All</button>
  </div>
  <div class="legend">
    <div class="li" id="li-0"><div class="swatch" style="background:#60a5fa" onclick="toggleLine(0)" title="Click to hide/show"></div><span onclick="toggleLine(0)">% &gt; SMA10</span><button class="style-btn active" id="style-0" onclick="toggleStep(0)">Line</button></div>
    <div class="li" id="li-1"><div class="swatch" style="background:#fb923c" onclick="toggleLine(1)" title="Click to hide/show"></div><span onclick="toggleLine(1)">% &gt; SMA20</span><button class="style-btn active" id="style-1" onclick="toggleStep(1)">Line</button></div>
    <div class="li" id="li-2"><div class="swatch" style="background:#34d399" onclick="toggleLine(2)" title="Click to hide/show"></div><span onclick="toggleLine(2)">% &gt; SMA50</span><button class="style-btn active" id="style-2" onclick="toggleStep(2)">Step</button></div>
    <div class="li" id="li-3"><div class="swatch" style="background:#f87171" onclick="toggleLine(3)" title="Click to hide/show"></div><span onclick="toggleLine(3)">% &gt; SMA200</span><button class="style-btn active" id="style-3" onclick="toggleStep(3)">Step</button></div>
    <div class="li" id="li-4"><div class="swatch dashed" onclick="toggleLine(4)" title="Click to hide/show"></div><span onclick="toggleLine(4)">NIFTY MidSml 400 (norm.)</span><button class="style-btn active" id="style-4" onclick="toggleStep(4)">Step</button></div>
  </div>
  <canvas id="bc" height="400"></canvas>
</div>

<div class="stats" id="stat-cards"></div>

<script>
const D = {data_json};

function sl(arr, n) {{ return n > 0 ? arr.slice(-n) : [...arr]; }}

const DATASETS = [
  {{ label: '% > SMA10',  key: 'p10',  color: '#60a5fa', width: 1.5, step: false }},
  {{ label: '% > SMA20',  key: 'p20',  color: '#fb923c', width: 1.5, step: false }},
  {{ label: '% > SMA50',  key: 'p50',  color: '#34d399', width: 2.0, step: true  }},
  {{ label: '% > SMA200', key: 'p200', color: '#f87171', width: 2.5, step: true  }},
  {{ label: 'NIFTY MidSml 400 (norm.)', key: 'bench', color: '#a78bfa', width: 1, dash: [5,3], step: true  }},
];

function makeDatasets(n) {{
  return DATASETS.map((d, i) => ({{
    label: d.label,
    data: sl(D[d.key], n),
    borderColor: d.color,
    borderWidth: d.width,
    borderDash: d.dash || [],
    pointRadius: 0,
    stepped: d.step ? 'middle' : false,
    tension: d.step ? 0 : 0.1,
    fill: false,
    spanGaps: true,
    hidden: [1, 2].includes(i),
  }}));
}}

let currentRange = 90;
const stepState = DATASETS.map(d => d.step);
const ctx = document.getElementById('bc').getContext('2d');

// Reference line plugin
const refPlugin = {{
  id: 'refLines',
  afterDraw(chart) {{
    const {{ ctx: c, chartArea: {{ left, right }}, scales: {{ y }} }} = chart;
    if (!y) return;
    const lines = [
      {{ v: 80, color: 'rgba(52,211,153,0.45)',  label: '80%', lc: '#34d399' }},
      {{ v: 50, color: 'rgba(255,255,255,0.18)', label: '50%', lc: '#888'    }},
      {{ v: 20, color: 'rgba(248,113,113,0.45)', label: '20%', lc: '#f87171' }},
    ];
    c.save();
    lines.forEach(({{ v, color, label, lc }}) => {{
      const py = y.getPixelForValue(v);
      c.setLineDash([4, 4]);
      c.strokeStyle = color;
      c.lineWidth = 1;
      c.beginPath(); c.moveTo(left, py); c.lineTo(right, py); c.stroke();
      c.setLineDash([]);
      c.fillStyle = lc;
      c.font = '10px Segoe UI';
      c.fillText(label, left + 5, py - 3);
    }});
    c.restore();
  }}
}};
Chart.register(refPlugin);

const chart = new Chart(ctx, {{
  type: 'line',
  data: {{ labels: sl(D.dates, 90), datasets: makeDatasets(90) }},
  options: {{
    responsive: true,
    animation: false,
    interaction: {{ mode: 'index', intersect: false }},
    plugins: {{
      legend: {{ display: false }},
      tooltip: {{
        backgroundColor: '#1e2130',
        titleColor: '#ccc',
        bodyColor: '#aaa',
        borderColor: '#3a3d4e',
        borderWidth: 1,
        callbacks: {{
          label: ctx => {{
            const v = ctx.parsed.y;
            return ` ${{ctx.dataset.label}}: ${{v != null ? v.toFixed(1) + '%' : 'N/A'}}`;
          }},
        }},
      }},
    }},
    scales: {{
      x: {{
        grid: {{ color: 'rgba(255,255,255,0.04)' }},
        ticks: {{ color: '#555', maxTicksLimit: 12, maxRotation: 0 }},
      }},
      y: {{
        min: 0, max: 100,
        grid: {{ color: 'rgba(255,255,255,0.04)' }},
        ticks: {{ color: '#555', callback: v => v + '%' }},
      }},
    }},
  }},
}});

function setRange(n) {{
  currentRange = n;
  ['60','90','180','252','all'].forEach(k => document.getElementById('btn-' + k).classList.remove('active'));
  document.getElementById(n === 0 ? 'btn-all' : 'btn-' + n).classList.add('active');
  chart.data.labels = sl(D.dates, n);
  DATASETS.forEach((d, i) => {{ chart.data.datasets[i].data = sl(D[d.key], n); }});
  chart.update('none');
  updateStats(n);
}}

function toggleStep(i) {{
  stepState[i] = !stepState[i];
  const step = stepState[i];
  chart.data.datasets[i].stepped = step ? 'middle' : false;
  chart.data.datasets[i].tension = step ? 0 : 0.1;
  const btn = document.getElementById('style-' + i);
  if (btn) {{ btn.textContent = step ? 'Step' : 'Line'; }}
  chart.update('none');
}}

function toggleLine(i) {{
  chart.data.datasets[i].hidden = !chart.data.datasets[i].hidden;
  const li = document.getElementById('li-' + i);
  if (li) li.classList.toggle('dim', chart.data.datasets[i].hidden);
  chart.update('none');
}}

function updateStats(n) {{
  const labels = sl(D.dates, n);
  const last = labels[labels.length - 1];
  const idx = D.dates.indexOf(last);
  const cards = [
    {{ label: 'SMA10', val: D.p10[idx],  cls: 'blue'   }},
    {{ label: 'SMA20', val: D.p20[idx],  cls: 'orange'  }},
    {{ label: 'SMA50', val: D.p50[idx],  cls: 'green'   }},
    {{ label: 'SMA200',val: D.p200[idx], cls: 'red'     }},
  ];
  document.getElementById('stat-cards').innerHTML = cards.map(c => `
    <div class="stat">
      <div class="stat-label">% Above ${{c.label}} &nbsp;(${{last}})</div>
      <div class="stat-val ${{c.cls}}">${{c.val != null ? c.val.toFixed(1) + '%' : 'N/A'}}</div>
    </div>`).join('');
}}

// Initialize dim state for datasets hidden by default
DATASETS.forEach((_, i) => {{
  if (chart.data.datasets[i].hidden) {{
    const li = document.getElementById('li-' + i);
    if (li) li.classList.add('dim');
  }}
}});

updateStats(90);
</script>
</body>
</html>"""


# ── Main ──────────────────────────────────────────────────────────────────────


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    print("Fetching universe from TradingView...")
    symbols = get_universe()
    print(f"Universe: {len(symbols)} stocks")

    print("Loading OHLC from SQLite...")
    ohlc_map = load_ohlc_many(symbols, lookback=LOOKBACK)
    print(f"Loaded: {len(ohlc_map)} stocks with data")

    print("Computing breadth across all dates...")
    breadth = compute_breadth(ohlc_map)
    print(f"Breadth: {len(breadth)} trading days")

    # Incremental update: append only dates newer than last CSV entry
    if os.path.exists(CSV_PATH):
        existing = pd.read_csv(CSV_PATH)
        last_date = existing["date"].max()
        new_rows = breadth[breadth["date"] > last_date]
        if new_rows.empty:
            print("CSV up to date — no new dates to append")
            combined = existing
        else:
            print(
                f"Appending {len(new_rows)} new date(s) (last: {new_rows['date'].max()})"
            )
            combined = pd.concat([existing, new_rows], ignore_index=True)
    else:
        print("First run — writing full backfill history")
        combined = breadth

    combined.to_csv(CSV_PATH, index=False)
    print(f"CSV -> {CSV_PATH}")

    # Benchmark overlay
    bench_df = load_ohlc(BENCH_SYM, lookback=LOOKBACK)

    # Generate HTML
    html = build_html(combined, bench_df)
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Chart -> {HTML_PATH}")

    # Summary
    if not combined.empty:
        latest = combined.iloc[-1]
        print(f"\n--- Breadth snapshot ({latest['date']}) ---")
        for period, label in [
            (10, "SMA10 "),
            (20, "SMA20 "),
            (50, "SMA50 "),
            (200, "SMA200"),
        ]:
            v = latest.get(f"pct_above_{period}")
            n = latest.get(f"n_{period}", 0)
            if pd.notna(v):
                bar = "█" * int(v / 5)
                print(f"  {label}: {v:5.1f}%  {bar}  (n={int(n)})")
            else:
                print(f"  {label}: N/A")


if __name__ == "__main__":
    main()
