// ============================================================
// NSE Knowledge Graph — Neo4j Schema Constraints & Indexes
// Run once on fresh database before any data loading
// Neo4j 5.x Community Edition compatible
// ============================================================


// ─── UNIQUENESS CONSTRAINTS ──────────────────────────────────
// Prevents duplicate nodes and enables fast MERGE operations

CREATE CONSTRAINT company_nse_code IF NOT EXISTS
FOR (c:Company) REQUIRE c.nse_code IS UNIQUE;

CREATE CONSTRAINT company_isin IF NOT EXISTS
FOR (c:Company) REQUIRE c.isin IS UNIQUE;

CREATE CONSTRAINT industry_name IF NOT EXISTS
FOR (i:Industry) REQUIRE i.name IS UNIQUE;

CREATE CONSTRAINT sector_name IF NOT EXISTS
FOR (s:Sector) REQUIRE s.name IS UNIQUE;

CREATE CONSTRAINT theme_name IF NOT EXISTS
FOR (t:Theme) REQUIRE t.name IS UNIQUE;

CREATE CONSTRAINT govt_scheme_name IF NOT EXISTS
FOR (g:GovernmentScheme) REQUIRE g.name IS UNIQUE;

CREATE CONSTRAINT risk_id IF NOT EXISTS
FOR (r:Risk) REQUIRE r.risk_id IS UNIQUE;

// Catalyst: unique per company + type + date (composite via id)
CREATE CONSTRAINT catalyst_id IF NOT EXISTS
FOR (c:Catalyst) REQUIRE c.catalyst_id IS UNIQUE;

// Quarter: unique per company + period (e.g. "WELCORP_Q4FY25")
CREATE CONSTRAINT quarter_id IF NOT EXISTS
FOR (q:Quarter) REQUIRE q.quarter_id IS UNIQUE;

// Guidance: unique per company + concall date
CREATE CONSTRAINT guidance_id IF NOT EXISTS
FOR (g:Guidance) REQUIRE g.guidance_id IS UNIQUE;

// OrderBook snapshot: unique per company + date
CREATE CONSTRAINT orderbook_id IF NOT EXISTS
FOR (o:OrderBook) REQUIRE o.orderbook_id IS UNIQUE;

// CapexPlan: unique per company + announcement date
CREATE CONSTRAINT capex_id IF NOT EXISTS
FOR (c:CapexPlan) REQUIRE c.capex_id IS UNIQUE;

// ManagementPerson: unique per name + company (via composite id)
CREATE CONSTRAINT person_id IF NOT EXISTS
FOR (p:ManagementPerson) REQUIRE p.person_id IS UNIQUE;


// ─── LOOKUP INDEXES ──────────────────────────────────────────
// Speed up frequent property lookups

CREATE INDEX company_name IF NOT EXISTS
FOR (c:Company) ON (c.name);

CREATE INDEX company_sector IF NOT EXISTS
FOR (c:Company) ON (c.sector_name);

CREATE INDEX company_conviction IF NOT EXISTS
FOR (c:Company) ON (c.conviction_score);

CREATE INDEX company_quality IF NOT EXISTS
FOR (c:Company) ON (c.quality_score);

CREATE INDEX catalyst_type IF NOT EXISTS
FOR (c:Catalyst) ON (c.type);

CREATE INDEX catalyst_date IF NOT EXISTS
FOR (c:Catalyst) ON (c.date);

CREATE INDEX catalyst_ep_prob IF NOT EXISTS
FOR (c:Catalyst) ON (c.ep_probability);

CREATE INDEX quarter_period IF NOT EXISTS
FOR (q:Quarter) ON (q.period);

CREATE INDEX theme_maturity IF NOT EXISTS
FOR (t:Theme) ON (t.theme_maturity);


// ─── FULL-TEXT INDEXES ───────────────────────────────────────
// Enable text search across analysis/thesis fields

CREATE FULLTEXT INDEX company_search IF NOT EXISTS
FOR (c:Company) ON EACH [c.name, c.nse_code, c.business_description];

CREATE FULLTEXT INDEX theme_search IF NOT EXISTS
FOR (t:Theme) ON EACH [t.name, t.vikram_thesis];

CREATE FULLTEXT INDEX catalyst_search IF NOT EXISTS
FOR (c:Catalyst) ON EACH [c.description, c.source];


// ─── VERIFY ──────────────────────────────────────────────────
// Run after applying constraints to confirm setup

SHOW CONSTRAINTS;
SHOW INDEXES;
