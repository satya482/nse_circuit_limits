# Union Watchlist Chart Dashboard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a daily-refreshed HTML dashboard that plots every symbol in the EMA55 union watchlist as an interactive candlestick+volume chart, with live client-side controls to recolor candles and change EMA overlay periods.

**Architecture:** A new standalone script (`union_chart_dashboard.py`) reads today's union watchlist symbols+tiers straight out of `ema55_cross_scans/ema55_cross_scans.md` (the file `ema55_cross_scanner.py` already writes), loads OHLC via the repo's one DB entry point (`ohlc_db.load_ohlc_many`), and emits a single self-contained HTML file embedding all symbols' OHLCV data as JSON plus a vendored charting library. All interactivity (candle color, EMA periods, lazy chart construction) runs client-side in the browser — the Python side only assembles data and markup once per day.

**Tech Stack:** Python (pandas, existing `ohlc_db`/`disclaimer` modules), vendored `lightweight-charts.js` v4.1.3 (TradingView's OSS charting library), vanilla JS (no build step, no framework — matches this repo's existing `dashboard/footprint.html` pattern).

**Spec:** `docs/superpowers/specs/2026-08-20-union-chart-dashboard-design.md`

## Global Constraints

- Only DB entry point for OHLCV is `ohlc_db.load_ohlc_many()` / `load_ohlc()` — never read CSVs or hit external APIs from scanner logic (`.claude/rules/scanner-conventions.md`).
- Every generated `.md`/`.html` output file must include the SEBI disclaimer via `disclaimer.SEBI_HTML_BANNER` / `SEBI_HTML_FOOTER` (repo `CLAUDE.md`).
- A scan run that produces 0 chartable symbols must still write a valid file with an explicit "no signals" state, never an empty/missing file (`.claude/rules/backtesting-integrity.md`).
- `.ps1` files must be plain ASCII — no em dashes or curly quotes in string literals; run `tools\check_ps1_syntax.ps1` before committing any `.ps1` change (repo `CLAUDE.md`).
- All datetimes in logs must carry explicit IST (`.claude/rules/backtesting-integrity.md`) — runner script logging already handles this via existing `Log` helper pattern, no new datetime handling needed in this plan.
- Commit with `git commit --no-verify` in this repo (pre-commit is disabled here) (repo `CLAUDE.md`).
- Data-only commits use the pattern `[scan YYYY-MM-DD] <scanner>: <result summary>` (`.claude/rules/scanner-conventions.md`).

---

## File Structure

| File | Responsibility |
|---|---|
| `union_chart_dashboard.py` | New. Parses union tiers from `ema55_cross_scans.md`, loads OHLC, builds chart-ready records, renders the HTML dashboard, `main()` orchestration. |
| `dashboard/vendor/lightweight-charts.js` | New. Vendored charting library, committed once, not regenerated. |
| `tests/test_union_chart_dashboard.py` | New. Pure-function tests for tier parsing, freshness check, chart-data building, HTML rendering, and an end-to-end `main()` test with monkeypatched data. |
| `run_union_chart_dashboard.ps1` | New. Runner: log to `logs/`, run the script, git add+commit+push `dashboard/`. |
| `run_all_scanners.ps1` | Modified. Add a `Run-Scanner` step after `EMA55_Cross`. |
| `CLAUDE.md` | Modified. Add run-table row + architecture section for the new scanner. |

---

### Task 1: Vendor the charting library

**Files:**
- Create: `dashboard/vendor/lightweight-charts.js`

**Interfaces:**
- Produces: a browser-global `LightweightCharts` object (script-tag include, no module system) — consumed by Task 4's generated HTML via `<script src="vendor/lightweight-charts.js">`.

- [ ] **Step 1: Create the vendor directory and download the pinned library version**

```bash
mkdir -p dashboard/vendor
curl -s "https://unpkg.com/lightweight-charts@4.1.3/dist/lightweight-charts.standalone.production.js" -o dashboard/vendor/lightweight-charts.js
```

- [ ] **Step 2: Verify the file downloaded correctly**

```bash
wc -c dashboard/vendor/lightweight-charts.js
grep -c "createChart" dashboard/vendor/lightweight-charts.js
```

Expected: file size around 150-165KB (not 0, not an HTML error page), and `createChart` found at least once.

