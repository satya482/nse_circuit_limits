> **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# ATR Bible Pine Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the two-script ATR Bible suite from `research/atr-bible-pinescript-spec.md` — `pine_scripts/ATR_Bible_Overlay.pine` (candle coloring, stop/target lines, dashboard, signals, 7 alerts) and `pine_scripts/ATR_Bible_Panel.pine` (ATR(10)/ATR(50) lines + fill, CR line with zones, expansion histogram, verdict label).

**Architecture:** Two self-contained `.pine` v6 files (this repo has no shared Pine library — every file duplicates its calc block, per `Consolidation_Panel.pine` / `Consolidation_PreBreak_Alerts.pine`). Both scripts share the same ATR core + CR state machine calc block; overlay adds trade math and visuals, panel adds volatility-structure visuals. No Python counterpart exists yet — parity table in each header points at the spec.

**Tech Stack:** Pine Script v6, TradingView. No local compiler — verification is paste-into-TradingView per task.

## Global Constraints

- `@version=6` always — **deliberate deviation from spec Section 9 (`//@version=5`)**; user rule `pine-script-conventions.md` overrides the spec.
- No float equality — inequalities and `ta.crossover`/`ta.crossunder` only (spec already complies; keep it that way).
- Inputs camelCase (`atrFast`, not spec's `atr_fast`), boolean signals verb phrases, per `pine-script-conventions.md`.
- Alert message format: pipe-delimited `SIGNAL_TYPE|{{ticker}}|description|TF:{{interval}}` — **deviation from spec Section 6's prose messages**; dynamic values injected via `{{plot("Name")}}` placeholders backed by hidden plots (`display=display.none`), because `alertcondition()` messages must be const strings.
- Header comment block in each file: what it does, companion script, alert format (per convention).
- Pine has no `15_00_00_000` underscore literals — write `150000000` (₹15 Cr).
- NSE-flag *detection* stays pure (no `and showNseFlags` inside the boolean, unlike spec Section 3) — the toggle gates only display, never the alert logic.
- Dashboard table and lines update inside `if barstate.islast` — **deviation from spec Section 9's "update every bar" note** (tables are single persistent objects; the spec's claim that `islast` gating makes them disappear on historical bars is wrong, and `islast` is the standard cheap pattern).
- No look-ahead: no negative offsets anywhere.
- Commits with `git commit --no-verify` (repo CLAUDE.md standing exception). Do not touch the already-modified `.ohlc_data/data_manifest.csv`.

---

### Task 1: Overlay — calc block + candle/background/corridor/signal visuals

**Files:**
- Create: `pine_scripts/ATR_Bible_Overlay.pine`

**Interfaces:**
- Produces (consumed by Tasks 2–3 in the same file): `atr10`, `atr50`, `cr` (float, na until `atr50 > 0`), `crState` (string incl. `"WARMUP"`), `rajanVerdict` (string), `ep`, `stopMult`, `stopLvl`, `stopAmt`, `t1`, `t2`, `t3`, `rT1`, `rT2`, `rT3`, `shares` (int), `posValue`, `squeeze3Star`, `squeeze1Star`, `atrExpandDown`, `dist3Day`, `circuitSuspect`, `specSuspect`, `epSeason`, all inputs listed below.

- [ ] **Step 1: Write the file — header, inputs, calcs, visuals**

