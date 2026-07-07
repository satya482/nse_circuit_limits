# Consolidation Panel (Pine Indicator 1) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `pine_scripts/Consolidation_Panel.pine` — the visual oscillator companion to `Consolidation_PreBreak_Alerts.pine`, plotting live Quality + Imminence scores (0-100), an EMA-stage background, and a CMF histogram, mirroring the Python `consolidation/quality.py` + `consolidation/imminence.py` formulas.

**Architecture:** Single self-contained `.pine` v6 script (this repo has no shared Pine library — every `.pine` file duplicates its calc block, per existing `Consolidation_PreBreak_Alerts.pine` and `CMF_ZeroCross.pine`). Task 1 builds the calc block (EMA compression, BB/KC squeeze, RS character, volume exhaustion, CMF) plus the Quality score. Task 2 adds the Imminence score plus all visuals. No delivery-%-based points are available in Pine (no NSE bhavcopy data feed in TradingView) — those points are fixed at 0, a documented deviation matching the pattern already established in `Consolidation_PreBreak_Alerts.pine`'s header.

**Tech Stack:** Pine Script v6, TradingView.

## Global Constraints

- `@version=6` always ([pine-script-conventions.md](../../../.claude/rules/pine-script-conventions.md))
- No float equality — use `math.abs(...) < syminfo.mintick` or `ta.crossover`/`ta.crossunder`, never `==` on floats
- Header comment block required: what it does, companion indicator, alert message format (N/A here — no alerts in this file, only alertcondition-free visuals)
- Python↔Pine parity: any threshold change must be mirrored in `consolidation/quality.py` / `consolidation/imminence.py` and vice versa
- RS benchmark: `NSE:NIFTYMIDSML400` (verify resolves at paste-time — same caveat as `Consolidation_PreBreak_Alerts.pine`)
- Mirror the DELIBERATE DEVIATIONS already declared in `Consolidation_PreBreak_Alerts.pine`: RS character computed DAILY-NATIVE (not weekly-resampled), no delivery-% signal available in Pine
- No look-ahead — every value at bar `t` uses `close`/`high`/`low`/`volume` through bar `t` only, no `[negative offset]`

---

### Task 1: Calc block + Quality score

**Files:**
- Create: `pine_scripts/Consolidation_Panel.pine`

**Interfaces:**
- Produces (consumed by Task 2 in the same file — single script, no cross-file interface): `spreadDelta`, `bbWidthPct`, `squeezeOn`, `ageBars`, `rangeHi` (reuse pattern from `Consolidation_PreBreak_Alerts.pine`), plus new in this task: `cmf` (float, Chaikin Money Flow), `volPercentile` (float, 0-100), `rsChar` (string, one of `"CHAR_1_DECLINING"`/`"CHAR_2_FLAT"`/`"CHAR_3_HOLDING"`/`"CHAR_4_RISING"`/`"CHAR_5_RS_BREAKOUT"`), `emaStage` (string, `"STAGE_1_CONVERGING"`/`"STAGE_2_COMPRESSED"`/`"STAGE_3_DIVERGING"`), `qualityScore` (float, 0-100)

- [ ] **Step 1: Write the calc block (EMA compression, BB/KC, vol exhaustion, RS, CMF)**

