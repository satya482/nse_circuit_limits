> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Union Chart Signal Overlays and Responsive Layout — Design

Date: 2026-08-26

## Purpose

Enhance `dashboard/union_charts.html` for frequent use on phones, tablets, and
desktop monitors. The dashboard will repaint historical Pocket Pivot and
WaveTrend signal candles, draw the Satya EMAs mini-coil range, preserve at
least six months of immediately visible history, keep volume from obscuring
price, and make EMA overlays clear but optional.

This extends the existing union-watchlist dashboard. It does not create a
second chart page or change the EMA55 union-watchlist membership rules.

## Selected Architecture

Signal annotations are calculated in Python while the dashboard is generated.
The browser receives raw OHLCV bars plus compact annotations and is responsible
only for rendering them. Server-side calculations make the historical signals
deterministic and unit-testable while avoiding repeated calculations as cards
are lazily initialized on the client.

`union_chart_dashboard.py` remains the generator and continues reading OHLCV
through `ohlc_db.load_ohlc_many()`. Each output record retains the existing
symbol, tier, and bars fields and adds day-change, industry, candle-color, and
coil-box annotations.

## Data Window

- Load 250 daily trading bars per symbol, as today.
- Retain all 250 bars in the page for EMA200 warm-up and backward panning in
  Interactive mode.
- Set each newly constructed chart's initial viewport to the latest six
  calendar months of candles plus 15 blank future logical slots.
- Users may pan farther back into the retained history after enabling
  Interactive mode.
- Continue requiring at least 130 bars for a symbol to be included.

Current-day percentage change uses the latest two available completed daily
candles: `(latest_close / previous_close - 1) * 100`. Store the unrounded value
for sorting and display it rounded to two decimal places.

## TradingView Industry Classification

Refresh symbol-to-industry mappings from TradingView during each dashboard run,
using TradingView's `industry` field. Make one NSE common-equity query selecting
`name` and `industry`, then retain the current union symbols rather than relying
on the March 2026 static universe CSV.

Overlay every non-empty live classification onto the prior cache. After a
successful non-empty response, atomically store the merged mapping and refresh
date in `.union_chart_cache/industries.json`. Add `.union_chart_cache/` to
`.gitignore`; the downloaded cache is local runtime data and must not be
committed.

If TradingView is unavailable or returns an unusable response, use the last
successful cache. If neither live data nor a cached classification exists for a
symbol, assign `Unclassified`. Industry refresh failure must not prevent OHLC
charts from being generated.

## Pocket Pivot Candle Repaint

Use the Pocket Pivot Volume definition from `pine_scripts/Satya_All_Overlay.pine`:

1. The signal candle closes above the previous candle's close.
2. Walk backward, collecting the most recent 10 down days. A down day closes
   below its preceding day's close.
3. The signal candle's volume must be greater than the maximum volume among
   all 10 collected down days.
4. Do not signal unless 10 prior down days are available.

Pocket Pivot candles are blue. This definition intentionally uses the most
recent 10 down days, which may span more than 10 trading bars. It does not use
the Bounce-RS EMA10 proximity condition.

## WaveTrend Candle Repaint

Use fixed Satya All Overlay parameters:

- Channel length: 10
- Average length: 21
- Signal line: four-bar simple moving average of WT1
- Bull signal: WT1 crosses above WT2 on the completed daily candle
- Bear signal: WT1 crosses below WT2 on the completed daily candle

Calculate from daily `hlc3` exactly as the Pine function does:

1. `esa = EMA(hlc3, 10)`
2. `d = EMA(abs(hlc3 - esa), 10)`
3. `ci = d != 0 ? (hlc3 - esa) / (0.015 * d) : 0`
4. `WT1 = EMA(ci, 21)`
5. `WT2 = SMA(WT1, 4)`

Any bull cross repaints the candle white. Any bear cross repaints the candle
yellow; no oversold or overbought zone qualification applies.

WaveTrend has precedence over Pocket Pivot. If a completed candle qualifies
for both, a bull cross is white or a bear cross is yellow rather than blue.
Candles without either signal use the current configurable up/down colors.

## Satya EMAs Mini-Coil Box

Match the active mini-coil behavior in `pine_scripts/Satya EMAs.txt` with the
approved dashboard duration:

1. A mother candle is followed by at least two consecutive candles whose highs
   are at or below the mother high and whose lows are at or above the mother
   low.