```pine
//@version=6
indicator("ATR Bible · Overlay [Rajan Mehta]",
     shorttitle       = "ATRB-OV",
     overlay          = true,
     max_lines_count  = 10,
     max_labels_count = 10)
// ATR Bible suite, Script A (research/atr-bible-pinescript-spec.md).
// Colors candles by ATR(10)/ATR(50) Compression Ratio state, draws stop /
// entry / T1-T3 target lines with fixed-INR position sizing, dashboard table,
// squeeze / exit / distribution signals, NSE flags (circuit / low-notional /
// EP season). entryPx=0 -> live scan mode (lines follow close); entryPx>0 ->
// trade mode (lines locked to entry).
// Companion: pine_scripts/ATR_Bible_Panel.pine (run below chart; set Group 1
// + Group 3 inputs identically in both).
// Alert format: SIGNAL_TYPE|{{ticker}}|description|TF:{{interval}} — dynamic
// values via {{plot("CR")}} etc. hidden plots. 7 alertconditions (Task 3).
// DELIBERATE DEVIATIONS from the spec: v6 not v5 (repo rule); camelCase
// inputs; pipe-delimited alerts; NSE-flag booleans not gated on the display
// toggle (toggle gates display only, so alerts stay pure); table/lines
// updated on barstate.islast only.

// ─────────────── GROUP 1 · ATR CORE (match Panel) ───────────────
atrFast = input.int(10, "ATR Fast Period", minval=1, group="ATR Core")
atrSlow = input.int(50, "ATR Slow Period", minval=1, group="ATR Core")

// ─────────────── GROUP 2 · POSITION SETUP ───────────────
riskInr   = input.float(15000.0, "Risk Per Trade (₹)", minval=0.0, group="Position Setup")
entryPx   = input.float(0.0, "Entry Price (0 = current close)", minval=0.0, group="Position Setup")
setupType = input.string("1PB", "Setup Type", options=["VCP", "1PB", "GRIND", "3WT", "EP"], group="Position Setup")

// ─────────────── GROUP 3 · CR THRESHOLDS (match Panel) ───────────────
crExtreme  = input.float(0.50, "Extreme Squeeze Level", step=0.05, group="CR Thresholds")
crBuild    = input.float(0.70, "Squeeze Building Level", step=0.05, group="CR Thresholds")
crExpand   = input.float(1.00, "Expansion Start Level", step=0.05, group="CR Thresholds")
crExtended = input.float(1.50, "Expanded Level", step=0.05, group="CR Thresholds")
crDanger   = input.float(2.00, "Overextended / Danger Level", step=0.05, group="CR Thresholds")

// ─────────────── GROUP 4 · DISPLAY ───────────────
showDashboard     = input.bool(true,  "Show Dashboard Table", group="Display")
showStops         = input.bool(true,  "Show Stop Line", group="Display")
showTargets       = input.bool(true,  "Show T1 / T2 / T3 Lines", group="Display")
showAtrCorridor   = input.bool(false, "Show ATR Noise Corridor", group="Display")
colorCandles      = input.bool(true,  "Color Candles by CR State", group="Display")
showSqueezeSignal = input.bool(true,  "Mark Squeeze Bars", group="Display")
showExitWarn      = input.bool(true,  "Show Exit / Distribution Warnings", group="Display")
showNseFlags      = input.bool(true,  "Show NSE Flags (Circuit, Spec, EP Window)", group="Display")
dashPos           = input.string("top_right", "Dashboard Position", options=["top_right", "top_left", "bottom_right"], group="Display")
lineExtendBars    = input.int(50, "Extend Lines (bars to the right)", minval=1, group="Display")

// ─────────────── ATR CORE + CR STATE ───────────────
atr10 = ta.atr(atrFast)
atr50 = ta.atr(atrSlow)
cr = atr50 > 0 ? atr10 / atr50 : na

crState = na(cr) ? "WARMUP" :
     cr < crExtreme  ? "EXTREME SQUEEZE" :
     cr < crBuild    ? "SQUEEZE BUILDING" :
     cr < crExpand   ? "NORMAL" :
     cr < crExtended ? "EXPANDING" :
     cr < crDanger   ? "EXPANDED" :
     "OVEREXTENDED"

rajanVerdict = na(cr) ? "WARMUP. WAIT FOR BARS." :
     cr < crExtreme  ? "COILED. ENTER AT TRIGGER." :
     cr < crBuild    ? "BUILDING. ADD TO WATCHLIST." :
     cr < crExpand   ? "NORMAL. WAIT." :
     cr < crExtended ? "BREAKING OUT. CONFIRM VOLUME." :
     cr < crDanger   ? "LET IT RUN. TRAIL STOP." :
     "DANGER ZONE. REDUCE OR EXIT."

// ─────────────── STOP / TARGETS / SIZING ───────────────
ep = entryPx > 0 ? entryPx : close
stopMult = setupType == "VCP" ? 1.0 :
     setupType == "3WT"   ? 1.0 :
     setupType == "1PB"   ? 1.5 :
     setupType == "GRIND" ? 2.0 :
     2.5  // EP
stopLvl = ep - stopMult * atr10
stopAmt = ep - stopLvl
t1 = ep + 3 * atr10
t2 = ep + 5 * atr10
t3 = ep + 8 * atr10
rT1 = stopAmt > 0 ? (t1 - ep) / stopAmt : na
rT2 = stopAmt > 0 ? (t2 - ep) / stopAmt : na
rT3 = stopAmt > 0 ? (t3 - ep) / stopAmt : na
shares = stopAmt > 0 ? math.floor(riskInr / stopAmt) : 0
posValue = shares * ep

// ─────────────── SQUEEZE / EXIT / DISTRIBUTION ───────────────
volSma20 = ta.sma(volume, 20)
star1 = cr < crExtreme
star2 = volume < volSma20 * 0.50
star3 = high < high[1] and low > low[1]
squeeze3Star = star1 and star2 and star3
squeeze1Star = star1 and not squeeze3Star

atrExpandDown = (high - low) > atr10[1] * 1.5 and close < open
dist3Day = atrExpandDown and atrExpandDown[1] and atrExpandDown[2] and close < close[1] and close[1] < close[2]

// ─────────────── NSE FLAGS (pure booleans; toggles gate display only) ───────────────
circuitSuspect = (high - low) < atr50 * 0.20
specSuspect = volume * close < 150000000  // ₹15 Cr daily notional (approx)
epSeason = month == 1 or month == 4 or month == 7 or month == 10

// ─────────────── CANDLE COLORING (spec 4.1) ───────────────
barCol = na(cr) ? na :
     squeeze3Star    ? color.new(#00FF88, 0)  :
     star1           ? color.new(#3FB950, 15) :
     cr < crBuild    ? color.new(#58A6FF, 25) :
     cr > crDanger   ? color.new(#F85149, 20) :
     cr > crExtended ? color.new(#E8A020, 30) :
     cr > crExpand   ? color.new(#D29922, 25) :
     na
barcolor(colorCandles ? barCol : na)

// ─────────────── BACKGROUND (spec 4.2) ───────────────
bgcolor(showSqueezeSignal and squeeze3Star ? color.new(#3FB950, 93) : na)
bgcolor(showExitWarn and dist3Day ? color.new(#F85149, 82) : na)
bgcolor(showExitWarn and atrExpandDown and not dist3Day ? color.new(#F85149, 88) : na)
bgcolor(showNseFlags and epSeason ? color.new(#D29922, 96) : na)

// ─────────────── ATR NOISE CORRIDOR (spec 4.3) ───────────────
plot(showAtrCorridor ? close + atr10 : na, "ATR Upper", color=color.new(#58A6FF, 70), linewidth=1)
plot(showAtrCorridor ? close - atr10 : na, "ATR Lower", color=color.new(#58A6FF, 70), linewidth=1)

// ─────────────── SIGNALS (spec 4.5) ───────────────
plotshape(showSqueezeSignal and squeeze3Star, "3-Star Squeeze", style=shape.triangleup, location=location.belowbar, color=#00FF88, text="★★★", size=size.normal)
plotshape(showSqueezeSignal and squeeze1Star, "1-Star Squeeze", style=shape.triangleup, location=location.belowbar, color=#3FB950, text="★", size=size.small)
plotshape(showExitWarn and atrExpandDown and not dist3Day, "Exit Warning", style=shape.xcross, location=location.abovebar, color=#F85149, text="⚠", size=size.small)
plotshape(showExitWarn and dist3Day, "Distribution", style=shape.arrowdown, location=location.abovebar, color=#C03030, text="DIST", size=size.normal)
plotshape(showNseFlags and circuitSuspect, "Circuit Suspect", style=shape.circle, location=location.abovebar, color=#FF8800, text="⚡", size=size.small)
plotshape(showNseFlags and specSuspect, "SPEC Suspect", style=shape.square, location=location.abovebar, color=#FF8800, text="₹", size=size.tiny)
plotshape(showNseFlags and epSeason and not epSeason[1], "EP Season Open", style=shape.flag, location=location.top, color=#D29922, text="EP WIN", size=size.small)
```