```pine
//@version=6
indicator("Consolidation Panel", shorttitle="ConsolPanel", overlay=false)
// Consolidation Tracker Phase 6 companion (spec Sec 12, Indicator 1) -- visual
// quality/imminence oscillator + CMF sub-plot + EMA-stage background. Meant to
// run on Tier 1/2 stocks from the Python scanner's daily output (spec Sec 10.5).
// This repo has no shared Pine library -- every .pine file is self-contained
// (see pine_scripts/CMF_ZeroCross.pine, Consolidation_PreBreak_Alerts.pine).
//
// DELIBERATE DEVIATIONS from consolidation/quality.py + imminence.py:
//   - RS character computed DAILY-NATIVE, not weekly-resampled (matches the
//     same deviation already declared in Consolidation_PreBreak_Alerts.pine).
//   - Delivery-% has no TradingView feed -- deliv_trend contributes 0 points
//     to Quality (Python: up to 10 pts) and signal3 (quiet accumulation) is
//     capped at weight 0.5 instead of the delivery-confirmed 1.0 (spec Sec 12
//     explicitly accepts this: "no delivery % in TV").
//   - CMF is plotted as cmf*100 on the same 0-100 scaled pane as Quality/
//     Imminence (TradingView's indicator() has one pane/one scale; this keeps
//     everything in one panel per spec's "CMF histogram sub-plot" intent).
//
// Companion: Consolidation_PreBreak_Alerts.pine (6 pre-break alertconditions)
// Python counterpart: consolidation/quality.py, consolidation/imminence.py --
// mirror any threshold change both places (pine-script-conventions.md)

benchSymbol = input.symbol("NSE:NIFTYMIDSML400", "RS Benchmark (verify resolves at paste-time)", group="RS")

// ─────────────── EMA COMPRESSION (Sec 2.1) ───────────────
ema50  = ta.ema(close, 50)
ema100 = ta.ema(close, 100)
ema200 = ta.ema(close, 200)

emaHigh = math.max(ema50, math.max(ema100, ema200))
emaLow  = math.min(ema50, math.min(ema100, ema200))
emaSpread = emaHigh - emaLow
spreadPct = ema200 != 0 ? emaSpread / ema200 : na
spreadDelta = spreadPct - spreadPct[5]

emaStage = spreadDelta < -0.001 ? "STAGE_1_CONVERGING" : spreadDelta > 0.001 ? "STAGE_3_DIVERGING" : "STAGE_2_COMPRESSED"

// ─────────────── BB / KC SQUEEZE (Sec 2.2) ───────────────
bbBasis = ta.sma(close, 20)
bbStd = ta.stdev(close, 20)
bbUpper = bbBasis + 2.0 * bbStd
bbLower = bbBasis - 2.0 * bbStd
bbWidth = bbUpper - bbLower
bbWidthPct = ta.percentrank(bbWidth, 252)

kcAtr = ta.sma(ta.tr, 20)
kcBasis = ta.sma(close, 20)
kcUpper = kcBasis + 1.5 * kcAtr
kcLower = kcBasis - 1.5 * kcAtr
squeezeOn = bbUpper < kcUpper and bbLower > kcLower

atr50 = ta.sma(ta.tr, 50)
spreadAtrRatio = atr50 != 0 ? emaSpread / atr50 : na
EMA_ATR_GATE = 1.5
EMA_PCT_GATE = 0.03
emaGateOk = spreadAtrRatio < EMA_ATR_GATE and spreadPct < EMA_PCT_GATE

BB_WIDTH_PCT_MAX = 20.0
sqOkRaw = squeezeOn and bbWidthPct <= BB_WIDTH_PCT_MAX

var int ageBars = 0
ageBars := (emaGateOk and sqOkRaw) ? ageBars + 1 : 0

// ─────────────── VOLUME EXHAUSTION (Sec 2.3) ───────────────
volMa5 = ta.sma(volume, 5)
volPercentile = ta.percentrank(volMa5, 252)
quietAccumBar = volume >= 1.5 * ta.sma(volume, 10) and math.abs(close / close[1] - 1) < 0.01

// ─────────────── RS CHARACTER (Sec 2.4, DAILY-NATIVE) ───────────────
benchClose = request.security(benchSymbol, timeframe.period, close, lookahead = barmerge.lookahead_off)
rs = close / benchClose
rsEma9 = ta.ema(rs, 9)
rsSlope = rs[20] != 0 ? rs / rs[20] - 1 : na
aboveEma = rs > rsEma9
priceFlat = math.abs(close / close[20] - 1) < 0.05
rs252High = ta.highest(rs, 252)
rs52wkHigh = rs >= rs252High * 0.999
price20dHigh = close >= ta.highest(close, 20) * 0.999
RS_FLAT_THRESHOLD = 0.01

isChar5 = rs52wkHigh and priceFlat and not price20dHigh
isChar4 = rsSlope > RS_FLAT_THRESHOLD and priceFlat
isChar3 = aboveEma and math.abs(rsSlope) <= RS_FLAT_THRESHOLD
isChar1 = not aboveEma and rsSlope < -RS_FLAT_THRESHOLD

rsChar = isChar5 ? "CHAR_5_RS_BREAKOUT" : isChar4 ? "CHAR_4_RISING" : isChar3 ? "CHAR_3_HOLDING" : isChar1 ? "CHAR_1_DECLINING" : "CHAR_2_FLAT"

// ─────────────── CMF (Sec 2.5) ───────────────
mfm = (high - low) != 0 ? ((close - low) - (high - close)) / (high - low) : 0.0
mfv = mfm * volume
cmf = ta.sma(volume, 20) != 0 ? math.sum(mfv, 20) / math.sum(volume, 20) : na

// ─────────────── QUALITY SCORE (Sec 3) ───────────────
bbPts = math.max(0.0, (20 - bbWidthPct) * 1.0)
stagePts = emaStage == "STAGE_2_COMPRESSED" ? 20.0 : emaStage == "STAGE_1_CONVERGING" ? 8.0 : 0.0
volPts = math.max(0.0, (20 - volPercentile) * 0.75)
rsPts = rsChar == "CHAR_4_RISING" or rsChar == "CHAR_5_RS_BREAKOUT" ? 20.0 : rsChar == "CHAR_3_HOLDING" ? 12.0 : rsChar == "CHAR_2_FLAT" ? 5.0 : 0.0
cmfPts = cmf > 0.10 ? 15.0 : cmf > 0.05 ? 10.0 : cmf > 0 ? 6.0 : 0.0
// deliv_pts fixed at 0 -- no TradingView delivery-% feed (see header deviations)
qualityScore = bbPts + stagePts + volPts + rsPts + cmfPts
```

