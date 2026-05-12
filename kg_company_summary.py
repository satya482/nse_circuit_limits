"""
KG Company Summary Generator

Synthesises Neo4j KG company data + fresh telegram research reports into a
Vikram Iyer-style investment summary using Claude Sonnet.

Usage:
  python kg_company_summary.py KRN
  python kg_company_summary.py NTPC --days 30
  python kg_company_summary.py KRN --dry-run     # print assembled context, skip Claude
  python kg_company_summary.py KRN --save        # save to kg_summaries/NSE_DATE.md

Strategy:
  1. Load company profile from Neo4j (falls back to CSV + stock_labels.json)
  2. Fetch company's BENEFITS_FROM themes from KG; follow SUBTHEME_OF to linked
     telegram themes to get fresh research timestamps
  3. Score all telegram JSON reports by relevance (direct mention >> theme overlap
     >> sector keyword overlap)
  4. Feed company profile + KG themes + top relevant reports to Claude Sonnet
     as Vikram Iyer for synthesis
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv

# Ensure UTF-8 output on Windows terminals that default to cp1252
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
elif sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

_HERE = Path(__file__).parent
load_dotenv(_HERE / "fundamental_context" / ".env")

# ── Config ────────────────────────────────────────────────────────────────────
ANTHROPIC_KEY  = os.getenv("ANTHROPIC_API_KEY", "")
SONNET_MODEL   = "claude-sonnet-4-6"

NEO4J_URI  = os.getenv("NEO4J_URI",      "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER",     "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

_UNIVERSE_CSV  = _HERE / "NSE_500cr_15CrNotional10D_50rs_sector_industry.csv"
_LABELS_JSON   = _HERE / "tools" / "stock_labels.json"
_THEMES_DIR    = _HERE / "telegram_themes"
_SUMMARIES_DIR = _HERE / "kg_summaries"

# ── Cypher ────────────────────────────────────────────────────────────────────
_Q_COMPANY = """
MATCH (c:Company {nse_code: $nse_code})
RETURN c.name             AS name,
       c.sector           AS sector,
       c.industry         AS industry,
       c.quality_score    AS quality_score,
       c.conviction_score AS conviction_score
LIMIT 1
"""

_Q_THEMES = """
MATCH (c:Company {nse_code: $nse_code})-[bf:BENEFITS_FROM]->(t:Theme)
WHERE NOT coalesce(t.source, '') = 'telegram'
OPTIONAL MATCH (tg:Theme {source:'telegram'})-[:SUBTHEME_OF]->(t)
RETURN t.name           AS theme,
       t.vikram_thesis  AS thesis,
       bf.magnitude     AS mag,
       collect(DISTINCT tg.name) AS tg_themes
