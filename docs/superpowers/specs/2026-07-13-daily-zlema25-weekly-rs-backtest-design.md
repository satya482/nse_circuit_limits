> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Daily ZLEMA25 With Weekly RS EMA9 Backtest Design

## Objective

Measure the historical returns and win rate of daily ZLEMA25 uptrend episodes when the stock's relative-strength setup is supportive. The initial run covers TRIVENI, CARTRADE, and KIRLOSENG over their common locally available period, 2021-08-20 through 2026-07-13.

The backtest must be repeatable for other NSE symbols and dates through command-line arguments. It uses the repository's local OHLC database and does not fetch live data.

## Data and Indicators

- Load stock and benchmark daily OHLC through `ohlc_db.py`.
- Use `NIFTY MIDSML 400` as the RS benchmark.
- Daily ZLEMA25 is `2 * EMA(close, 25) - EMA(EMA(close, 25), 25)` with pandas `ewm(span=25, adjust=False)`.
- Daily RS is `(stock close / benchmark close) * 1000` on common trading dates.
- Weekly RS EMA9 is reconstructed as of every daily bar. For each trading date, the current day's RS is the last value of the current partial week and is combined with prior completed weekly values before EMA9 is calculated. The rising test compares that as-of-date EMA9 with the EMA9 of the prior completed week. No later observation from the same week may affect an earlier daily bar.
- Require at least 25 stock bars and 9 weekly RS observations before a bar can signal.

Indicators may use observations before the requested start date for warm-up. Entry dates remain restricted to the requested inclusive date range.

## Trade Rules

A stock can have at most one open trade.

Enter at the current daily close when all conditions are true:

1. Daily ZLEMA25 is strictly higher than the prior bar.
2. On the prior bar, ZLEMA25 was flat or falling relative to its preceding bar.
3. Daily RS is above the as-of-date weekly RS EMA9.
4. The as-of-date weekly RS EMA9 is strictly higher than the prior completed week's weekly RS EMA9.

After entry, exit at the current close on the first bar where either:

- daily ZLEMA25 is strictly lower than the prior bar; or
- weekly RS EMA9 is no longer strictly rising.

If both occur on the same bar, record `ZLEMA_AND_RS` as the exit reason. Otherwise use `ZLEMA_DOWN` or `RS_NOT_RISING`.

Daily RS falling below weekly RS EMA9 after entry is not itself an exit. The user required the EMA9 slope to remain rising; the RS-above-EMA condition is an entry qualification only.

There are no next-bar fills, brokerage charges, slippage, stops, profit targets, position sizing, dividends, or overlapping trades. An entry and exit both use the recorded daily close.

Trades still open on the final date are reported separately and excluded from completed-trade statistics. They are not force-closed or counted as wins or losses.

## Components

Add a root-level `backtest_daily_zlema25_weekly_rs.py` consistent with the repository's flat backtest convention. Its responsibilities are:

- parse symbols, start date, end date, and output directory;
- load OHLC through `ohlc_db.py`;
- compute no-look-ahead indicators in independently testable functions;
- simulate one stock at a time;
- aggregate trades and statistics; and
- write CSV and Markdown results.

Add focused tests in `tests/test_backtest_daily_zlema25_weekly_rs.py`. Do not change the existing squeeze backtest because its stops, targets, and squeeze rules are unrelated to this strategy.

## Outputs

Write results under `backtest_results/` by default:

- `daily_zlema25_weekly_rs_trades.csv`: one row per completed trade, with symbol, entry and exit dates, entry and exit closes, percentage return, holding trading days, holding calendar days, and exit reason.
- `daily_zlema25_weekly_rs_open.csv`: open trades at the end date. Write headers even when there are no open trades.
- `daily_zlema25_weekly_rs_summary.md`: method, period, per-stock metrics, combined metrics, completed trade log, and open-trade section. Build it with `SEBI_MD_HEADER` and `SEBI_MD_FOOTER` from `disclaimer.py`.

Per-stock and combined completed-trade metrics are:

- trade count, wins, losses, and zero-return trades;
- win rate, where only returns strictly above zero are wins;
- arithmetic average and median return;
- sequential compounded return, calculated as `product(1 + return) - 1`;
- best and worst return; and
- average holding time in trading days.

The combined compounded return is a strategy-sequence diagnostic, not a realizable portfolio return, because trades in different stocks may overlap.

## Error Handling

- Fail clearly if the benchmark is unavailable.
- Report and skip a requested stock that is unavailable or has insufficient data; do not silently treat it as having zero trades.
- Fail if dates are invalid or the start date is after the end date.
- Keep valid zero-trade stocks in the summary with zero counts and undefined return statistics shown as `N/A`.
- Do not perform network calls or modify the OHLC database.

## Testing and Verification

Focused tests cover:

- the first strictly rising ZLEMA bar is detected once per rising episode;
- weekly RS EMA9 values for an earlier weekday do not change when later same-week data is added;
- entries require ZLEMA turn-up, RS above EMA9, and EMA9 rising on the same bar;
- exits occur on the first ZLEMA downturn or loss of EMA9 rise, including combined reasons;
- open trades are excluded from win-rate statistics;
- wins, zero returns, average, median, compounded return, and holding-period calculations; and
- Markdown output contains `SEBI registered`.

Verification runs the focused pytest file first, then executes the backtest for TRIVENI, CARTRADE, and KIRLOSENG over 2021-08-20 through 2026-07-13 and inspects the generated summaries for internal consistency.

## Repository Handoff

After implementation and verification, update `HANDOFF.md` with the new backtest command, output locations, signal definition, and latest tested period. Preserve unrelated shared-worktree changes.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
