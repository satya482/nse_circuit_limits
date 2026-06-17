"""
Screener.in Insights Loader

For every company in the Neo4j universe, fetches:
  1. Key Points  (/wiki/company/{id}/commentary/v2/)  — business overview, KPIs
  2. Latest concall summary (/concalls/summary/{id}/) — structured AI summary

Sends combined text to Claude (sonnet) to extract:
  - Theme classifications  -> BENEFITS_FROM edges
  - Order book size        -> OrderBook node + conviction score +10
  - Guidance numbers       -> Guidance node
  - Working capital days   -> Company property
  - Market share / capacity utilization -> Company properties

Saves a local progress cache so runs are resumable.

Run   : python load_screener_insights.py
Resume: safe — re-run skips already-processed companies
Flags : --symbol RVNL   (single company)
        --limit  50     (process first N unprocessed)
        --no-claude     (fetch + cache only; skip Claude + Neo4j writes)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from neo4j import GraphDatabase

try:
    import anthropic

    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV = _HERE.parent.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")
SCR_EMAIL = os.getenv("SCREENER_EMAIL", "")
SCR_PASSWORD = os.getenv("SCREENER_PASSWORD", "")

CLAUDE_MODEL = "claude-sonnet-4-6"
CACHE_FILE = _HERE.parent.parent / "data" / "screener_insights_cache.json"

SCREENER_BASE = "https://www.screener.in"

# All valid theme names (must match Neo4j Theme nodes)
VALID_THEMES = [
    "GovernmentCapex",
    "ManufacturingTailwind",
    "FutureEconomy",
    "InfraCapex",
    "Defence",
    "PowerCapex",
    "Railways",
    "Roads",
    "Ports",
    "Defence_Electronics",
    "Defence_Platforms",
    "Defence_MRO",
    "PowerT&D",
    "RenewableEnergy",
    "PLI_Electronics",
    "PLI_Chemicals",
    "China+1_Textiles",
    "Semiconductor",
    "DataCentre",
    "EV_Components",
    "SpecialtyChemicals",
    "Hospitals_HealthcareInfra",
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


# ── Screener.in auth session ──────────────────────────────────────────────────
def make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update(HEADERS)
    lp = s.get(f"{SCREENER_BASE}/login/", timeout=15)
    csrf = BeautifulSoup(lp.text, "html.parser").select_one(
        "input[name=csrfmiddlewaretoken]"
    )
    if not csrf:
        raise RuntimeError("Could not get CSRF token from screener.in login page")
    s.post(
        f"{SCREENER_BASE}/login/",
        data={
            "csrfmiddlewaretoken": csrf["value"],
            "username": SCR_EMAIL,
            "password": SCR_PASSWORD,
            "next": "/",
        },
        headers={"Referer": f"{SCREENER_BASE}/login/"},
        timeout=15,
    )
    return s


# ── Fetch helpers ─────────────────────────────────────────────────────────────
def get_company_id(session: requests.Session, nse_code: str) -> int | None:
    """Resolve NSE code -> screener.in numeric company ID."""
    r = session.get(
        f"{SCREENER_BASE}/api/company/search/?q={nse_code}",
        timeout=10,
    )
    if r.status_code != 200:
        return None
    results = r.json()
    for item in results:
        # Match exact NSE symbol in URL
        url = item.get("url", "")
        if f"/{nse_code}/" in url.upper() or f"/{nse_code.upper()}/" in url.upper():
            return item.get("id")
    return results[0].get("id") if results else None


def fetch_key_points(session: requests.Session, company_id: int) -> str:
    """Fetch Key Points wiki text. Returns plain text."""
    r = session.get(
        f"{SCREENER_BASE}/wiki/company/{company_id}/commentary/v2/",
        timeout=15,
    )
    if r.status_code != 200:
        return ""
    soup = BeautifulSoup(r.text, "html.parser")
    # Extract just the about + key-points content blocks
    content_div = soup.select_one(".wiki-content, #wiki-content, .commentary, article")
    if content_div:
        return content_div.get_text("\n", strip=True)
    # Fallback: find the section between "About" and the sidebar
    body = soup.get_text("\n", strip=True)
    # Strip nav/footer noise — keep from "About" to end of meaningful content
    m = re.search(r"(About\n.+)", body, re.S)
    return m.group(1)[:5000] if m else body[:3000]


def fetch_concall_ids(session: requests.Session, nse_code: str) -> list[int]:
    """Get list of concall summary IDs from the company page (newest first)."""
    r = session.get(
        f"{SCREENER_BASE}/company/{nse_code}/consolidated/",
        timeout=15,
    )
    if r.status_code != 200:
        return []
    soup = BeautifulSoup(r.text, "html.parser")
    ids = []
    for btn in soup.select("[data-url*='/concalls/summary/']"):
        m = re.search(r"/concalls/summary/(\d+)/", btn.get("data-url", ""))
        if m:
            ids.append(int(m.group(1)))
    return ids[:3]  # latest 3 concalls


def fetch_concall_summary(session: requests.Session, concall_id: int) -> str:
    """Fetch a single concall summary page. Returns plain text."""
    r = session.get(f"{SCREENER_BASE}/concalls/summary/{concall_id}/", timeout=15)
    if r.status_code != 200:
        return ""
    soup = BeautifulSoup(r.text, "html.parser")
    # Concall content is in the main article/div
    content = soup.select_one(".concall-summary, article, .content-wrapper, main")
    if content:
        return content.get_text("\n", strip=True)[:6000]
    body = soup.get_text("\n", strip=True)
    m = re.search(r"(Concall Summary.+)", body, re.S | re.I)
    return m.group(0)[:6000] if m else body[500:6500]


# ── Claude extraction ─────────────────────────────────────────────────────────
_SYSTEM = """You are Vikram Iyer, 30-year Indian equity veteran.
Extract structured data from company Key Points and concall summaries.
Return ONLY valid JSON — no prose, no markdown fences, no explanation."""

_SCHEMA = (
    """
{
  "themes": [<list of theme names that apply, chosen ONLY from: """
    + ", ".join(f'"{t}"' for t in VALID_THEMES)
    + """>],
  "theme_confidence": {<theme_name>: "High"|"Medium"|"Low"},
  "order_book_crore": <latest order book in Rs Cr, number or null>,
  "order_inflow_crore": <guided order inflow for current year, number or null>,
  "revenue_growth_guided_pct": <guided revenue/topline growth %, number or null>,
  "margin_guided_pct": <guided EBITDA or PAT margin %, number or null>,
  "working_capital_days": <working capital / net working capital days, number or null>,
  "market_share_pct": <market share in primary segment %, number or null>,
  "capacity_utilization_pct": <manufacturing capacity utilization %, number or null>,
  "management_confidence": <1-10 integer>,
  "management_tone": "Cautious"|"Neutral"|"Confident"|"Bullish",
  "key_risks": [<up to 3 short risk strings>],
  "business_summary": "<2-line Vikram-style summary: what business does + key metric>"
}"""
)


def extract_with_claude(nse_code: str, key_points: str, concall_text: str) -> dict:
    if not ANTHROPIC_AVAILABLE or not ANTHROPIC_KEY:
        return {}
    combined = f"Company: {nse_code}\n\n### KEY POINTS\n{key_points[:3000]}\n\n### LATEST CONCALL\n{concall_text[:3000]}"
    prompt = (
        f"Extract structured data from the following company information.\n\n"
        f"{combined}\n\n"
        f"Return JSON matching this schema exactly:\n{_SCHEMA}"
    )
    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
        msg = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=800,
            system=_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
        )
        text = msg.content[0].text.strip()
        text = re.sub(r"^```[a-z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
        return json.loads(text)
    except Exception as exc:
        print(f"[CLAUDE] ERROR {nse_code}: {exc}")
        return {}


# ── Neo4j writes ──────────────────────────────────────────────────────────────
_MERGE_BENEFITS_FROM = """
MATCH (c:Company {nse_code: $nse_code})
MATCH (t:Theme {name: $theme})
MERGE (c)-[r:BENEFITS_FROM]->(t)
  ON CREATE SET r.direct = true, r.confidence = $confidence, r.magnitude = 'Medium', r.source = 'screener_keypoints'
  ON MATCH  SET r.confidence = $confidence