- [ ] **Step 2: Verify in TradingView**

Paste into TradingView Pine editor on any NSE daily chart (e.g. `NSE:RELIANCE`). Expected: compiles clean; candles recolor when `colorCandles` on; corridor appears only when toggled; EP-season gold background visible on Jan/Apr/Jul/Oct bars; no runtime errors on first 50 bars (CR na → default candles).

- [ ] **Step 3: Commit**

```powershell
git add pine_scripts/ATR_Bible_Overlay.pine docs/superpowers/plans/2026-07-16-atr-bible-pine-suite.md
git commit --no-verify -m "feat(pine): ATR Bible overlay - calc block, candle coloring, signals"
git push
```

---

### Task 2: Overlay — stop/target lines + dashboard table

**Files:**
- Modify: `pine_scripts/ATR_Bible_Overlay.pine` (append after the plotshape block)

**Interfaces:**
- Consumes: everything from Task 1.
- Produces: `fmtInr(v)` string helper (used in labels + table).

- [ ] **Step 1: Append lines, labels, and dashboard**

```pine
// ─────────────── ₹ FORMAT HELPER ───────────────
fmtInr(float v) =>
    str.format("₹{0,number,#,###.##}", v)

// ─────────────── STOP / ENTRY / TARGET LINES (spec 4.4) ───────────────
var line stopLine  = na
var line entryLine = na
var line t1Line    = na
var line t2Line    = na
var line t3Line    = na
var label stopLbl  = na
var label entryLbl = na
var label t1Lbl    = na
var label t2Lbl    = na
var label t3Lbl    = na

if barstate.islast
    line.delete(stopLine)
    line.delete(entryLine)
    line.delete(t1Line)
    line.delete(t2Line)
    line.delete(t3Line)
    label.delete(stopLbl)
    label.delete(entryLbl)
    label.delete(t1Lbl)
    label.delete(t2Lbl)
    label.delete(t3Lbl)
    x2 = bar_index + lineExtendBars
    if showStops or showTargets
        entryLine := line.new(bar_index, ep, x2, ep, color=#E6EDF3, width=1, style=line.style_dashed)
        entryLbl  := label.new(x2, ep, "ENTRY " + fmtInr(ep) + " · " + setupType, style=label.style_label_left, color=color.new(#21262D, 40), textcolor=#E6EDF3, size=size.small)
    if showStops
        stopLine := line.new(bar_index, stopLvl, x2, stopLvl, color=#F85149, width=2)
        stopLbl  := label.new(x2, stopLvl, "STOP " + fmtInr(stopLvl) + " (−" + fmtInr(stopAmt) + " / share)", style=label.style_label_left, color=color.new(#2A1010, 40), textcolor=#F85149, size=size.small)
    if showTargets
        t1Line := line.new(bar_index, t1, x2, t1, color=#2D6A3F, width=1, style=line.style_dotted)
        t1Lbl  := label.new(x2, t1, "T1 " + fmtInr(t1) + " · +3R · Sell 50%", style=label.style_label_left, color=color.new(#0D1F10, 40), textcolor=#2D6A3F, size=size.small)
        t2Line := line.new(bar_index, t2, x2, t2, color=#3FB950, width=1, style=line.style_dashed)
        t2Lbl  := label.new(x2, t2, "T2 " + fmtInr(t2) + " · +5R · Sell 25%", style=label.style_label_left, color=color.new(#0D1F10, 40), textcolor=#3FB950, size=size.small)
        t3Line := line.new(bar_index, t3, x2, t3, color=#7FE09F, width=2)
        t3Lbl  := label.new(x2, t3, "T3 " + fmtInr(t3) + " · +8R · Trail", style=label.style_label_left, color=color.new(#0D1F10, 40), textcolor=#7FE09F, size=size.small)

// ─────────────── DASHBOARD TABLE (spec 4.6) ───────────────
dashPosition = dashPos == "top_left" ? position.top_left : dashPos == "bottom_right" ? position.bottom_right : position.top_right
var table dash = table.new(dashPosition, 2, 13, bgcolor=#0D1117, border_color=#30363D, border_width=1, frame_color=#58A6FF, frame_width=1)

// Palette
COL_HDR_BG    = #1C2128
COL_HDR_TX    = #58A6FF
COL_LBL_BG    = #161B22
COL_LBL_TX    = #8B949E
COL_SQZ_BG    = #1A4228
COL_SQZ_TX    = #3FB950
COL_OVR_BG    = #3D1A1A
COL_OVR_TX    = #F85149
COL_STOP_BG   = #2A1010
COL_TGT_BG    = #0D1F10
COL_NORM_BG   = #21262D
COL_NORM_TX   = #E6EDF3
COL_FLAG_BG   = #2A1A00
COL_FLAG_TX   = #FF8800

if barstate.islast and showDashboard
    table.clear(dash, 0, 0, 1, 12)
    inSqueeze = not na(cr) and cr < crBuild
    overExt   = not na(cr) and cr > crDanger
    crBg = inSqueeze ? COL_SQZ_BG : overExt ? COL_OVR_BG : COL_NORM_BG
    crTx = inSqueeze ? COL_SQZ_TX : overExt ? COL_OVR_TX : COL_NORM_TX
    table.cell(dash, 0, 0, "ATR BIBLE · " + setupType, bgcolor=COL_HDR_BG, text_color=COL_HDR_TX, text_size=size.small)
    table.cell(dash, 1, 0, syminfo.ticker,             bgcolor=COL_HDR_BG, text_color=COL_HDR_TX, text_size=size.small)
    table.cell(dash, 0, 1, "ATR(" + str.tostring(atrFast) + ")", bgcolor=COL_LBL_BG, text_color=COL_LBL_TX, text_size=size.small)
    table.cell(dash, 1, 1, fmtInr(atr10),              bgcolor=COL_NORM_BG, text_color=COL_NORM_TX, text_size=size.small)
    table.cell(dash, 0, 2, "ATR(" + str.tostring(atrSlow) + ")", bgcolor=COL_LBL_BG, text_color=COL_LBL_TX, text_size=size.small)
    table.cell(dash, 1, 2, fmtInr(atr50),              bgcolor=COL_NORM_BG, text_color=COL_NORM_TX, text_size=size.small)
    table.cell(dash, 0, 3, "CR",                       bgcolor=COL_LBL_BG, text_color=COL_LBL_TX, text_size=size.small)
    table.cell(dash, 1, 3, (na(cr) ? "—" : str.format("{0,number,#.##}", cr)) + " · " + crState, bgcolor=crBg, text_color=crTx, text_size=size.small)
    table.cell(dash, 0, 4, "VERDICT",                  bgcolor=COL_LBL_BG, text_color=COL_LBL_TX, text_size=size.small)
    table.cell(dash, 1, 4, rajanVerdict,               bgcolor=crBg, text_color=crTx, text_size=size.small)
    table.cell(dash, 0, 5, "STOP (−" + str.tostring(stopMult, "#.#") + "×ATR)", bgcolor=COL_LBL_BG, text_color=COL_LBL_TX, text_size=size.small)
    table.cell(dash, 1, 5, fmtInr(stopLvl) + " / Risk " + fmtInr(stopAmt) + "/sh", bgcolor=COL_STOP_BG, text_color=COL_OVR_TX, text_size=size.small)
    table.cell(dash, 0, 6, "POSITION SIZE",            bgcolor=COL_LBL_BG, text_color=COL_LBL_TX, text_size=size.small)
    table.cell(dash, 1, 6, stopAmt > 0 ? str.tostring(shares) + " shares · " + fmtInr(posValue) : "INVALID SETUP", bgcolor=COL_NORM_BG, text_color=stopAmt > 0 ? COL_NORM_TX : COL_OVR_TX, text_size=size.small)
    table.cell(dash, 0, 7, "T1 (3× ATR)",              bgcolor=COL_LBL_BG, text_color=COL_LBL_TX, text_size=size.small)
    table.cell(dash, 1, 7, fmtInr(t1) + " · " + str.tostring(rT1, "#.#") + "R · Sell 50%", bgcolor=COL_TGT_BG, text_color=#2D6A3F, text_size=size.small)
    table.cell(dash, 0, 8, "T2 (5× ATR)",              bgcolor=COL_LBL_BG, text_color=COL_LBL_TX, text_size=size.small)
    table.cell(dash, 1, 8, fmtInr(t2) + " · " + str.tostring(rT2, "#.#") + "R · Sell 25%", bgcolor=COL_TGT_BG, text_color=#3FB950, text_size=size.small)
    table.cell(dash, 0, 9, "T3 (8× ATR)",              bgcolor=COL_LBL_BG, text_color=COL_LBL_TX, text_size=size.small)
    table.cell(dash, 1, 9, fmtInr(t3) + " · " + str.tostring(rT3, "#.#") + "R · Trail", bgcolor=COL_TGT_BG, text_color=#7FE09F, text_size=size.small)
    // NSE flag rows (spec 4.6) — only when detected and toggle on
    if showNseFlags and circuitSuspect
        table.cell(dash, 0, 10, "⚡ [CIRCUIT]", bgcolor=COL_FLAG_BG, text_color=COL_FLAG_TX, text_size=size.small)
        table.cell(dash, 1, 10, "ATR unreliable today", bgcolor=COL_FLAG_BG, text_color=COL_FLAG_TX, text_size=size.small)
    if showNseFlags and specSuspect
        table.cell(dash, 0, 11, "[SPEC]", bgcolor=COL_FLAG_BG, text_color=COL_FLAG_TX, text_size=size.small)
        table.cell(dash, 1, 11, "Low notional. Half size.", bgcolor=COL_FLAG_BG, text_color=COL_FLAG_TX, text_size=size.small)
    if showNseFlags and epSeason
        table.cell(dash, 0, 12, "[EP WIN]", bgcolor=COL_FLAG_BG, text_color=#D29922, text_size=size.small)
        table.cell(dash, 1, 12, "Results season. Highest EP rate.", bgcolor=COL_FLAG_BG, text_color=#D29922, text_size=size.small)
```

