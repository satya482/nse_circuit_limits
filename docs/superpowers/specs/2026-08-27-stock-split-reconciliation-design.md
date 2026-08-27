> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Stock-Split OHLC Reconciliation Design

**Status:** Approved design; deferred for later implementation
**Date:** 2026-08-27

## Purpose

Prevent stock splits and similar corporate-action adjustments from leaving a
mixture of stale pre-action candles and current post-action candles in
`.ohlc_data/market.db`. The union chart dashboard and its EMA, WaveTrend,
Pocket Pivot, mini-coil, and daily-change calculations must consume one
internally consistent daily OHLCV series.

This design does not calculate split ratios locally. Kite's adjusted daily
history remains the canonical source.

## Current Failure Mode

`fetch_data.py` stores historical candles with `INSERT OR IGNORE` and updates a
mature symbol by inserting only the current quote. Existing historical rows are
therefore not replaced when Kite later adjusts its history for a corporate
action.

If a split occurs after a symbol was originally backfilled, the database can
retain old pre-split prices while adding new post-split prices. The resulting
artificial discontinuity can distort:

- EMA lines;
- WaveTrend state and crosses;
- Pocket Pivot volume comparisons;
- mini-coil detection;
- current-day percentage change on the action date.

## Selected Architecture

Use provider-history reconciliation with two triggers:

1. **Immediate targeted reconciliation:** after the normal daily update,
   inspect every updated stock. An absolute overnight gap of at least 35
   percent between the previous close and latest open makes the symbol a
   reconciliation candidate.
2. **Weekly safety reconciliation:** refetch the current union-watchlist
   symbols once per week, even when no large gap is detected.

Detection only schedules a refetch; it never changes prices or infers a split
ratio. A genuine market gap may remain after reconciliation and is retained as
valid provider data.

## Components and Interfaces

### Gap detection

Add a focused helper with an interface equivalent to:

```python
is_reconciliation_candidate(previous_close: float, latest_open: float,
                            threshold: float = 0.35) -> bool
```

The threshold is inclusive: an absolute change of exactly 35 percent qualifies.
Missing, non-finite, or non-positive prices do not qualify through this helper;
they are handled as data-validation failures elsewhere.

### Historical fetch

Refetch 400 calendar days of daily OHLCV for each candidate or weekly union
symbol using Kite's historical-data endpoint. Normalize each returned candle to
the existing schema:

```text
symbol, date, open, high, low, close, volume
```

The fetch unit returns normalized rows but does not write to SQLite.

### Validation

Before changing the database, require:

- at least two returned daily candles;
- unique dates in ascending order after normalization;
- finite, positive open, high, low, and close values;
- `high >= max(open, close)` and `low <= min(open, close)`;
- nonnegative finite volume;
- all returned rows to belong to the requested symbol and 400-day window.

Validation failure is a reconciliation failure and must not modify existing
rows.

### Transactional upsert

Write one symbol's complete fetched window inside a single SQLite transaction:

```sql
INSERT INTO ohlc(symbol, date, open, high, low, close, volume)
VALUES (?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(symbol, date) DO UPDATE SET
    open = excluded.open,
    high = excluded.high,
    low = excluded.low,
    close = excluded.close,
    volume = excluded.volume;
```

Commit only after every row for that symbol succeeds. Roll back the entire
symbol update on any database error. The reconciliation path must replace both
prices and volume because adjusted history can affect both.

The existing historical backfill path should use the same upsert primitive so
a future refetch cannot silently retain stale rows.

### Current-day candle finalization

The quote-based daily delta may remain as a provisional current-day update.
After market close, reconciliation should use the daily historical endpoint to
replace that row with the provider's official EOD candle. The dashboard must be
generated only after required reconciliation and EOD finalization complete.

### Dashboard eligibility

Produce a reconciliation result per requested symbol with one of these states:

- `REFRESHED`: valid history was transactionally stored;
- `GENUINE_GAP`: valid refreshed history still contains the large gap;
- `NOT_REQUIRED`: no immediate trigger applied;
- `FAILED`: fetch, validation, or transaction failed.

A current union symbol in `FAILED` state is excluded from that dashboard run,
and the skip reason is logged. Other valid symbols continue normally. Do not
emit a record using potentially mixed split history.

