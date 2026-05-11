# Cypher Query Library

Reference queries for the NSE Knowledge Graph.
Run in Neo4j Browser (http://localhost:7474) or via Python driver.

---

## Diagnostics

```cypher
-- Node counts by type
MATCH (n) RETURN labels(n) AS type, count(n) AS count ORDER BY count DESC;

-- Relationship counts by type
MATCH ()-[r]->() RETURN type(r) AS relationship, count(r) AS count ORDER BY count DESC;

-- Companies missing fundamentals
MATCH (c:Company)
WHERE c.roe_3yr_avg IS NULL
RETURN c.nse_code, c.name, c.sector_name
ORDER BY c.name;

-- Schema constraints
SHOW CONSTRAINTS;
```

---

## Conviction & Quality Screening

```cypher
-- Top 20 by conviction score
MATCH (c:Company)
WHERE c.conviction_score IS NOT NULL
RETURN c.nse_code, c.name, c.sector_name,
       c.conviction_score, c.quality_score,
       c.order_book_to_revenue_ratio
ORDER BY c.conviction_score DESC
LIMIT 20;

-- HIGH CONVICTION stocks (score > 80)
MATCH (c:Company)
WHERE c.conviction_score > 80
RETURN c.nse_code, c.name, c.conviction_score,
       c.roe_3yr_avg, c.roce_3yr_avg, c.order_book_to_revenue_ratio
ORDER BY c.conviction_score DESC;

-- Quality filter pass (all 5 criteria)
MATCH (c:Company)
WHERE c.roe_3yr_avg > 25
  AND c.roce_3yr_avg > 30
  AND c.promoter_pct > 50
  AND c.pledge_pct = 0
  AND c.order_book_to_revenue_ratio > 2
RETURN c.nse_code, c.name, c.quality_score, c.conviction_score
ORDER BY c.quality_score DESC;
```

---

## EP Screener

```cypher
-- EP candidates: OrderWin in last 30 days + high conviction
MATCH (c:Company)-[:TRIGGERED]->(cat:Catalyst)
WHERE cat.type = 'OrderWin'
  AND cat.date >= date() - duration('P30D')
  AND c.conviction_score >= 70
  AND c.order_book_to_revenue_ratio >= 2
  AND c.quality_score >= 7
RETURN c.nse_code, c.name, c.conviction_score,
       cat.magnitude, cat.ep_probability, cat.date
ORDER BY c.conviction_score DESC;

-- All catalysts in last 7 days
MATCH (c:Company)-[:TRIGGERED]->(cat:Catalyst)
WHERE cat.date >= date() - duration('P7D')
RETURN c.nse_code, c.name, cat.type, cat.magnitude,
       cat.ep_probability, cat.date
ORDER BY cat.date DESC;

-- High EP probability catalysts (any time)
MATCH (c:Company)-[:TRIGGERED]->(cat:Catalyst {ep_probability: 'High'})
RETURN c.nse_code, c.name, c.conviction_score,
       cat.type, cat.magnitude, cat.date
ORDER BY cat.date DESC
LIMIT 20;
```

---

## Theme & Sector Analysis

```cypher
-- Companies in a theme, by conviction (parameterised)
MATCH (c:Company)-[:BENEFITS_FROM]->(t:Theme {name: $theme_name})
RETURN c.nse_code, c.name, c.conviction_score, c.quality_score
ORDER BY c.conviction_score DESC;

-- All themes and their beneficiary count
MATCH (t:Theme)<-[:BENEFITS_FROM]-(c:Company)
RETURN t.name, count(c) AS company_count, t.theme_maturity
ORDER BY company_count DESC;

-- Multi-theme companies (strong thematic alignment)
MATCH (c:Company)-[:BENEFITS_FROM]->(t:Theme)
WITH c, count(t) AS theme_count, collect(t.name) AS themes
WHERE theme_count >= 2
RETURN c.nse_code, c.name, theme_count, themes, c.conviction_score
ORDER BY theme_count DESC, c.conviction_score DESC;

-- Sector summary: avg conviction + quality
MATCH (c:Company)
WHERE c.conviction_score IS NOT NULL
RETURN c.sector_name,
       count(c) AS company_count,
       round(avg(c.conviction_score), 1) AS avg_conviction,
       round(avg(c.quality_score), 1) AS avg_quality
ORDER BY avg_conviction DESC;
```

---

## Supply Chain Traversal

```cypher
-- Who supplies TO a given company (1 hop)
MATCH (supplier:Company)-[r:SUPPLIES_TO]->(c:Company {nse_code: $nse_code})
RETURN supplier.nse_code, supplier.name, r.product, r.revenue_share_pct;

-- Full upstream supply chain (2 hops)
MATCH path = (upstream:Company)-[:SUPPLIES_TO*1..2]->(c:Company {nse_code: $nse_code})
RETURN path;

-- Who does a company supply TO (downstream customers)
MATCH (c:Company {nse_code: $nse_code})-[r:SUPPLIES_TO]->(customer:Company)
RETURN customer.nse_code, customer.name, r.revenue_share_pct
ORDER BY r.revenue_share_pct DESC;

-- Full supply chain for InfraCapex theme
MATCH (c:Company)-[:BENEFITS_FROM]->(t:Theme {name:'InfraCapex'})
OPTIONAL MATCH (c)-[:SUPPLIES_TO]->(downstream:Company)
RETURN c.nse_code, c.name, collect(downstream.nse_code) AS supplies_to
ORDER BY c.conviction_score DESC;
```

---

## Peer Comparison

```cypher
-- Competitors of a company
MATCH (c:Company {nse_code: $nse_code})-[:COMPETES_WITH]->(peer:Company)
RETURN peer.nse_code, peer.name,
       peer.pe_current, peer.ev_ebitda_current,
       peer.roce_3yr_avg, peer.conviction_score
ORDER BY peer.ev_ebitda_current;

-- Cheaper peers with similar ROCE
MATCH (c:Company {nse_code: $nse_code})-[:COMPETES_WITH]->(peer:Company)
WHERE peer.ev_ebitda_current < c.ev_ebitda_current
  AND peer.roce_3yr_avg > c.roce_3yr_avg * 0.85
RETURN peer.nse_code, peer.name,
       peer.ev_ebitda_current AS peer_evebitda, c.ev_ebitda_current AS my_evebitda,
       peer.roce_3yr_avg AS peer_roce, c.roce_3yr_avg AS my_roce;
```

---

## Management & Governance

```cypher
-- Stocks with governance flags
MATCH (c:Company)-[:RISK_EXPOSED_TO]->(r:Risk)
WHERE r.type = 'Governance' OR r.severity = 'Critical'
RETURN c.nse_code, c.name, r.type, r.severity, r.description;

-- High pledge stocks (filter out of EP candidates)
MATCH (c:Company)
WHERE c.pledge_pct > 0
RETURN c.nse_code, c.name, c.pledge_pct, c.promoter_pct
ORDER BY c.pledge_pct DESC;

-- Management tenure (experienced teams)
MATCH (p:ManagementPerson {designation:'MD'})-[:MANAGES]->(c:Company)
WHERE p.tenure_years > 10
RETURN p.name, c.nse_code, c.name, p.tenure_years, p.track_record_score
ORDER BY p.track_record_score DESC;
```

---

## Order Book Analysis

```cypher
-- Latest order book snapshot for a company
MATCH (c:Company {nse_code: $nse_code})-[:HAS_ORDER_BOOK]->(ob:OrderBook)
RETURN ob.date, ob.size_crore, ob.revenue_coverage_ratio,
       ob.govt_client_pct, ob.execution_months
ORDER BY ob.date DESC
LIMIT 1;

-- Order book trend (all snapshots)
MATCH (c:Company {nse_code: $nse_code})-[:HAS_ORDER_BOOK]->(ob:OrderBook)
RETURN ob.date, ob.size_crore, ob.revenue_coverage_ratio
ORDER BY ob.date;

-- Companies with order book > 3x revenue (very strong visibility)
MATCH (c:Company)
WHERE c.order_book_to_revenue_ratio > 3
  AND c.quality_score >= 7
RETURN c.nse_code, c.name, c.order_book_to_revenue_ratio,
       c.order_book_crore, c.conviction_score
ORDER BY c.order_book_to_revenue_ratio DESC;
```

---

## Guidance & Quarterly Results

```cypher
-- Latest guidance for a company
MATCH (c:Company {nse_code: $nse_code})-[:GUIDED]->(g:Guidance)
RETURN g.concall_date, g.revenue_growth_guided_pct,
       g.margin_guided_low, g.margin_guided_high,
       g.management_confidence, g.management_tone,
       g.vikram_verdict
ORDER BY g.concall_date DESC
LIMIT 1;

-- Companies that guided >20% revenue growth with high management confidence
MATCH (c:Company)-[:GUIDED]->(g:Guidance)
WHERE g.revenue_growth_guided_pct > 20
  AND g.management_confidence >= 8
RETURN c.nse_code, c.name, g.revenue_growth_guided_pct,
       g.management_confidence, g.management_tone, g.concall_date
ORDER BY g.revenue_growth_guided_pct DESC;

-- Last 4 quarters for a company
MATCH (c:Company {nse_code: $nse_code})-[:REPORTED]->(q:Quarter)
RETURN q.period, q.revenue_crore, q.pat_crore,
       q.ebitda_margin_pct, q.beat_pct, q.yoy_revenue_growth
ORDER BY q.period DESC
LIMIT 4;
```

---

## Dot-Connecting Queries

```cypher
-- "Government announces big railway budget — who benefits?"
MATCH (c:Company)-[:BENEFITS_FROM]->(t:Theme {name:'Railways'})
WHERE c.quality_score >= 6
OPTIONAL MATCH (c)-[:TRIGGERED]->(cat:Catalyst)
WHERE cat.date >= date() - duration('P90D')
RETURN c.nse_code, c.name, c.conviction_score,
       c.order_book_to_revenue_ratio,
       collect(cat.type) AS recent_catalysts
ORDER BY c.conviction_score DESC;

-- "OrderWin announced — who else in the same theme might follow?"
MATCH (c:Company {nse_code: $nse_code})-[:BENEFITS_FROM]->(t:Theme)<-[:BENEFITS_FROM]-(peer:Company)
WHERE peer.nse_code <> $nse_code
  AND peer.quality_score >= 6
RETURN t.name, peer.nse_code, peer.name, peer.conviction_score
ORDER BY peer.conviction_score DESC;

-- "New capex plan filed — does execution capacity exist?"
MATCH (c:Company {nse_code: $nse_code})
RETURN c.capacity_utilisation_pct,
       c.order_book_execution_months,
       c.capex_completion_date,
       CASE WHEN c.capacity_utilisation_pct < 80 THEN 'HEADROOM EXISTS'
            WHEN c.capacity_utilisation_pct < 90 THEN 'LIMITED HEADROOM'
            ELSE 'AT CAPACITY - WATCH EXECUTION' END AS capacity_verdict;
```
