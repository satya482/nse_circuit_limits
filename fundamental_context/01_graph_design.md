# Graph Design — Node & Edge Schema

## Design Philosophy

This is a **fundamentals-first** knowledge graph. Unlike dashboards that track
price and technical signals, this graph stores *why* a business deserves conviction
and *what new information* confirms or breaks that thesis.

The graph answers questions flat databases cannot:
- Which stocks benefit if NTPC doubles its capex? (multi-hop supply chain)
- Which competitors of WELCORP are cheaper on EV/EBITDA but similar ROCE?
- Which stocks had an OrderWin catalyst AND high quality score in the last 30 days?
- When the defence budget increases, which companies light up across all supply chain layers?

---

## Node Types

### `Company`

```
Core Identity
├── nse_code                    (primary key — NSE ticker)
├── isin
├── name
├── sector_name
├── industry_name
├── business_description        (2-3 lines, Vikram Iyer style)
└── listing_date

Quality Scorecard
├── roe_3yr_avg                 threshold: >25%
├── roce_3yr_avg                threshold: >30%
├── promoter_pct                threshold: >50%
├── pledge_pct                  threshold: = 0
├── debt_to_equity
└── quality_score               (0–10 composite)

Order Book
├── order_book_crore
├── order_book_to_revenue_ratio threshold: >2x
├── order_book_updated_date
└── order_book_execution_months

Financial Snapshot
├── revenue_ttm
├── pat_ttm
├── ebitda_margin_ttm
├── revenue_cagr_3yr
├── pat_cagr_3yr
└── cash_conversion_ratio       (CFO / PAT)

Capacity & Capex
├── current_capacity
├── expanded_capacity
├── capex_announced_crore
├── capex_completion_date
└── capacity_utilisation_pct

Valuation
├── pe_current
├── pe_5yr_avg
├── ev_ebitda_current
├── mcap_to_sales
└── dcf_fair_value

Scoring
├── conviction_score            (0–100, auto-computed)
├── quality_score               (0–10, from quality filters)
└── updated_at
```

---

### `Industry`

```
├── name
├── sector
├── tam_crore                   (total addressable market)
├── industry_growth_rate_pct
├── entry_barrier               (High / Medium / Low)
├── pricing_power               (High / Medium / Low)
├── cyclicality                 (Cyclical / Defensive / Secular)
├── import_dependence_pct
├── export_opportunity_pct
└── government_policy_sensitivity (High / Medium / Low)
```

---

### `Sector`

```
├── name
├── description
├── policy_sensitivity          (High / Medium / Low)
└── budget_allocation_crore     (annual govt spend, if applicable)
```

---

### `Theme`

Cross-sector macro themes that link companies with structural tailwinds.

```
├── name                        e.g. "PLI_Electronics", "InfraCapex", "Defence"
├── government_allocation_crore
├── policy_document_ref
├── expected_beneficiary_count
├── theme_maturity              (Emerging / Growing / Mature)
└── vikram_thesis               (2-3 line fundamental narrative)
```

**Current themes to seed:**
InfraCapex, Defence, PLI_Electronics, PLI_Chemicals, DataCentre,
Railways, PowerT&D, China+1_Textiles, EV_Components, RenewableEnergy,
Semiconductor, SpecialtyChemicals, Hospitals_HealthcareInfra

---

### `Catalyst`

The live pulse of the graph. Created whenever new fundamental information arrives.

```
├── catalyst_id                 (nse_code + type + date, hashed)
├── type                        (see Catalyst Types below)
├── date
├── magnitude                   (Small / Medium / Large / Transformative)
├── description
├── source                      (BSE filing / Concall / News / Screener)
├── ep_probability              (Low / Medium / High)
└── conviction_delta            (numeric — how much this moves conviction ±)
```

**Catalyst Types:**
| Type | EP Signal | Typical conviction_delta |
|------|-----------|--------------------------|
| `OrderWin` | High | +8 to +10 |
| `EarningsBeat` | High | +6 to +8 |
| `CapacityExpansion` | Medium | +5 to +7 |
| `GovtApproval` | Medium-High | +6 to +8 |
| `PLIInclusion` | Medium | +5 |
| `PromotorBuy` | Medium | +4 to +5 |
| `ManagementGuidanceRaise` | High | +5 to +7 |
| `SectorPolicy` | Medium | +3 to +5 |
| `M&A` | Situational | ±varies |
| `GovernanceFlag` | Negative | -10 to -20 |

---

### `Quarter`

```
├── quarter_id                  (e.g. "WELCORP_Q4FY25")
├── period                      (e.g. "Q4FY25")
├── revenue_crore
├── pat_crore
├── eps
├── ebitda_margin_pct
├── beat_pct                    (vs consensus estimate)
├── yoy_revenue_growth
├── yoy_pat_growth
└── announcement_date
```

---

### `Guidance`

Created from concall transcript extraction.

```
├── guidance_id                 (nse_code + concall_date)
├── concall_date
├── revenue_growth_guided_pct
├── margin_guided_band          (e.g. "18-19%")
├── order_inflow_guided_crore
├── confidence                  (1–10, Vikram Iyer assessment)
├── management_tone             (Cautious / Neutral / Confident / Bullish)
└── key_quotes[]                (timestamped array)
```

---

### `OrderBook`

Snapshot node — created each time order book is updated.