"""

_UPDATE_COMPANY = """
MATCH (c:Company {nse_code: $nse_code})
SET
  c.business_summary          = CASE WHEN $summary IS NOT NULL THEN $summary ELSE c.business_summary END,
  c.order_book_crore          = CASE WHEN $ob_crore IS NOT NULL THEN $ob_crore ELSE c.order_book_crore END,
  c.order_book_to_revenue_ratio = CASE WHEN $ob_ratio IS NOT NULL THEN $ob_ratio ELSE c.order_book_to_revenue_ratio END,
  c.market_share_pct          = CASE WHEN $mkt_share IS NOT NULL THEN $mkt_share ELSE c.market_share_pct END,
  c.capacity_utilization_pct  = CASE WHEN $cap_util IS NOT NULL THEN $cap_util ELSE c.capacity_utilization_pct END,
  c.working_capital_days      = CASE WHEN $wc_days IS NOT NULL THEN $wc_days ELSE c.working_capital_days END
"""

_MERGE_GUIDANCE = """
MERGE (g:Guidance {guidance_id: $gid})
  ON CREATE SET
    g.nse_code               = $nse_code,
    g.concall_date           = date($concall_date),
    g.revenue_growth_guided  = $rev_growth,
    g.margin_guided          = $margin,
    g.management_confidence  = $confidence,
    g.management_tone        = $tone,
    g.source                 = 'screener_concall'
  ON MATCH SET
    g.revenue_growth_guided  = $rev_growth,
    g.margin_guided          = $margin
