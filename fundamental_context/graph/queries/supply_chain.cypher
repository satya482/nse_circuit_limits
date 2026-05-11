// Supply Chain — upstream suppliers for a given company (2 hops)
// Parameter: $nse_code (string)
//
// Usage: run in Neo4j Browser with :param nse_code => "WELCORP"

// 1-hop: direct suppliers
MATCH (supplier:Company)-[r:SUPPLIES_TO]->(c:Company {nse_code: $nse_code})
RETURN
  1                      AS hop,
  supplier.nse_code      AS symbol,
  supplier.name          AS name,
  supplier.conviction_score AS conviction,
  r.product              AS product,
  r.revenue_share_pct    AS revenue_share_pct,
  c.nse_code             AS supplies_to

UNION

// 2-hop: suppliers of suppliers
MATCH (tier2:Company)-[r2:SUPPLIES_TO]->(mid:Company)-[:SUPPLIES_TO]->(c:Company {nse_code: $nse_code})
WHERE tier2.nse_code <> $nse_code
RETURN
  2                       AS hop,
  tier2.nse_code          AS symbol,
  tier2.name              AS name,
  tier2.conviction_score  AS conviction,
  r2.product              AS product,
  r2.revenue_share_pct    AS revenue_share_pct,
  mid.nse_code            AS supplies_to

ORDER BY hop ASC, conviction DESC