ORDER BY t.name
"""

# ── Universe loaders ──────────────────────────────────────────────────────────
def _load_universe() -> dict[str, dict]:
    if not _UNIVERSE_CSV.exists():
        return {}
    out: dict[str, dict] = {}
    with open(_UNIVERSE_CSV, encoding="cp1252") as fh:
        for row in csv.DictReader(fh):
            code = (row.get("NSE Code") or "").strip().upper()
            if code:
                out[code] = {
                    "name":     (row.get("Stock Name") or "").strip(),
                    "sector":   (row.get("sector_name") or "").strip(),
                    "industry": (row.get("Industry Name") or "").strip(),
                }
    return out


def _load_labels() -> dict[str, str]:
    if not _LABELS_JSON.exists():
        return {}
    with open(_LABELS_JSON, encoding="utf-8") as fh:
        return json.load(fh)


# ── KG query ─────────────────────────────────────────────────────────────────
def _query_kg(nse_code: str) -> dict | None:
    """Return {name, sector, industry, quality_score, conviction_score, themes:[]} or None."""
    try:
        from neo4j import GraphDatabase
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
        driver.verify_connectivity()
    except Exception as exc:
        print(f"[SUMMARY] KG unavailable ({exc}) — using CSV/label fallback only")
        return None

    result: dict | None = None
    with driver.session() as session:
        rec = session.run(_Q_COMPANY, nse_code=nse_code).single()
        if rec:
            result = dict(rec)
            rows = session.run(_Q_THEMES, nse_code=nse_code)
            result["themes"] = [dict(r) for r in rows]
    driver.close()
    return result


# ── Telegram report loader ────────────────────────────────────────────────────
def _load_telegram_reports(days: int = 30) -> list[dict]:
    cutoff = datetime.now() - timedelta(days=days)
    reports: list[dict] = []
    for p in sorted(_THEMES_DIR.glob("themes_*.json"), reverse=True):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", p.name)
        if not m:
            continue
        file_date = datetime.strptime(m.group(1), "%Y-%m-%d")
        if file_date < cutoff:
            break
        with open(p, encoding="utf-8") as fh:
            data = json.load(fh)
        for r in data.get("reports", []):
            r["_file_date"] = m.group(1)
        reports.extend(data.get("reports", []))
    return reports


# ── Relevance scoring ─────────────────────────────────────────────────────────
_NOISE = {'and', 'the', 'of', 'in', 'for', 'a', 'an', 'by', 'with', 'to', 'at', 'on',
          'is', 'its', 'limited', 'ltd', 'india', 'indian', 'growth', 'expansion'}

def _tokenise(text: str) -> set[str]:
    return {t for t in re.sub(r'[&,\-\(\)/]', ' ', text.lower()).split()
            if len(t) > 3 and t not in _NOISE}


def _theme_score(company_themes: list[str], report_themes: list[str]) -> float:
    """Score based on exact theme name overlap + partial token overlap."""
    if not company_themes or not report_themes:
        return 0.0
    ct_exact = {t.lower() for t in company_themes}
    rt_exact = {t.lower() for t in report_themes}
    exact = len(ct_exact & rt_exact)
    if exact:
        return min(1.0, exact / max(len(ct_exact), len(rt_exact)) + 0.3)
    ct_toks = {tok for t in ct_exact for tok in _tokenise(t)}
    rt_toks = {tok for t in rt_exact for tok in _tokenise(t)}
    overlap = len(ct_toks & rt_toks)
    return overlap / max(len(ct_toks), len(rt_toks), 1) * 0.5 if overlap else 0.0


def _find_relevant_reports(
    nse_code: str,
    kg_theme_names: list[str],
    tg_theme_names: list[str],
    sector: str,
    industry: str,
    description: str,
    all_reports: list[dict],
    top_n: int = 12,
) -> list[tuple[float, dict]]:
    """Score every report for relevance. Returns top_n (score, report) pairs."""
    # Context tokens from sector / industry / description for broad fallback
    ctx_toks = _tokenise(f"{sector} {industry} {description}")

    # Combined set of theme names to match against (curated + linked telegram)
    all_company_themes = kg_theme_names + tg_theme_names

    scored: list[tuple[float, dict]] = []
    for r in all_reports:
        report_cos = {
            (c.get("nse_code") or c.get("symbol") or "").strip().upper()
            for c in (r.get("companies") or [])
        }
        report_themes = r.get("themes") or []

        if nse_code in report_cos:
            score = 2.0                          # direct mention — top priority
        else:
            score = _theme_score(all_company_themes, report_themes)
            if score < 0.15:                     # broad sector fallback
                rt_toks = {tok for t in report_themes for tok in _tokenise(t)}
                overlap = len(ctx_toks & rt_toks)
                if overlap:
                    score = max(score, overlap / max(len(ctx_toks), len(rt_toks)) * 0.35)

        if score >= 0.10:
            scored.append((score, r))

    scored.sort(key=lambda x: -x[0])
    return scored[:top_n]


# ── Report compactor ──────────────────────────────────────────────────────────
def _compact(report: dict, nse_code: str) -> str:
    themes = ", ".join(report.get("themes") or []) or "—"
    cos = ", ".join(
        c.get("nse_code") or c.get("symbol") or ""
        for c in (report.get("companies") or [])
        if (c.get("nse_code") or c.get("symbol"))
    ) or "—"
    kps = "\n".join(f"  • {k}" for k in (report.get("key_points") or [])[:5])
    cats = "; ".join(report.get("catalysts") or []) or "—"
    src = Path(report.get("source", "?")).stem
    date = report.get("_file_date") or report.get("date") or "?"
    summary = (report.get("summary") or "")[:350]
    direct = nse_code in {
        (c.get("nse_code") or c.get("symbol") or "").upper()
        for c in (report.get("companies") or [])
    }
    tag = f"★ DIRECT ({nse_code} mentioned)" if direct else "THEME MATCH"
    return (
        f"[{tag} | {src} | {date} | Conviction: {report.get('conviction','?')}]\n"
        f"Themes: {themes}\n"
        f"Companies: {cos}\n"
        f"Summary: {summary}\n"
        f"Key points:\n{kps}\n"
        f"Catalysts: {cats}"
    )


# ── Claude prompt ─────────────────────────────────────────────────────────────
_SYSTEM = (
    "You are Vikram Iyer, a 30-year veteran Indian equity research analyst. "
    "Head of Equity Research at a top-tier Indian brokerage. ~78% accuracy on "
    "12-month price targets. Called multi-baggers: Titan, Bajaj Finance, Asian Paints, "
    "Deepak Nitrite — well before the crowd. "
    "Philosophy: fundamentals tell you WHAT, technicals tell you WHEN. Blunt — "
    "if the thesis is weak, say so clearly. Never pad. Output structured markdown."
)


def _build_prompt(
    nse_code: str,
    name: str,
    sector: str,
    industry: str,
    description: str,
    quality_score,
    conviction_score,
    kg_themes: list[dict],
    relevant_reports: list[tuple[float, dict]],
    all_reports: list[dict] | None = None,
) -> str:
    qs = f"{quality_score:.0f}/100" if quality_score is not None else "—"
    cs = f"{conviction_score:.0f}/100" if conviction_score is not None else "—"

    # KG theme block
    if kg_themes:
        theme_lines = []
        for t in kg_themes:
            thesis = (t.get("thesis") or "")[:200]
            mag = t.get("mag") or "—"
            tg_linked = t.get("tg_themes") or []
            tg_note = f"\n    ↳ Telegram: {', '.join(tg_linked[:3])}" if tg_linked else ""
            theme_lines.append(f"- **{t['theme']}** (magnitude: {mag}){tg_note}\n  {thesis}")
        theme_block = "\n".join(theme_lines)
    else:
        theme_block = "_Company not yet mapped in KG — infer relevance from sector context and research below._"

    # Research block — full detail for relevant reports
    report_blocks = [_compact(r, nse_code) for _, r in relevant_reports]
    research_block = "\n\n---\n\n".join(report_blocks) if report_blocks else ""

    # When keyword matching found nothing, add all reports in ultra-compact form
    # so Claude can do the semantic matching itself
    if len(relevant_reports) < 3 and all_reports:
        seen = {r.get("source") for _, r in relevant_reports}
        ultra = []
        for r in all_reports:
            if r.get("source") in seen:
                continue
            themes = "; ".join((r.get("themes") or [])[:4]) or "—"
            cos = ", ".join(
                c.get("nse_code") or c.get("symbol") or ""
                for c in (r.get("companies") or [])[:5]
                if c.get("nse_code") or c.get("symbol")
            ) or "—"
            src = Path(r.get("source", "?")).stem[:35]
            summary_snippet = (r.get("summary") or "")[:120]
            ultra.append(f"• [{src}] Themes: {themes} | Cos: {cos}\n  {summary_snippet}")
        if ultra:
            bg = "\n".join(ultra)
            research_block += (
                "\n\n---\n\n**Additional research (all reports — select what's relevant "
                f"to {name}):**\n{bg}"
            )

    if not research_block:
        research_block = "_No telegram research available._"

    return f"""## COMPANY PROFILE