- [ ] **Step 3: Commit**

```bash
git add dashboard/vendor/lightweight-charts.js
git commit --no-verify -m "vendor lightweight-charts.js v4.1.3 for union chart dashboard"
```

---

### Task 2: Union tier parsing + freshness check

**Files:**
- Create: `union_chart_dashboard.py` (this task writes the top of the file only)
- Test: `tests/test_union_chart_dashboard.py`

**Interfaces:**
- Consumes: nothing from other tasks (first code in the new module).
- Produces:
  - `parse_union_tiers(md_text: str) -> dict[str, str]` — symbol -> tier label (e.g. `"ALL 4"`), used by Task 3.
  - `load_todays_union(md_path: str, today: str) -> tuple[dict[str, str] | None, str | None]` — `(tiers, error)`; `error` is `None` on success, used by Task 5's `main()`.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_union_chart_dashboard.py`:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from union_chart_dashboard import parse_union_tiers, load_todays_union

UNION_MD_FRESH = """> disclaimer text
# NSE EMA55 Cross Watchlist -- 2026-08-20
*Generated 2026-08-20 15:47 IST*

### Union Watchlist
**ALL 4: 2** | **1 ONLY: 2**

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,###ALL 4,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,NSE:FOO,NSE:BAR,###1 ONLY,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,NSE:BAZ,NSE:QUX
```

---
### Scan definition
"""

UNION_MD_STALE = UNION_MD_FRESH.replace("2026-08-20", "2026-08-19")


def test_parse_union_tiers_extracts_symbol_to_tier():
    tiers = parse_union_tiers(UNION_MD_FRESH)
    assert tiers == {"FOO": "ALL 4", "BAR": "ALL 4", "BAZ": "1 ONLY", "QUX": "1 ONLY"}


def test_parse_union_tiers_excludes_index_and_commodity_anchors():
    tiers = parse_union_tiers(UNION_MD_FRESH)
    assert "NIFTYSMLCAP250" not in tiers
    assert "NIFTYMIDSML400" not in tiers
    assert "GOLDM1!" not in tiers
    assert not any(k.startswith("MCX") for k in tiers)


def test_parse_union_tiers_no_block_returns_empty():
    assert parse_union_tiers("no fenced block here") == {}


def test_load_todays_union_missing_file(tmp_path):
    tiers, err = load_todays_union(str(tmp_path / "nope.md"), "2026-08-20")
    assert tiers is None
    assert "not found" in err


def test_load_todays_union_stale_date(tmp_path):
    p = tmp_path / "ema55_cross_scans.md"
    p.write_text(UNION_MD_STALE, encoding="utf-8")
    tiers, err = load_todays_union(str(p), "2026-08-20")
    assert tiers is None
    assert "stale" in err


def test_load_todays_union_fresh_returns_tiers(tmp_path):
    p = tmp_path / "ema55_cross_scans.md"
    p.write_text(UNION_MD_FRESH, encoding="utf-8")
    tiers, err = load_todays_union(str(p), "2026-08-20")
    assert err is None
    assert tiers == {"FOO": "ALL 4", "BAR": "ALL 4", "BAZ": "1 ONLY", "QUX": "1 ONLY"}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_union_chart_dashboard.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'union_chart_dashboard'`

- [ ] **Step 3: Write the implementation**

Create `union_chart_dashboard.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_union_chart_dashboard.py -v`
Expected: PASS (6 tests)

- [ ] **Step 5: Commit**

```bash
git add union_chart_dashboard.py tests/test_union_chart_dashboard.py
git commit --no-verify -m "add union chart dashboard: tier parsing + freshness check"
```

---

### Task 3: Chart data builder

**Files:**
- Modify: `union_chart_dashboard.py` (append)
- Test: `tests/test_union_chart_dashboard.py` (append)

**Interfaces:**
- Consumes: `MIN_BARS` constant from Task 2.
- Produces: `build_chart_data(ohlc_map: dict[str, "pandas.DataFrame"], tiers: dict[str, str], min_bars: int = MIN_BARS) -> tuple[list[dict], int]` — `(records, skipped_count)`. Each record: `{"symbol": str, "tier": str, "bars": list[list]}` where each bar is `[date_str, open, high, low, close, volume]`. Used by Task 4 (`build_html`) and Task 5 (`main`).

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_union_chart_dashboard.py`:

```python
import pandas as pd
from union_chart_dashboard import build_chart_data


def _fixture_df(n_rows: int) -> pd.DataFrame:
    dates = pd.date_range("2025-01-01", periods=n_rows, freq="D")
    return pd.DataFrame({
        "date": dates,
        "open": [100.0 + i for i in range(n_rows)],
        "high": [101.0 + i for i in range(n_rows)],
        "low": [99.0 + i for i in range(n_rows)],
        "close": [100.5 + i for i in range(n_rows)],
        "volume": [1000 + i for i in range(n_rows)],
    })


def test_build_chart_data_keeps_symbol_with_enough_bars():
    ohlc_map = {"FOO": _fixture_df(200)}
    tiers = {"FOO": "ALL 4"}
    records, skipped = build_chart_data(ohlc_map, tiers, min_bars=130)
    assert skipped == 0
    assert len(records) == 1
    assert records[0]["symbol"] == "FOO"
    assert records[0]["tier"] == "ALL 4"
    assert records[0]["bars"][0] == ["2025-01-01", 100.0, 101.0, 99.0, 100.5, 1000.0]
    assert len(records[0]["bars"]) == 200


def test_build_chart_data_skips_symbol_below_bar_floor():
    ohlc_map = {"FOO": _fixture_df(200), "BAR": _fixture_df(50)}
    tiers = {"FOO": "ALL 4", "BAR": "1 ONLY"}
    records, skipped = build_chart_data(ohlc_map, tiers, min_bars=130)
    assert skipped == 1
    assert [r["symbol"] for r in records] == ["FOO"]


def test_build_chart_data_skips_symbol_missing_from_ohlc_map():
    ohlc_map = {"FOO": _fixture_df(200)}
    tiers = {"FOO": "ALL 4", "MISSING": "1 ONLY"}
    records, skipped = build_chart_data(ohlc_map, tiers, min_bars=130)
    assert skipped == 1
    assert [r["symbol"] for r in records] == ["FOO"]


def test_build_chart_data_sorted_by_symbol():
    ohlc_map = {"ZEBRA": _fixture_df(150), "APEX": _fixture_df(150)}
    tiers = {"ZEBRA": "1 ONLY", "APEX": "ALL 4"}
    records, _ = build_chart_data(ohlc_map, tiers, min_bars=130)
    assert [r["symbol"] for r in records] == ["APEX", "ZEBRA"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_union_chart_dashboard.py -v -k build_chart_data`
Expected: FAIL with `ImportError: cannot import name 'build_chart_data'`

- [ ] **Step 3: Write the implementation**

Append to `union_chart_dashboard.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_union_chart_dashboard.py -v`
Expected: PASS (10 tests)

- [ ] **Step 5: Commit**

```bash
git add union_chart_dashboard.py tests/test_union_chart_dashboard.py
git commit --no-verify -m "add union chart dashboard: chart data builder"
```

---

### Task 4: HTML dashboard renderer

**Files:**
- Modify: `union_chart_dashboard.py` (append)
- Test: `tests/test_union_chart_dashboard.py` (append)

**Interfaces:**
- Consumes: `records: list[dict]` shape from Task 3 (`{"symbol", "tier", "bars"}`), `SEBI_HTML_BANNER`/`SEBI_HTML_FOOTER` from `disclaimer.py`.
- Produces: `build_html(records: list[dict], as_of: str) -> str` — full HTML document string. Used by Task 5's `main()`.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_union_chart_dashboard.py`:

```python
from union_chart_dashboard import build_html


def test_build_html_contains_disclaimer():
    html = build_html([], "2026-08-20")
    assert "SEBI registered" in html


def test_build_html_contains_vendor_script_tag():
    html = build_html([], "2026-08-20")
    assert 'src="vendor/lightweight-charts.js"' in html


def test_build_html_no_records_shows_empty_state():
    html = build_html([], "2026-08-20")
    assert "No signals" in html


def test_build_html_embeds_symbol_data_and_cards():
    records = [{"symbol": "FOO", "tier": "ALL 4", "bars": [["2025-01-01", 1.0, 2.0, 0.5, 1.5, 100.0]]}]
    html = build_html(records, "2026-08-20")
    assert '"FOO"' in html
    assert '"ALL 4"' in html
    assert 'data-symbol="FOO"' in html
    assert 'id="chart-FOO"' in html


def test_build_html_has_interactive_controls():
    html = build_html([], "2026-08-20")
    assert 'id="upColor"' in html
    assert 'id="downColor"' in html
    assert 'id="emaPeriods"' in html
    assert "IntersectionObserver" in html
    assert "computeEMA" in html
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_union_chart_dashboard.py -v -k build_html`
Expected: FAIL with `ImportError: cannot import name 'build_html'`