Note: `table.clear` before repaint keeps flag rows from sticking when a flag turns off. If `table.new(dashPosition, ...)` rejects the non-const position at compile time, replace with three `var table` declarations behind a `switch` — but input-driven positions compile in current Pine v6; try as written first.

- [ ] **Step 2: Verify in TradingView**

Re-paste full script. Expected: compiles; dashboard top-right with 10 rows (+flag rows when applicable); set `entryPx` to a real price → entry/stop/target lines lock to it and labels show ₹ values matching hand-check (`stop = ep − stopMult×ATR10`, `t1 = ep + 3×ATR10`); `shares × stopAmt ≤ 15000`; toggle `showStops`/`showTargets`/`showDashboard` off → elements disappear.

- [ ] **Step 3: Commit**

```powershell
git add pine_scripts/ATR_Bible_Overlay.pine
git commit --no-verify -m "feat(pine): ATR Bible overlay - stop/target lines + dashboard table"
git push
```

---

### Task 3: Overlay — hidden plots + 7 alertconditions

**Files:**
- Modify: `pine_scripts/ATR_Bible_Overlay.pine` (append at end)

**Interfaces:**
- Consumes: `cr`, `atr10`, `stopLvl`, `shares`, `crExtreme`, `crBuild`, `crDanger`, `squeeze3Star`, `atrExpandDown`, `dist3Day`, `circuitSuspect` from Tasks 1–2.

