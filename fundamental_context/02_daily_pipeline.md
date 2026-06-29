> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Daily Pipeline — Update Architecture

## Overview

The pipeline runs nightly after market close (~5:00 PM IST).
Total runtime: ~7–10 minutes. Zero manual intervention for technical signals.
~15 min/week for reviewing auto-classified BSE catalysts.

```
Market Close (3:30 PM IST)
        │
        ▼ (~5:00 PM IST, via cron/scheduler)
daily_pipeline.py
        │
        ├── [1] bse_rss_parser.py         ← BSE corporate announcements
        ├── [2] update_fundamentals.py    ← quarterly/periodic fundamentals
        ├── [3] concall_extractor.py      ← manual trigger on concall days
        ├── [4] recompute_scores.py       ← conviction score refresh
        └── [5] flag_ep_candidates.py     ← EP watchlist output
        │
        ▼
    Neo4j DB  (updated same evening)
        │
        ▼
  Bloom Visual / React Dashboard
```

---

## What Updates — By Frequency

### Daily (fully automated)

| Source | What gets updated | Node/Edge created |
|--------|-------------------|-------------------|
| BSE Announcements RSS | Order wins, capex, M&A | `Catalyst` node + `TRIGGERED` edge |
| BSE Bulk Deals | Promoter buy/sell | Update `promoter_pct`, `Catalyst` if significant |
| Conviction score recompute | All 962 companies | Update `Company.conviction_score` |
| EP flag check | Stocks meeting all 4 EP criteria | EP watchlist log |

### Weekly (automated, Friday)

| Source | What gets updated |
|--------|-------------------|
| Peer comparison edges | Refresh `CHEAPER_THAN`, `HIGHER_ROCE_THAN` |
| Theme alignment check | Re-score `BENEFITS_FROM` edge weights |

### Quarterly (semi-automated — results season)

| Source | What gets updated | Manual effort |
|--------|-------------------|---------------|
| BSE results filings | `Quarter` nodes, beat/miss calc | Review auto-parsed EPS |
| Concall transcripts | `Guidance`, `OrderBook` snapshot | Paste transcript into extractor |
| Screener.in export | Bulk fundamentals refresh | Download CSV, run loader |
| Promoter shareholding | `promoter_pct`, `pledge_pct` | BSE shareholding file |

### One-time / On-demand

| Trigger | Action |
|---------|--------|
| New stock to track | Add fundamentals + theme edges manually |
| New govt policy announced | Create `GovernmentScheme` + `ELIGIBLE_FOR` edges |
| New supply chain identified | Add `SUPPLIES_TO` edge |
| Governance event | Create `Risk` node, apply conviction penalty |

---

## BSE Announcements Classification

```python
KEYWORD_MAP = {
    "OrderWin": [
        "order", "contract", "LoA", "Letter of Award",
        "purchase order", "work order", "awarded"
    ],
    "CapacityExpansion": [
        "capacity expansion", "greenfield", "brownfield",
        "new plant", "capex", "capital expenditure"
    ],
    "EarningsBeat": [
        "results", "quarterly results", "financial results"
        # Cross-check with estimate DB for beat classification
    ],
    "GovtApproval": [
        "approval", "PLI", "government", "ministry",
        "license", "clearance", "DPIIT"
    ],
    "PromotorBuy": [
        "acquisition of shares", "inter-se transfer",
        "promoter purchase", "creeping acquisition"
    ],
    "M&A": [
        "merger", "acquisition", "amalgamation",
        "takeover", "stake acquisition"
    ],
    "GovernanceFlag": [
        "investigation", "BSE query", "show cause",
        "SEBI notice", "auditor resignation", "qualified opinion"
    ]
}
```

**Magnitude classification** (from ₹ value extracted via regex):
- `Transformative`: > 50% of last annual revenue
- `Large`: 20–50% of revenue
- `Medium`: 5–20% of revenue
- `Small`: < 5% of revenue

---

## Concall Extraction Workflow

This is the highest-value manual workflow (~20 min/concall):

```
Step 1: Copy concall transcript text
Step 2: python etl/concall_extractor.py --company WELCORP --file transcript.txt
Step 3: Claude API (Vikram Iyer persona) extracts:
        - Revenue/margin guidance → Guidance node
        - Order book commentary → update HAS_ORDER_BOOK edge
        - Capex plans → CapexPlan node
        - Management confidence score (1–10)
        - Risk flags → Risk nodes
        - Key quotes (timestamped array)
Step 4: Review extracted JSON (30 sec scan)
Step 5: Confirm write → nodes created in Neo4j
Step 6: Conviction score auto-recalculates
```