If reconciliation cannot initialize or fails systemically before any requested
symbol can be assessed, do not overwrite the previous good dashboard.

## Data Flow

1. Complete the normal instrument refresh and daily quote update.
2. Read the previous close and latest open for each updated stock.
3. Queue symbols whose absolute overnight gap is at least 35 percent.
4. Add all current union-watchlist symbols when the weekly reconciliation mode
   is active.
5. Deduplicate the queue and fetch 400 calendar days per symbol.
6. Normalize and validate each response without changing SQLite.
7. Transactionally upsert the validated window.
8. Re-read the stored rows and classify the result as `REFRESHED` or
   `GENUINE_GAP`; classify any failure as `FAILED`.
9. Generate charts only from eligible reconciled data.

## Command-Line and Scheduling Contract

Extend `fetch_data.py` with an explicit weekly mode equivalent to:

```powershell
python fetch_data.py --reconcile-union
```

Normal daily execution performs only immediate 35-percent candidate checks.
The scheduled weekly workflow runs `--reconcile-union` after the union report is
fresh and before `union_chart_dashboard.py` publishes the dashboard.

The weekly scope is the current union watchlist, not every symbol in the OHLC
database. This bounds API use while protecting every chart that may be
published.

No raw Kite responses, SQLite databases, secrets, or reconciliation caches are
committed. The existing data manifest may continue recording symbol, latest
date, and row count; reconciliation does not require a schema migration.

## Error Handling and Observability

Log a concise run summary containing:

- symbols inspected for immediate gaps;
- immediate candidates;
- weekly union symbols queued;
- successfully refreshed symbols;
- genuine gaps remaining after refresh;
- fetch, validation, and transaction failures;
- union symbols excluded from dashboard generation.

Log each failed symbol and its failure stage without printing credentials or
raw API payloads. One symbol's failure must not stop reconciliation of other
symbols.

Retries must be bounded. A failed refetch is not permission to fall back to the
known-suspect series for that dashboard run.

## Testing

### Unit tests

- A gap below 35 percent does not trigger; exactly 35 percent and above do.
- Invalid prices are rejected safely.
- Historical normalization produces unique ascending dates.
- Invalid OHLC relationships, negative volume, and incomplete responses fail
  validation.
- Upsert replaces existing open, high, low, close, and volume values without
  increasing the row count for matching dates.
- Any write failure rolls back all rows for that symbol.
- A failed reconciliation returns `FAILED` and excludes the affected union
  symbol.

### Integration tests

- Preload stale pre-split rows, return adjusted Kite history, reconcile, and
  verify the artificial gap disappears.
- Confirm EMA, WaveTrend, Pocket Pivot, mini-coil, and day-change inputs use the
  adjusted series after reconciliation.
- Return valid provider history containing a genuine large gap and verify the
  rows are retained with `GENUINE_GAP` status.
- Simulate one failed symbol among successful symbols and verify only that
  symbol is omitted.
- Simulate a systemic initialization failure and verify the previous dashboard
  artifact remains unchanged.
- Verify weekly mode queues exactly the current union-watchlist symbols.

## Acceptance Criteria

- Refetched adjusted history can replace previously stored rows.
- Immediate reconciliation uses an inclusive 35-percent overnight-gap trigger.
- Weekly reconciliation covers every current union-chart symbol and no broader
  universe by default.
- No local split-ratio calculation is used.
- Price and volume history are replaced atomically per symbol.
- Failed candidate reconciliation excludes that stock from the dashboard.
- A systemic reconciliation failure preserves the previous good dashboard.
- Generated charts never knowingly combine stale pre-split history with
  current post-split candles.
- Focused and full repository tests pass, and generated or modified Markdown
  and HTML artifacts retain the required `SEBI registered` disclaimer.

## Deferred Scope

This specification is saved for later implementation. It does not currently
change `fetch_data.py`, the SQLite database, scheduled tasks, or dashboard
behavior.

Explicitly deferred:

- an NSE corporate-action feed;
- locally calculated split, bonus, or demerger factors;
- reconciliation of every tracked NSE symbol each week;
- rewriting historical data outside the provider's returned 400-day window.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