- [ ] **Step 1: Append hidden plots and alerts**

```pine
// ─────────────── HIDDEN PLOTS (alert placeholders) ───────────────
plot(cr,      "CR",      display=display.none)
plot(atr10,   "ATR10",   display=display.none)
plot(stopLvl, "StopLvl", display=display.none)
plot(shares,  "Shares",  display=display.none)

// ─────────────── ALERTS (spec Sec 6; pipe format per repo convention) ───────────────
// Set alerts to "Once Per Bar Close" in the TradingView alert dialog.
alertcondition(ta.crossunder(cr, crExtreme),
     "1 · Extreme Squeeze",
     'SQUEEZE_EXTREME|{{ticker}}|CR {{plot("CR")}} dropped below extreme level, ATR10 {{plot("ATR10")}}, check chart for entry trigger|TF:{{interval}}')
alertcondition(squeeze3Star,
     "2 · 3-Star Squeeze (Max Conviction)",
     'SQUEEZE_3STAR|{{ticker}}|CR {{plot("CR")}}, volume dried, inside bar - all 3 conditions. Stop {{plot("StopLvl")}}, shares {{plot("Shares")}}|TF:{{interval}}')
alertcondition(ta.crossover(cr, crBuild) and cr[1] < crExtreme,
     "3 · Expansion Starting",
     'EXPANSION_START|{{ticker}}|CR {{plot("CR")}} rising from squeeze, ATR10 {{plot("ATR10")}}, confirm volume before entry|TF:{{interval}}')
alertcondition(atrExpandDown and not atrExpandDown[1],
     "4 · Exit Warning (ATR expand, down day)",
     'EXIT_WARN|{{ticker}}|ATR expanded 1.5x+ on down close, institutional selling possible, check position|TF:{{interval}}')
alertcondition(dist3Day and not dist3Day[1],
     "5 · Distribution Confirmed (3-day)",
     'DISTRIBUTION|{{ticker}}|3 consecutive days expanding ATR + lower closes. Exit all, do not average|TF:{{interval}}')
alertcondition(ta.crossover(cr, crDanger),
     "6 · Overextended (CR Danger)",
     'OVEREXTENDED|{{ticker}}|CR {{plot("CR")}} above danger level, trail stops to 20-day MA, reduce|TF:{{interval}}')
alertcondition(circuitSuspect and not circuitSuspect[1],
     "7 · Circuit Suspect",
     'CIRCUIT_SUSPECT|{{ticker}}|Range under 20% of ATR50, ATR unreliable today, use pivot structure for stops|TF:{{interval}}')
```

