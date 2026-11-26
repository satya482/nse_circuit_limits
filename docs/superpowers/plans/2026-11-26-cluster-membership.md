# Cluster membership maintenance plan

> Warning: I am not a SEBI registered investment advisor. Educational information only; consult a SEBI registered investment advisor before investing.

**Approved scope:** All NSE common equities including new IPOs, price strictly above Rs25, market cap Rs1,000 crore to Rs5 lakh crore inclusive. Daily discovery, weekly membership updates, monthly description refreshes, visible pending coverage and membership changes. Preserve manual overrides.

**Architecture:** Paginate the existing TradingView company discovery query and atomically save a validated eligible universe. Discover before FetchData in NSE_AllScanners. Perform due weekly/monthly maintenance before SectorRotation; track successful ISO week/month only after success. Restrict peer building and daily sector signals to eligible companies. Preserve valid descriptions on fetch failure. Use the existing monthly task as a safe maintenance entry point. Do not publish caches.

**Files:** tools/company_fetcher.py (universe/description retrieval); tools/peer_group_builder.py (eligible stable memberships); cluster_membership.py (cadence, changes, coverage); sector_rotation_scanner.py and cluster_dashboard.py (gated daily signals and visible pending stocks); PowerShell runners (ordering, native exit checks and generated output paths).

**Verification:** Focused tests for strict boundaries, common-equity query, pagination beyond 1,000, empty/incomplete fetch preservation, cadence/retries, overrides and stable group identities, pending categories, daily gate enforcement and dashboard escaping. Live daily discovery, full external description refresh, direct scanner/dashboard generation, report/HTML parity, Python and PowerShell syntax, broader focused regressions and diff checks. Full refresh completed 2026-11-26: 1,465 usable descriptions from 1,477 eligible stocks, 12 description failures retained as pending, 29 qualifying breadth groups. Monitoring also found and fixed a changed Trendlyne selector; current/legacy selector tests and a live fetch passed.

- [x] Write focused tests; observe missing behaviour.
- [x] Implement discovery and weekly/monthly maintenance with safe writes.
- [x] Integrate scanner eligibility, coverage and runner scheduling.
- [x] Execute tests and live verification; update HANDOFF.md.

Publication of this follow-up requires explicit authorization.
