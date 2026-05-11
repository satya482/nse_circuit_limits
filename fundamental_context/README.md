# NSE Knowledge Graph

A Neo4j-powered fundamental knowledge graph of ~962 NSE-listed stocks.

**Core purpose**: Store *why* a business deserves conviction, then surface
which stocks to act on when new fundamental information arrives — order wins,
concall guidance, policy announcements, earnings beats.

---

## Quick Start

```bash
# 1. Clone / open project
code nse-knowledge-graph

# 2. Set up Python env
python -m venv .venv && source .venv/bin/activate
pip install neo4j python-dotenv anthropic requests feedparser pandas

# 3. Start Neo4j
docker start nse-knowledge-graph   # or Neo4j Desktop

# 4. Copy .env.example → .env and fill in credentials

# 5. Load schema
python -c "exec(open('graph/schema/load_schema.py').read())"

# 6. Load universe
python graph/loaders/load_universe.py

# 7. Open in Claude Code (⚡ sidebar) — it reads CLAUDE.md automatically
```

---

## Project Structure

```
nse-knowledge-graph/
│
├── CLAUDE.md                        ← Claude Code reads this every session
├── .env                             ← Neo4j + Anthropic credentials (never commit)
├── .claudeignore
│
├── data/
│   ├── raw/
│   │   └── NSE_500cr_universe.csv   ← 962-stock universe
│   └── processed/
│       ├── fundamentals/            ← per-stock fundamental CSVs
│       └── ep_watchlist_*.csv       ← daily EP candidate output
│
├── graph/
│   ├── schema/
│   │   └── constraints.cypher       ← run once on fresh DB
│   ├── loaders/
│   │   ├── load_universe.py         ← Session 1: 962 stocks → nodes
│   │   ├── load_fundamentals.py     ← Session 2: ROE/ROCE/OB etc
│   │   ├── load_themes.py           ← Session 3: themes + edges
│   │   └── load_catalyst.py         ← manual catalyst entry
│   └── queries/
│       ├── ep_screener.cypher
│       ├── conviction_score.cypher
│       ├── supply_chain.cypher
│       └── theme_beneficiaries.cypher
│
├── etl/
│   ├── bse_rss_parser.py            ← Session 4: daily BSE filings
│   ├── concall_extractor.py         ← Session 5: transcript → nodes
│   ├── recompute_scores.py          ← nightly conviction refresh
│   └── daily_pipeline.py           ← orchestrator
│
├── docs/
│   ├── 01_graph_design.md           ← full node/edge schema
│   ├── 02_daily_pipeline.md         ← update architecture
│   ├── 03_setup_and_sessions.md     ← VS Code + Neo4j setup guide
│   └── 04_cypher_queries.md         ← query library reference
│
└── notebooks/
    └── exploration.ipynb
```

---

## The Five Build Sessions

| Session | What gets built | Time |
|---------|----------------|------|
| 1 | Schema + 962-stock universe loaded into Neo4j | ~45 min |
| 2 | Fundamentals loader + 5 seed stocks enriched | ~60 min |
| 3 | Theme nodes + EP screener query | ~45 min |
| 4 | BSE RSS daily catalyst pipeline | ~90 min |
| 5 | Concall extractor (Claude API → structured nodes) | ~60 min |

Full setup instructions: `docs/03_setup_and_sessions.md`

---

## Key Docs

| Doc | Contents |
|-----|----------|
| `CLAUDE.md` | Full project context for Claude Code |
| `docs/01_graph_design.md` | All node types, edge types, conviction score formula |
| `docs/02_daily_pipeline.md` | Daily update architecture, cron setup, BSE classifier |
| `docs/03_setup_and_sessions.md` | VS Code setup, Neo4j Docker, session-by-session prompts |
| `docs/04_cypher_queries.md` | 30+ ready-to-use Cypher queries |
| `graph/schema/constraints.cypher` | Neo4j schema — run before any data loading |

---

## Conviction Score (0–100)

```
Business Quality    35 pts  ROE, ROCE, Order Book, Pledge, Promoter
Earnings Quality    20 pts  Cash conversion, Beat streak, Working capital
Thematic Alignment  20 pts  Theme count, Govt scheme, Industry growth
Catalyst Layer      25 pts  OrderWin, EarningsBeat, GovtApproval (time-decayed)
```

Score > 80 = HIGH CONVICTION. Score 60–79 = WATCH. Score < 60 = MONITOR.

---

## Daily Workflow (after setup)

```
5:00 PM IST → python etl/daily_pipeline.py --mode full
              (7-10 min, fully automated)

On concall days:
              python etl/concall_extractor.py --company WELCORP --file transcript.txt
              (20 min including review)

Weekly:
              Review auto-classified BSE catalysts in logs/
              Confirm or reject edge creations
```

---

## Stack

- **Graph DB**: Neo4j 5.x Community (free)
- **Python**: neo4j driver v5.x, anthropic SDK, feedparser, pandas
- **AI**: Claude API (claude-sonnet-4-20250514) for concall extraction (Vikram Iyer persona)
- **Dev**: VS Code + Claude Code extension
- **Visualization**: Neo4j Bloom (built-in) + future React layer