Note: alert 3's `cr[1] < crExtreme` condition is spec-verbatim (Sec 6, Alert 3) — it requires a one-bar jump from below 0.50 to above 0.70; keep as specified, tune later if it never fires.

- [ ] **Step 2: Verify in TradingView**

Re-paste. Expected: compiles; "Create Alert" dialog lists all 7 conditions under the indicator; hidden plots do not appear on the chart or in the style tab's visible plots.

- [ ] **Step 3: Commit**

```powershell
git add pine_scripts/ATR_Bible_Overlay.pine
git commit --no-verify -m "feat(pine): ATR Bible overlay - 7 alertconditions with pipe format"
git push
```

---

### Task 4: Panel script (Script B)

**Files:**
- Create: `pine_scripts/ATR_Bible_Panel.pine`

**Interfaces:**
- Consumes: nothing from other files (self-contained; duplicates Group 1 + Group 3 inputs and the ATR/CR calc block from the overlay — keep both copies in sync per Python↔Pine parity convention).

- [ ] **Step 1: Write the file**

```pine
//@version=6
indicator("ATR Bible · Panel [Rajan Mehta]",
     shorttitle       = "ATRB-PNL",
     overlay          = false,
     max_labels_count = 10)
// ATR Bible suite, Script B (research/atr-bible-pinescript-spec.md).
// Volatility-structure panel: ATR(10)/ATR(50) lines with squeeze/expansion
// fill, Compression Ratio line with state colors + threshold hlines + zone
// backgrounds, TR-vs-ATR expansion histogram, plain-English verdict label.
// Companion: pine_scripts/ATR_Bible_Overlay.pine (run on chart; set ATR Core
// + CR Threshold inputs identically in both).
// Alert message format: N/A — all 7 suite alerts live in the overlay script.
// DELIBERATE DEVIATIONS from the spec: v6 not v5 (repo rule); camelCase
// inputs; Group 2 (risk/entry/setup) inputs omitted — the panel consumes
// none of them (spec Sec 1 says duplicate all shared inputs; dead inputs cut).

// ─────────────── GROUP 1 · ATR CORE (match Overlay) ───────────────
atrFast = input.int(10, "ATR Fast Period", minval=1, group="ATR Core")
atrSlow = input.int(50, "ATR Slow Period", minval=1, group="ATR Core")

// ─────────────── GROUP 3 · CR THRESHOLDS (match Overlay) ───────────────
crExtreme  = input.float(0.50, "Extreme Squeeze Level", step=0.05, group="CR Thresholds")
crBuild    = input.float(0.70, "Squeeze Building Level", step=0.05, group="CR Thresholds")
crExpand   = input.float(1.00, "Expansion Start Level", step=0.05, group="CR Thresholds")
crExtended = input.float(1.50, "Expanded Level", step=0.05, group="CR Thresholds")
crDanger   = input.float(2.00, "Overextended / Danger Level", step=0.05, group="CR Thresholds")

// ─────────────── ATR CORE + CR (same math as Overlay) ───────────────
atr10 = ta.atr(atrFast)
atr50 = ta.atr(atrSlow)
cr = atr50 > 0 ? atr10 / atr50 : na

rajanVerdict = na(cr) ? "WARMUP. WAIT FOR BARS." :
     cr < crExtreme  ? "COILED. ENTER AT TRIGGER." :
     cr < crBuild    ? "BUILDING. ADD TO WATCHLIST." :
     cr < crExpand   ? "NORMAL. WAIT." :
     cr < crExtended ? "BREAKING OUT. CONFIRM VOLUME." :
     cr < crDanger   ? "LET IT RUN. TRAIL STOP." :
     "DANGER ZONE. REDUCE OR EXIT."

// ─────────────── 5.1 ATR LINES + FILL ───────────────
atr10Plot = plot(atr10, "ATR(10) Tactical", color=#3FB950, linewidth=2)
atr50Plot = plot(atr50, "ATR(50) Strategic", color=#58A6FF, linewidth=1)
fill(atr10Plot, atr50Plot, color=atr10 < atr50 ? color.new(#3FB950, 85) : color.new(#F85149, 85))

// ─────────────── 5.2 CR LINE + ZONES ───────────────
crColor = na(cr) ? #484F58 :
     cr < crExtreme  ? #3FB950 :
     cr < crBuild    ? #58A6FF :
     cr < crExpand   ? #484F58 :
     cr < crExtended ? #D29922 :
     cr < crDanger   ? #E8A020 :
     #F85149
plot(cr, "Compression Ratio", color=crColor, linewidth=2)

hline(0.50, "Extreme Squeeze", color=#3FB950, linestyle=hline.style_dashed)
hline(0.70, "Squeeze Building", color=#58A6FF, linestyle=hline.style_dotted)
hline(1.00, "Normal", color=#484F58, linestyle=hline.style_dotted)
hline(1.50, "Expanded", color=#D29922, linestyle=hline.style_dotted)
hline(2.00, "Overextended / Danger", color=#F85149, linestyle=hline.style_dashed)

bgcolor(not na(cr) and cr < crExtreme ? color.new(#3FB950, 90) : na)
bgcolor(not na(cr) and cr > crDanger  ? color.new(#F85149, 90) : na)

// ─────────────── 5.3 ATR EXPANSION HISTOGRAM ───────────────
atrDelta = ta.tr - atr10
histColor = atrDelta > 0 and close < open ? #F85149 :
     atrDelta > 0 ? #3FB950 :
     #484F58
plot(atrDelta, "ATR Delta", style=plot.style_histogram, color=histColor, linewidth=2)
hline(0, "Zero", color=#30363D)

// ─────────────── 5.4 VERDICT LABEL ───────────────
var label verdictLabel = na
if barstate.islast
    label.delete(verdictLabel)
    verdictLabel := label.new(
         bar_index, cr,
         rajanVerdict + "\nCR: " + (na(cr) ? "—" : str.format("{0,number,#.##}", cr)),
         style     = label.style_label_left,
         color     = not na(cr) and cr < crExtreme ? color.new(#3FB950, 70) :
                     not na(cr) and cr > crDanger  ? color.new(#F85149, 70) :
                     color.new(#21262D, 70),
         textcolor = #E6EDF3,
         size      = size.small)
```