- [ ] **Step 2: Manual verification (no Pine test harness in this repo)**

Paste into TradingView Pine Editor on a stock currently in a known consolidation (cross-check today's row in `results/YYYY-MM-DD-consolidation.csv` from `consolidation_scanner.py`, if one ran today). Confirm:
- Script compiles with no errors
- `qualityScore` plots would be in `[0, 100]` (add a temporary `plot(qualityScore)` and check the value in the Data Window against the CSV's `quality` column for that symbol — should be close; not exact, since RS is daily-native here vs weekly in Python and delivery contributes 0 here vs up to 10 pts in Python)

- [ ] **Step 3: Commit**

```bash
git add pine_scripts/Consolidation_Panel.pine
git commit -m "feat: add Consolidation Panel Pine v6 calc block + Quality score (Sec 12 Indicator 1, part 1)"
```

---

### Task 2: Imminence score + visuals

**Files:**
- Modify: `pine_scripts/Consolidation_Panel.pine` (append to the file created in Task 1)

**Interfaces:**
- Consumes: `spreadDelta`, `bbWidthPct`, `ageBars`, `quietAccumBar`, `rs52wkHigh`, `priceFlat`, `price20dHigh`, `isChar5`, `emaStage`, `qualityScore`, `cmf` from Task 1
- Produces: `imminenceScore` (float, 0-100), final plots/hlines/bgcolor (terminal — nothing downstream consumes these)

- [ ] **Step 1: Write the pre-break signals + Imminence score**

```pine
// ─────────────── PRE-BREAK SIGNALS (Sec 4, mirrors Consolidation_PreBreak_Alerts.pine) ───────────────
sig1_rsNewHigh = rs52wkHigh and not price20dHigh
sig2_spreadDeltaCross = spreadDelta > 0 and spreadDelta[1] <= 0

// signal3: no delivery feed in Pine -> capped at 0.5 weight instead of Python's 1.0
sig3_wt = quietAccumBar ? 0.5 : 0.0

sig4_bbWidthBreathing = bbWidthPct[2] < 15 and bbWidthPct[1] > bbWidthPct[2] and bbWidthPct > bbWidthPct[1]
sig5_higherLow = low > ta.lowest(low[1], 5)

rangeHi = ta.highest(high, math.max(ageBars, 10))
rangeLo = ta.lowest(low, math.max(ageBars, 10))
prevBodyTop = math.max(open[1], close[1])
prevRange = high[1] - low[1]
prevWick = high[1] - prevBodyTop
nearTop = high[1] >= rangeHi * 0.98
longWick = prevRange > 0 and prevWick > prevRange * 0.3
absorbed = close >= prevBodyTop
sig6_wickRejectionAbsorbed = nearTop and longWick and absorbed

// ─────────────── STAGE 3 FLAG (fresh fanout after >=10 bars held negative) ───────────────
var int negStreak = 0
negStreak := spreadDelta <= 0 ? negStreak + 1 : 0
stage3Flag = sig2_spreadDeltaCross and negStreak[1] >= 10

// ─────────────── BB BREATHING FLAG (same formula as sig4, separate 15pt component per spec table) ───────────────
bbBreathingFlag = sig4_bbWidthBreathing

// ─────────────── RANGE POSITION ───────────────
rangePos = rangeHi == rangeLo ? 0.0 : (close - rangeLo) / (rangeHi - rangeLo)

// ─────────────── IMMINENCE SCORE (Sec 4) ───────────────
prebreakCount = (sig1_rsNewHigh ? 1.0 : 0.0) + (sig2_spreadDeltaCross ? 1.0 : 0.0) + sig3_wt + (sig4_bbWidthBreathing ? 1.0 : 0.0) + (sig5_higherLow ? 1.0 : 0.0) + (sig6_wickRejectionAbsorbed ? 1.0 : 0.0)
prebreakPts = prebreakCount / 6.0 * 30
stage3Pts = stage3Flag ? 25.0 : 0.0
rsBreakoutPts = isChar5 ? 20.0 : 0.0
bbBreathingPts = bbBreathingFlag ? 15.0 : 0.0
rangePts = rangePos >= 2.0 / 3.0 ? 10.0 : 0.0
imminenceScore = prebreakPts + stage3Pts + rsBreakoutPts + bbBreathingPts + rangePts
```

- [ ] **Step 2: Write the visuals (lines, hlines, bgcolor, CMF sub-plot)**

```pine
// ─────────────── VISUALS ───────────────
plot(qualityScore, title="Quality", color=color.aqua, linewidth=2)
plot(imminenceScore, title="Imminence", color=color.yellow, linewidth=2)

hline(60, title="HOT Threshold (Imminence>=60)", color=color.orange, linestyle=hline.style_dashed)
hline(80, title="Imminent (Imminence>=80)", color=color.red, linestyle=hline.style_dashed)

bgColor = emaStage == "STAGE_1_CONVERGING" ? color.new(color.blue, 90) : emaStage == "STAGE_2_COMPRESSED" ? color.new(color.green, 90) : color.new(color.orange, 90)
bgcolor(bgColor, title="EMA Stage")

// CMF histogram, scaled *100 onto the same 0-100 pane (see header deviations) --
// distinguishable from Quality/Imminence because it's the only series that can go negative
cmfDisplay = cmf * 100
plot(cmfDisplay, title="CMF x100", style=plot.style_columns, color=cmf >= 0 ? color.new(color.teal, 40) : color.new(color.maroon, 40))
hline(0, title="Zero / CMF Baseline", color=color.gray)
```

- [ ] **Step 3: Manual verification**

Paste the full file into TradingView on 2-3 known stocks (per spec Sec 0 guardrail: "Validate every indicator against TradingView on 2-3 known stocks before universe run"):
- Confirm script compiles with no errors
- Confirm `qualityScore`/`imminenceScore` plots stay within `[0, 100]` visually
- Confirm background color changes between blue/green/orange as EMA stage changes across the chart's history
- Confirm CMF columns cross the zero hline in the expected direction vs price action (rising price + rising CMF = accumulation, per Sec 2.5)
- Pick one stock also present in today's `results/YYYY-MM-DD-consolidation.csv` and sanity-check `qualityScore`/`imminenceScore` are in the same ballpark as that row's `quality`/`imminence` columns (not exact — daily-native RS and zero delivery points are expected to cause some drift)

- [ ] **Step 4: Commit**

```bash
git add pine_scripts/Consolidation_Panel.pine
git commit -m "feat: add Consolidation Panel Imminence score + visuals (Sec 12 Indicator 2, part 2)"
```

---

## Self-Review

**Spec coverage (Sec 12, Indicator 1):**
- "plot quality score + imminence score as two lines" — Task 2 Step 2 ✓
- "hline 60 (HOT threshold), hline 80 (imminent)" — Task 2 Step 2 ✓
- "bgcolor by EMA stage: blue=converging, green=compressed, orange=diverging" — Task 2 Step 2 ✓
- "CMF histogram sub-plot, zero line" — Task 2 Step 2 (single-pane deviation documented) ✓
- Sec 0 guardrail "validate against TradingView on 2-3 known stocks" — Task 1 Step 2 + Task 2 Step 3 ✓
- Sec 2.1-2.5 formulas mirrored from `consolidation/indicators.py` and `consolidation/quality.py`/`imminence.py` — Task 1 Step 1, Task 2 Step 1 ✓

**Placeholder scan:** none — every step has complete, runnable Pine code.

**Type consistency:** `emaStage`/`rsChar` are strings used identically across both tasks (same file, same variable names — no cross-task renaming risk since this is a single script, not multiple files).

**Note on `tracker.py` scope:** No Python changes in this plan — Indicator 1 is Pine-only, consuming nothing from Python at runtime (per spec Sec 10.5's Layer 2 design: Pine re-derives everything live, Python's daily CSV only tells a human which stocks to load onto the chart).
