// Theme Beneficiaries — all companies in a theme family
// Climbs SUBTHEME_OF hierarchy so querying "InfraCapex" returns
// companies tagged Railways, Roads, Ports, etc. as well.
// Parameter: $theme_name (string)
//
// Usage: run in Neo4j Browser with :param theme_name => "GovernmentCapex"

MATCH (target:Theme {name: $theme_name})

// Get the target theme AND all its descendants
OPTIONAL MATCH (descendant:Theme)-[:SUBTHEME_OF*1..]->(target)

WITH collect(target) + collect(descendant) AS theme_family

UNWIND theme_family AS t
MATCH (c:Company)-[r:BENEFITS_FROM]->(t)

RETURN DISTINCT
  c.nse_code           AS symbol,
  c.name               AS name,
  c.conviction_score   AS conviction,
  c.quality_score      AS quality,
  t.name               AS via_theme,
  r.direct             AS direct_beneficiary

ORDER BY conviction DESC
