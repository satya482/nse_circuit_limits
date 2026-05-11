# Setup Guide — VS Code + Claude Code + Neo4j

## Prerequisites Checklist

```
[ ] VS Code 1.98.0 or newer
[ ] Claude Pro / Max / Team subscription (claude.ai)
[ ] Docker Desktop (for Neo4j) OR Neo4j Desktop
[ ] Python 3.10+
[ ] Git
```

---

## Step 1 — Install Claude Code Extension

Open VS Code → Extensions (`Ctrl+Shift+X` / `Cmd+Shift+X`)  
Search: **Claude Code**  
Install: the one by **Anthropic** (verified publisher, 2M+ installs)

After install:
- A **Spark icon** (⚡) appears in the VS Code sidebar
- Click it to open the Claude Code panel
- Sign in with your Anthropic account (same as claude.ai)

If Spark icon doesn't appear: `Ctrl+Shift+P` → "Developer: Reload Window"

### Three Modes — Know When to Use Each

| Mode | When to use |
|------|-------------|
| **Plan mode** | Schema changes, adding new node types, large refactors. Claude writes a Markdown plan — you annotate it — then it executes |
| **Normal mode** | Day-to-day. Claude asks before each file edit, shows diff. Default |
| **Auto-accept** | Mechanical bulk ops only (loading 962 stocks from CSV) |

### Key Shortcuts

| Action | Shortcut |
|--------|----------|
| Open Claude panel | Click ⚡ in sidebar |
| New conversation | `Ctrl+N` / `Cmd+N` |
| @-mention a file | Type `@filename` in prompt |
| Reference selected lines | Select code → `Alt+K` / `Option+K` |
| Rewind to checkpoint | `/rewind` in chat, or press `Esc` twice |

---

## Step 2 — Neo4j Setup (Docker — Recommended)

```bash
# Pull and run Neo4j Community Edition (free)
docker run \
  --name nse-knowledge-graph \
  -p 7474:7474 \
  -p 7687:7687 \
  -v $HOME/neo4j/data:/data \
  -v $HOME/neo4j/logs:/logs \
  -e NEO4J_AUTH=neo4j/yourpassword123 \
  --restart unless-stopped \
  neo4j:5.18-community

# Verify it's running
docker ps | grep neo4j
```

**Browser UI**: http://localhost:7474  
**Username**: neo4j | **Password**: yourpassword123  
**Bolt URL**: bolt://localhost:7687 (Python connects here)

**Stop/start:**
```bash
docker stop nse-knowledge-graph
docker start nse-knowledge-graph
```

### Alternative: Neo4j Desktop (no Docker)
Download from https://neo4j.com/download/ — GUI installer, free.
Create a new project → Add Database → Local DBMS → Start.

---

## Step 3 — Python Environment

```bash
# In your project folder
cd nse-knowledge-graph

# Create virtual environment
python -m venv .venv

# Activate
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows

# Install dependencies
pip install neo4j python-dotenv anthropic requests feedparser pandas
```