WITH g
MATCH (c:Company {nse_code: $nse_code})
MERGE (c)-[:GUIDED]->(g)
"""

_MERGE_ORDERBOOK = """
MERGE (ob:OrderBook {orderbook_id: $ob_id})
  ON CREATE SET
    ob.size_crore   = $size_crore,
    ob.ob_date      = date($ob_date),
    ob.source       = 'screener_keypoints'
  ON MATCH SET
    ob.size_crore   = $size_crore
WITH ob
MATCH (c:Company {nse_code: $nse_code})
MERGE (c)-[:HAS_ORDER_BOOK]->(ob)
"""


def write_to_neo4j(
    nse_code: str, extracted: dict, revenue_ttm: float | None, session
) -> None:
    today = date.today().isoformat()

    # Order book ratio
    ob_crore = extracted.get("order_book_crore")
    ob_ratio = None
    if ob_crore and revenue_ttm and revenue_ttm > 0:
        ob_ratio = round(ob_crore / revenue_ttm, 2)

    # Update Company node
    session.run(
        _UPDATE_COMPANY,
        nse_code=nse_code,
        summary=extracted.get("business_summary"),
        ob_crore=ob_crore,
        ob_ratio=ob_ratio,
        mkt_share=extracted.get("market_share_pct"),
        cap_util=extracted.get("capacity_utilization_pct"),
        wc_days=extracted.get("working_capital_days"),
    )

    # BENEFITS_FROM edges
    themes = extracted.get("themes") or []
    confidence = extracted.get("theme_confidence") or {}
    for theme in themes:
        if theme in VALID_THEMES:
            session.run(
                _MERGE_BENEFITS_FROM,
                nse_code=nse_code,
                theme=theme,
                confidence=confidence.get(theme, "Medium"),
            )
            print(
                f"[GRAPH] BENEFITS_FROM | {nse_code} -> {theme} | {confidence.get(theme,'Medium')}"
            )

    # OrderBook node
    if ob_crore:
        session.run(
            _MERGE_ORDERBOOK,
            ob_id=f"{nse_code}_{today}",
            nse_code=nse_code,
            size_crore=ob_crore,
            ob_date=today,
        )
        print(
            f"[GRAPH] OrderBook MERGE | {nse_code} | Rs.{ob_crore:.0f} Cr (ratio={ob_ratio})",
            flush=True,
        )

    # Guidance node
    rev_growth = extracted.get("revenue_growth_guided_pct")
    margin = extracted.get("margin_guided_pct")
    tone = extracted.get("management_tone")
    conf = extracted.get("management_confidence")
    if any(x is not None for x in [rev_growth, margin, tone]):
        session.run(
            _MERGE_GUIDANCE,
            gid=f"{nse_code}_{today}_screener",
            nse_code=nse_code,
            concall_date=today,
            rev_growth=rev_growth,
            margin=margin,
            confidence=conf,
            tone=tone,
        )
        print(
            f"[GRAPH] Guidance MERGE | {nse_code} | growth={rev_growth} margin={margin} tone={tone}"
        )


# ── Cache helpers ─────────────────────────────────────────────────────────────
def load_cache() -> dict:
    if CACHE_FILE.exists():
        with open(CACHE_FILE, encoding="utf-8") as fh:
            return json.load(fh)
    return {}


def save_cache(cache: dict) -> None:
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as fh:
        json.dump(cache, fh, indent=2, ensure_ascii=False)


# ── Main ──────────────────────────────────────────────────────────────────────
def run(
    symbol: str | None = None, limit: int | None = None, no_claude: bool = False
) -> None:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))

    # Get all companies from Neo4j
    with driver.session() as neo_session:
        if symbol:
            rows = list(
                neo_session.run(
                    "MATCH (c:Company {nse_code: $s}) RETURN c.nse_code AS code, c.revenue_ttm AS rev",
                    s=symbol,
                )
            )
        else:
            rows = list(
                neo_session.run(
                    "MATCH (c:Company) WHERE c.roe_3yr_avg IS NOT NULL "
                    "RETURN c.nse_code AS code, c.revenue_ttm AS rev ORDER BY c.nse_code"
                )
            )

    codes = [(r["code"], r["rev"]) for r in rows]
    print(f"[INSIGHTS] {len(codes)} companies to process")

    cache = load_cache()
    session = make_session()
    print(f"[INSIGHTS] Authenticated as {SCR_EMAIL}")

    processed = 0
    for nse_code, revenue_ttm in codes:
        if limit and processed >= limit:
            break
        if nse_code in cache and not symbol:
            continue  # already done

        print(f"\n[INSIGHTS] Processing {nse_code}...")

        # 1. Get screener.in company ID
        company_id = get_company_id(session, nse_code)
        if not company_id:
            print(f"[INSIGHTS] {nse_code}: not found on screener.in, skipping")
            cache[nse_code] = {"status": "not_found"}
            save_cache(cache)
            continue

        time.sleep(0.5)

        # 2. Fetch Key Points
        key_points = fetch_key_points(session, company_id)
        time.sleep(0.5)

        # 3. Fetch latest concall summary
        concall_ids = fetch_concall_ids(session, nse_code)
        concall_text = ""
        if concall_ids:
            concall_text = fetch_concall_summary(session, concall_ids[0])
            time.sleep(0.5)

        if not key_points and not concall_text:
            print(f"[INSIGHTS] {nse_code}: no content fetched, skipping")
            cache[nse_code] = {"status": "no_content"}
            save_cache(cache)
            continue

        # 4. Claude extraction
        if no_claude:
            extracted = {}
            cache[nse_code] = {
                "status": "fetched_only",
                "key_points": key_points[:500],
                "concall_snippet": concall_text[:500],
            }
        else:
            extracted = extract_with_claude(nse_code, key_points, concall_text)
            cache[nse_code] = {"status": "done", "extracted": extracted}

        save_cache(cache)

        if extracted and not no_claude:
            # 5. Write to Neo4j
            rev = float(revenue_ttm) if revenue_ttm else None
            with driver.session() as neo_session:
                write_to_neo4j(nse_code, extracted, rev, neo_session)

            summary = (
                (extracted.get("business_summary") or "")[:80]
                .encode("ascii", "replace")
                .decode()
            )
            themes = extracted.get("themes") or []
            ob = extracted.get("order_book_crore")
            tone = extracted.get("management_tone")
            print(f"  themes={themes} ob={ob} tone={tone} summary={summary!r}")

            # Trigger score recompute for this company
            try:
                import importlib.util

                _etl = _HERE.parent.parent / "etl" / "recompute_scores.py"
                spec = importlib.util.spec_from_file_location("recompute_scores", _etl)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                new_score = mod.run(nse_code)
                print(f"  [SCORES] {nse_code} recomputed ({new_score} updated)")
            except Exception as exc:
                print(f"  [SCORES] recompute skipped: {exc}")

        processed += 1
        time.sleep(1.0)  # rate limit

    driver.close()
    print(
        f"\n[INSIGHTS] Done — {processed} companies processed, {len(cache)} total in cache"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Load screener.in Key Points + concall summaries"
    )
    parser.add_argument("--symbol", help="Process single NSE symbol")
    parser.add_argument("--limit", type=int, help="Max companies to process this run")
    parser.add_argument(
        "--no-claude", action="store_true", help="Fetch only, skip Claude + Neo4j"
    )
    args = parser.parse_args()
    run(symbol=args.symbol, limit=args.limit, no_claude=args.no_claude)


if __name__ == "__main__":
    main()