Note: hline requires const/input prices — the 5 thresholds are plotted at their **default** values (0.50/0.70/1.00/1.50/2.00 literals), while the CR color logic uses the live inputs. If a user changes a threshold input, the hline stays at the default level. This matches `hline()`'s limitation; acceptable because the zone backgrounds and CR color follow the inputs. Documented here so nobody "fixes" it into a compile error. (Alternative if exact tracking wanted later: `plot(crExtreme, ...)` instead of hline.)

- [ ] **Step 2: Verify in TradingView**

Paste as a second indicator below the chart. Expected: compiles; green fill when ATR10 < ATR50, red when above; CR line changes color across zones; histogram red on expanding down days; verdict label at right edge tracks CR and matches the overlay dashboard's VERDICT row on the same bar.

- [ ] **Step 3: Commit**

```powershell
git add pine_scripts/ATR_Bible_Panel.pine
git commit --no-verify -m "feat(pine): ATR Bible panel - ATR lines, CR zones, histogram, verdict"
git push
```

---

## Self-Review Notes

- **Spec coverage:** Sec 1–3 → Task 1; Sec 4.1–4.5 → Task 1; Sec 4.4/4.6 → Task 2; Sec 6 → Task 3; Sec 5 → Task 4; Sec 7 principles embedded (verdict voice, zero mental math, setup-aware, live-scan vs trade mode via `entryPx`); Sec 8 exclusions honored (nothing extra built); Sec 9 edge cases: `atr50=0 → cr na` (guarded everywhere with `na(cr)`), `stopAmt<=0 → INVALID SETUP` (Task 2 row 6), warmup bars (WARMUP state).
- **Known deviations (all in Global Constraints):** v6, camelCase, pipe alerts, pure flag booleans, `barstate.islast` gating, panel drops dead Group 2 inputs, hlines at default thresholds.
- **Type consistency:** `fmtInr` defined Task 2, used Task 2 only (Task 4 inlines `str.format` — panel has no ₹ prices, only CR). Variable names identical across both files' shared calc blocks.

---

*Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
