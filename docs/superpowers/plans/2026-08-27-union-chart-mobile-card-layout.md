> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Union Chart Mobile Card Layout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make union chart cards larger and easier to use across phones, tablets, and desktops, start every page load with EMAs hidden, and place the clickable symbol at the right edge of each card header.

**Architecture:** Keep `union_chart_dashboard.py` as the sole HTML generator and make only HTML-template, CSS, and initial UI-state changes. Protect the behavior with generated-HTML contract tests in `tests/test_union_chart_dashboard.py`; preserve lazy chart creation, explicit six-month logical ranges, resize-driven coil redraws, sorting, and stale-input safeguards.

**Tech Stack:** Python 3.13, pytest, vanilla JavaScript/CSS, TradingView Lightweight Charts 4.1.3, PowerShell.

## Global Constraints

- Modify the existing `dashboard/union_charts.html` artifact; do not create a parallel dashboard.
- Every page load starts with EMAs off; do not persist EMA visibility in local storage, session storage, cookies, or URL parameters.
- Keep volume off by default and independent from EMA visibility.
- Preserve the explicit six-calendar-month fixed range plus 15 blank future logical slots; never fabricate future OHLCV or call `fitContent()`.
- Preserve vertical page scrolling over charts and automatic one/two-column tablet reflow.
- Use a 440px preferred grid minimum, `clamp(330px, 38vw, 400px)` chart height, and a one-column 330px phone layout at 600px or below.
- Render percentage left, tier centered, and the TradingView symbol link right; give the symbol a minimum 44px-high tap target.
- Preserve existing EMA colors, hidden EMA price labels, volume/price scale separation, coil redraw ordering, signal candle colors, sorting, filtering, and interaction modes.
- Generate `dashboard/union_charts.html` only from a union report dated today; stale input must leave the previous dashboard byte-for-byte unchanged.
- Every new or generated Markdown/HTML file must contain `SEBI registered`; continue using `SEBI_HTML_BANNER` and `SEBI_HTML_FOOTER` in the generator.
- Preserve the user's existing `.ohlc_data/data_manifest.csv` modification and untracked `.superpowers/` directory.
- Commit with `git commit --no-verify`.

---

## File Structure

- Modify `tests/test_union_chart_dashboard.py`: generated-HTML contracts for default EMA state, header order/accessibility, and responsive CSS.
- Modify `union_chart_dashboard.py`: initial UI state, EMA checkbox markup, card-header markup/classes, and adaptive CSS.
- Modify `dashboard/union_charts.html` only when `ema55_cross_scans/ema55_cross_scans.md` is dated today and normal generation succeeds.
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

Expected: all union dashboard tests pass. The previous handoff recorded 44 tests; the exact new total may be higher after adding these contracts, but there must be zero failures.

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

### Task 3: Verify, conditionally regenerate, and document the handoff

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
rg -n "emaVisible: false|id=\"emaVisible\"|min\(100%,440px\)|clamp\(330px,38vw,400px\)|class=\"symbol-link\"|SEBI registered" dashboard/union_charts.html
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
- Every viewport: six months plus 15 blank future slots remain visible in Fixed mode; EMA and Volume start off; the symbol link is easy to tap and opens TradingView; enabling/disabling EMA preserves colors and coil alignment; Interactive pan/pinch and return to Fixed work; volume never covers price candles; industry/day-change sorting and filtering still work.

Stop the server with `Ctrl+C` after the checks.

- [ ] **Step 6: Update the handoff with exact evidence**

Add a dated entry near the top of `HANDOFF.md` with four exact bullets:

- State that EMA starts hidden, cards use a 440px adaptive minimum and 330-400px height, and the header order is percentage/tier/symbol with a 44px symbol target.
- State that fixed-range, scroll, tablet reflow, sorting, volume separation, signal candles, and coil behavior were preserved.
- Record the exact focused and full pytest pass counts, warning count, `git diff --check` result, and each completed manual viewport check.
- Record either the fresh report date plus generated chart count, or the stale report date plus the matching before/after SHA256 values that prove preservation.

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
