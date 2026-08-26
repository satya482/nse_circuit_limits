# Union Chart Signal Overlays Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the EMA55 union dashboard with Pine-parity signal candle colors, Satya EMAs coil boxes, optional EMA/volume layers, live TradingView industry grouping, day-change sorting, fixed/interactive chart modes, and adaptive mobile/tablet/desktop behavior.

**Architecture:** Keep `union_chart_dashboard.py` as the sole generator and calculate all historical annotations in Python before embedding records. Reuse `WaveTrendCalculator` for WaveTrend parity, keep Lightweight Charts as the client renderer, and add only compact signal/coil/industry metadata to the existing OHLCV payload. Client JavaScript owns rendering, regrouping, responsive behavior, and page-level switches; a gitignored JSON cache makes TradingView industry lookup non-fatal.

**Tech Stack:** Python 3.13, pandas, tradingview-screener, pytest, vanilla JavaScript/CSS, TradingView Lightweight Charts 4.1.3, PowerShell runner.

## Global Constraints

- Preserve the existing `dashboard/union_charts.html` artifact; do not create a parallel chart page.
- Load and retain 250 daily bars; require at least 130 bars per symbol.
- Fixed mode defaults to the latest six calendar months of candles plus 15 blank future logical slots; never fabricate future OHLCV.
- Pocket Pivot uses the most recent 10 down days and strict `volume > max_down_volume`.
- WaveTrend uses `hlc3`, EMA10, EMA10 deviation, EMA21 CI, and SMA4 signal; WaveTrend colors override Pocket Pivot blue.
- Coil confirmation uses two contained bars, mother high/low, 15 future trading-bar indices, and replacement of the last overlapping box.
- Volume defaults off and must never overlap the price region when enabled.
- EMA20 is cyan, EMA50 orange, EMA200 magenta; all EMA last-value and price-line labels stay hidden.
- Industry grouping defaults on; named industries sort alphabetically, `Unclassified` is last, and cards within a group sort by day change descending.
- Vertical page scrolling must work over charts on phones and tablets in both Fixed and Interactive modes.
- Do not add a runtime dependency or commit `.union_chart_cache/`, secrets, databases, logs, or raw downloads.
- Every generated or new Markdown/HTML artifact must contain `SEBI registered`; use `SEBI_HTML_BANNER` and `SEBI_HTML_FOOTER` in the generator.
- Preserve the user's existing `.ohlc_data/data_manifest.csv` modification.
- Commit with `git commit --no-verify`.

---

### Task 1: Historical signal and coil annotations

**Files:**
- Modify: `union_chart_dashboard.py:18-96`
- Modify: `tests/test_union_chart_dashboard.py:65-114`

**Interfaces:**
- Consumes: normalized ascending OHLCV `pd.DataFrame` with `date`, `open`, `high`, `low`, `close`, `volume`.
- Produces: `compute_pocket_pivot_flags(df, pp_len=10) -> list[bool]`, `compute_wavetrend_kinds(df) -> list[str | None]`, `compute_signal_kinds(df) -> list[str | None]`, and `compute_coil_boxes(df, min_inside=2, extend_bars=15) -> list[dict]`.
- Signal kinds are `None`, `"ppv"`, `"wt_bull"`, or `"wt_bear"`; later rendering relies on these exact strings.
- Coil dictionaries are `{"start_index": int, "end_index": int, "high": float, "low": float}`; `end_index` may be beyond the final OHLC row and Fixed mode reserves 15 blank logical slots so the full active projection is visible.

- [ ] **Step 1: Write failing Pocket Pivot tests**

Add imports and fixtures to `tests/test_union_chart_dashboard.py`:

```python
from union_chart_dashboard import (
    compute_coil_boxes,
    compute_pocket_pivot_flags,
    compute_signal_kinds,
    compute_wavetrend_kinds,
)


def _ohlcv(closes, volumes, highs=None, lows=None):
    n = len(closes)
    highs = highs or [c + 1.0 for c in closes]
    lows = lows or [c - 1.0 for c in closes]
    return pd.DataFrame({
        "date": pd.date_range("2026-01-01", periods=n, freq="D"),
        "open": closes,
        "high": highs,
        "low": lows,
        "close": closes,
        "volume": volumes,
    })


def test_pocket_pivot_uses_most_recent_ten_down_days_not_ten_bars():
    closes = [100.0]
    volumes = [100.0]
    for i in range(1, 22):
        closes.append(closes[-1] - 1 if i % 2 else closes[-1] + 2)
        volumes.append(100.0 + i)
    closes.append(closes[-1] + 1)
    volumes.append(1000.0)
    flags = compute_pocket_pivot_flags(_ohlcv(closes, volumes))
    assert flags[-1] is True


def test_pocket_pivot_requires_ten_prior_down_days_and_strictly_higher_volume():
    few = _ohlcv([10, 9, 10, 9, 10, 11], [1, 10, 1, 20, 1, 100])
    assert compute_pocket_pivot_flags(few)[-1] is False

    closes = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 11]
    volumes = [1, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100]
    assert compute_pocket_pivot_flags(_ohlcv(closes, volumes))[-1] is False
```

- [ ] **Step 2: Run Pocket Pivot tests and verify failure**

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "pocket_pivot" -v
```

Expected: FAIL during import because `compute_pocket_pivot_flags` does not exist.

- [ ] **Step 3: Implement historical Pocket Pivot flags**

Add to `union_chart_dashboard.py`:

```python
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
```

- [ ] **Step 4: Write failing WaveTrend and precedence tests**

Use a deterministic oscillating fixture and assert against the repo calculator:

```python
from wavetrend_scanner import WaveTrendCalculator


def test_wavetrend_kinds_match_existing_calculator_for_all_bars():
    closes = [100 + ((i % 14) - 7) * 2 + i * 0.05 for i in range(100)]
    df = _ohlcv(closes, [1000.0] * len(closes))
    expected = WaveTrendCalculator().calc_from_series(
        (df["high"] + df["low"] + df["close"]) / 3
    )["cross_type"].map({
        "BULL_CROSS": "wt_bull",
        "BEAR_CROSS": "wt_bear",
        "NONE": None,
    }).tolist()
    assert compute_wavetrend_kinds(df) == expected


def test_wavetrend_kind_overrides_pocket_pivot(monkeypatch):
    df = _ohlcv([10, 11, 12], [10, 20, 30])
    monkeypatch.setattr(
        "union_chart_dashboard.compute_pocket_pivot_flags",
        lambda frame: [False, False, True],
    )
    monkeypatch.setattr(
        "union_chart_dashboard.compute_wavetrend_kinds",
        lambda frame: [None, None, "wt_bull"],
    )
    assert compute_signal_kinds(df) == [None, None, "wt_bull"]
```

- [ ] **Step 5: Implement WaveTrend mapping and precedence**

Add the import and functions:

```python
from wavetrend_scanner import WaveTrendCalculator


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
```

- [ ] **Step 6: Write failing Satya EMAs coil tests**

```python
def test_coil_box_uses_mother_range_and_fifteen_bars_after_confirmation():
    df = _ohlcv(
        [10, 10, 10],
        [100, 100, 100],
        highs=[12, 11, 11.5],
        lows=[8, 9, 8.5],
    )
    assert compute_coil_boxes(df) == [
        {"start_index": 0, "end_index": 17, "high": 12.0, "low": 8.0}
    ]


def test_new_overlapping_coil_replaces_previous_box():
    df = _ohlcv(
        [10, 10, 10, 10],
        [100] * 4,
        highs=[12, 11.5, 11, 10.5],
        lows=[8, 8.5, 9, 9.5],
    )
    assert compute_coil_boxes(df) == [
        {"start_index": 1, "end_index": 18, "high": 11.5, "low": 8.5}
    ]
```

- [ ] **Step 7: Implement coil-box calculation**

```python
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
```

- [ ] **Step 8: Run focused annotation tests**

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "pocket_pivot or wavetrend or coil" -v
```

Expected: all new tests PASS.

- [ ] **Step 9: Commit Task 1**