### `.env` file (create in project root, never commit to git)

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=yourpassword123
ANTHROPIC_API_KEY=sk-ant-...
```

### `.claudeignore` (create in project root)

```
.env
.venv/
__pycache__/
*.pyc
data/raw/*.csv
logs/
.git/
node_modules/
```

---

## Step 4 — Load Schema

Open Neo4j browser at http://localhost:7474  
Copy contents of `graph/schema/constraints.cypher`  
Paste into the query box and run.

Or from Python:
```bash
python -c "
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
load_dotenv()
driver = GraphDatabase.driver(os.getenv('NEO4J_URI'),
    auth=(os.getenv('NEO4J_USER'), os.getenv('NEO4J_PASSWORD')))
with open('graph/schema/constraints.cypher') as f:
    queries = [q.strip() for q in f.read().split(';') if q.strip()]
with driver.session() as session:
    for q in queries:
        if q and not q.startswith('//'):
            session.run(q)
            print(f'OK: {q[:60]}...')
driver.close()
"
```

---

## Step 5 — Open Project in VS Code

```bash
code nse-knowledge-graph
```

Claude Code automatically reads `CLAUDE.md` from the workspace root at the start
of every session. This gives it full context about:
- Your stock universe and quality filters
- Node/edge schema
- Coding rules (MERGE not CREATE, etc.)
- Vikram Iyer persona for analysis text

**First thing to say in Claude Code panel:**
```
Read CLAUDE.md and confirm you understand the project.
Then list what's in data/raw/ and graph/schema/.
```

---

## Step 6 — First Claude Code Sessions

Run these sequentially. Each session builds on the previous.

### Session 1 — Universe Load (~45 min)

**Prompt:**
```
Read CLAUDE.md and data/raw/NSE_500cr_universe.csv (first 10 rows to understand structure).

Create graph/loaders/load_universe.py that:
1. Reads all 962 rows from the CSV
2. Creates Company nodes (MERGE on nse_code)
3. Creates Industry nodes (MERGE on name)
4. Creates Sector nodes (MERGE on sector_name)
5. Creates BELONGS_TO edges (Company → Industry)
6. Creates PART_OF edges (Industry → Sector)
7. Prints summary: X companies, Y industries, Z sectors created/updated

Use neo4j driver v5.x, read credentials from .env.
Follow all coding rules in CLAUDE.md.
```

**Expected output:**
```
[GRAPH] Company MERGE | WELCORP | created
...
[GRAPH] Summary | 962 companies | 119 industries | 29 sectors
```

---

### Session 2 — Fundamentals Loader (~60 min)

**Prompt:**
```
Read CLAUDE.md and graph/loaders/load_universe.py (to understand pattern).

Create graph/loaders/load_fundamentals.py that:
- Accepts a dict with: nse_code, roe_3yr_avg, roce_3yr_avg, promoter_pct,
  pledge_pct, order_book_crore, revenue_ttm, pat_ttm, ebitda_margin_ttm,
  revenue_cagr_3yr, pat_cagr_3yr, cash_conversion_ratio, pe_current,
  ev_ebitda_current, debt_to_equity, capacity_utilisation_pct
- MERGEs into existing Company node
- Computes order_book_to_revenue_ratio = order_book_crore / (revenue_ttm/4 * 4)
- Computes quality_score (0–10) based on thresholds in CLAUDE.md
- Computes initial conviction_score using Business Quality layer only

Then seed these 5 companies with realistic estimated data:
WELCORP, STLTECH, AIIL, RPTECH, ROSSTECH
(use reasonable estimates — flag them as estimated=True)
```

---

### Session 3 — Themes + EP Screener (~45 min)

**Prompt:**
```
Read CLAUDE.md.

1. Create graph/loaders/load_themes.py that creates all Theme nodes listed
   in CLAUDE.md and appropriate BENEFITS_FROM edges for our 5 seeded companies.

2. Create graph/queries/ep_screener.cypher — query returning companies where:
   - order_book_to_revenue_ratio > 2
   - quality_score > 7
   - Has a Catalyst node created in last 30 days
   - conviction_score > 60
   Ordered by conviction_score DESC

3. Create graph/queries/supply_chain.cypher — query showing all companies
   that SUPPLIES_TO a given company (parameterised: $nse_code), 2 hops deep.

4. Create graph/queries/theme_beneficiaries.cypher — given a Theme name,
   return all Company nodes with BENEFITS_FROM edge, sorted by conviction_score.
```

---

### Session 4 — BSE RSS Pipeline (~90 min)

**Prompt:**
```
Read CLAUDE.md and etl/ folder structure.

Build etl/bse_rss_parser.py that:
1. Fetches BSE corporate announcements (use feedparser on BSE RSS or
   requests on https://www.bseindia.com/corporates/ann.html)
2. Classifies each into Catalyst types using keyword mapping in docs/02_daily_pipeline.md
3. Extracts ₹ value if present → determines magnitude (Small/Med/Large/Transformative)
4. For matched companies (check nse_code against universe), creates Catalyst node
   with TRIGGERED edge using MERGE (idempotent — same announcement = no duplicate)
5. Sets ep_probability: High if OrderWin+Large or EarningsBeat, Medium otherwise

Wire into etl/daily_pipeline.py with:
  python daily_pipeline.py --mode full
  python daily_pipeline.py --mode bse
  python daily_pipeline.py --mode scores
```

---

### Session 5 — Concall Extractor (~60 min)

**Prompt:**
```
Read CLAUDE.md. Focus on the Vikram Iyer persona and Guidance/OrderBook node schemas
in docs/01_graph_design.md.

Build etl/concall_extractor.py that:
1. Accepts --company NSE_CODE --file transcript.txt
2. Calls Claude API (claude-sonnet-4-20250514) with full Vikram Iyer system prompt
   and the extraction JSON schema from docs/02_daily_pipeline.md
3. Parses the JSON response
4. Writes to Neo4j:
   - Guidance node (MERGE on guidance_id = nse_code + concall_date)
   - Updates HAS_ORDER_BOOK edge if order book size mentioned
   - CapexPlan node if capex mentioned
   - Risk nodes for each risk_flag
5. Triggers conviction score recompute for this company
6. Prints Vikram's verdict to console

Test with a fake WELCORP transcript you generate.
```

---

## Useful Cypher Queries (run in Neo4j Browser)

```cypher
// How many nodes of each type?
MATCH (n) RETURN labels(n) AS type, count(n) AS count ORDER BY count DESC;

// Top 10 by conviction score
MATCH (c:Company) WHERE c.conviction_score IS NOT NULL
RETURN c.nse_code, c.name, c.conviction_score, c.quality_score
ORDER BY c.conviction_score DESC LIMIT 10;

// Recent catalysts (last 7 days)
MATCH (c:Company)-[:TRIGGERED]->(cat:Catalyst)
WHERE cat.date >= date() - duration('P7D')
RETURN c.nse_code, cat.type, cat.magnitude, cat.ep_probability, cat.date
ORDER BY cat.date DESC;

// Companies in InfraCapex theme with quality score > 7
MATCH (c:Company)-[:BENEFITS_FROM]->(t:Theme {name:'InfraCapex'})
WHERE c.quality_score > 7
RETURN c.nse_code, c.name, c.quality_score, c.conviction_score
ORDER BY c.conviction_score DESC;

// Supply chain: who supplies to WELCORP?
MATCH (supplier:Company)-[:SUPPLIES_TO]->(c:Company {nse_code:'WELCORP'})
RETURN supplier.nse_code, supplier.name, supplier.conviction_score;

// Full graph of a company
MATCH (c:Company {nse_code:'WELCORP'})-[r]-(connected)
RETURN c, r, connected;
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Claude Code Spark icon missing | `Ctrl+Shift+P` → "Developer: Reload Window" |
| Neo4j connection refused | `docker start nse-knowledge-graph` |
| MERGE creates duplicates | Check constraint exists: `SHOW CONSTRAINTS;` |
| Claude Code can't see CSV | @-mention it: `@data/raw/NSE_500cr_universe.csv` |
| Conviction score not updating | Run `python daily_pipeline.py --mode scores` |
| BSE RSS blocked | Try with VPN or switch to BSE API alternative |
