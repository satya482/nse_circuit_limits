# Cluster weekly RS breadth

Warning: I am not a SEBI registered investment advisor. Educational information only; consult a SEBI registered investment advisor before investing.

Approved: percentage and count of each group's eligible members whose current developing-week RS is strictly above its own weekly EMA9. Benchmark NIFTY MIDSML 400. Evaluate all eligible group members, including falling ZL members; this is an annotation, not a qualification gate.

Implementation: load long histories separately from the existing 60-bar daily calculation; use matched weekly closes, EMA9 adjust=False and at least nine consecutive valid weekly samples. Report above/evaluated, percentage among evaluated members, and unavailable count. Append fields to the existing sector report and parser; add three sortable cluster columns. Existing seven-column input remains supported as unavailable RS. Preserve current ZL outputs and expanded members.

Verification: independent EMA calculation, developing-week inclusion, equal/below states, missing/stale/invalid/short histories, mismatched weekly closes, group counts including non-rising members, backwards-compatible parsing, JS numeric sorting for all columns, live report/page parity, tests and diff check. Publish the reviewed cluster update through the existing authorized workflow.