```powershell
git add union_chart_dashboard.py tests/test_union_chart_dashboard.py
git commit --no-verify -m "feat(charts): add signal annotations"
```

### Task 2: TradingView industry cache

**Files:**
- Modify: `.gitignore`
- Modify: `union_chart_dashboard.py:18-74`
- Modify: `tests/test_union_chart_dashboard.py`

**Interfaces:**
- Produces: `fetch_tradingview_industries(symbols: set[str]) -> dict[str, str]` and `resolve_industries(symbols, cache_path, as_of, fetcher=fetch_tradingview_industries) -> dict[str, str]`.
- Cache JSON is `{"as_of": "YYYY-MM-DD", "industries": {"SYMBOL": "Industry"}}` and is written atomically.
- Every requested symbol is returned; missing values are exactly `"Unclassified"`.

- [ ] **Step 1: Write failing cache and fallback tests**

Add `import json` with the standard-library imports in
`tests/test_union_chart_dashboard.py`, then add:

```python
from union_chart_dashboard import resolve_industries


def test_resolve_industries_merges_live_values_and_writes_cache(tmp_path):
    cache = tmp_path / "industries.json"
    cache.write_text(
        json.dumps({"as_of": "2026-08-25", "industries": {"OLD": "Banks"}}),
        encoding="utf-8",
    )
    result = resolve_industries(
        {"OLD", "NEW", "MISS"},
        str(cache),
        "2026-08-26",
        fetcher=lambda symbols: {"NEW": "Software"},
    )
    assert result == {"OLD": "Banks", "NEW": "Software", "MISS": "Unclassified"}
    saved = json.loads(cache.read_text(encoding="utf-8"))
    assert saved["as_of"] == "2026-08-26"
    assert saved["industries"] == {"NEW": "Software", "OLD": "Banks"}
    assert not (tmp_path / "industries.json.tmp").exists()


def test_resolve_industries_uses_cache_when_live_fetch_fails(tmp_path):
    cache = tmp_path / "industries.json"
    cache.write_text(
        json.dumps({"as_of": "2026-08-25", "industries": {"AAA": "Steel"}}),
        encoding="utf-8",
    )
    def fail(_symbols):
        raise RuntimeError("TradingView unavailable")
    assert resolve_industries({"AAA", "BBB"}, str(cache), "2026-08-26", fail) == {
        "AAA": "Steel",
        "BBB": "Unclassified",
    }
```

- [ ] **Step 2: Run cache tests and verify failure**

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "resolve_industries" -v
```

Expected: FAIL during import because `resolve_industries` does not exist.

- [ ] **Step 3: Implement TradingView fetch, merge, and atomic cache write**

Add constants and functions:

```python
INDUSTRY_CACHE = os.path.join(REPO_DIR, ".union_chart_cache", "industries.json")


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
            cached = json.load(fh).get("industries", {})
    except (FileNotFoundError, OSError, ValueError, TypeError):
        cached = {}
    try:
        live = {k: v for k, v in fetcher(set(symbols)).items() if k and v}
        if live:
            merged = {**cached, **live}
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            tmp = cache_path + ".tmp"
            with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump({"as_of": as_of, "industries": dict(sorted(merged.items()))}, fh)
                fh.write("\n")
            os.replace(tmp, cache_path)
            cached = merged
    except Exception as exc:
        print(f"[union_chart_dashboard] industry refresh fallback: {exc}")
    return {symbol: cached.get(symbol, "Unclassified") for symbol in sorted(symbols)}
```

- [ ] **Step 4: Ignore the runtime cache and run tests**

Append to `.gitignore`:

```gitignore
.union_chart_cache/
```

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "resolve_industries" -v
```

Expected: both cache tests PASS.

- [ ] **Step 5: Commit Task 2**

```powershell
git add .gitignore union_chart_dashboard.py tests/test_union_chart_dashboard.py
git commit --no-verify -m "feat(charts): cache TV industries"
```

### Task 3: Enriched chart-record contract

