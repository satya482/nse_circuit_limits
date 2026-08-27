> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Union Chart Mobile Card Layout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make union chart cards larger and easier to use across phones, tablets, and desktops, start every page load with EMAs hidden, place the clickable symbol at the right edge, and add an independent Pine-parity ZLEMA25 overlay.

**Architecture:** Keep `union_chart_dashboard.py` as the sole HTML generator and compute ZLEMA25 client-side from the already embedded closes. Protect layout/defaults with generated-HTML contracts and execute the generated ZLEMA function with Node for golden-value parity; preserve lazy chart creation, explicit six-month logical ranges, Chrome-safe scheduled coil redraws, sorting, and stale-input safeguards.

**Tech Stack:** Python 3.13, pytest, vanilla JavaScript/CSS, TradingView Lightweight Charts 4.1.3, PowerShell.

## Global Constraints

- Modify the existing `dashboard/union_charts.html` artifact; do not create a parallel dashboard.
- Every page load starts with EMAs off; do not persist EMA visibility in local storage, session storage, cookies, or URL parameters.
- Add a separate ZLEMA25 switch that starts off on every page load and does not alter EMA visibility.
- ZLEMA25 uses lag 12 and Pine's recursive EMA seed, renders as a width-1 step line, colors rising points `#ffffff` and first/flat/falling points `#ff0000`, and hides last-value and price-line labels.
- Keep volume off by default and independent from EMA visibility.
- Preserve the explicit six-calendar-month fixed range plus 15 blank future logical slots; never fabricate future OHLCV or call `fitContent()`.
- Preserve vertical page scrolling over charts and automatic one/two-column tablet reflow.
- Use a 440px preferred grid minimum, `clamp(330px, 38vw, 400px)` chart height, and a one-column 330px phone layout at 600px or below.
- Render percentage left, tier centered, and the TradingView symbol link right; give the symbol a minimum 44px-high tap target.
- Preserve existing EMA colors, hidden EMA price labels, volume/price scale separation, Chrome-safe double-animation-frame coil redraw and `z-index: 2`, signal candle colors, sorting, filtering, and interaction modes.
- Generate `dashboard/union_charts.html` only from a union report dated today; stale input must leave the previous dashboard byte-for-byte unchanged.
- Every new or generated Markdown/HTML file must contain `SEBI registered`; continue using `SEBI_HTML_BANNER` and `SEBI_HTML_FOOTER` in the generator.
- Preserve the user's existing `.ohlc_data/data_manifest.csv` modification and untracked `.superpowers/` directory.
- Commit with `git commit --no-verify`.

---

## File Structure

- Modify `tests/test_union_chart_dashboard.py`: generated-HTML contracts for default EMA/ZLEMA states, header order/accessibility, responsive CSS, ZLEMA controls, and Node-executed calculation parity.
- Modify `union_chart_dashboard.py`: initial UI state, EMA/ZLEMA controls and series, card-header markup/classes, and adaptive CSS.
- Modify `dashboard/union_charts.html` through normal generation only when `ema55_cross_scans/ema55_cross_scans.md` is dated today. With stale input, a renderer-only artifact patch is permitted only when the embedded `CHART_DATA` bytes and displayed as-of date remain unchanged.
- Modify `HANDOFF.md` after verification to record the completed behavior, test evidence, and whether the tracked dashboard was refreshed or preserved.

### Task 1: Add failing HTML contract tests

**Files:**
- Modify: `tests/test_union_chart_dashboard.py:283-413`

**Interfaces:**
- Consumes: `build_html(records: list[dict], as_of: str) -> str`.
- Produces: regression contracts over the generated HTML string; no runtime API changes.

- [ ] **Step 1: Add a reusable one-card fixture**

Add this helper immediately before `test_build_html_embeds_symbol_data_and_cards`:

```python
def _chart_record(
    symbol="FOO", tier="ALL 5", industry="Software", day_change=2.3456
):
    return {
        "symbol": symbol,
        "tier": tier,
        "industry": industry,
        "day_change": day_change,
        "bars": [["2026-08-25", 1, 2, 0.5, 1.5, 100]],
        "signals": [None],
        "coil_boxes": [],
    }
```

Refactor the nearby single-record HTML tests to call `build_html([_chart_record(...)], ...)` where doing so removes duplicated record dictionaries without changing their assertions. Keep the hostile-symbol test's explicit dictionary because it verifies JSON escaping.

