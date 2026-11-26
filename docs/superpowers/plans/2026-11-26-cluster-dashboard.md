# Cluster dashboard implementation plan

Warning: I am not a SEBI registered investment advisor. For educational purposes only; consult a SEBI registered investment advisor before investing.

**Goal:** Generate root `cluster.html` containing all qualifying ZL breadth groups and refresh it through NSE_AllScanners.

**Architecture:** Reuse the sector-rotation report parser, preserve its columns and ordering, and render a standalone responsive HTML table. Run the existing local-data sector scanner before generating the page in its runner, and call that runner before Dashboard in the weekday pipeline.

**Validation:** Test more than 20 groups, escaping, empty results, missing input preservation and scheduled runner order. Run the scanner and generator directly without publication, inspect report/page parity, and parse PowerShell scripts.

- [x] Add focused regression tests and observe failure.
- [x] Add `cluster_dashboard.py`, update `run_sector_rotation.ps1` and `run_all_scanners.ps1`, and use shared disclaimer constants in sector reports.
- [x] Generate current local reports/page, run focused checks, update HANDOFF.md and review the diff. Leave publication for explicit authorization.