**Files:**
- Modify: `union_chart_dashboard.py:74-96,264-285`
- Modify: `tests/test_union_chart_dashboard.py:81-114,155-266`

**Interfaces:**
- Changes `build_chart_data(ohlc_map, tiers, industries=None, min_bars=MIN_BARS) -> tuple[list[dict], int]`.
- Each record is `{"symbol", "tier", "industry", "day_change", "bars", "signals", "coil_boxes"}`.
- `day_change` remains unrounded for sorting; rendering formats two decimals.

- [ ] **Step 1: Update the record test to fail on missing metadata**

Replace the positive record test assertions with:

```python
def test_build_chart_data_enriches_record_with_metadata_and_annotations(monkeypatch):
    ohlc_map = {"FOO": _fixture_df(200)}
    monkeypatch.setattr(
        "union_chart_dashboard.compute_signal_kinds",
        lambda df: [None] * 199 + ["ppv"],
    )
    monkeypatch.setattr(
        "union_chart_dashboard.compute_coil_boxes",
        lambda df: [{"start_index": 180, "end_index": 197, "high": 300.0, "low": 290.0}],
    )
    records, skipped = build_chart_data(
        ohlc_map,
        {"FOO": "ALL 4"},
        industries={"FOO": "Software"},
        min_bars=130,
    )
    record = records[0]
    assert skipped == 0
    assert record["industry"] == "Software"
    assert record["day_change"] == pytest.approx((299.5 / 298.5 - 1) * 100)
    assert record["signals"][-1] == "ppv"
    assert record["coil_boxes"][0]["end_index"] == 197
```

Add `import pytest` near the existing imports.

- [ ] **Step 2: Run the record test and verify failure**

```powershell
python -m pytest tests/test_union_chart_dashboard.py::test_build_chart_data_enriches_record_with_metadata_and_annotations -v
```

Expected: FAIL because the signature does not accept `industries` and metadata is absent.

- [ ] **Step 3: Implement record enrichment and per-symbol failure isolation**

Change `build_chart_data` so the loop contains:

```python
industries = industries or {}
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
                float(row.open), float(row.high), float(row.low),
                float(row.close), float(row.volume),
            ]
            for row in df.itertuples(index=False)
        ]
        previous_close = bars[-2][4]
        day_change = (bars[-1][4] / previous_close - 1) * 100
        records.append({
            "symbol": symbol,
            "tier": tier,
            "industry": industries.get(symbol, "Unclassified"),
            "day_change": day_change,
            "bars": bars,
            "signals": compute_signal_kinds(df),
            "coil_boxes": compute_coil_boxes(df),
        })
    except Exception as exc:
        skipped += 1
        print(f"[union_chart_dashboard] skip {symbol}: annotation failure: {exc}")
return records, skipped
```

- [ ] **Step 4: Update `main()` to resolve industries before building records**

Use:

```python
industries = resolve_industries(tiers.keys(), INDUSTRY_CACHE, TODAY)
ohlc_map = load_ohlc_many(list(tiers.keys()), lookback=LOOKBACK)
records, skipped = build_chart_data(ohlc_map, tiers, industries=industries)
```

In main-path tests, monkeypatch `resolve_industries` to return deterministic mappings and avoid network access:

```python
monkeypatch.setattr(
    ucd,
    "resolve_industries",
    lambda symbols, cache_path, as_of: {sym: "Test Industry" for sym in symbols},
)
```

- [ ] **Step 5: Run the full focused test file**

```powershell
python -m pytest tests/test_union_chart_dashboard.py -v
```

Expected: all dashboard tests PASS.

- [ ] **Step 6: Commit Task 3**

```powershell
git add union_chart_dashboard.py tests/test_union_chart_dashboard.py
git commit --no-verify -m "feat(charts): enrich chart records"
```

### Task 4: Signal colors, EMA switch, optional volume, and coil boxes

**Files:**
- Modify: `union_chart_dashboard.py:99-261`
- Modify: `tests/test_union_chart_dashboard.py:116-153`

