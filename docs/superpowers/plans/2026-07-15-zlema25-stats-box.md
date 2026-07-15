# ZLEMA25 + EMA20 Stats Box Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a middle-right stats table to `pine_scripts/ZLEMA25_Trend_Labels.pine` showing ZLEMA25 and EMA20 current-uptrend age + % change, position-nudgeable via empty padding rows.

**Architecture:** Single Pine v6 overlay file. New EMA20 trend-tracking block mirrors the existing ZLEMA25 `var` start-price/bar pattern. A `table.new(position.middle_right, 1, padAbove + 2 + padBelow)` is deleted/recreated on `barstate.islast`. No existing drawings change.

**Tech Stack:** Pine Script v6 (TradingView). No local compiler — final verification is pasting into TradingView's Pine editor.

## Global Constraints

- `//@version=6` stays (pine-script-conventions).
- No float equality — rising checks use `>` / `<` only.
- Naming: inputs camelCase, boolean signals verb phrases.
- Spec: `docs/superpowers/specs/2026-07-15-zlema25-stats-box-design.md`.
- Repo commits use `git commit --no-verify`; push immediately after every commit.

---

### Task 1: Commit pre-existing user tweaks

**Files:**
- Modify: none (commit only) — `pine_scripts/ZLEMA25_Trend_Labels.pine` working tree already has: plot line commented out, turn-candle color yellow→fuchsia.

- [ ] **Step 1: Commit and push**

```bash
git add pine_scripts/ZLEMA25_Trend_Labels.pine
git commit --no-verify -m "chore(pine): ZLEMA25 labels - hide ZLEMA plot, fuchsia turn candle"
git push
```

---

### Task 2: EMA20 trend stats + stats box

**Files:**
- Modify: `pine_scripts/ZLEMA25_Trend_Labels.pine` (append after the live-label block at end of file; update header comment)

**Interfaces:**
- Consumes: existing `daysFromStart` (int, na when ZLEMA25 not rising), `pctChangeFromStart` (float, same na rule).
- Produces: nothing consumed elsewhere (terminal display feature).

- [ ] **Step 1: Update header comment**

In the header block (lines 2–20), after the "Current uptrend: live white label..." bullet, add:

```pine
//     - Stats box (middle-right table): ZLEMA25 + EMA20 current-uptrend age and
//       % since trend start ("ZL25 12d | +8.4%"); dash when line not rising.
//       Vertical nudge via "Empty rows above/below" inputs. EMA20 stats mirror
//       the ZLEMA25 convention (base = close of bar before turn-up bar).
```

- [ ] **Step 2: Append stats-box code at end of file**

```pine
// ── Stats box: ZLEMA25 + EMA20 current-uptrend age / % since trend start ────
grpBox = "Stats Box"
showStatsBox = input.bool(true, "Show stats box", group=grpBox)
padAbove = input.int(0, "Empty rows above (push box down)", minval=0, group=grpBox)
padBelow = input.int(0, "Empty rows below (push box up)", minval=0, group=grpBox)
ema20Len = input.int(20, "EMA length (2nd row)", minval=1, group=grpBox)

// EMA20 trend stats — mirrors ZLEMA25 convention: start = turn-up bar,
// % base = close of the bar BEFORE the turn-up bar.
ema20 = ta.ema(close, ema20Len)
emaUpTrend = ema20 > ema20[1]
emaDownTrend = ema20 < ema20[1]
emaUpStart = emaUpTrend and not emaUpTrend[1]

var float emaStartPrice = na
var int emaStartBar = na
if emaUpStart
    emaStartPrice := close[1]
    emaStartBar := bar_index
if emaDownTrend
    emaStartPrice := na
    emaStartBar := na

emaDaysFromStart = emaUpTrend and not na(emaStartBar) ? (bar_index - emaStartBar) : na
emaPctFromStart = emaUpTrend and not na(emaStartPrice) ? ((close - emaStartPrice) / emaStartPrice) * 100 : na

var table statsBox = na
if barstate.islast
    table.delete(statsBox)
    if showStatsBox
        statsBox := table.new(position.middle_right, 1, padAbove + 2 + padBelow)
        cellBg = color.new(color.black, 30)
        padBg = color.new(color.black, 100)
        if padAbove > 0
            for i = 0 to padAbove - 1
                table.cell(statsBox, 0, i, " ", text_size=size.small, bgcolor=padBg)
        zlText = not na(daysFromStart) and not na(pctChangeFromStart) ? "ZL25  " + str.tostring(daysFromStart) + "d | " + str.tostring(pctChangeFromStart, "#.##") + "%" : "ZL25  —"
        emaText = not na(emaDaysFromStart) and not na(emaPctFromStart) ? "EMA20 " + str.tostring(emaDaysFromStart) + "d | " + str.tostring(emaPctFromStart, "#.##") + "%" : "EMA20 —"
        table.cell(statsBox, 0, padAbove, zlText, text_color=color.white, text_size=size.small, text_halign=text.align_left, bgcolor=cellBg)
        table.cell(statsBox, 0, padAbove + 1, emaText, text_color=color.white, text_size=size.small, text_halign=text.align_left, bgcolor=cellBg)
        if padBelow > 0
            for i = 0 to padBelow - 1
                table.cell(statsBox, 0, padAbove + 2 + i, " ", text_size=size.small, bgcolor=padBg)
```

Notes for implementer:
- Pad cells use `" "` (single space), not `""` — empty-text cells collapse to zero height and the nudge does nothing.
- `table.delete` before recreate so pad-input changes rebuild the table.
- Keep the `zlText`/`emaText` ternaries on single lines — Pine line-wrap indentation rules inside `if` blocks are error-prone.

- [ ] **Step 3: Static self-check (no local compiler)**

Read the modified file end-to-end and confirm:
- `//@version=6` first line unchanged.
- No `==` on floats anywhere in new code.
- All new identifiers unique (no clash with existing `upTrend`, `daysFromStart`, etc.).
- Every `table.cell` row index < declared row count for all pad values.

- [ ] **Step 4: Commit and push**

```bash
git add pine_scripts/ZLEMA25_Trend_Labels.pine
git commit --no-verify -m "feat(pine): stats box with ZLEMA25+EMA20 uptrend age/% in ZLEMA25 Trend Labels"
git push
```

- [ ] **Step 5: User verification on TradingView**

User pastes file into TradingView Pine editor, daily chart:
- Compiles clean.
- ZL25 row numbers match the live white label.
- EMA20 row age = count of consecutive rising EMA20 bars.
- Falling line shows `—`.
- Pad inputs move the box up/down.

If compile errors: fix, re-run Steps 3–4.