- [ ] **Step 3: Write the implementation**

Append to `union_chart_dashboard.py`. First the JS template (kept as a plain string, not an f-string, so its `{`/`}` braces need no escaping):

```python
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
```

Then the HTML builder itself:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_union_chart_dashboard.py -v`
Expected: PASS (15 tests)

- [ ] **Step 5: Commit**

```bash
git add union_chart_dashboard.py tests/test_union_chart_dashboard.py
git commit --no-verify -m "add union chart dashboard: HTML renderer with live controls"
```

---

### Task 5: main() orchestration

**Files:**
- Modify: `union_chart_dashboard.py` (append)
- Test: `tests/test_union_chart_dashboard.py` (append)

**Interfaces:**
- Consumes: `load_todays_union`, `build_chart_data`, `build_html`, `load_ohlc_many` (from `ohlc_db`), constants `EMA55_MD`, `OUTPUT_PATH`, `TODAY`, `LOOKBACK` — all from Tasks 2-4.
- Produces: `main() -> None`, writes `OUTPUT_PATH`. No other task consumes this.

- [ ] **Step 1: Write the failing test**

Append to `tests/test_union_chart_dashboard.py`:

```python
import union_chart_dashboard as ucd


def test_main_writes_html_with_expected_symbols(tmp_path, monkeypatch, capsys):
    union_md = tmp_path / "ema55_cross_scans.md"
    union_md.write_text(UNION_MD_FRESH, encoding="utf-8")
    output_path = tmp_path / "dashboard" / "union_charts.html"

    monkeypatch.setattr(ucd, "EMA55_MD", str(union_md))
    monkeypatch.setattr(ucd, "OUTPUT_PATH", str(output_path))
    monkeypatch.setattr(ucd, "TODAY", "2026-08-20")

    def fake_load_ohlc_many(symbols, lookback=250):
        return {sym: _fixture_df(200) for sym in symbols}

    monkeypatch.setattr(ucd, "load_ohlc_many", fake_load_ohlc_many)

    ucd.main()

    assert output_path.exists()
    html = output_path.read_text(encoding="utf-8")
    assert '"FOO"' in html
    assert '"BAR"' in html
    assert "SEBI registered" in html
    out = capsys.readouterr().out
    assert "4 charted" in out