**Interfaces:**
- Client state is `uiState = {emaVisible: true, volumeVisible: false, interactive: false}`.
- `chartsBySymbol[symbol]` stores `chart`, `candleSeries`, `volumeSeries`, `emaSeries`, `coilLayer`, `record`.
- Fixed signal colors are `ppv=#2962ff`, `wt_bull=#ffffff`, `wt_bear=#fdd835`.
- EMA palette begins `#00bcd4`, `#ff9800`, `#e040fb`.

- [ ] **Step 1: Write failing HTML-contract tests**

Extend `test_build_html_has_interactive_controls` and add a rendering test:

```python
def test_build_html_has_layer_switches_and_fixed_signal_colors():
    html = build_html([], "2026-08-26")
    assert 'id="emaVisible"' in html
    assert 'id="volumeVisible"' in html
    assert 'id="chartMode"' in html
    assert 'volumeVisible: false' in html
    assert 'interactive: false' in html
    assert 'ppv: "#2962ff"' in html
    assert 'wt_bull: "#ffffff"' in html
    assert 'wt_bear: "#fdd835"' in html
    assert "lastValueVisible: false" in html
    assert "priceLineVisible: false" in html


def test_build_html_separates_volume_and_price_scales():
    html = build_html([], "2026-08-26")
    assert "bottom: 0.05" in html
    assert "bottom: 0.25" in html
    assert "top: 0.78" in html
```

- [ ] **Step 2: Run new HTML tests and verify failure**

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "layer_switches or separates_volume" -v
```

Expected: both tests FAIL because the controls and scale options are absent.

- [ ] **Step 3: Add page-level state and candle signal rendering**

At the top of `_JS_TEMPLATE`, add:

```javascript
const SIGNAL_COLORS = { ppv: "#2962ff", wt_bull: "#ffffff", wt_bear: "#fdd835" };
const EMA_COLORS = ["#00bcd4", "#ff9800", "#e040fb", "#8bc34a", "#ff5252"];
const uiState = { emaVisible: true, volumeVisible: false, interactive: false };

function candleData(record) {
  return record.bars.map(function(b, i) {
    const point = { time: b[0], open: b[1], high: b[2], low: b[3], close: b[4] };
    const color = SIGNAL_COLORS[record.signals[i]];
    if (color) {
      point.color = color;
      point.borderColor = color;
      point.wickColor = color;
    }
    return point;
  });
}
```

Change `dataBySymbol` into `recordBySymbol`, set `candleSeries.setData(candleData(record))`, and preserve normal up/down series options so only annotated points carry fixed colors.

When chart construction finishes, store the complete entry before applying
controls or drawing overlays:

```javascript
const entry = {
  chart: chart,
  candleSeries: candleSeries,
  volumeSeries: volumeSeries,
  emaSeries: [],
  coilLayer: el.parentElement.querySelector(".coil-layer"),
  record: record,
};
chartsBySymbol[symbol] = entry;
entry.emaSeries = addEmaSeries(entry, getEmaPeriods());
applyVolumeState(entry);
redrawCoils(entry);
```

- [ ] **Step 4: Add deterministic EMA lines and visibility switch**

Use this exact series factory:

```javascript
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
```

Bind `#emaVisible` so it updates `uiState.emaVisible` and calls `rebuildEmas` for initialized charts.

- [ ] **Step 5: Make volume default-hidden and non-overlapping**

After creating the histogram series, call:

```javascript
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
```

Bind `#volumeVisible`; Pocket Pivot data remains in the candle series and is not recomputed or hidden.

- [ ] **Step 6: Draw and redraw Satya coil boxes in a clipped overlay**

Add `<div class="coil-layer"></div>` inside each `.chart-wrap`, make `.chart-wrap` positioned, and use:

```javascript
function redrawCoils(entry) {
  entry.coilLayer.replaceChildren();
  entry.record.coil_boxes.forEach(function(box) {
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
}
```

Subscribe with `timeScale().subscribeVisibleLogicalRangeChange`, call after chart creation/control updates, and attach a `ResizeObserver`. CSS must set `overflow:hidden`, gray border, `rgba(128,128,128,.10)` fill, and `pointer-events:none`. Fixed mode exposes logical indices through `bars.length - 1 + 15`; these are blank display slots only and must not be added to candle or volume data.

