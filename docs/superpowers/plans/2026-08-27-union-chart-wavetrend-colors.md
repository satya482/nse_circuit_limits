# Union Chart WaveTrend Colors Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Repaint WaveTrend bull-cross candles lime and bear-cross candles yellow in the union chart dashboard, while preserving the current dashboard data.

**Architecture:** Keep WaveTrend calculations and signal precedence unchanged. Update the single client-side signal-color mapping, lock it with a focused HTML contract test, and rebuild only the renderer around the existing generated artifact's embedded data.

**Tech Stack:** Python 3, pytest, vanilla JavaScript, TradingView Lightweight Charts, generated HTML.

## Global Constraints

- WaveTrend bull cross is lime `#76FF03`.
- WaveTrend bear cross is yellow `#FDD835`.
- Preserve Pocket Pivot blue, ordinary candle colors, all signal calculations, and WaveTrend-over-Pocket-Pivot precedence.
- Preserve the generated artifact's embedded data hash, record count, coil-box count, and title date.
- Every modified Markdown and HTML file must contain `SEBI registered`.
- Do not stage `.ohlc_data/data_manifest.csv` or `.superpowers/`.
- Commit with `git commit --no-verify` and push `main` only after verification passes.

---

### Task 1: Change and verify the WaveTrend repaint palette

**Files:**
- Modify: `tests/test_union_chart_dashboard.py`
- Modify: `union_chart_dashboard.py`
- Modify: `dashboard/union_charts.html`
- Modify: `HANDOFF.md`

**Interfaces:**
- Consumes: `build_html(records: list[dict], as_of: str) -> str` and the existing `SIGNAL_COLORS` JavaScript object.
- Produces: generated candle points whose WaveTrend bull body, border, and wick are `#76ff03`, and whose WaveTrend bear body, border, and wick are `#fdd835`.

- [ ] **Step 1: Change the focused test to require the selected palette**

In `test_build_html_has_layer_switches_and_fixed_signal_colors`, replace the WaveTrend assertions with:

```python
assert 'wt_bull: "#76ff03"' in html
assert 'wt_bear: "#fdd835"' in html
```

- [ ] **Step 2: Run the focused test and verify the red phase**

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py::test_build_html_has_layer_switches_and_fixed_signal_colors -v -p no:cacheprovider --basetemp=.pytest_tmp/wt-colors-red
```

Expected: FAIL because generated HTML still contains `wt_bull: "#ffffff"`; the bear assertion already passes.

- [ ] **Step 3: Apply the minimal source change**

In `_JS_TEMPLATE` inside `union_chart_dashboard.py`, use this exact mapping:

```javascript
const SIGNAL_COLORS = { ppv: "#2962ff", wt_bull: "#76ff03", wt_bear: "#fdd835" };
```

Do not modify `compute_wavetrend_kinds`, `compute_signal_kinds`, or `candleData`; the existing `color`, `borderColor`, and `wickColor` assignment already repaints the complete candle.

- [ ] **Step 4: Run the focused test and complete the green phase**

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py::test_build_html_has_layer_switches_and_fixed_signal_colors -v -p no:cacheprovider --basetemp=.pytest_tmp/wt-colors-green
```

Expected: PASS.

- [ ] **Step 5: Capture the generated artifact data identity**

Run:

```powershell
node -e "const fs=require('fs'),c=require('crypto');const s=fs.readFileSync('dashboard/union_charts.html','utf8');const m=s.match(/const CHART_DATA = (.*);\r?\nconst chartsBySymbol/s);const d=JSON.parse(m[1]);console.log(JSON.stringify({sha256:c.createHash('sha256').update(m[1]).digest('hex'),records:d.length,coil_boxes:d.reduce((n,r)=>n+(r.coil_boxes||[]).length,0),title:(s.match(/<title>(.*?)<\/title>/)||[])[1]}));"
```

Expected baseline:

```text
SHA-256: 3df30913702616bc5ff1010aa43fd95d6fd4122e93dc8e4056b0e9cf2b1476bd
Records: 749
Coil boxes: 3958
Title date: 2026-08-27
```

If the current values differ because a scanner refreshed the artifact after this plan was written, treat the newly observed values as the preservation baseline and document them in `HANDOFF.md`.

- [ ] **Step 6: Rebuild only the artifact renderer**

Parse the existing artifact's `CHART_DATA` and title date, then call the updated `build_html(data, as_of)` and atomically replace `dashboard/union_charts.html` using LF newlines. Do not fetch OHLCV or rerun upstream scanners.

Run:

```powershell
python -c "import json,os,re,tempfile; from pathlib import Path; from union_chart_dashboard import build_html; p=Path('dashboard/union_charts.html'); s=p.read_text(encoding='utf-8'); data=json.loads(re.search(r'const CHART_DATA = (.*);\nconst chartsBySymbol',s,re.S).group(1)); as_of=re.search(r'<title>Union Watchlist Charts - ([0-9-]+)</title>',s).group(1); fd,tmp=tempfile.mkstemp(dir=p.parent,suffix='.tmp'); os.close(fd); Path(tmp).write_text(build_html(data,as_of),encoding='utf-8',newline='\n'); os.replace(tmp,p)"
```

- [ ] **Step 7: Update the handoff record**

Add a dated entry to `HANDOFF.md` stating:

```markdown
Updated 2026-08-27 by Codex, compact WaveTrend repaint colors:

- Union-chart WaveTrend bull-cross candles now repaint lime `#76FF03`; bear-cross candles remain yellow `#FDD835` for stronger compact-chart separation.
- WaveTrend calculations, signal precedence, and all other overlays are unchanged.
- Record focused/full test results and the preserved artifact data identity after verification.
```

- [ ] **Step 8: Run focused and full verification**

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py -v -p no:cacheprovider --basetemp=.pytest_tmp/wt-colors-focused
python -m pytest -p no:cacheprovider --basetemp=.pytest_tmp/wt-colors-full
git diff --check
```

Expected: 53 union-dashboard tests pass; all repository tests pass with only the five known pandas FutureWarnings; `git diff --check` returns no output.

- [ ] **Step 9: Verify the final artifact**

Assert that `dashboard/union_charts.html` contains `wt_bull: "#76ff03"` and `wt_bear: "#fdd835"`, contains `SEBI registered`, and retains the Step 5 data hash, record count, coil-box count, and title date.

Run the Step 5 command again and compare all four values, then run:

```powershell
rg -n 'SEBI registered|wt_bull: "#76ff03"|wt_bear: "#fdd835"' dashboard/union_charts.html
```

Expected: all three tokens are present and the data-identity values exactly match the Step 5 baseline.

- [ ] **Step 10: Commit only scoped files and push**

```powershell
git add -- HANDOFF.md dashboard/union_charts.html tests/test_union_chart_dashboard.py union_chart_dashboard.py
git commit --no-verify -m "fix(charts): distinguish WaveTrend candles"
git push origin main
```

Expected: `origin/main` advances to the new commit; `.ohlc_data/data_manifest.csv` and `.superpowers/` remain unstaged.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
