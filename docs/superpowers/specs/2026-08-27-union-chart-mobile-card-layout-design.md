> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Union Chart Mobile Card Layout Design

**Status:** Approved design
**Date:** 2026-08-27

## Purpose

Improve the existing union-watchlist chart dashboard for frequent phone,
tablet, and desktop use by:

1. starting with EMA overlays hidden;
2. enlarging chart cards so six months of candles are easier to read on tablets
   and desktops;
3. moving the clickable symbol to the right side of each card header for easier
   right-thumb access.

This design modifies the existing `dashboard/union_charts.html` generator. It
does not create another dashboard, change union membership, change indicator
calculations, or reduce the fixed six-month display range.

## Selected Approach

Use CSS-only adaptive card enlargement while retaining the current lazy chart
initialization and Lightweight Charts behavior.

- Increase the adaptive grid's minimum card width from 320px to 440px.
- Increase chart height from the current 240-320px range to 330-400px.
- Keep phones at one full-width card per row without horizontal scrolling.
- Keep the complete fixed six-month range plus 15 blank future logical slots on
  every device.
- Change the card header to three stable alignment zones: percentage on the
  left, tier in the center, and clickable symbol on the right.
- Change EMA state and markup so every page load starts with EMAs off.

The alternatives were rejected as follows:

- One chart per row on every device would improve spacing but cause excessive
  desktop scrolling.
- A Compact/Large control would add state and interface complexity without
  being necessary for the requested default.
- Horizontal card scrolling on phones would undermine the fixed overview and
  complicate page gestures.

## Responsive Card Layout

Use this adaptive grid contract:

```css
#grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 440px), 1fr));
  gap: 10px;
}

.chart {
  height: clamp(330px, 38vw, 400px);
}

@media (max-width: 600px) {
  #grid { grid-template-columns: 1fr; }
  .chart { height: 330px; }
}
```

Expected behavior:

- Phone: one full-width card with a 330px-high chart.
- Tablet portrait, landscape, and split-screen: automatically one or two
  columns according to available width.
- Desktop: an auto-fitting multi-column grid with substantially larger cards
  than the current 320px minimum.

Do not introduce a fixed device list, horizontal page scrolling, or horizontal
card scrolling. The existing `ResizeObserver` must continue passing both the
rendered chart width and height to Lightweight Charts and redrawing coil boxes
after every size change.

### Phone density constraint

A phone cannot give six months of daily candles more horizontal space while
also showing the entire range within the viewport. The selected behavior keeps
all six months visible and uses the full phone width. The increased height
improves price-scale and wick readability, but the candles remain necessarily
dense on narrow phones.

## Fixed Range and Interaction

Do not change chart-range semantics:

- Fixed mode remains the default.
- The visible range begins at the first candle on or after the six-calendar-
  month cutoff.
- The visible range ends 15 logical slots after the latest actual OHLCV bar.
- Future logical slots contain no fabricated OHLCV data.
- Interactive mode retains horizontal drag and pinch.
- Vertical touch dragging remains disabled inside Lightweight Charts so page
  scrolling works over charts.

Enlarging the card must not call `fitContent()` or replace the explicit fixed
logical range.

## Card Header Layout

Render each header in this visual order:

1. signed current-day percentage change on the left;
2. confluence tier in the center;
3. clickable stock symbol on the right.

Use a three-column layout rather than relying on `margin-left: auto`, so short
and long symbols do not shift the tier away from the center:

```css
.hdr {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
}

.day-change { justify-self: start; }
.tier { justify-self: center; }
.symbol-link {
  justify-self: end;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  padding-left: 12px;
}
```

The stock symbol remains the TradingView link and must remain fully keyboard
accessible. Its mobile tap target is at least 44px high and is right-aligned for
right-thumb access.

Retain the current percentage semantics:

- positive values are green;
- negative values are red;
- exact zero is neutral;
- displayed values are signed and rounded to two decimal places.

Industry remains a group heading and is not repeated inside each card.

## EMA Default State

Change page-level client state from EMA-visible to EMA-hidden:

```javascript
const uiState = {
  emaVisible: false,
  volumeVisible: false,
  interactive: false,
};
```

Render the EMA checkbox without `checked`. Do not persist the choice in
`localStorage`, session storage, cookies, or URL parameters. Every page load
starts with EMAs off.

When the user enables EMAs:

- build the configured EMA series with the existing colors;
- keep last-value and price-line labels hidden;
- redraw coil overlays after EMA series change;
- preserve the current fixed or interactive chart mode.

Turning EMAs off removes their series and redraws the coil overlays. Volume
remains off by default and retains its independent switch and non-overlapping
scale margins.

## Accessibility

- Keep visible text beside every switch.
- Do not communicate percentage direction by color alone; retain the plus or
  minus sign.
- Keep the symbol as a semantic link with its existing destination and
  new-tab behavior.
- Ensure the 44px symbol tap target does not overlap the centered tier.
- Preserve keyboard focus visibility supplied by the browser or add an
  explicit visible focus outline if existing CSS suppresses it.

## Testing

Update focused HTML contract tests to verify:

- `uiState.emaVisible` is `false`;
- the EMA checkbox has no `checked` attribute;
- generated header markup orders percentage, tier, then symbol;
- the symbol link carries the class used for right alignment and tap sizing;
- grid minimum width is 440px;
- chart height uses the 330-400px adaptive range;
- the phone breakpoint remains one column with 330px chart height;
- the symbol tap target has a minimum 44px height.

Retain regression coverage for:

- exact six-calendar-month fixed range;
- 15 blank future logical slots;
- no fabricated future OHLCV;
- vertical page scrolling in both chart modes;
- tablet auto-reflow and resize handling;
- industry and daily-change sorting;
- default-hidden volume and price/volume scale separation;
- EMA toggling and coil redraw ordering;
- SEBI banner and footer presence.

## Generation and Verification

After implementation:

1. Run the focused union dashboard tests.
2. Run the full repository suite using a worktree-local pytest temporary
   directory.
3. Require `git diff --check` to pass for changed files.
4. Generate `dashboard/union_charts.html` only when the union input is dated
   today.
5. Verify the generated page contains the new EMA default, header order, and
   responsive CSS.
6. Check phone, tablet portrait, tablet landscape, and desktop viewport sizes.
7. Confirm vertical page scrolling, Fixed/Interactive behavior, sorting, EMA
   toggling, volume separation, signal candle colors, and coil alignment.

If today's union data is stale or unavailable, preserve the previous good
dashboard rather than publishing a stale replacement.

## Acceptance Criteria

- Every page load begins with EMA overlays off and the EMA switch unchecked.
- Users can enable and disable EMAs without losing chart mode or coil alignment.
- Adaptive cards use a 440px preferred minimum and 330-400px chart height.
- Phones show one full-width 330px-high chart without horizontal scrolling.
- The full six-month fixed range plus 15 blank future slots remains visible on
  every device.
- Each header displays percentage left, tier centered, and clickable symbol
  right.
- The right-aligned symbol has at least a 44px-high tap target.
- Tablet layouts automatically reflow between one and two columns.
- Existing sorting, filtering, volume, interaction, disclaimer, and stale-input
  safeguards remain intact.
- Focused and full tests pass, and the generated page passes the manual viewport
  checklist before publication.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
