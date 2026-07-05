# Bounce-RS Dashboard Integration — Design

**Status:** Design approved, ready for implementation plan
**Date:** 2026-07-05
**Depends on:** `scanners/bounce_rs_scanner.py` (merged to main, `docs/superpowers/specs/2026-07-04-bounce-rs-scanner-design.md`)

---

## 1. Purpose

The Bounce-RS Scanner ships as a pure function (`run(universe_df, as_of) -> pd.DataFrame`) with no runner, no output file, no dashboard visibility — by design, deferred at merge time. This work wires it into `wt_squeeze_dashboard.html`, the dashboard the user visits most, as a table at the top of the page, visible only on days it fires.

---

## 2. Scheduling Constraint (the reason this isn't a 1-file change)

`wt_squeeze_dashboard.py` currently builds at **4:40 PM** (`run_wt_squeeze_dashboard.ps1`). Bounce-RS needs today's `ratio_5d` from `data/breadth_history.csv`, which `breadth_monitor.py` doesn't write until its own scheduled run at **~5:30 PM** (`run_breadth_monitor.ps1`, `NSE_BreadthMonitor` task). At 4:40 PM, today's breadth row doesn't exist yet.

**Resolution:** `run_breadth_monitor.ps1` gains two trailing steps after its existing `breadth_monitor.py` + commit: run the new Bounce-RS scanner, then re-invoke `run_wt_squeeze_dashboard.ps1`. The dashboard HTML now gets built twice a day — 4:40 PM (Bounce-RS section absent or stale) and ~5:35 PM (Bounce-RS current). This mirrors the existing pattern where `run_breadth_monitor.ps1` is already a self-contained trailing pipeline (`kite_auth → fetch_data.py --all → breadth_monitor.py → commit`).

---

## 3. New Files

### `run_bounce_rs_scanner.py`

Follows `inside_bar_scanner.py`'s shape (single-file scanner script, TradingView watchlist, `load_ohlc`-backed, SEBI-disclaimed markdown output):

- **Watchlist:** TradingView screener, NSE common equity, `market_cap_basic` between ₹800 Cr and ₹1 Lakh Cr — same filter as `inside_bar_scanner.py::get_watchlist()`. No pre-filter on EMA structure; Bounce-RS does its own RS/EMA gating internally, so the watchlist here is a plain liquid-universe query, not a pre-qualified trend watchlist.
- **Run:** builds `universe_df = pd.DataFrame({"symbol": watchlist})`, calls `bounce_rs_scanner.run(universe_df, date.today())` (IST date, matching `breadth_monitor.py`'s `datetime.now(IST).date()` pattern).
- **Output:** `bounce_rs_scans/bounce_rs_scan_latest.md` + `bounce_rs_scans/bounce_rs_scan_YYYY-MM-DD.md`, both written every run (per `scanner-conventions.md`'s output-file discipline — even when 0 rows, write `*No signals.*`, never an empty file). SEBI header/footer via `disclaimer.py`.
- **Table columns (all 8, matches `run()`'s `OUTPUT_COLUMNS` exactly):** `Symbol | RS Dip% | EMA Type | Setup | Dip Low | Ratio Now | Bounce | Score`.

### `run_bounce_rs_scanner.ps1`

Thin runner, logs to `logs/bounce_rs_scanner_YYYY-MM-DD.log`, matches every other scanner's `.ps1` shape (kite auth assumed already fresh from the day's earlier `run_fetch_data.ps1`, no separate auth step needed since this runs after breadth_monitor which already re-authenticates).

---

## 4. Modified Files

### `run_breadth_monitor.ps1`

Append after the existing commit step:
```powershell
.\run_bounce_rs_scanner.ps1
.\run_wt_squeeze_dashboard.ps1
```
(Both logged independently, matching existing convention — this file already runs multiple sub-steps as one scheduled task.)

### `wt_squeeze_dashboard.py`

- New constant: `BOUNCE_RS_MD = os.path.join(BASE, "bounce_rs_scans", "bounce_rs_scan_latest.md")`
- New function `parse_bounce_rs(content: str) -> list[dict]`, same pipe-table-line-splitting pattern as `parse_wt_rows` (`wt_squeeze_dashboard.py:95`), but for the Bounce-RS 8-column schema — returns one dict per row with keys `symbol, rs_pct, ema_type, setup, dip_low, ratio_now, bounce, score`.
- New section builder inline in `build_html()` (same pattern as `conf_section`/`sqz_section`, `wt_squeeze_dashboard.py:436-517`): builds `bounce_rs_section = ""` if no rows, else a `<div class="section">` block with its own small table (8 cols, not the shared 13-col `_TABLE_HDR` — Bounce-RS rows aren't WT rows and don't fit that schema).
- **Placement:** `bounce_rs_section` is inserted **first**, above `{wg_section}` in the final `f"""..."""` HTML assembly (`wt_squeeze_dashboard.py:550`) — topmost section on the page, above Trend×WT confluence, above Weekly RS Gate, above everything.
- **Visibility:** hidden entirely when `bounce_rs_rows` is empty (same `if conf_rows:` pattern already used for every other conditional section) — no permanent placeholder, since a dip-bounce regime is rare.
- `main()` (`wt_squeeze_dashboard.py:583`) gains `bounce_rs_rows = parse_bounce_rs(read_file(BOUNCE_RS_MD))`, passed into `build_html(...)`.

### `CLAUDE.md`

- Add `run_bounce_rs_scanner.ps1` to the run table, positioned after `run_breadth_monitor.ps1` in the schedule list (fires as its trailing step, ~5:30-5:35 PM).
- Add `bounce_rs_scans/bounce_rs_scan_latest.md` to the "Output files (git-tracked)" table.
- Note in the WT+Squeeze dashboard section that it now builds twice daily (4:40 PM initial, ~5:35 PM refresh with Bounce-RS data).

---

## 5. Data Flow (end to end)

```
run_fetch_data.ps1 (4:05 PM)  →  today's OHLC in SQLite
run_wt_squeeze_dashboard.ps1 (4:40 PM)  →  dashboard built WITHOUT Bounce-RS row (breadth not ready yet)
run_breadth_monitor.ps1 (~5:30 PM)
  → breadth_monitor.py writes today's ratio_5d row to data/breadth_history.csv
  → run_bounce_rs_scanner.py: watchlist → bounce_rs_scanner.run() → bounce_rs_scan_latest.md
  → run_wt_squeeze_dashboard.py (2nd build): parses bounce_rs_scan_latest.md → top table (if non-empty) → dashboard rebuilt
```

---

## 6. Out of Scope

Push alerts (Telegram/webhook) remain v2/Low priority per the original scanner design's backlog — unchanged, not part of this work.

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
