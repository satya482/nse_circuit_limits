"""
Concall Extractor — Trendlyne RSS -> YouTube -> Claude API -> Neo4j

Two modes:
  Auto  : polls Trendlyne RSS for new concalls, fetches YouTube transcripts
  Manual: reads a local transcript file (fallback when YouTube unavailable)

Usage:
  python concall_extractor.py --mode auto
  python concall_extractor.py --mode manual --company WELCORP --file transcript.txt

Requires: feedparser, youtube-transcript-api, anthropic, neo4j, python-dotenv
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import unicodedata
from datetime import date, datetime
from pathlib import Path

import feedparser
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from neo4j import GraphDatabase

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    YT_AVAILABLE = True
except ImportError:
    YT_AVAILABLE = False
    print("[CONCALL] WARNING: youtube-transcript-api not installed")

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("[CONCALL] WARNING: anthropic package not installed")

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV  = _HERE.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI      = os.getenv("NEO4J_URI",         "bolt://localhost:7687")
NEO4J_USER     = os.getenv("NEO4J_USER",         "neo4j")
NEO4J_PASS     = os.getenv("NEO4J_PASSWORD",     "")
ANTHROPIC_KEY  = os.getenv("ANTHROPIC_API_KEY",  "")

TRENDLYNE_RSS     = "https://trendlyne.com/feeds/earning-calls-podcast-rss/"
TRENDLYNE_SITEMAP = "https://trendlyne.com/equity-sitemap-stocks.xml"
SITEMAP_CACHE     = _HERE.parent / "data" / "trendlyne_sitemap_cache.json"
CLAUDE_MODEL      = "claude-sonnet-4-6"


# ── Trendlyne sitemap -> slug_to_symbol lookup ─────────────────────────────────
def _slugify(name: str) -> str:
    """Normalize company name to URL slug (matches Trendlyne sitemap format)."""
    name = name.lower().strip()
    name = unicodedata.normalize("NFKD", name)
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"[\s_]+", "-", name)
    return name.strip("-")


def fetch_sitemap() -> dict[str, str]:
    """
    Fetch Trendlyne equity sitemap and build {name_slug: nse_symbol} dict.
    Caches locally (refresh weekly).
    URL pattern: /equity/{id}/{NSE_SYMBOL}/{company-name-slug}/
    """
    if SITEMAP_CACHE.exists():
        age_days = (time.time() - SITEMAP_CACHE.stat().st_mtime) / 86400
        if age_days < 7:
            with open(SITEMAP_CACHE, encoding="utf-8") as fh:
                return json.load(fh)

    print("[SITEMAP] Fetching Trendlyne equity sitemap...")
    try:
        resp = requests.get(TRENDLYNE_SITEMAP, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as exc:
        print(f"[SITEMAP] ERROR: {exc}")
        return {}

    slug_to_symbol: dict[str, str] = {}
    # Extract URLs like /equity/12345/AARTIIND/aarti-industries-ltd/
    for m in re.finditer(r"/equity/\d+/([A-Z0-9&]+)/([a-z0-9-]+)/", resp.text):
        symbol = m.group(1)
        slug   = m.group(2)
        slug_to_symbol[slug] = symbol

    SITEMAP_CACHE.parent.mkdir(parents=True, exist_ok=True)
    with open(SITEMAP_CACHE, "w", encoding="utf-8") as fh:
        json.dump(slug_to_symbol, fh)

    print(f"[SITEMAP] Cached {len(slug_to_symbol)} entries")
    return slug_to_symbol


def resolve_symbol(company_name: str, slug_to_symbol: dict[str, str]) -> str | None:
    """Map Trendlyne company name to NSE symbol via sitemap slug."""
    slug = _slugify(company_name)
    return slug_to_symbol.get(slug)


# ── YouTube transcript fetch ──────────────────────────────────────────────────
def extract_yt_id(html_description: str) -> str | None:
    """Extract YouTube video ID from RSS description HTML."""
    patterns = [
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})",
        r"youtube\.com/embed/([a-zA-Z0-9_-]{11})",
    ]
    for pat in patterns:
        m = re.search(pat, html_description)
        if m:
            return m.group(1)
    return None


def fetch_transcript(video_id: str) -> str | None:
    """Fetch YouTube auto-generated transcript as plain text."""
    if not YT_AVAILABLE:
        return None
    try:
        segments = YouTubeTranscriptApi.get_transcript(video_id, languages=["en", "en-IN"])
        return " ".join(s["text"] for s in segments)
    except Exception as exc:
        print(f"[YT] ERROR fetching transcript {video_id}: {exc}")
        return None


# ── Claude API extraction ─────────────────────────────────────────────────────
VIKRAM_SYSTEM_PROMPT = """You are Vikram Iyer, a 30-year veteran fundamental analyst covering Indian equities.
Extract structured data from a company earnings call transcript.
Return ONLY valid JSON — no prose, no markdown, no explanation.
Be precise: extract actual numbers mentioned by management."""

EXTRACTION_SCHEMA = """
{
  "revenue_growth_guided_pct":   <number or null — percentage growth guided by management>,
  "margin_guided_low":           <number or null — lower end of EBITDA/PAT margin guidance>,
  "margin_guided_high":          <number or null — upper end of margin guidance>,
  "order_book_commentary":       "<string — specific numbers if mentioned, else null>",
  "order_book_size_crore":       <number or null — total order book in ₹ Cr if mentioned>,
  "order_inflow_guided_crore":   <number or null — expected order inflows in ₹ Cr>,
  "capex_plans": [
    {"size_crore": <number>, "purpose": "<string>", "timeline": "<string>"}
  ],
  "management_confidence":       <1-10 integer — your assessment of management tone and specificity>,
  "management_tone":             "<Cautious|Neutral|Confident|Bullish>",
  "risk_flags":                  ["<specific risks mentioned by management>"],
  "key_quotes": [
    {"quote": "<verbatim quote>", "context": "<what it refers to>"}
  ],
  "vikram_verdict":              "<BUY|ACCUMULATE|HOLD|AVOID> — <1-line reason> — <key number>"
}
"""


def extract_via_claude(company: str, transcript: str) -> dict | None:
    """Call Claude API with Vikram Iyer persona to extract structured data."""
    if not ANTHROPIC_AVAILABLE or not ANTHROPIC_KEY:
        print("[CLAUDE] anthropic package or API key not available")
        return None

    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    user_msg = (
        f"Company: {company}\n\n"
        f"Extract all fields from this earnings call transcript.\n"
        f"Return JSON matching this schema exactly:\n{EXTRACTION_SCHEMA}\n\n"
        f"TRANSCRIPT:\n{transcript[:30000]}"
    )

    try:
        message = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=2048,
            system=VIKRAM_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}],
        )
        raw = message.content[0].text.strip()
        # Strip markdown code blocks if present
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"[CLAUDE] JSON parse error: {exc}")
        return None
    except Exception as exc:
        print(f"[CLAUDE] API error: {exc}")
        return None


# ── Neo4j writes ──────────────────────────────────────────────────────────────
_CHECK_COMPANY = "MATCH (c:Company {nse_code: $nse_code}) RETURN c.nse_code LIMIT 1"

_CHECK_GUIDANCE = """
MATCH (g:Guidance {guidance_id: $guidance_id}) RETURN g.guidance_id LIMIT 1
"""

_MERGE_GUIDANCE = """
MERGE (g:Guidance {guidance_id: $guidance_id})
  ON CREATE SET
    g.concall_date             = date($concall_date),
    g.revenue_growth_guided_pct = $revenue_growth,
    g.margin_guided_low        = $margin_low,
    g.margin_guided_high       = $margin_high,
    g.order_inflow_guided_crore = $order_inflow,
    g.confidence               = $confidence,
    g.management_tone          = $tone,
    g.key_quotes               = $key_quotes,
    g.vikram_verdict           = $vikram_verdict
  ON MATCH SET
    g.revenue_growth_guided_pct = $revenue_growth,
    g.margin_guided_low        = $margin_low,
    g.margin_guided_high       = $margin_high,
    g.management_tone          = $tone,
    g.vikram_verdict           = $vikram_verdict