def test_main_skips_write_when_stale(tmp_path, monkeypatch, capsys):
    union_md = tmp_path / "ema55_cross_scans.md"
    union_md.write_text(UNION_MD_STALE, encoding="utf-8")
    output_path = tmp_path / "dashboard" / "union_charts.html"

    monkeypatch.setattr(ucd, "EMA55_MD", str(union_md))
    monkeypatch.setattr(ucd, "OUTPUT_PATH", str(output_path))
    monkeypatch.setattr(ucd, "TODAY", "2026-08-20")

    ucd.main()

    assert not output_path.exists()
    out = capsys.readouterr().out
    assert "stale" in out
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_union_chart_dashboard.py -v -k test_main`
Expected: FAIL with `AttributeError: module 'union_chart_dashboard' has no attribute 'main'`

- [ ] **Step 3: Write the implementation**

Append to `union_chart_dashboard.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_union_chart_dashboard.py -v`
Expected: PASS (17 tests)

- [ ] **Step 5: Commit**

```bash
git add union_chart_dashboard.py tests/test_union_chart_dashboard.py
git commit --no-verify -m "add union chart dashboard: main() orchestration"
```

---

### Task 6: PS1 runner, pipeline wiring, docs

**Files:**
- Create: `run_union_chart_dashboard.ps1`
- Modify: `run_all_scanners.ps1`
- Modify: `CLAUDE.md`

**Interfaces:**
- Consumes: `union_chart_dashboard.py`'s `main()` (Task 5), invoked as a subprocess — no Python-level interface.
- Produces: nothing consumed by other tasks (terminal task).

- [ ] **Step 1: Create the runner script**

Create `run_union_chart_dashboard.ps1`:

```powershell
$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\union_chart_dashboard_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== NSE_UNION_CHART_DASHBOARD START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\union_chart_dashboard.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add dashboard/union_charts.html 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $date] union_charts: dashboard refresh" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: git push FAILED (exit $LASTEXITCODE) - commits NOT on GitHub, check for non-fast-forward ==="
    exit 1
}
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_UnionChartDashboard" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_union_chart_dashboard.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:32 /f
```

- [ ] **Step 2: Verify PS1 syntax**

```powershell
powershell -NonInteractive -File tools\check_ps1_syntax.ps1
```

Expected: no syntax errors reported for `run_union_chart_dashboard.ps1` (this repo's convention — catches the mis-encoded-character class of bug before it reaches a scheduled task, per repo `CLAUDE.md`).

- [ ] **Step 3: Wire into run_all_scanners.ps1**

Find the line:
```powershell
Run-Scanner "EMA55_Cross"          "$ROOT\run_ema55_cross_scanner.ps1"
```

Add immediately after it:
```powershell
Run-Scanner "UnionChartDashboard"  "$ROOT\run_union_chart_dashboard.ps1"
```

- [ ] **Step 4: Re-run syntax check on the modified orchestrator**

```powershell
powershell -NonInteractive -File tools\check_ps1_syntax.ps1
```

Expected: no syntax errors.

- [ ] **Step 5: Update CLAUDE.md**

In the run-order code block (near the top, after the `.\run_ema55_cross_scanner.ps1` line), add:

```
.\run_union_chart_dashboard.ps1  # ~4:32 PM -- runs AFTER EMA55_Cross (needs its union watchlist)
                                   #   interactive candlestick+volume charts for every union symbol
```

In the "Scanner pipeline" section, after the "Scanner pipeline -- EMA55 Cross Watchlist" subsection, add a new subsection:

```markdown
### Scanner pipeline -- Union Watchlist Chart Dashboard (`union_chart_dashboard.py`)

Full design: `docs/superpowers/specs/2026-08-20-union-chart-dashboard-design.md`.

1. Reads today's union watchlist symbols + confluence tier straight from
   `ema55_cross_scans/ema55_cross_scans.md`'s union tv-paste block
   (`parse_union_tiers`/`load_todays_union`) -- aborts with nothing written
   if that file is missing or not dated today (no stale publish)
2. `load_ohlc_many(symbols, lookback=250)` -- only DB entry point, per repo
   convention; symbols with <130 bars skipped (count logged, not silent)
3. `build_chart_data()` -- OHLCV per symbol as a plain `[date,o,h,l,c,v]`
   array, no server-side EMA (computed client-side so the live period
   control needs no regenerate)
4. `build_html()` -- one self-contained HTML file: vendored
   `lightweight-charts.js`, a global control bar (candle up/down color,
   EMA periods, symbol/tier filter), and a card grid (one chart per
   symbol) that lazy-constructs each chart via `IntersectionObserver` as
   it scrolls into view (required at ~500 symbols to keep first paint fast)
5. Writes `dashboard/union_charts.html`
```

In the "Output files (git-tracked)" table, add a row:

```
| `dashboard/union_charts.html` | `union_chart_dashboard.py` |
```

- [ ] **Step 6: Commit**

```bash
git add run_union_chart_dashboard.ps1 run_all_scanners.ps1 CLAUDE.md
git commit --no-verify -m "wire union chart dashboard into daily scanner pipeline"
```

---

## Manual verification (not automatable — no JS test runner in this repo)

After Task 6, on a machine with today's `market.db` populated and a fresh `ema55_cross_scans.md`:

```bash
python union_chart_dashboard.py
```

Open `dashboard/union_charts.html` in a browser and confirm:
- Cards render as you scroll (chart appears once a card enters view, not all at once on load)
- Typing new EMA periods (e.g. `10,30`) updates the overlay lines on already-visible charts
- Changing the up/down color pickers recolors visible candles immediately
- The symbol/tier filter box hides non-matching cards
- SEBI disclaimer banner/footer visible