2. Confirmation occurs on the second contained candle.
3. Draw a lightly shaded box from the mother candle through 15 trading bars
   after the confirmation candle. The confirmation candle is not counted as
   one of those 15 future bars. The box boundaries are the mother high and
   mother low.
4. When a newly confirmed box overlaps the preceding box's time span, remove
   the preceding box and retain the newer one, matching Satya EMAs replacement
   behavior.
5. Do not repaint the mother candle. The box is the only coil visualization.
6. Do not add labels or breakout markers.

The client converts each box's start/end dates and high/low prices to chart
coordinates. It recalculates those coordinates after pan, zoom, resize, and
device-orientation changes so boxes remain aligned with their candles.
Use the Satya EMAs visual language: a gray border and approximately 10-percent
opaque gray fill, without text.

## EMA Overlays

Keep the current default periods and make their colors deterministic:

- EMA20: cyan
- EMA50: orange
- EMA200: magenta

Custom periods continue to use the comma-separated EMA-period input and cycle
through a fixed contrasting palette. Add one page-level EMA visibility switch
that hides or restores all EMA lines without regenerating the dashboard.

EMA lines must set last-value visibility and price-line visibility off. No EMA
or other indicator may add a label to a price candle or the price scale.

## Price and Volume Separation

Add a page-level flip switch for volume visibility. Volume is hidden by default
because Pocket Pivot candles already expose the relevant volume signals. Pocket
Pivot detection and repainting remain active when the histogram is hidden.

When volume is hidden, remove its series from view and give the price scale a
`bottom` margin of `0.05`, allowing price to use almost the complete chart.
When volume is enabled, it must never cover price candles, EMA lines, or
mini-coil boxes. Give the price scale a `bottom` margin of `0.25`; give the
overlay volume scale a `top` margin of `0.78` and a `bottom` margin of `0.00`.
This reserves 22 percent for volume and leaves a three-percent gap between the
price and volume regions. The two regions remain visually aligned on the same
time axis.

## Responsive Layout and Touch Behavior

Use the selected adaptive card grid:

- Phone widths: one full-width chart card per row.
- Tablet widths and orientations: an auto-adjusting grid, normally one or two
  columns depending on the available card width rather than a hard-coded
  device model.
- Desktop widths: an auto-fitting multi-column grid.
- The page remains vertically scrollable at every width.
- A vertical swipe over a chart scrolls the page in both chart modes.
- Horizontal pan and pinch zoom are available only in Interactive mode.
- Desktop mouse-wheel input scrolls the page in both modes; chart dragging pans
  time only in Interactive mode.

Use `repeat(auto-fit, minmax(min(100%, 320px), 1fr))` for the grid and a
`600px`-and-narrower breakpoint that forces one column. Card and chart sizes
must be based on container width so tablet portrait, split-screen, and
landscape layouts reflow without reload.

Configure chart touch handling so vertical touch-drag never belongs to the
chart. Toggle horizontal touch-drag, mouse drag, and pinch scaling when the
Fixed/Interactive control changes.

Keep `IntersectionObserver` lazy construction. Off-screen cards are not
instantiated until they approach the viewport, which remains necessary for a
dashboard containing hundreds of symbols.

The control bar remains available while scrolling and wraps or collapses into
a compact arrangement at narrow widths. It retains symbol/tier filtering,
up/down candle color controls, EMA periods, and the new EMA visibility switch.
It also includes the volume visibility flip switch, initially off.

## Card Sorting and Industry Grouping

Add a client-side sort selector with three modes:

1. `Industry groups` — the default. Render named industry headings in
   alphabetical order, followed by `Unclassified` last. Within each group,
   order cards by current-day percentage change descending, then symbol
   ascending as the deterministic tie-breaker.
2. `Day change: highest first` — one flat grid ordered by day change descending,
   then symbol ascending.
3. `Day change: lowest first` — one flat grid ordered by day change ascending,
   then symbol ascending.

Sorting and regrouping happen immediately in the browser and do not regenerate
the page. Moving an already initialized card must preserve its chart instance.
Industry names appear only as group headings in `Industry groups` mode; do not
show an industry tag or line inside individual cards in either flat mode.
The existing symbol/tier filter continues to apply after sorting; hide an
industry heading when all cards in that group are filtered out.

Every card header displays the current-day percentage change rounded to two
decimal places. Positive values are green, negative values are red, and exact
zero is muted/neutral.

## Fixed and Interactive Chart Modes

Add one page-level `Fixed / Interactive` flip switch, defaulting to `Fixed`.

In Fixed mode:

- Show historical candles from the latest bar back exactly six calendar months,
  plus 15 blank logical trading slots to the right of the latest bar. These
  future slots display the complete active coil-box projection and contain no
  fabricated OHLCV.
- Disable horizontal panning, mouse-wheel scaling, drag scaling, and pinch
  zoom.
- Leave vertical page scrolling available even when a gesture starts over a
  chart.

In Interactive mode:

- Enable horizontal mouse/touch panning and pinch zoom.
- Keep vertical touch-drag assigned to page scrolling and keep the desktop
  mouse wheel assigned to page scrolling.
- Retain the 250 loaded bars as the maximum history available for backward pan.

Switching from Interactive back to Fixed immediately resets every initialized
chart to the latest six-calendar-month history plus 15 blank future slots and
disables further pan/zoom. Charts initialized later use the currently selected
mode.

## Failure Handling and Output Integrity

- Preserve the fresh-union-report check. A stale or missing input causes a
  logged skip and leaves the prior dashboard untouched.
- Continue skipping and counting symbols with missing or insufficient OHLCV.
- Treat a per-symbol annotation calculation failure as a skipped symbol and
  report it; do not emit a partially annotated record for that symbol.
- Treat TradingView industry refresh failure as non-fatal: use the last good
  cache and fall back to `Unclassified` per symbol.
- Write the industry cache atomically and never commit it.
- If no requested symbols can be charted, retain the previous good dashboard.
- Continue writing the HTML through a temporary file followed by atomic
  replacement.
- Preserve the HTML SEBI banner and footer.

## Testing and Verification

Add focused Python tests for:

- Pocket Pivot detection using the most recent 10 down days rather than the
  previous 10 bars, including insufficient-down-day and strict-volume cases.
- WaveTrend bull and bear crosses with the fixed 10/21/four-bar parameters.
- WaveTrend-over-Pocket-Pivot candle-color precedence.
- Two-contained-candle mini-coil confirmation.
- Mother high/low box coordinates, 15-trading-bar duration, and overlapping-box
  replacement.
- Annotation serialization into chart records.
- Retaining 250 bars while configuring the initial six-calendar-month history
  plus 15 blank future logical slots without fabricated OHLCV.
- EMA colors, hidden last-value/price-line labels, and the visibility switch.
- Volume hidden by default, its flip switch, Pocket Pivot independence from
  histogram visibility, price expansion while hidden, and price/volume scale
  separation while visible.
- Day-change calculation, two-decimal display, sign coloring, deterministic
  ascending/descending ordering, and tie-breaking.
- Live TradingView industry mapping, atomic cache refresh, stale-cache fallback,
  and `Unclassified` placement last.
- Default industry grouping, headings, within-industry day-change sorting, flat
  modes, empty-heading filtering, and preserving initialized charts during DOM
  reorder.
- Fixed mode as the default, exact six-calendar-month candle history plus 15
  blank future slots, disabled pan/zoom, Interactive-mode gestures, and reset
  when returning to Fixed.
- Responsive auto-fit grid and touch-option configuration.
- Existing stale-input, no-OHLC, atomic-write, and disclaimer safeguards.

Verification sequence:

1. Run focused `tests/test_union_chart_dashboard.py` tests.
2. Run the full Python test suite.
3. Generate the current union dashboard from local OHLCV.
4. Check generated HTML freshness, disclaimer, embedded annotations, and output
   integrity.
5. Manually verify Pocket Pivot, WaveTrend, and coil examples against the Pine
   scripts.
6. Manually test phone, tablet portrait, tablet landscape/split-screen, and
   desktop widths, including orientation reflow, sorting/regrouping, day-change
   display, Fixed/Interactive switching, vertical scrolling in both modes,
   Interactive pan/pinch, EMA switching, default-hidden volume, volume
   switching, price expansion, and volume separation.
7. Run `git diff --check` before commit or publish.

## Files Expected to Change During Implementation

| File | Change |
|---|---|
| `union_chart_dashboard.py` | Server-side annotations, HTML controls, signal colors, coil boxes, viewport, responsive and touch behavior |
| `tests/test_union_chart_dashboard.py` | Focused signal, serialization, HTML, and safety tests |
| `dashboard/union_charts.html` | Regenerated verified dashboard |
| `CLAUDE.md` | Document the enhanced chart contract if operating details materially change |
| `.gitignore` | Exclude the local TradingView industry cache |

No new runtime package is required. The existing vendored TradingView
Lightweight Charts library remains the renderer.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