- [ ] **Step 7: Add accessible flip-switch markup and CSS**

Add to `#controls`:

```html
<label class="switch-row"><span>EMAs</span><input type="checkbox" id="emaVisible" checked><span class="switch"></span></label>
<label class="switch-row"><span>Volume</span><input type="checkbox" id="volumeVisible"><span class="switch"></span></label>
<label class="switch-row"><span>Interactive</span><input type="checkbox" id="chartMode"><span class="switch"></span></label>
```

Keep visible text next to every switch; do not rely on color alone.

- [ ] **Step 8: Run focused rendering tests**

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "build_html" -v
```

Expected: all HTML tests PASS.

- [ ] **Step 9: Commit Task 4**

```powershell
git add union_chart_dashboard.py tests/test_union_chart_dashboard.py
git commit --no-verify -m "feat(charts): render signal layers"
```

### Task 5: Industry sorting, fixed mode, and adaptive touch layout

**Files:**
- Modify: `union_chart_dashboard.py:99-261`
- Modify: `tests/test_union_chart_dashboard.py:116-153`

**Interfaces:**
- Sort values are exactly `industry`, `day-desc`, `day-asc`; default is `industry`.
- Fixed mode begins at the first bar on/after the six-calendar-month cutoff and ends 15 logical slots after the latest OHLC bar.
- `applySortAndFilter()` owns both DOM order and empty industry-heading visibility.

- [ ] **Step 1: Write failing card/sort/responsive tests**

```python
def test_build_html_renders_day_change_and_sort_metadata():
    records = [{
        "symbol": "FOO", "tier": "ALL 5", "industry": "Software",
        "day_change": 2.3456,
        "bars": [["2026-08-25", 1, 2, 0.5, 1.5, 100]],
        "signals": [None], "coil_boxes": [],
    }]
    html = build_html(records, "2026-08-26")
    assert 'data-industry="Software"' in html
    assert 'data-day-change="2.3456"' in html
    assert "+2.35%" in html
    assert 'id="sortMode"' in html
    assert '<option value="industry" selected>' in html
    assert '<option value="day-desc">' in html
    assert '<option value="day-asc">' in html


def test_build_html_has_fixed_mode_and_adaptive_touch_contract():
    html = build_html([], "2026-08-26")
    assert "repeat(auto-fit,minmax(min(100%,320px),1fr))" in html.replace(" ", "")
    assert "vertTouchDrag: false" in html
    assert "setVisibleLogicalRange" in html
    assert "setUTCMonth" in html
    assert "Unclassified" in html
```

Update the older `test_build_html_embeds_symbol_data_and_cards` literal record
to include `industry`, `day_change`, `signals`, and `coil_boxes` with this same
shape. Do not make production rendering silently accept an incomplete record.

- [ ] **Step 2: Run the new UI tests and verify failure**

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "sort_metadata or adaptive_touch" -v
```

Expected: both tests FAIL because sort metadata and fixed-mode functions are absent.

- [ ] **Step 3: Render card metadata and signed day change**

Escape dynamic HTML using `html.escape` imported as `_escape`, and build headers with:

```python
change = float(r["day_change"])
change_class = "gain" if change > 0 else "loss" if change < 0 else "flat"
change_text = f"{change:+.2f}%" if change else "0.00%"
card = (
    f'<div class="card" data-q="{_escape(r["symbol"])} {_escape(r["tier"])}" '
    f'data-symbol="{_escape(r["symbol"])}" '
    f'data-industry="{_escape(r["industry"])}" data-day-change="{change}">'
    f'<div class="hdr"><a href="https://in.tradingview.com/chart/?symbol=NSE:{_escape(r["symbol"])}" '
    f'target="_blank">{_escape(r["symbol"])}</a>'
    f'<span class="day-change {change_class}">{change_text}</span>'
    f'<span class="tier">{_escape(r["tier"])}</span></div>'
    f'<div class="chart-wrap"><div class="chart" id="chart-{_escape(r["symbol"])}"></div>'
    f'<div class="coil-layer"></div></div></div>'
)
```