**{name}** (`{nse_code}`)
Sector: {sector} | Industry: {industry}
Description: {description or '—'}
KG Quality Score: {qs} | KG Conviction Score: {cs}

## KG THEME ALIGNMENT
{theme_block}

## FRESH TELEGRAM RESEARCH ({len(relevant_reports)} reports)
{research_block}

---

Based on the above data, generate a complete investment summary:

**1. Investment Thesis** — 2–3 sentences. Why this company, why relevant now. Vikram's voice.

**2. Why Now** — What in this week's research makes this timely. Cite specific theme and report.

**3. Key Points** — 5–7 bullets extracted or inferred from the research above. Only include points relevant to this specific company.

**4. Catalysts** — 3–5 specific, actionable bullets. Time-bound where possible.

**5. Risks** — 2–3 honest bullets. What breaks the thesis.

**6. Verdict** — One line: `BUY / ACCUMULATE / WATCH / AVOID` | Conviction: High/Medium/Low | Time Horizon: Trading/6–12M/2Y+

**7. R:R Setup** — Entry zone, stop loss, target 1, target 2, R:R ratio. Use `—` if insufficient price data.

Write in Vikram's voice: direct, data-grounded, no filler. If the thesis is thin, say so."""


# ── Main function ─────────────────────────────────────────────────────────────
def generate_summary(
    nse_code: str,
    days: int = 30,
    dry_run: bool = False,
    save: bool = False,
) -> str:
    nse_code = nse_code.strip().upper()
    print(f"\n[SUMMARY] == {nse_code} ==================================")

    # 1. Company profile
    universe = _load_universe()
    labels   = _load_labels()
    csv_info = universe.get(nse_code, {})

    name        = csv_info.get("name") or nse_code
    sector      = csv_info.get("sector") or "Unknown"
    industry    = csv_info.get("industry") or "Unknown"
    description = labels.get(nse_code) or ""

    quality_score = conviction_score = None
    kg_themes: list[dict] = []

    kg_data = _query_kg(nse_code)
    if kg_data:
        name             = kg_data.get("name") or name
        sector           = kg_data.get("sector") or sector
        industry         = kg_data.get("industry") or industry
        quality_score    = kg_data.get("quality_score")
        conviction_score = kg_data.get("conviction_score")
        kg_themes        = [t for t in (kg_data.get("themes") or []) if t.get("theme")]

    if not csv_info and not kg_data:
        print(f"[SUMMARY] WARNING: {nse_code} not found in NSE universe CSV")

    print(f"[SUMMARY] {name} | {sector} | {industry}")
    print(f"[SUMMARY] KG: quality={quality_score} conviction={conviction_score} themes={len(kg_themes)}")
    print(f"[SUMMARY] Description: {description[:80] or '—'}")

    # Build list of theme names for scoring
    kg_theme_names = [t["theme"] for t in kg_themes if t.get("theme")]
    tg_theme_names = [
        tg for t in kg_themes for tg in (t.get("tg_themes") or [])
    ]

    # 2. Telegram research
    all_reports = _load_telegram_reports(days)
    print(f"[SUMMARY] Telegram reports: {len(all_reports)} loaded (last {days}d)")

    relevant = _find_relevant_reports(
        nse_code, kg_theme_names, tg_theme_names,
        sector, industry, description, all_reports,
    )
    print(f"[SUMMARY] Relevant reports: {len(relevant)}")
    for score, r in relevant:
        direct = nse_code in {
            (c.get("nse_code") or c.get("symbol") or "").upper()
            for c in (r.get("companies") or [])
        }
        tag = "DIRECT" if direct else f"score={score:.2f}"
        themes_preview = ", ".join((r.get("themes") or [])[:2])
        print(f"  [{tag}] {r.get('source','?')} | {themes_preview}")

    # 3. Build prompt
    prompt = _build_prompt(
        nse_code, name, sector, industry, description,
        quality_score, conviction_score, kg_themes, relevant,
        all_reports=all_reports,
    )

    if dry_run:
        sep = "=" * 72
        print(f"\n{sep}\nDRY RUN — assembled context (Claude call skipped)\n{sep}\n")
        print(prompt)
        return prompt

    # 4. Claude call
    if not ANTHROPIC_KEY:
        print("[SUMMARY] ERROR: ANTHROPIC_API_KEY not set in fundamental_context/.env")
        sys.exit(1)
    try:
        import anthropic
    except ImportError:
        print("[SUMMARY] ERROR: pip install anthropic")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    print(f"[SUMMARY] Calling {SONNET_MODEL}...")
    resp = client.messages.create(
        model=SONNET_MODEL,
        max_tokens=2048,
        system=_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    output = resp.content[0].text.strip()

    # 5. Wrap with header
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M IST")
    header = (
        f"# {name} ({nse_code}) — KG Investment Summary\n"
        f"_Generated {date_str} | {len(relevant)} telegram reports | "
        f"KG themes: {len(kg_themes)}_\n\n---\n\n"
    )
    full = header + output

    sep = "=" * 72
    print(f"\n{sep}")
    print(full)
    print(sep)

    if save:
        _SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)
        out_path = _SUMMARIES_DIR / f"{nse_code}_{datetime.now().strftime('%Y-%m-%d')}.md"
        out_path.write_text(full, encoding="utf-8")
        print(f"[SUMMARY] Saved → {out_path}")

    return full


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate KG+Telegram company summary via Claude")
    parser.add_argument("nse_code",  help="NSE code (e.g. KRN, NTPC, SOLARINDS)")
    parser.add_argument("--days",    type=int, default=30,
                        help="Days of telegram history to scan (default: 30)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print assembled context without calling Claude")
    parser.add_argument("--save",    action="store_true",
                        help="Save markdown output to kg_summaries/")
    args = parser.parse_args()

    generate_summary(args.nse_code, days=args.days, dry_run=args.dry_run, save=args.save)


if __name__ == "__main__":
    main()