```
├── orderbook_id                (nse_code + date)
├── date
├── size_crore
├── revenue_coverage_ratio      (order book / annualised revenue)
├── domestic_pct
├── export_pct
├── govt_client_pct
├── private_client_pct
└── execution_months            (expected delivery timeline)
```

---

### `CapexPlan`

```
├── capex_id
├── announcement_date
├── size_crore
├── purpose                     (Greenfield / Brownfield / Acquisition)
├── capacity_addition_pct
├── completion_date
├── funded_by                   (Internal / Debt / Equity / Mixed)
└── status                      (Announced / Approved / Under Construction / Complete)
```

---

### `GovernmentScheme`

```
├── name                        (e.g. "PLI Scheme - Electronics")
├── total_outlay_crore
├── period                      (e.g. "FY23-FY28")
├── beneficiary_sectors[]
├── disbursement_status         (Announced / Active / Disbursing / Closed)
└── nodal_ministry
```

---

### `ManagementPerson`

```
├── person_id                   (name + company hash)
├── name
├── designation
├── tenure_years
├── track_record_score          (1–10, capital allocation history)
└── public_statements[]         (key concall quotes, timestamped)
```

---

### `Risk`

```
├── risk_id
├── type                        (Execution / Regulatory / ClientConcentration /
│                                RawMaterial / Governance / Macro / Competition)
├── severity                    (Low / Medium / High / Critical)
├── description
└── mitigant                    (what management/structure protects against this)
```

---

## Edge Types

### Structural Edges (permanent, built once)

```cypher
(Company)  -[BELONGS_TO]->          (Industry)
(Industry) -[PART_OF]->             (Sector)
(Company)  -[COMPETES_WITH]->       (Company)   // {overlap_pct, basis}
(Company)  -[SUPPLIES_TO]->         (Company)   // {revenue_share_pct, product}
(Company)  -[CUSTOMERS_INCLUDE]->   (Customer)  // {concentration_pct, type}
(Company)  -[RAW_MATERIAL_FROM]->   (Supplier)  // {criticality: High/Med/Low}
(Person)   -[MANAGES]->             (Company)   // {since, designation}
(Company)  -[PART_OF_GROUP]->       (PromoterGroup)
```

### Thematic Edges (review quarterly)

```cypher
(Company)  -[BENEFITS_FROM]->       (Theme)           // {direct/indirect, magnitude}
(Company)  -[ELIGIBLE_FOR]->        (GovernmentScheme) // {approval_status}
(Industry) -[DRIVEN_BY]->           (Theme)
```

### Fundamental / Live Edges (created on new information)

```cypher
(Company)  -[REPORTED]->            (Quarter)
(Company)  -[HAS_ORDER_BOOK]->      (OrderBook)
(Company)  -[TRIGGERED]->           (Catalyst)
(Company)  -[GUIDED]->              (Guidance)
(Company)  -[EXPANDING_CAPACITY]->  (CapexPlan)
(Company)  -[RISK_EXPOSED_TO]->     (Risk)
```

### Computed Edges (weekly refresh)

```cypher
(Company)  -[CO_MOVES_WITH]->       (Company)   // {correlation, period}
(Company)  -[CHEAPER_THAN]->        (Company)   // {metric, discount_pct}
(Company)  -[HIGHER_ROCE_THAN]->    (Company)   // {delta_pct}
```

---

## Key Supply Chain Chains (seed manually)

```
Iron Ore → Sponge Iron → Steel → Pipes/Tubes → Oil & Gas / Infra / Water
Coal → Power Generation → T&D Equipment → Industrial Capex
Silicon → Wafers → Chips → EMS → Consumer Electronics
Copper → Cables & Wires → Power Infra / Telecom
Cement + Steel → Construction → Real Estate / Roads
Defence Components → Sub-systems → Prime Contractors (DRDO/DPSUs)
```

---

## Conviction Score Computation

```
Score = BusinessQuality + EarningsQuality + ThematicAlignment + CatalystLayer

BusinessQuality (max 35):
  roe_3yr_avg > 25%           → +8
  roce_3yr_avg > 30%          → +8
  order_book_to_revenue > 2x  → +10
  pledge_pct == 0             → +5
  promoter_pct > 50%          → +4

EarningsQuality (max 20):
  cash_conversion > 85%       → +8
  beat_3_of_last_4_quarters   → +7
  working_capital_days < 90   → +5

ThematicAlignment (max 20):
  BENEFITS_FROM any Theme     → +8
  ELIGIBLE_FOR approved scheme → +7
  industry_growth_rate > 15%  → +5

CatalystLayer (max 25, decays 20%/quarter):
  OrderWin (Large)            → +10
  EarningsBeat (>15%)         → +8
  CapacityExpansion           → +7
  GovtApproval                → +8
  ManagementBuy               → +5
```

**Negative adjustments:**
- Pledge > 0%: −10
- Governance flag (BSE investigation, auditor change): −20
- Order book < 1x revenue: −8
- D/E > 1.5: −5

---

## Dot-Connecting: How New Information Propagates

When a `Catalyst` node is created, the graph automatically checks:

1. **Order book impact** — does this materially change HAS_ORDER_BOOK ratio?
2. **Theme confirmation** — does it strengthen a BENEFITS_FROM edge?
3. **Peer signal** — do COMPETES_WITH peers merit a look too?
4. **Supply chain ripple** — does it benefit SUPPLIES_TO upstream companies?
5. **EP conditions** — are all 4 EP preconditions now met?

This propagation is the core analytical value of the graph.