Do not render industry inside a card.

- [ ] **Step 4: Add sort selector and deterministic DOM regrouping**

Add:

```html
<label>Sort <select id="sortMode">
  <option value="industry" selected>Industry groups</option>
  <option value="day-desc">Day change: highest first</option>
  <option value="day-asc">Day change: lowest first</option>
</select></label>
```

Implement:

```javascript
function cardCompare(a, b, direction) {
  const delta = Number(a.dataset.dayChange) - Number(b.dataset.dayChange);
  if (delta !== 0) return direction * delta;
  return a.dataset.symbol.localeCompare(b.dataset.symbol);
}

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
      const groupCards = groups[industry].sort(function(a, b) { return cardCompare(a, b, -1); });
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
```

Bind both `#sortMode` change and `#q` input to `applySortAndFilter()`, then call it before registering the `IntersectionObserver`.

- [ ] **Step 5: Implement Fixed/Interactive behavior with 15 blank future slots**

```javascript
function fixedLogicalRange(record) {
  const last = record.bars[record.bars.length - 1][0];
  const cutoff = new Date(last + "T00:00:00Z");
  cutoff.setUTCMonth(cutoff.getUTCMonth() - 6);
  const cutoffText = cutoff.toISOString().slice(0, 10);
  const firstIndex = record.bars.findIndex(function(bar) { return bar[0] >= cutoffText; });
  return {
    from: firstIndex >= 0 ? firstIndex : 0,
    to: record.bars.length - 1 + 15,
  };
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
      axisPressedMouseMove: uiState.interactive,
      mouseWheel: false,
      pinch: uiState.interactive,
    },
  });
  if (!uiState.interactive) {
    entry.chart.timeScale().setVisibleLogicalRange(fixedLogicalRange(entry.record));
  }
}
```

Bind `#chartMode`; when unchecked, every initialized chart immediately resets. Do not call `fitContent()` after applying the fixed logical range and do not append future data points. Add `applyChartMode(entry)` to the end of `buildChart()` after the entry is stored in `chartsBySymbol`, so lazily initialized cards honor the current mode.

- [ ] **Step 6: Apply adaptive grid, sticky controls, and resize behavior**

Use:

```css
#controls{position:sticky;top:0;z-index:20;display:flex;flex-wrap:wrap}
#grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:10px}
.industry-heading{grid-column:1/-1;margin:14px 0 0}
.chart-wrap{position:relative;overflow:hidden}
.chart{height:clamp(240px,42vw,320px)}
@media(max-width:600px){#grid{grid-template-columns:1fr}.chart{height:290px}}
```

In each chart's `ResizeObserver`, call `chart.applyOptions({width: el.clientWidth})` and `redrawCoils(entry)`. This lets tablet portrait, landscape, and split-screen widths reflow without reload. Do not set CSS `touch-action`; Lightweight Charts' `vertTouchDrag: false` must remain responsible for yielding vertical gestures to page scrolling while Interactive mode retains horizontal drag and pinch.

