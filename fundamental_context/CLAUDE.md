> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# NSE Knowledge Graph — Claude Code Context

## What This Is

A Neo4j knowledge graph of ~962 NSE-listed stocks with fundamental data,
sector/industry relationships, thematic overlaps, and EP catalyst tracking.

**Core goal**: Connect dots between new fundamental information (order wins,
concall guidance, policy announcements) and existing conviction scores —
so that when a catalyst arrives, the graph immediately surfaces which stocks
benefit, how much conviction increases, and whether EP conditions are met.

---

## Stock Universe

- **File**: `data/raw/NSE_500cr_universe.csv`
- **Columns**: Stock Name, NSE Code, ISIN, Industry Name, sector_name, Sector Description
- **Size**: ~962 stocks, 29 sectors, 119 industries
- **Filters applied at source**: Mkt Cap >₹500Cr, 10D avg notional >₹15Cr, Price >₹50

---

## Quality Filters (hardcoded thresholds — never change without asking)

| Metric | Threshold | Points |
|--------|-----------|--------|
| ROE (3yr avg) | >25% | +8 |
| ROCE (3yr avg) | >30% | +8 |
| Order Book / Revenue | >2x | +10 |
| Promoter stake | >50% | +4 |
| Pledge % | = 0 | +5 |

---

## Neo4j Connection

Credentials in `.env`. Never hardcode.

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=yourpassword
```

Always use `neo4j` Python driver v5.x (not py2neo, not neomodel).
Always use `MERGE` not `CREATE` for all node/edge writes — idempotency is mandatory.

---

## Node Types

| Node | Key Properties |
|------|---------------|
| `Company` | nse_code, name, sector, industry, quality_score, conviction_score |
| `Industry` | name, sector, tam_crore, growth_rate_pct, entry_barrier, cyclicality |
| `Sector` | name, description, policy_sensitivity |
| `Theme` | name, govt_allocation_crore, theme_maturity, vikram_thesis |
| `Catalyst` | type, date, magnitude, ep_probability, conviction_delta |
| `Quarter` | period, revenue, pat, eps, beat_pct, yoy_growth |
| `Guidance` | revenue_growth_guided, margin_guided, confidence, concall_date |
| `OrderBook` | size_crore, revenue_coverage_ratio, mix, execution_months |
| `CapexPlan` | size_crore, completion_date, funded_by, capacity_addition_pct |
| `GovernmentScheme` | name, total_outlay_crore, period, disbursement_status |
| `ManagementPerson` | name, designation, tenure_years, track_record_score |
| `Risk` | type, severity, description, mitigant |

---

## Edge Types

### Structural (permanent)
```
(Company)  -[BELONGS_TO]->         (Industry)
(Industry) -[PART_OF]->            (Sector)
(Company)  -[COMPETES_WITH]->      (Company)   {overlap_pct}
(Company)  -[SUPPLIES_TO]->        (Company)   {revenue_share_pct}
(Company)  -[CUSTOMERS_INCLUDE]->  (Customer)  {concentration_pct}
(Person)   -[MANAGES]->            (Company)   {since, designation}
```

### Thematic (review quarterly)
```
(Company)  -[BENEFITS_FROM]->      (Theme)          {direct/indirect, magnitude}
(Company)  -[ELIGIBLE_FOR]->       (GovernmentScheme) {approval_status}
(Industry) -[DRIVEN_BY]->          (Theme)
```

### Fundamental / Live (updated on new information)
```
(Company)  -[REPORTED]->           (Quarter)
(Company)  -[HAS_ORDER_BOOK]->     (OrderBook)
(Company)  -[TRIGGERED]->          (Catalyst)
(Company)  -[GUIDED]->             (Guidance)
(Company)  -[EXPANDING_CAPACITY]-> (CapexPlan)
(Company)  -[RISK_EXPOSED_TO]->    (Risk)
```

---

## Conviction Score (0–100)

```
Business Quality Layer     max 35 pts
  ROE >25%                  +8
  ROCE >30%                 +8
  Order book >2x revenue   +10
  Zero pledge               +5
  Promoter >50%             +4

Earnings Quality Layer     max 20 pts
  Cash conversion >85%      +8
  Consistent beat history   +7
  Low working capital days  +5

Thematic Alignment Layer   max 20 pts
  Connected to 1+ live theme         +8
  Govt scheme eligible + approved   +7
  Industry tailwind (growth >15%)   +5

Catalyst Layer             max 25 pts (time-decayed 20%/quarter)
  OrderWin (Large)          +10
  EarningsBeat (>15%)       +8
  CapacityExpansion         +7
  GovtApproval              +8
  ManagementBuy             +5
```

Score interpretation:
- **80–100** → HIGH CONVICTION (size up, EP watch)
- **60–79**  → WATCH (wait for catalyst or better price)
- **<60**    → MONITOR (in universe, not active)

---

## EP Framework (Qullamaggie — NSE Adapted)

**Catalyst types**: OrderWin, EarningsBeat (>15% above estimate), CapacityExpansion,
GovtApproval, PLIInclusion, PromotorBuy, SectorPolicy

**EP preconditions**:
- Stock sideways 3–6+ months prior to catalyst
- Volume on catalyst day > 5x 20D avg
- Quality score > 7/10
- Order book > 2x revenue

**EP window**: 3–4 weeks post results season (Jan / Apr / Jul / Oct)

**Position sizing**: ₹15,000 fixed risk per trade, max 15% of capital per position.
Stop = lows of day (max 1–1.5x ATR).

---

## Sector Bias

Prefer: Capex / Infra / Power / Manufacturing / Defence / Railways / Cables

Avoid initiating: FMCG, IT Services (unless specific re-rating catalyst)

---

## Coding Rules (mandatory)

1. Always `MERGE` not `CREATE` — idempotency is non-negotiable
2. All `.cypher` query files go in `graph/queries/`
3. All loaders must be runnable standalone (`python loader.py`) AND importable as modules
4. Log every graph write: `[GRAPH] {action} | {node_type} | {identifier} | {count}`
5. Read credentials from `.env` via `python-dotenv` — never hardcode
6. Use `neo4j` Python driver v5.x
7. All financial figures in Indian notation (₹ Cr) in comments/logs
8. Type-hint all function signatures
9. One loader per node type — don't combine multiple node types in one file

---

## Analytical Persona — Vikram Iyer

When writing thesis text, node descriptions, or stock analysis:

- 30-year veteran fundamental analyst, India-specific
- Blunt and data-first — no fluff, no filler
- GARP orientation (Growth at Reasonable Price)
- Always anchors to order book visibility, capital allocation track record
- Flags governance issues immediately (pledge, related-party, auditor changes)
- Target format: "BUY / ACCUMULATE / HOLD / AVOID — [1-line reason] — [key number]"

---

## Project Status

- [ ] Phase 1: Schema + 962-stock universe loaded
- [ ] Phase 2: Fundamentals for tracked stocks (start with 5: WELCORP, STLTECH, AIIL, RPTECH, ROSSTECH)
- [ ] Phase 3: Theme nodes + BENEFITS_FROM edges
- [ ] Phase 4: BSE RSS catalyst pipeline
- [ ] Phase 5: Concall extractor (Claude API → structured nodes)
- [ ] Phase 6: Conviction score auto-computation
- [ ] Phase 7: React/Bloom visualization layer

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
