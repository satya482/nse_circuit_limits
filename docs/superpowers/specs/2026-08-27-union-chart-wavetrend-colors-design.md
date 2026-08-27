# Union Chart WaveTrend Repaint Colors — Design

Date: 2026-08-27

## Purpose

Make WaveTrend bull and bear cross candles easier to distinguish when six
months of candles are compressed on a black phone, tablet, or desktop chart.

## Selected Palette

- WaveTrend bull cross: lime `#76FF03`.
- WaveTrend bear cross: yellow `#FDD835`.

The colors repaint the complete signal candle body, border, and wick, matching
the dashboard's existing signal-candle treatment.

## Scope

Change only the WaveTrend color mapping in `union_chart_dashboard.py` and the
generated `dashboard/union_charts.html` artifact. Preserve:

- WaveTrend cross calculations and fixed parameters;
- WaveTrend precedence over Pocket Pivot signals;
- Pocket Pivot blue and normal configurable up/down candle colors;
- EMA, ZLEMA25, volume, inside-bar boxes, sorting, and chart interaction;
- the current generated dashboard's embedded OHLCV and annotation data.

## Verification

- Add or update the focused HTML contract test for the exact lime/yellow values.
- Run all union-chart dashboard tests and the full repository test suite.
- Verify the generated artifact contains the new colors and retains the same
  embedded data hash, record count, coil-box count, and title date.
- Run `git diff --check`, commit only scoped files, and push `main`.

---

*Warning: I am not a SEBI registered investment advisor. All content is for
educational and informational purposes only and does not constitute investment
advice. Please consult a SEBI registered investment advisor before making any
investment decisions. Investments in securities market are subject to market
risks, read all related documents carefully before investing.*