- [ ] **Step 2: Add the default-hidden EMA test**

Add:

```python
def test_build_html_starts_with_emas_hidden_and_switch_unchecked():
    html = build_html([], "2026-08-27")
    assert "emaVisible: false" in html
    label_start = html.index("<span>EMAs</span>")
    input_start = html.index("<input", label_start)
    ema_input = html[input_start : html.index(">", input_start) + 1]
    assert "checked" not in ema_input
    assert "localStorage" not in html
    assert "sessionStorage" not in html
```

The split isolates the EMA `<input>` opening tag so another checkbox cannot satisfy or invalidate the assertion.

- [ ] **Step 3: Add header-order and tap-target tests**

Add:

```python
def test_build_html_orders_change_tier_and_symbol_for_right_thumb_access():
    html = build_html([_chart_record()], "2026-08-27")
    header = html.split('<div class="hdr">', 1)[1].split("</div>", 1)[0]
    assert header.index('class="day-change gain"') < header.index('class="tier"')
    assert header.index('class="tier"') < header.index('class="symbol-link"')
    assert 'class="symbol-link"' in header
    assert 'href="https://in.tradingview.com/chart/?symbol=NSE:FOO"' in header
    assert 'target="_blank"' in header


def test_build_html_has_centered_header_and_44px_symbol_target():
    compact = "".join(build_html([], "2026-08-27").split())
    assert ".hdr{display:grid;grid-template-columns:1frauto1fr;align-items:center" in compact
    assert ".day-change{justify-self:start" in compact
    assert ".tier{justify-self:center" in compact
    assert ".symbol-link{justify-self:end;min-height:44px" in compact
```

- [ ] **Step 4: Update the adaptive-layout contract**

Replace the old 320px assertion in `test_build_html_has_fixed_mode_and_adaptive_touch_contract` and add height/breakpoint assertions:

```python
def test_build_html_has_fixed_mode_and_adaptive_touch_contract():
    html = build_html([], "2026-08-27")
    compact = "".join(html.split())
    assert "repeat(auto-fit,minmax(min(100%,440px),1fr))" in compact
    assert ".chart{height:clamp(330px,38vw,400px)}" in compact
    assert "@media(max-width:600px){#grid{grid-template-columns:1fr}.chart{height:330px}}" in compact
    assert "vertTouchDrag:false" in compact
    assert "setVisibleLogicalRange" in html
    assert "fitContent(" not in html
    assert "setUTCMonth" not in html
    assert "Unclassified" in html
```

