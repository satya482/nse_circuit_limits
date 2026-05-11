// EP Screener — Episodic Pivot candidates
// Climbs SUBTHEME_OF hierarchy so a company tagged Railways also passes
// the InfraCapex / GovernmentCapex theme-alignment check.
//
// Usage: run in Neo4j Browser or via Python driver (no parameters)

MATCH (c:Company)-[:TRIGGERED]->(cat:Catalyst)
WHERE cat.date >= date() - duration('P30D')
  AND c.conviction_score >= 70
  AND c.order_book_to_revenue_ratio >= 2
  AND c.quality_score >= 7

// Theme alignment: direct or via any ancestor theme
MATCH (c)-[:BENEFITS_FROM]->(t:Theme)
OPTIONAL MATCH (t)-[:SUBTHEME_OF*1..]->(ancestor:Theme)

RETURN DISTINCT
  c.nse_code               AS symbol,
  c.name                   AS name,
  c.conviction_score       AS conviction,
  c.quality_score          AS quality,
  c.order_book_to_revenue_ratio AS ob_ratio,
  cat.type                 AS catalyst_type,
  cat.date                 AS catalyst_date,
  cat.ep_probability       AS ep_prob,
  t.name                   AS theme

ORDER BY c.conviction_score DESC
