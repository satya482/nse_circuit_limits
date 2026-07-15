# ZLEMA25 + EMA20 Stats Box — ZLEMA25_Trend_Labels.pine

**Date:** 2026-07-15
**File:** `pine_scripts/ZLEMA25_Trend_Labels.pine`

## Goal

Add a small fixed-position stats box (Pine `table`) at the middle-right of the price
chart showing, for both ZLEMA25 and EMA20, the current uptrend's age (bars) and
% change since trend start. Vertical position adjustable via empty padding rows.

## Requirements

1. **ZLEMA25 row** — reuse existing `daysFromStart` / `pctChangeFromStart`.
2. **EMA20 row** — new. Mirror the ZLEMA25 convention exactly:
   - `ema20 = ta.ema(close, len)`, length input default 20.
   - Trend start = bar where EMA20 turns rising (`ema20 > ema20[1] and not (ema20[1] > ema20[2])`
     via the same `upTrend and not upTrend[1]` structure as ZLEMA25).
   - % base = `close[1]` at the turn-up bar (close of bar before the turn), same as
     the ZL Chg% reference in ema25_zl_scanner.py.
   - `var` start price/bar, reset to `na` on downtrend.
3. **Downtrend display** — when a line is not rising, its row shows `—` (dash).
   Row never hidden; box size stable.
4. **Existing drawings untouched** — completed-trend silver labels, live white label,
   turn-candle barcolor all stay as-is.

## Inputs (group "Stats Box")

| Input | Type | Default | Purpose |
|---|---|---|---|
| `showStatsBox` | bool | true | toggle box |
| `padAbove` | int ≥ 0 | 0 | empty rows above → push box down |
| `padBelow` | int ≥ 0 | 0 | empty rows below → push box up |
| `ema20Len` | int | 20 | EMA length for second row |

## Implementation

- `var table statsBox` created/recreated inside `if barstate.islast`:
  `table.new(position.middle_right, 1, padAbove + 2 + padBelow)`.
  Delete previous table first (`table.delete`) so pad-input changes take effect.
- Padding cells: empty text, fully transparent bg.
- Data rows: `"ZL25  12d | +8.4%"` / `"EMA20 5d | +3.1%"` or `"ZL25  —"` when not
  rising. White text, `size.small`, `color.new(color.black, 30)` cell bg.
- `na` guards identical to existing live-label block. No float equality anywhere
  (rising checks use `>` comparisons only, per pine-script-conventions).
- Header comment block updated to mention the stats box.

## Out of scope

- Downtrend age/% tracking.
- Anchor-position dropdown.
- Python-side mirror (display-only feature, no signal logic — parity rule applies to
  parameters/signals, not UI).

## Testing

Load on TradingView daily chart; verify ZL25 row matches the live white label numbers;
verify EMA20 row age by counting rising bars; verify dash on a falling line; verify
pad inputs move the box.