**Vikram Iyer extraction prompt template:**
```
You are Vikram Iyer, a 30-year veteran fundamental analyst covering Indian equities.
Extract structured data from this {company} concall transcript.

Return ONLY valid JSON with these fields:
{
  "revenue_growth_guided_pct": number or null,
  "margin_guided_low": number or null,
  "margin_guided_high": number or null,
  "order_book_commentary": "string — specific numbers if mentioned",
  "order_inflow_guided_crore": number or null,
  "capex_plans": [{"size_crore": n, "purpose": "str", "timeline": "str"}],
  "management_confidence": 1-10 integer,
  "management_tone": "Cautious|Neutral|Confident|Bullish",
  "risk_flags": ["string list of specific risks mentioned"],
  "key_quotes": [{"quote": "str", "context": "str"}],
  "vikram_verdict": "BUY|ACCUMULATE|HOLD|AVOID — one line reason — key number"
}
```

---

## Conviction Score Recomputation

Runs nightly on all Company nodes with `updated_at` < today.

```python
def compute_conviction(company_data: dict, graph_context: dict) -> int:
    score = 0

    # Business Quality (max 35)
    if company_data["roe_3yr_avg"] > 25:       score += 8
    if company_data["roce_3yr_avg"] > 30:      score += 8
    if company_data["ob_to_revenue"] > 2:      score += 10
    if company_data["pledge_pct"] == 0:        score += 5
    if company_data["promoter_pct"] > 50:      score += 4

    # Earnings Quality (max 20)
    if company_data["cash_conversion"] > 0.85: score += 8
    if graph_context["beat_streak"] >= 3:      score += 7
    if company_data["wc_days"] < 90:           score += 5

    # Thematic Alignment (max 20)
    if graph_context["theme_count"] > 0:       score += 8
    if graph_context["scheme_approved"]:       score += 7
    if graph_context["industry_growth"] > 15:  score += 5

    # Catalyst Layer (max 25, time-decayed)
    for catalyst in graph_context["recent_catalysts"]:
        delta = catalyst["conviction_delta"]
        age_quarters = catalyst["age_quarters"]
        decayed = delta * (0.8 ** age_quarters)
        score += decayed

    # Negative adjustments
    if company_data["pledge_pct"] > 0:         score -= 10
    if graph_context["governance_flag"]:       score -= 20
    if company_data["ob_to_revenue"] < 1:      score -= 8
    if company_data["debt_to_equity"] > 1.5:   score -= 5

    return max(0, min(100, round(score)))
```

---

## EP Candidate Flag Logic

After conviction score refresh, runs EP screening:

```cypher
// Stocks ready for EP watchlist
MATCH (c:Company)-[:TRIGGERED]->(cat:Catalyst)
WHERE cat.date >= date() - duration('P30D')
  AND cat.ep_probability = 'High'
  AND c.conviction_score >= 70
  AND c.order_book_to_revenue_ratio >= 2
  AND c.quality_score >= 7
RETURN c.nse_code, c.name, c.conviction_score,
       cat.type, cat.magnitude, cat.date
ORDER BY c.conviction_score DESC
```

Output: written to `data/processed/ep_watchlist_YYYYMMDD.csv`

---

## Infrastructure

### Cron Schedule (Linux/Mac)

```bash
# Edit with: crontab -e
# Run pipeline weekdays at 5:00 PM IST (11:30 UTC)
30 11 * * 1-5 cd /path/to/nse-knowledge-graph && python etl/daily_pipeline.py --mode full >> logs/pipeline.log 2>&1
```

### Windows Task Scheduler

```
Program: python.exe
Arguments: C:\path\to\nse-knowledge-graph\etl\daily_pipeline.py --mode full
Start in: C:\path\to\nse-knowledge-graph
Trigger: Daily, 5:00 PM IST
```

### Manual Runs

```bash
python etl/daily_pipeline.py --mode full    # everything
python etl/daily_pipeline.py --mode bse     # only BSE parser
python etl/daily_pipeline.py --mode scores  # only conviction recompute
python etl/daily_pipeline.py --mode ep      # only EP flag check
```

---

## Error Handling & Monitoring

```python
# Every pipeline run logs to logs/pipeline_YYYYMMDD.log
# Format:
[17:02:01] INFO  | BSE Parser      | fetched 124 announcements
[17:02:03] INFO  | Classifier      | matched 8 to universe stocks
[17:02:03] GRAPH | Catalyst MERGE  | WELCORP OrderWin Large | created
[17:02:04] GRAPH | Catalyst MERGE  | RPTECH GovtApproval Med | updated (duplicate)
[17:02:15] INFO  | Score Refresh   | 962 companies updated
[17:02:16] INFO  | EP Screen       | 3 candidates flagged
[17:02:16] INFO  | Pipeline Done   | 75 seconds total
```

Send failure alerts via email or Telegram bot if pipeline exits non-zero.

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