- [ ] **Step 5: Run the new contracts and verify they fail for the intended reasons**

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "emas_hidden or right_thumb or centered_header or adaptive_touch" -v
```

Expected: four failures identifying the current `emaVisible: true`, checked EMA input, symbol-first header, 320px grid minimum, and 240-320px/290px chart heights. There must be no import, fixture, or syntax error.

### Task 2: Implement the approved responsive layout and defaults

**Files:**
- Modify: `union_chart_dashboard.py:268`
- Modify: `union_chart_dashboard.py:558-565`
- Modify: `union_chart_dashboard.py:584-603`
- Modify: `union_chart_dashboard.py:612`

**Interfaces:**
- Consumes: the existing `uiState`, `build_html`, `buildChart`, `rebuildEmas`, `ResizeObserver`, and sorting code.
- Produces: the same standalone HTML interface and control IDs; adds only the `symbol-link` presentation class.

- [ ] **Step 1: Default EMA visibility to off**

Change only the initial value in `_JS_TEMPLATE`:

```javascript
const uiState = { emaVisible: false, volumeVisible: false, interactive: false };
```

Leave `addEmaSeries`, `rebuildEmas`, the EMA switch handler, EMA colors, `lastValueVisible: false`, and `priceLineVisible: false` unchanged. This makes lazy-created charts honor the current switch state without adding persistence.

- [ ] **Step 2: Render the three header zones in visual and DOM order**

Replace the header portion of each generated card with:

```python
f'<div class="hdr">'
f'<span class="day-change {change_class}">{change_text}</span>'
f'<span class="tier">{_escape(r["tier"])}</span>'
f'<a class="symbol-link" '
f'href="https://in.tradingview.com/chart/?symbol=NSE:{_escape(r["symbol"])}" '
f'target="_blank" rel="noopener noreferrer">{_escape(r["symbol"])}</a>'
f'</div>'
```

Do not change `data-symbol`, `data-day-change`, percentage rounding/color semantics, the TradingView destination, or sort behavior.

- [ ] **Step 3: Apply the adaptive grid, chart height, and header CSS**

Replace the relevant rules with these minified generator-string forms:

```css
#grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));gap:10px}}
.hdr{{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;font-weight:600;margin-bottom:6px}}
.symbol-link{{justify-self:end;min-height:44px;display:inline-flex;align-items:center;padding-left:12px;color:#58a6ff;text-decoration:none}}
.symbol-link:focus-visible{{outline:2px solid #58a6ff;outline-offset:2px}}
.tier{{justify-self:center;font-size:.7rem;color:#8b949e;border:1px solid #30363d;border-radius:4px;padding:1px 6px}}
.day-change{{justify-self:start;font-size:.8rem}}
.chart{{height:clamp(330px,38vw,400px)}}
@media(max-width:600px){{#grid{{grid-template-columns:1fr}}.chart{{height:330px}}}}
```

Remove the superseded `.hdr a`, flex header, percentage auto margins, 320px grid minimum, 240-320px chart height, and 290px phone height. Leave `.chart-wrap`, `ResizeObserver`, coil overlay, and page overflow behavior unchanged.

- [ ] **Step 4: Make the EMA switch markup unchecked**

Render:

```html
<label class="switch-row"><span>EMAs</span><input type="checkbox" id="emaVisible"><span class="switch"></span></label>
```

Do not change the volume or interaction switches.

- [ ] **Step 5: Run the focused tests**

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py -v --basetemp=.pytest_tmp/union-card-layout-focused
```

Expected: all union dashboard tests pass. The current suite has 46 tests before the layout/ZLEMA additions; the exact new total will be higher, with zero failures.

- [ ] **Step 6: Inspect the focused diff**

Run:

```powershell
git diff --check -- union_chart_dashboard.py tests/test_union_chart_dashboard.py
git diff -- union_chart_dashboard.py tests/test_union_chart_dashboard.py
```

Expected: no whitespace errors; the diff contains only the planned contracts, UI-state default, card-header order/classes, responsive CSS, and unchecked EMA input.

- [ ] **Step 7: Commit the tested implementation**

Run:

```powershell
git add -- union_chart_dashboard.py tests/test_union_chart_dashboard.py
git diff --cached --check
git diff --cached --name-only
git commit --no-verify -m "feat(charts): enlarge mobile-friendly cards"
```

Expected staged names: only `union_chart_dashboard.py` and `tests/test_union_chart_dashboard.py`.

### Task 3: Add the independent Pine-parity ZLEMA25 overlay

**Files:**
- Modify: `tests/test_union_chart_dashboard.py`
- Modify: `union_chart_dashboard.py`

**Interfaces:**
- Consumes: each record's existing `bars` array and close at `bar[4]`.
- Produces: `computeZlema25(closes) -> Array<number | null>`, `zlema25LineData(record) -> Array<{time, value, color}>`, and `rebuildZlema25(entry) -> void`.
- Adds `uiState.zlema25Visible: boolean`, `entry.zlema25Series`, and checkbox ID `zlema25Visible`.

- [ ] **Step 1: Add failing state, control, and rendering contracts**

Add:

```python
def test_build_html_starts_with_zlema25_hidden_and_switch_unchecked():
    html = build_html([], "2026-08-27")
    assert "zlema25Visible: false" in html
    label_start = html.index("<span>ZLEMA25</span>")
    input_start = html.index("<input", label_start)
    zlema_input = html[input_start : html.index(">", input_start) + 1]
    assert 'id="zlema25Visible"' in zlema_input
    assert "checked" not in zlema_input


def test_build_html_configures_zlema25_as_hidden_label_step_line():
    html = build_html([], "2026-08-27")
    rebuild = html.split("function rebuildZlema25(entry) {", 1)[1].split(
        "function applyVolumeState(entry)", 1
    )[0]
    assert "LightweightCharts.LineType.WithSteps" in rebuild
    assert "lineWidth: 1" in rebuild
    assert "lastValueVisible: false" in rebuild
    assert "priceLineVisible: false" in rebuild
    assert 'document.getElementById(\'zlema25Visible\')' in html
```

- [ ] **Step 2: Add a Node-executed ZLEMA golden-value test**

Add `shutil` and `subprocess` imports, then add:

```python
def _run_generated_js_function(html, start_marker, end_marker, expression):
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for generated JavaScript parity tests")
    function_source = start_marker + html.split(start_marker, 1)[1].split(
        end_marker, 1
    )[0]
    completed = subprocess.run(
        [node, "-e", function_source + "\nconsole.log(JSON.stringify(" + expression + "));"],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def test_generated_zlema25_matches_pine_recursive_ema_seed():
    html = build_html([], "2026-08-27")
    closes = list(range(1, 41))
    values = _run_generated_js_function(
        html,
        "function computeZlema25(closes) {",
        "function zlema25LineData(record)",
        f"computeZlema25({json.dumps(closes)})",
    )
    assert values[:12] == [None] * 12
    assert values[12] == pytest.approx(25.0)
    assert values[13] == pytest.approx(25.076923076923077)
    assert values[-1] == pytest.approx(41.38230658545096)
```

The last expected value is generated from the same independent recurrence: adjusted closes are `2 * close[i] - close[i - 12]`, the first adjusted value seeds the EMA, and subsequent values use alpha `1 / 13`.

- [ ] **Step 3: Run the ZLEMA tests and verify intended failure**

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "zlema25" -v -p no:cacheprovider --basetemp=.pytest_tmp/zlema25-red
```

Expected: failures because the ZLEMA state, switch, functions, and series do not exist; no Python syntax or Node invocation error.

- [ ] **Step 4: Implement the Pine-parity calculation and colored data**

Add after `emaLineData`:

```javascript
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
    const rising = index > 0
      && values[index - 1] !== null
      && values[index] > values[index - 1];
    return {
      time: bar[0],
      value: values[index],
      color: rising ? "#ffffff" : "#ff0000",
    };
  }).filter(Boolean);
}
```

- [ ] **Step 5: Implement independent series lifecycle and state**

Extend initial state:

```javascript
const uiState = {
  emaVisible: false,
  zlema25Visible: false,
  volumeVisible: false,
  interactive: false,
};
```

Add before `applyVolumeState`:

```javascript
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
```

Add `zlema25Series: null` to each chart entry and call `rebuildZlema25(entry)` once during chart creation after assigning `chartsBySymbol[symbol]`.

- [ ] **Step 6: Add the independent switch and handler**

Add control markup after the EMA switch:

```html
<label class="switch-row"><span>ZLEMA25</span><input type="checkbox" id="zlema25Visible"><span class="switch"></span></label>
```

Add the handler after the EMA handler:

```javascript
document.getElementById('zlema25Visible').addEventListener('change', function(e) {
  uiState.zlema25Visible = e.target.checked;
  Object.keys(chartsBySymbol).forEach(function(symbol) {
    const entry = chartsBySymbol[symbol];
    rebuildZlema25(entry);
    scheduleCoilRedraw(entry);
  });
});
```

Do not call `rebuildZlema25` from `applyControls` or the EMA handler; this preserves control independence.

- [ ] **Step 7: Run ZLEMA and focused dashboard tests**

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "zlema25" -v -p no:cacheprovider --basetemp=.pytest_tmp/zlema25-green
python -m pytest tests/test_union_chart_dashboard.py -v -p no:cacheprovider --basetemp=.pytest_tmp/union-layout-zlema-focused
```

Expected: every selected and focused union-dashboard test passes, including the Node-executed golden calculation and Chrome coil regressions.

- [ ] **Step 8: Commit the independent overlay**

Run:

```powershell
git add -- union_chart_dashboard.py tests/test_union_chart_dashboard.py
git diff --cached --check
git commit --no-verify -m "feat(charts): add optional ZLEMA25"
```

### Task 4: Verify, conditionally regenerate, and document the handoff

**Files:**
- Modify: `dashboard/union_charts.html` only if today's union report is fresh.
- Modify: `HANDOFF.md`.

**Interfaces:**
- Consumes: `union_chart_dashboard.main()` and its existing freshness gate.
- Produces: a verified tracked dashboard when fresh, or explicit evidence that a stale input preserved the previous good artifact.

- [ ] **Step 1: Run the full suite in a worktree-local temporary directory**

Run:

```powershell
python -m pytest -v --basetemp=.pytest_tmp/union-card-layout-full
```

Expected: all tests pass. Record the exact passed count and any pre-existing warnings for `HANDOFF.md`.

- [ ] **Step 2: Check input freshness before generation**

Run:

```powershell
Get-Content ema55_cross_scans/ema55_cross_scans.md -TotalCount 12
```

Expected fresh case: the title line contains `2026-08-27`. If it carries another date, treat it as stale and do not manually bypass `load_todays_union`.

- [ ] **Step 3: Exercise the real generation safeguard**

Capture the artifact hash, run the generator, and capture it again:

```powershell
$beforeHash = (Get-FileHash dashboard/union_charts.html -Algorithm SHA256).Hash
python union_chart_dashboard.py
$afterHash = (Get-FileHash dashboard/union_charts.html -Algorithm SHA256).Hash
Write-Output "before=$beforeHash"
Write-Output "after=$afterHash"
```

Expected fresh case: output reports a nonzero charted count and the hash changes. Expected stale case: output begins with `[union_chart_dashboard] SKIP:`, the two hashes match, and the previous dashboard remains intact.

- [ ] **Step 4: Verify the generated artifact when the input is fresh**

Run this only when Step 3 generated the page:

```powershell
rg -n "emaVisible: false|zlema25Visible: false|id=\"emaVisible\"|id=\"zlema25Visible\"|min\(100%,440px\)|clamp\(330px,38vw,400px\)|class=\"symbol-link\"|computeZlema25|LineType.WithSteps|SEBI registered" dashboard/union_charts.html
git diff --check -- dashboard/union_charts.html
```

Expected: every contract appears, the EMA input has no `checked` attribute, the disclaimer appears, and there are no whitespace errors.

- [ ] **Step 5: Perform the viewport and interaction checkpoint**

Serve the repository locally:

```powershell
python -m http.server 8000
```

Open `http://localhost:8000/dashboard/union_charts.html` and check:

- 390x844 phone: one full-width 330px chart, vertical page scroll over the chart, percentage left, tier center, symbol right, and no horizontal page scroll.
- 768x1024 tablet portrait: automatic one-column layout where two 440px cards cannot fit.
- 1024x768 tablet landscape: automatic two-column layout.
- 1440x900 desktop: adaptive multi-column cards with chart height within 330-400px.
- Every viewport: six months plus 15 blank future slots remain visible in Fixed mode; EMA, ZLEMA25, and Volume start off; the symbol link is easy to tap and opens TradingView; EMA20/50/200 and ZLEMA25 toggle independently; ZLEMA25 is a white-rising/red-flat-or-falling step line; toggling either overlay preserves coil alignment; Interactive pan/pinch and return to Fixed work; volume never covers price candles; industry/day-change sorting and filtering still work.

Stop the server with `Ctrl+C` after the checks.

- [ ] **Step 6: Update the handoff with exact evidence**

Add a dated entry near the top of `HANDOFF.md` with four exact bullets:

- State that EMA and ZLEMA25 start hidden, cards use a 440px adaptive minimum and 330-400px height, and the header order is percentage/tier/symbol with a 44px symbol target.
- Record the independent ZLEMA25 switch, Pine-parity lag/seed, step-line direction colors, and hidden price labels.
- State that fixed-range, scroll, tablet reflow, sorting, volume separation, signal candles, and coil behavior were preserved.
- Record the exact focused and full pytest pass counts, warning count, `git diff --check` result, and each completed manual viewport check.
- Record either the fresh report date plus generated chart count, or the stale report date plus matching extracted `CHART_DATA` SHA256 values proving that a renderer-only artifact patch preserved all market data.

- [ ] **Step 7: Commit only the verified handoff and optional artifact**

Fresh-input case:

```powershell
git add -- HANDOFF.md dashboard/union_charts.html
git diff --cached --check
git commit --no-verify -m "docs(charts): refresh responsive dashboard"
```

Stale-input case:

```powershell
git add -- HANDOFF.md
git diff --cached --check
git commit --no-verify -m "docs(charts): record layout verification"
```

Before committing, `git diff --cached --name-only` must not list `.ohlc_data/data_manifest.csv`, `.superpowers/`, databases, caches, logs, or raw downloaded data.

- [ ] **Step 8: Final repository and publication check**

Run:

```powershell
git status --short
git log -2 --oneline
git show --check --stat HEAD
```

Expected: only the user's pre-existing `.ohlc_data/data_manifest.csv` and `.superpowers/` state remains outside the feature commits. If publication is part of the execution request, push the feature commits with `git push` only after these checks; otherwise report the commits as local and give the hosted URL without claiming it has updated.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
