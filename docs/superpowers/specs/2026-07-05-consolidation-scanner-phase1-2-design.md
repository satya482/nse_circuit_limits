# Consolidation Tracker — Phase 1+2 Design (Indicators + Quality + Imminence + Tiers + Scanner)

Date: 2026-07-05

Source spec: `research/consolidation_capital_efficiency_spec.md` (full 7-phase, 14-section spec).
This design covers Phase 1+2 only: indicators → quality/imminence scoring → tier labelling →
daily ranked scanner output. Phase 3 (capital/time-stops/regime-throttle/slots), Phase 4
(already pulled forward — see below), Phase 5 (catalyst calendar), Phase 6 (Pine companion),
and Phase 7 (half-life backtest) are explicitly out of scope for this design.

## Deviations from the source spec (and why)

The spec's Build Order (Sec 13) defers CMF + delivery% integration to Phase 4. This design
pulls both into Phase 1+2 instead: `ohlc_db.py` already has `cmf_days()` (CMF formula) and a
`delivery` table + `load_delivery()`/`deliv_spike()`/`deliv_tag()` (NSE bhavcopy DELIV_PER,
fed daily by `run_fetch_delivery.ps1`) — both built and proven elsewhere in this repo. Deferring
would mean reinventing them later for no reason. The full Sec 3 quality-score table (100 pts,
including CMF=15 and Delivery%=10) ships from day one.

The spec's file layout (Sec 11) lists a `tracker.py` orchestrator class and a `signals.db`
persisted tier-transition table. Both are cut:

- **No `tracker.py`** — no other scanner in this repo wraps per-symbol logic in a class;
  `consolidation_scanner.py` loops over symbols calling module functions directly, same shape
  as `wt_bullcross_scanner.py`.
- **No `signals.db`** — everything Sec 5 needs (`consolidation_age`, "quality fell 15+ pts from
  peak", promotion/demotion transitions) is derivable statelessly by backward-scanning historical
  OHLC, the same "bars-ago scan" idiom `cmf_days()`/`zl25_stats()` already use in `ohlc_db.py`.
  Transition logging reuses the diff-against-yesterday's-file pattern `nse_ema_daily.py` already
  implements. No new DB, no persistence layer.

Universe: spec Sec 0 calls for a canonical CSV at `data/universe/nse_universe.csv`. Neither
that file nor a "full Kite instrument dump" universe currently exists as a persisted artifact —
`fetch_data.py`'s `instruments` table is pre-filtered to 800Cr–1L Cr at fetch time (a band
this scanner doesn't want) and the repo's persona CSV
(`NSE_500cr_15CrNotional10D_50rs_sector_industry.csv`) serves a different purpose (stock-analysis
personas). Per user decision, `consolidation_scanner.py` builds its own universe via a
TradingView `Query()` call mirroring `wt_bullcross_scanner.py` exactly: NSE common stock, mcap
1,000–5,00,000 Cr, price > ₹50 (price checked via `load_ohlc_many` close). No changes to
`fetch_data.py` or the shared `instruments` table.

## Module layout

```
consolidation/
├── indicators.py    # EMA compression (2.1), BB/KC squeeze (2.2), vol exhaustion (2.3),
│                     # RS character (2.4) — new calcs, follow existing Python↔Pine parity
│                     # conventions (ohlc_db.py / rules/pine-script-conventions.md)
├── quality.py        # quality score (Sec 3) — reuses CMF formula (factored out of cmf_days()
│                     # into a shared raw-value helper) and load_delivery() for the delivery%
│                     # trend calc (deliv_ma20 vs deliv_baseline*1.15 — different question from
│                     # deliv_spike()'s single-day spike check, so a new calc, not a new source)
├── imminence.py       # imminence score + 6 pre-break signals (Sec 4). Signal ③ (quiet
│                     # accumulation bar) reuses deliv_tag()/deliv_spike() directly — same
│                     # single-bar spike question.
├── tiers.py           # tier threshold lookup (Sec 5) + abandonment checks, computed from the
│                     # backward-scan described above — no state, no DB
└── consolidation_scanner.py   # run(universe_df, as_of) -> pd.DataFrame; own TV Query() for
                              # universe, load_ohlc_many() for OHLCV, per-symbol loop
```

## Scoring (as spec-written, full detail in source spec Sections 2-4)

**Quality (0-100)**: BB squeeze depth (20) + EMA stage (20) + vol exhaustion (15) +
RS character (20) + CMF accumulation (15) + delivery% trend (10). Computed only for stocks
passing the EMA dual-gate + BB squeeze gate.

**Imminence (0-100)**: pre-break signal count (30, from 6 booleans ①-⑥) + EMA Stage 3 flag (25)
+ RS breakout flag (20) + BB breathing (15) + range position (10).

**Tiers**: pure threshold lookup on today's (quality, imminence) — COLD/WARM/HOT/DEPLOYED per
Sec 5. `DEPLOYED` (breakout confirmed + position open) is a Phase 3 concept; this scanner emits
COLD/WARM/HOT only.

Per spec Sec 14, these thresholds (spread_delta ±0.001, imminence HOT≥60, deliv_baseline
120-bar median, CMF 0.10 "strong") are explicitly unvalidated placeholders, shipped as-is,
to be tuned later by the Phase 7 half-life backtest. Not addressed in this design.

## Output

Both written every run (repo convention, never hand-edited):

- `results/YYYY-MM-DD-consolidation.csv` — spec's own path (Sec 10.5), machine-readable; this
  is the Layer 1 → Layer 2 contract Pine will read tomorrow once Phase 6 exists.
- `consolidation_scans/consolidation_scan_latest.md` + dated `.md` — SEBI disclaimer
  (`disclaimer.py` SEBI_MD_HEADER/FOOTER, required by project CLAUDE.md), sorted tier desc then
  imminence desc — matches every other scanner's markdown convention, for manual review.

Columns (per spec Sec 11, trimmed to this phase's scope): `symbol, quality, imminence, tier,
age_bars, ema_stage, vol_phase, rs_char, cmf, deliv_trend, prebreak_count, regime, action`.
Dropping `days_to_results` and `median_wait_est` — Phase 5/7, not built here.

## Guardrails carried over unchanged

- No look-ahead bias — indicator at bar `t` uses data through `t` only (standing repo rule)
- IST-aware datetimes everywhere
- Minimum 250 bars history required; skip + log otherwise (spec Sec 0)
- Validate every indicator against TradingView on 2-3 known stocks before the first universe
  run (spec Sec 0) — explicit step in the implementation plan, not skipped
- New `run_consolidation_scanner.ps1` runner, logs to `logs/`, added to CLAUDE.md's run table
  (per `.claude/rules/scanner-conventions.md`'s new-scanner checklist) — exact schedule slot
  decided in the implementation plan

## Explicitly out of scope (later phases, not this design)

- Capital/time-stops/regime-throttle/slots (spec Sec 6, 8, 9 — Phase 3)
- Catalyst calendar (spec Sec 7 — Phase 5)
- PineScript companion (spec Sec 12 — Phase 6)
- Half-life backtest / `expected_annualized` ranking metric (spec Sec 10 — Phase 7)