WITH g
MATCH (c:Company {nse_code: $nse_code})
MERGE (c)-[:GUIDED]->(g)
"""

_MERGE_ORDERBOOK = """
MERGE (ob:OrderBook {orderbook_id: $orderbook_id})
  ON CREATE SET
    ob.date                  = date($ob_date),
    ob.size_crore            = $size_crore,
    ob.revenue_coverage_ratio = $coverage,
    ob.execution_months      = null
  ON MATCH SET
    ob.size_crore            = $size_crore
WITH ob
MATCH (c:Company {nse_code: $nse_code})
MERGE (c)-[:HAS_ORDER_BOOK]->(ob)
"""

_UPDATE_COMPANY_OB = """
MATCH (c:Company {nse_code: $nse_code})
SET c.order_book_crore            = $size_crore,
    c.order_book_to_revenue_ratio = $ratio
"""

_MERGE_RISK = """
MERGE (r:Risk {risk_id: $risk_id})
  ON CREATE SET
    r.type        = 'Execution',
    r.severity    = 'Medium',
    r.description = $description
WITH r
MATCH (c:Company {nse_code: $nse_code})
MERGE (c)-[:RISK_EXPOSED_TO]->(r)
"""


def write_to_neo4j(nse_code: str, concall_date: date, extracted: dict, session) -> None:
    """Write Guidance, OrderBook, Risk nodes from extracted data."""
    guidance_id = f"{nse_code}_{concall_date.isoformat()}"

    # Guidance node
    session.run(
        _MERGE_GUIDANCE,
        guidance_id    = guidance_id,
        nse_code       = nse_code,
        concall_date   = concall_date.isoformat(),
        revenue_growth = extracted.get("revenue_growth_guided_pct"),
        margin_low     = extracted.get("margin_guided_low"),
        margin_high    = extracted.get("margin_guided_high"),
        order_inflow   = extracted.get("order_inflow_guided_crore"),
        confidence     = extracted.get("management_confidence"),
        tone           = extracted.get("management_tone"),
        key_quotes     = json.dumps(extracted.get("key_quotes", [])),
        vikram_verdict = extracted.get("vikram_verdict"),
    )
    print(f"[GRAPH] Guidance MERGE | Guidance | {guidance_id} | ok")

    # OrderBook snapshot if size mentioned
    ob_size = extracted.get("order_book_size_crore")
    if ob_size:
        ob_id = f"{nse_code}_{concall_date.isoformat()}"
        # Fetch revenue for coverage ratio
        rev_row = session.run(
            "MATCH (c:Company {nse_code: $n}) RETURN c.revenue_ttm AS rev",
            n=nse_code
        ).single()
        rev = float(rev_row["rev"]) if rev_row and rev_row["rev"] else None
        coverage = round(ob_size / rev, 2) if rev and rev > 0 else None
        ratio    = round(ob_size / (rev / 4), 2) if rev and rev > 0 else None  # vs annualised quarterly

        session.run(
            _MERGE_ORDERBOOK,
            orderbook_id = ob_id,
            nse_code     = nse_code,
            ob_date      = concall_date.isoformat(),
            size_crore   = ob_size,
            coverage     = coverage,
        )
        session.run(
            _UPDATE_COMPANY_OB,
            nse_code   = nse_code,
            size_crore = ob_size,
            ratio      = ratio,
        )
        print(f"[GRAPH] OrderBook MERGE | OrderBook | {ob_id} | ₹{ob_size:.0f} Cr")

    # Risk nodes
    for i, risk_desc in enumerate(extracted.get("risk_flags") or []):
        import hashlib
        risk_id = hashlib.md5(f"{nse_code}:{risk_desc[:80]}".encode()).hexdigest()[:12]
        session.run(
            _MERGE_RISK,
            risk_id     = risk_id,
            nse_code    = nse_code,
            description = risk_desc[:500],
        )
        print(f"[GRAPH] Risk MERGE | Risk | {nse_code} | {risk_desc[:60]}")


# ── Auto mode ─────────────────────────────────────────────────────────────────
def run_auto(driver) -> None:
    slug_to_symbol = fetch_sitemap()
    if not slug_to_symbol:
        print("[CONCALL] Sitemap unavailable — aborting auto mode")
        return

    print("[CONCALL] Fetching Trendlyne concall RSS...")
    try:
        feed = feedparser.parse(TRENDLYNE_RSS)
    except Exception as exc:
        print(f"[CONCALL] RSS error: {exc}")
        return

    entries = feed.get("entries", [])
    print(f"[CONCALL] {len(entries)} entries in Trendlyne RSS")

    for entry in entries:
        creator     = entry.get("author", entry.get("dc_creator", ""))
        title       = entry.get("title", "")
        description = entry.get("summary", entry.get("description", ""))
        pub_date    = date.today()

        if entry.get("published"):
            try:
                from email.utils import parsedate_to_datetime
                pub_date = parsedate_to_datetime(entry["published"]).date()
            except Exception:
                pass

        nse_code = resolve_symbol(creator, slug_to_symbol)
        if not nse_code:
            print(f"[CONCALL] Skip — unresolved: '{creator}'")
            continue

        with driver.session() as session:
            if not session.run(_CHECK_COMPANY, nse_code=nse_code).single():
                continue  # not in universe

            guidance_id = f"{nse_code}_{pub_date.isoformat()}"
            if session.run(_CHECK_GUIDANCE, guidance_id=guidance_id).single():
                print(f"[CONCALL] Skip {nse_code} — already processed")
                continue

        yt_id = extract_yt_id(description)
        if not yt_id:
            print(f"[CONCALL] Skip {nse_code} — no YouTube URL found")
            continue

        transcript = fetch_transcript(yt_id)
        if not transcript:
            print(f"[CONCALL] Skip {nse_code} — transcript unavailable")
            continue

        print(f"\n[CONCALL] Processing {nse_code} ({creator}) — {pub_date}")
        extracted = extract_via_claude(creator, transcript)
        if not extracted:
            continue

        print(json.dumps(extracted, indent=2))
        confirm = input(f"Write to Neo4j? [y/N]: ").strip().lower()
        if confirm != "y":
            print("[CONCALL] Skipped by user")
            continue

        with driver.session() as session:
            write_to_neo4j(nse_code, pub_date, extracted, session)

        print(f"\n*** Vikram's Verdict: {extracted.get('vikram_verdict', 'N/A')} ***\n")

        # Recompute score for this company only
        from recompute_scores import run as scores_run  # type: ignore[import]
        scores_run(nse_code)


# ── Manual mode ───────────────────────────────────────────────────────────────
def run_manual(nse_code: str, transcript_file: str, driver) -> None:
    path = Path(transcript_file)
    if not path.exists():
        print(f"ERROR: transcript file not found: {path}")
        sys.exit(1)

    transcript = path.read_text(encoding="utf-8")
    concall_date = date.today()

    print(f"[CONCALL] Extracting from {path.name} for {nse_code}...")
    extracted = extract_via_claude(nse_code, transcript)
    if not extracted:
        print("ERROR: Claude extraction failed")
        sys.exit(1)

    print(json.dumps(extracted, indent=2))
    confirm = input("Write to Neo4j? [y/N]: ").strip().lower()
    if confirm != "y":
        sys.exit(0)

    with driver.session() as session:
        write_to_neo4j(nse_code, concall_date, extracted, session)

    print(f"\n*** Vikram's Verdict: {extracted.get('vikram_verdict', 'N/A')} ***\n")

    from recompute_scores import run as scores_run  # type: ignore[import]
    scores_run(nse_code)


# ── CLI ───────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(description="Concall extractor")
    parser.add_argument("--mode", choices=["auto", "manual"], default="auto")
    parser.add_argument("--company", help="NSE code (manual mode only)")
    parser.add_argument("--file",    help="Transcript .txt file (manual mode only)")
    args = parser.parse_args()

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))

    if args.mode == "auto":
        run_auto(driver)
    else:
        if not args.company or not args.file:
            print("ERROR: --company and --file required for manual mode")
            sys.exit(1)
        run_manual(args.company.upper(), args.file, driver)

    driver.close()


if __name__ == "__main__":
    main()