- [ ] **Step 7: Run focused UI tests**

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "build_html" -v
```

Expected: all HTML tests PASS.

- [ ] **Step 8: Commit Task 5**

```powershell
git add union_chart_dashboard.py tests/test_union_chart_dashboard.py
git commit --no-verify -m "feat(charts): add responsive sorting"
```

### Task 6: Integration, documentation, live generation, and verification

**Files:**
- Modify: `CLAUDE.md:177-195,437`
- Modify: `HANDOFF.md`
- Regenerate: `dashboard/union_charts.html`
- Verify: `run_union_chart_dashboard.ps1`

**Interfaces:**
- `main()` remains the scheduled entry point.
- `run_union_chart_dashboard.ps1` continues staging only `dashboard/union_charts.html`; runtime industry cache stays local.

- [ ] **Step 1: Run the focused dashboard suite**

```powershell
python -m pytest tests/test_union_chart_dashboard.py -v
```

Expected: all tests PASS with no network or real SQLite dependency.

- [ ] **Step 2: Run related WaveTrend regressions**

```powershell
python -m pytest tests/test_net_thrust_wavetrend.py tests/test_us_wt_bullcross_scanner.py -v
```

Expected: all selected tests PASS.

- [ ] **Step 3: Run the full Python suite**

```powershell
python -m pytest
```

Expected: all tests PASS. Record the exact passed count in `HANDOFF.md`.

- [ ] **Step 4: Update operating documentation**

In `CLAUDE.md`, replace the current union-chart bullets with the concrete contract:

```markdown
- Server-computed historical PPV, WaveTrend bull/bear, and Satya EMAs two-inside-bar coil annotations.
- Default TradingView-industry grouping with current-day highest/lowest sort modes and cached industry fallback.
- Fixed six-month view by default; page-level Interactive, EMA, and default-off volume switches.
- Adaptive one-column phone, auto-adjusting tablet, and auto-fit desktop grid; vertical page scroll remains enabled over charts.
```

Add a dated `HANDOFF.md` entry containing the implementation summary, test counts, generated dashboard date/size, live industry refresh or cache fallback status, and any manual browser checks still pending.

- [ ] **Step 5: Generate the dashboard from current local OHLCV**

First verify the union title date:

```powershell
Get-Content ema55_cross_scans\ema55_cross_scans.md -TotalCount 5
python union_chart_dashboard.py
```

Expected when the union input is fresh: a nonzero `N charted` message, industry refresh or explicit cache fallback, and atomic replacement of `dashboard/union_charts.html`. If the report is stale, expect the established `SKIP` message and do not overwrite the prior dashboard; record that constraint rather than running upstream live scanners without authorization.

- [ ] **Step 6: Verify the generated artifact**

```powershell
rg -n "SEBI registered|volumeVisible|emaVisible|chartMode|sortMode|wt_bull|coil_boxes|Industry groups" dashboard\union_charts.html
Get-Item dashboard\union_charts.html | Select-Object Length,LastWriteTime
```

Expected: every required token exists, the title date matches the fresh input when regeneration ran, and file size is nonzero.

- [ ] **Step 7: Perform manual browser/device checks**

Open `dashboard/union_charts.html` and verify:

```text
Phone width: one column; vertical drag over chart scrolls page.
Tablet portrait/landscape: grid changes automatically without reload.
Desktop: multiple columns and sticky controls.
Industry default: alphabetical headings, Unclassified last, day change descending inside each group.
Flat sorts: highest-first and lowest-first; card charts survive reorder.
Fixed: exactly six months of candles plus 15 blank future slots; no pan or pinch and no fabricated future OHLCV.
Interactive: horizontal pan and pinch work; vertical page scroll still works.
Return to Fixed: every initialized chart resets.
EMA: cyan/orange/magenta, no last-value labels, switch off/on works.
Volume: off initially; on uses lower 22% band and never covers price.
Signals: PPV blue; WaveTrend bull white/bear yellow override blue.
Coils: gray box, no mother-candle repaint, overlapping boxes replaced.
```

- [ ] **Step 8: Run final repository checks**

```powershell
git diff --check -- . ':!.ohlc_data/data_manifest.csv'
git status --short
```

Expected: no whitespace errors in task-owned changes. The pre-existing `.ohlc_data/data_manifest.csv` modification remains untouched. `.union_chart_cache/` is ignored. The brainstorming `.superpowers/` directory remains untracked unless separately ignored or removed with user approval.

- [ ] **Step 9: Commit implementation documentation and generated output**

Stage only task-owned paths:

```powershell
git add .gitignore union_chart_dashboard.py tests/test_union_chart_dashboard.py CLAUDE.md HANDOFF.md
if (Test-Path dashboard\union_charts.html) { git add dashboard\union_charts.html }
git commit --no-verify -m "docs(charts): document signal dashboard"
```

Before any push, inspect `git status --short` and the commits created by Tasks 1-6. Do not include `.ohlc_data/data_manifest.csv`, `.superpowers/`, or `.union_chart_cache/`.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
