#!/usr/bin/env python3
"""
NSE Daily Gainers Brief
Fetches top 20 movers (gainers + value stocks), enriches each with business
description, sector macro from KG themes, and renders a responsive HTML page
with day/night toggle — no Claude API required.

Data cascade per stock:
  1. Neo4j KG  → conviction score, BENEFITS_FROM themes (vikram_thesis)
  2. .company_cache/{SYM}.json  → screener/trendlyne descriptions (30d TTL)
  3. screener.in live scrape  → description (writes to cache)
  4. stock_labels.json  → one-liner fallback

Usage:
  python daily_gainers_brief.py             # fetch, enrich, write HTML
  python daily_gainers_brief.py --dry-run   # print context only, skip HTML
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_HERE = Path(__file__).parent
load_dotenv(_HERE / "fundamental_context" / ".env")

# ── Paths ─────────────────────────────────────────────────────────────────────
_UNIVERSE_CSV = _HERE / "NSE_500cr_15CrNotional10D_50rs_sector_industry.csv"
_LABELS_JSON = _HERE / "tools" / "stock_labels.json"
_CACHE_DIR = _HERE / ".company_cache"
_OUT_DIR = _HERE / "daily_briefs"
_OUT_LATEST = _HERE / "daily_brief.html"

# ── Config ────────────────────────────────────────────────────────────────────
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

TOP_N = 20
CACHE_DAYS = 30

GAINERS_URL = (
    "https://www.nseindia.com/api/live-analysis-variations"
    "?index=gainers&type=allSec&csv=true"
)
VALUE_URL = (
    "https://www.nseindia.com/api/live-analysis-most-active-securities"
    "?index=value&csv=true"
)
_NSE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "*/*, text/csv",
    "Referer": "https://www.nseindia.com/",
}
_SCRAPE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# ── KG Cypher ─────────────────────────────────────────────────────────────────
_Q_COMPANY = """
MATCH (c:Company {nse_code: $nse_code})
RETURN c.name AS name, c.sector AS sector, c.industry AS industry,
       c.quality_score AS quality_score, c.conviction_score AS conviction_score
LIMIT 1
"""
_Q_THEMES = """
MATCH (c:Company {nse_code: $nse_code})-[bf:BENEFITS_FROM]->(t:Theme)
WHERE NOT coalesce(t.source,'') = 'telegram'
RETURN t.name AS theme, t.vikram_thesis AS thesis, bf.magnitude AS magnitude
ORDER BY bf.magnitude DESC LIMIT 3
"""
_Q_CATALYSTS = """
MATCH (c:Company {nse_code: $nse_code})-[:TRIGGERED]->(cat:Catalyst)
WHERE cat.date >= date() - duration('P30D')
RETURN cat.type AS type, toString(cat.date) AS date
ORDER BY cat.date DESC LIMIT 3
"""


# ── Universe / labels ─────────────────────────────────────────────────────────
def _load_universe() -> dict[str, dict]:
    if not _UNIVERSE_CSV.exists():
        return {}
    out: dict[str, dict] = {}
    with open(_UNIVERSE_CSV, encoding="cp1252") as fh:
        for row in csv.DictReader(fh):
            code = (row.get("NSE Code") or "").strip().upper()
            if code:
                out[code] = {
                    "name": (row.get("Stock Name") or "").strip(),
                    "sector": (row.get("sector_name") or "").strip(),
                    "industry": (row.get("Industry Name") or "").strip(),
                }
    return out


def _load_labels() -> dict[str, str]:
    if not _LABELS_JSON.exists():
        return {}
    with open(_LABELS_JSON, encoding="utf-8") as fh:
        return json.load(fh)


# ── Company cache ─────────────────────────────────────────────────────────────
def _cache_path(symbol: str) -> Path:
    return _CACHE_DIR / f"{symbol}.json"


def _load_cache(symbol: str) -> dict | None:
    p = _cache_path(symbol)
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        fetched = datetime.fromisoformat(data.get("fetched_at", "2000-01-01"))
        if fetched.tzinfo is None:
            fetched = fetched.replace(tzinfo=timezone.utc)
        if (datetime.now(timezone.utc) - fetched) > timedelta(days=CACHE_DAYS):
            return None
        return data
    except Exception:
        return None


def _write_cache(symbol: str, screener_desc: str, tl_desc: str = "") -> None:
    _CACHE_DIR.mkdir(exist_ok=True)
    p = _cache_path(symbol)
    # Merge with existing cache if present (preserve trendlyne desc)
    existing = {}
    if p.exists():
        try:
            existing = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            pass
    existing.update(
        {
            "symbol": symbol,
            "screener_description": screener_desc
            or existing.get("screener_description", ""),
            "trendlyne_description": tl_desc
            or existing.get("trendlyne_description", ""),
            "combined_description": screener_desc or tl_desc,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "sources": ["screener"] if screener_desc else [],
        }
    )
    p.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")


# ── NSE data fetch ────────────────────────────────────────────────────────────
def _parse_nse_csv(text: str) -> list[dict]:
    rows = []
    try:
        reader = csv.DictReader(io.StringIO(text))
        for raw in reader:
            row = {k.strip(): v.strip() for k, v in raw.items() if k}
            rows.append(row)
    except Exception:
        pass
    return rows


def _norm_float(s: str) -> float:
    try:
        return float(s.replace(",", "").replace("%", "").strip())
    except Exception:
        return 0.0


def _extract_symbol_change(row: dict) -> tuple[str, float, float]:
    """Return (symbol, ltp, change_pct) from a raw NSE CSV row."""
    sym = ""
    for k in row:
        kl = k.lower().replace(" ", "")
        if kl in ("symbol", "sym"):
            sym = row[k].strip().upper()
            break

    ltp = 0.0
    for k in row:
        kl = k.lower().replace(" ", "")
        if kl in ("ltp", "lasttradedprice", "closeprice", "close", "price"):
            ltp = _norm_float(row[k])
            break

    chg = 0.0
    for k in row:
        kl = k.lower().replace(" ", "").replace("%", "pct")
        if kl in (
            "%chng",
            "pctchng",
            "netchgpct",
            "netprice",
            "changepct",
            "chgpct",
            "pctchange",
        ):
            chg = _norm_float(row[k])
            break
        if "%" in k and "chng" in k.lower():
            chg = _norm_float(row[k])
            break

    return sym, ltp, chg


def _fetch_nse_gainers() -> list[dict]:
    """Fetch both NSE endpoints, combine, dedup, return top TOP_N by % change."""
    print("Fetching NSE gainers...")
    session = requests.Session()
    session.headers.update(_NSE_HEADERS)
    try:
        session.get("https://www.nseindia.com", timeout=10)
    except Exception as e:
        print(f"  [warn] cookie seed failed: {e}")

    combined: dict[str, dict] = {}

    for label, url in [("gainers", GAINERS_URL), ("value", VALUE_URL)]:
        try:
            resp = session.get(url, timeout=15)
            if resp.status_code != 200:
                print(f"  [{label}] HTTP {resp.status_code}")
                continue
            rows = _parse_nse_csv(resp.content.decode("utf-8-sig"))
            added = 0
            for row in rows:
                sym, ltp, chg = _extract_symbol_change(row)
                if not sym:
                    continue
                if label == "value" and chg <= 0:
                    continue  # value list: positive change only
                if sym not in combined or chg > combined[sym]["change_pct"]:
                    combined[sym] = {
                        "symbol": sym,
                        "ltp": ltp,
                        "change_pct": chg,
                        "source_list": label,
                    }
                added += 1
            print(f"  [{label}] {added} rows parsed")
        except Exception as e:
            print(f"  [{label}] error: {e}")

    ranked = sorted(combined.values(), key=lambda x: x["change_pct"], reverse=True)[
        :TOP_N
    ]
    print(f"  Combined top {len(ranked)} stocks after dedup")
    return ranked


# ── Screener.in scrape ────────────────────────────────────────────────────────
def _scrape_screener(symbol: str) -> str:
    """Scrape screener.in for company description. Returns empty string on failure."""
    url = f"https://www.screener.in/company/{symbol}/"
    try:
        resp = requests.get(url, headers=_SCRAPE_HEADERS, timeout=15)
        if resp.status_code != 200:
            return ""
        soup = BeautifulSoup(resp.text, "html.parser")
        for sel in [
            "div.about p",
            "div.company-profile div.about p",
            "section.about-section p",
        ]:
            el = soup.select_one(sel)
            if el:
                text = el.get_text(separator=" ", strip=True)
                if len(text) > 50:
                    return text
    except Exception as e:
        print(f"    [screener] {symbol}: {e}")
    return ""


# ── KG query ──────────────────────────────────────────────────────────────────
def _open_kg_driver():
    try:
        from neo4j import GraphDatabase

        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
        driver.verify_connectivity()
        return driver
    except Exception as e:
        print(f"  [KG] unavailable ({type(e).__name__}) — using cache/scrape fallback")
        return None


def _query_kg(symbol: str, driver) -> dict:
    """Return KG data dict (empty dict if not found)."""
    result: dict = {}
    try:
        with driver.session() as sess:
            rec = sess.run(_Q_COMPANY, nse_code=symbol).single()
            if not rec:
                return result
            result.update(dict(rec))
            result["themes"] = [dict(r) for r in sess.run(_Q_THEMES, nse_code=symbol)]
            result["catalysts"] = [
                dict(r) for r in sess.run(_Q_CATALYSTS, nse_code=symbol)
            ]
    except Exception as e:
        print(f"    [KG] {symbol}: {e}")
    return result


# ── Context enrichment ────────────────────────────────────────────────────────
def _first_sentence(text: str) -> str:
    if not text:
        return ""
    for sep in (". ", "! ", "? "):
        idx = text.find(sep)
        if idx > 40:
            return text[: idx + 1].strip()
    return text[:200].strip()


def _enrich(stock: dict, universe: dict, labels: dict, kg_driver) -> dict:
    sym = stock["symbol"]
    uni = universe.get(sym, {})

    ctx: dict = {
        "symbol": sym,
        "name": uni.get("name", sym),
        "sector": uni.get("sector", ""),
        "industry": uni.get("industry", ""),
        "ltp": stock["ltp"],
        "change_pct": stock["change_pct"],
        "label": labels.get(sym, ""),
        "business": "",
        "tl_desc": "",
        "themes": [],
        "catalysts": [],
        "conviction": None,
        "quality": None,
        "kg_source": False,
    }

    # [C] KG first
    if kg_driver:
        kg = _query_kg(sym, kg_driver)
        if kg:
            ctx["kg_source"] = True
            ctx["conviction"] = kg.get("conviction_score")
            ctx["quality"] = kg.get("quality_score")
            if kg.get("sector"):
                ctx["sector"] = kg["sector"]
            if kg.get("industry"):
                ctx["industry"] = kg["industry"]
            if kg.get("name"):
                ctx["name"] = kg["name"]
            ctx["themes"] = kg.get("themes", [])
            ctx["catalysts"] = kg.get("catalysts", [])

    # [D] Cache
    cached = _load_cache(sym)
    if cached:
        ctx["business"] = cached.get("screener_description") or cached.get(
            "combined_description", ""
        )
        ctx["tl_desc"] = cached.get("trendlyne_description", "")

    # [E] Scrape screener.in if no description yet
    if not ctx["business"]:
        print(f"    [scrape] {sym} ...", end=" ", flush=True)
        desc = _scrape_screener(sym)
        if desc:
            ctx["business"] = desc
            _write_cache(sym, desc)
            print("ok")
        else:
            print("—")
        time.sleep(1.5)

    return ctx


# ── Content assembly ──────────────────────────────────────────────────────────
def _assemble(ctx: dict) -> dict:
    business = ctx["business"] or ctx["label"] or f"{ctx['sector']} company"

    # Products: trendlyne tends to list key segments; else first sentence of business desc
    products = ctx["tl_desc"] or _first_sentence(ctx["business"]) or ctx["label"]

    # Macro: join vikram_thesis from KG themes (top 2); else plain sector/industry
    if ctx["themes"]:
        theses = [t["thesis"] for t in ctx["themes"] if t.get("thesis")]
        macro = (
            "  ".join(theses[:2]) if theses else f"{ctx['industry']} · {ctx['sector']}"
        )
    else:
        macro = (
            f"{ctx['industry']} · {ctx['sector']}"
            if (ctx["industry"] or ctx["sector"])
            else ""
        )

    return {
        **ctx,
        "business_text": business,
        "products_text": products,
        "macro_text": macro,
    }


# ── HTML generation ───────────────────────────────────────────────────────────
_CSS = """
/* Light mode */
:root{
  --bg:#F8F6F2;--bg2:#EDEAE0;--bg3:#E3DFD4;--bd:#D0CBC0;
  --tx:#1A1A1A;--mu:#666;
  --grn:#1a6b2e;--red:#b91c1c;--blu:#1A365D;--acc:#0D5C75;
  --tag-bg:#EBF4F8;--tag-tx:#0D5C75;--tag-bd:#A8D4E2;
  --theme-bg:#F0EBF8;--theme-bd:#D0BCE8;--theme-tx:#5b21b6;
  --cat-bg:#FEF3C7;--cat-bd:#D4A84B;--cat-tx:#854d0e;
  --cv-bg:#D4EED9;--cv-bd:#8EC89A;--cv-tx:#1a6b2e;
}
/* Dark mode */
body.dark{
  --bg:#0d1117;--bg2:#161b22;--bg3:#21262d;--bd:#30363d;
  --tx:#e6edf3;--mu:#8b949e;
  --grn:#4ade80;--red:#f87171;--blu:#58a6ff;--acc:#A8D5E3;
  --tag-bg:rgba(168,213,227,.1);--tag-tx:#A8D5E3;--tag-bd:rgba(168,213,227,.3);
  --theme-bg:rgba(192,132,252,.1);--theme-bd:rgba(192,132,252,.25);--theme-tx:#c084fc;
  --cat-bg:rgba(251,211,141,.1);--cat-bd:rgba(251,211,141,.3);--cat-tx:#FBD38D;
  --cv-bg:rgba(74,222,128,.1);--cv-bd:rgba(74,222,128,.25);--cv-tx:#4ade80;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;font-size:13px;
     background:var(--bg);color:var(--tx);transition:background .2s,color .2s;
     min-height:100vh}

/* Top bar */
#topbar{background:var(--bg2);border-bottom:2px solid var(--bd);
        padding:10px 16px;display:flex;align-items:center;gap:10px;
        position:sticky;top:0;z-index:10}
#topbar h1{font-size:15px;font-weight:700;letter-spacing:.3px}
#topbar h1 span{color:var(--acc)}
.tb-meta{color:var(--mu);font-size:11px;margin-left:4px}
#toggle{margin-left:auto;background:transparent;border:1px solid var(--bd);
        border-radius:20px;padding:4px 10px;cursor:pointer;font-size:12px;
        color:var(--tx);font-family:inherit;transition:.15s}
#toggle:hover{border-color:var(--acc);color:var(--acc)}

/* Summary table */
#summary{padding:12px 16px;background:var(--bg2);border-bottom:1px solid var(--bd);overflow-x:auto}
.stbl{width:100%;border-collapse:collapse;font-size:12px}
.stbl th{padding:5px 9px;text-align:left;color:var(--mu);text-transform:uppercase;
         font-size:10px;letter-spacing:.4px;cursor:pointer;white-space:nowrap;user-select:none}
.stbl th:hover{color:var(--acc)}
.stbl td{padding:5px 9px;border-top:1px solid var(--bd);vertical-align:middle}
.stbl tr:hover td{background:var(--bg3)}
.sym-link{color:var(--acc);font-weight:700;text-decoration:none}
.sym-link:hover{text-decoration:underline}
.sc-link{margin-left:5px;font-size:10px;font-weight:600;padding:1px 5px;border-radius:3px;
         text-decoration:none;background:var(--mu);color:var(--bg);opacity:.7;vertical-align:middle}
.sc-link:hover{opacity:1}
.pos{color:var(--grn);font-weight:600}
.neg{color:var(--red);font-weight:600}

/* Cards grid */
#cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));
       gap:16px;padding:16px;max-width:1600px;margin:0 auto}
@media(max-width:600px){
  #cards{grid-template-columns:1fr;padding:10px}
  #topbar{flex-wrap:wrap}
  .tb-meta{display:none}
}

/* Individual card */
.card{background:var(--bg2);border:1px solid var(--bd);border-radius:8px;
      padding:14px 16px;display:flex;flex-direction:column;gap:10px;
      border-left:3px solid var(--bd)}
.card.kg-card{border-left-color:var(--grn)}

.card-hdr{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
.c-sym{font-size:15px;font-weight:700;text-decoration:none;color:var(--acc)}
.c-sym:hover{text-decoration:underline}
.c-sc{font-size:10px;font-weight:600;padding:1px 5px;border-radius:3px;
      text-decoration:none;background:var(--mu);color:var(--bg);opacity:.7;vertical-align:middle}
.c-sc:hover{opacity:1}
.c-name{font-size:12px;color:var(--mu);flex:1;min-width:0;overflow:hidden;
        text-overflow:ellipsis;white-space:nowrap}
.c-chg{font-size:13px;font-weight:700;margin-left:auto;white-space:nowrap}

.c-sector{font-size:10px;color:var(--mu);background:var(--bg3);
          padding:2px 8px;border-radius:10px;width:fit-content}

.sec-label{font-size:10px;color:var(--mu);text-transform:uppercase;
           letter-spacing:.5px;font-weight:600;margin-bottom:2px}
.sec-body{font-size:12px;line-height:1.6;color:var(--tx)}
.sec-small{font-size:11px;color:var(--mu)}

/* KG pills row */
.kg-row{display:flex;flex-wrap:wrap;gap:5px;margin-top:2px}
.kp{padding:2px 8px;border-radius:10px;font-size:10px;font-weight:600;
    border:1px solid;white-space:nowrap}
.kp-theme{background:var(--theme-bg);border-color:var(--theme-bd);color:var(--theme-tx)}
.kp-cat{background:var(--cat-bg);border-color:var(--cat-bd);color:var(--cat-tx)}
.kp-cv{background:var(--cv-bg);border-color:var(--cv-bd);color:var(--cv-tx)}
"""

_JS = """
const t=document.getElementById('toggle');
function applyTheme(d){
  document.body.classList.toggle('dark',d);
  t.textContent=d?'☀ Light':'🌙 Dark';
}
t.onclick=()=>{const d=!document.body.classList.contains('dark');applyTheme(d);localStorage.setItem('theme',d?'dark':'light')};
applyTheme(localStorage.getItem('theme')==='dark');

// Sortable summary table
document.querySelectorAll('.stbl th[data-col]').forEach(th=>{
  th.onclick=()=>{
    const col=th.dataset.col,num=th.dataset.num==='1';
    const tbody=th.closest('table').querySelector('tbody');
    const rows=[...tbody.querySelectorAll('tr')];
    const asc=th.dataset.asc!=='1';
    rows.sort((a,b)=>{
      const av=a.querySelector(`td[data-col="${col}"]`)?.textContent.replace(/[%,+₹]/g,'').trim()||'';
      const bv=b.querySelector(`td[data-col="${col}"]`)?.textContent.replace(/[%,+₹]/g,'').trim()||'';
      return num?(parseFloat(av)-parseFloat(bv))*(asc?1:-1):av.localeCompare(bv)*(asc?1:-1);
    });
    rows.forEach(r=>tbody.appendChild(r));
    th.dataset.asc=asc?'1':'';
  };
});
"""


def _html_card(c: dict) -> str:
    sym = c["symbol"]
    tv_url = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
    sc_url = f"https://www.screener.in/company/{sym}/"
    chg = c["change_pct"]
    chg_cls = "pos" if chg >= 0 else "neg"
    chg_str = f"+{chg:.2f}%" if chg >= 0 else f"{chg:.2f}%"
    sector = " · ".join(filter(None, [c.get("industry"), c.get("sector")]))
    kg_cls = "card kg-card" if c["kg_source"] else "card"

    business = _esc(c.get("business_text", ""))
    products = _esc(c.get("products_text", ""))
    macro = _esc(c.get("macro_text", ""))

    pills = ""
    for th in c.get("themes", [])[:3]:
        pills += f'<span class="kp kp-theme">{_esc(th["theme"])}</span>'
    for cat in c.get("catalysts", [])[:2]:
        days_ago = ""
        try:
            d = datetime.strptime(cat["date"][:10], "%Y-%m-%d")
            days_ago = f" · {(datetime.now() - d).days}d ago"
        except Exception:
            pass
        pills += f'<span class="kp kp-cat">{_esc(cat["type"])}{days_ago}</span>'
    if c.get("conviction") is not None:
        pills += f'<span class="kp kp-cv">CV {int(c["conviction"])}</span>'

    kg_row = f'<div class="kg-row">{pills}</div>' if pills else ""

    products_section = ""
    if products and products != business[: len(products)]:
        products_section = f"""
      <div class="sec-label">Products &amp; Segments</div>
      <p class="sec-body sec-small">{products}</p>"""

    macro_section = ""
    if macro:
        macro_section = f"""
      <div class="sec-label">Macro &amp; Sector</div>
      <p class="sec-body">{macro}</p>"""

    return f"""
    <div class="{kg_cls}">
      <div class="card-hdr">
        <a class="c-sym" href="{tv_url}" target="_blank">{sym}</a>
        <a class="c-sc" href="{sc_url}" target="_blank">SC</a>
        <span class="c-name">{_esc(c['name'])}</span>
        <span class="c-chg {chg_cls}">{chg_str}</span>
      </div>
      {f'<div class="c-sector">{_esc(sector)}</div>' if sector else ''}
      <div>
        <div class="sec-label">Business</div>
        <p class="sec-body">{business}</p>
      </div>{products_section}{macro_section}
      {kg_row}
    </div>"""


def _html_table_row(i: int, c: dict) -> str:
    sym = c["symbol"]
    tv_url = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
    sc_url = f"https://www.screener.in/company/{sym}/"
    chg = c["change_pct"]
    chg_cls = "pos" if chg >= 0 else "neg"
    chg_str = f"+{chg:.2f}%" if chg >= 0 else f"{chg:.2f}%"
    sector = c.get("sector", "")
    return (
        f"<tr>"
        f'<td data-col="rank">{i}</td>'
        f'<td data-col="sym"><a class="sym-link" href="{tv_url}" target="_blank">{sym}</a>'
        f'<a class="sc-link" href="{sc_url}" target="_blank">SC</a></td>'
        f'<td data-col="name">{_esc(c["name"])}</td>'
        f'<td data-col="chg" class="{chg_cls}">{chg_str}</td>'
        f'<td data-col="ltp">{c["ltp"]:.2f}</td>'
        f'<td data-col="sector">{_esc(sector)}</td>'
        f"</tr>"
    )


def _esc(s: str) -> str:
    return (
        (s or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _build_html(cards: list[dict], date_str: str, gen_time: str) -> str:
    table_rows = "\n".join(_html_table_row(i + 1, c) for i, c in enumerate(cards))
    card_html = "\n".join(_html_card(c) for c in cards)
    kg_count = sum(1 for c in cards if c["kg_source"])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NSE Daily Brief — {date_str}</title>
<style>{_CSS}</style>
</head>
<body>

<div id="topbar">
  <h1>NSE Daily Brief &nbsp;<span>{date_str}</span></h1>
  <span class="tb-meta">Top {len(cards)} movers · Gainers + Value</span>
  <span class="tb-meta">· {gen_time} IST</span>
  {f'<span class="tb-meta">· KG: {kg_count}/{len(cards)}</span>' if kg_count else ''}
  <button id="toggle">🌙 Dark</button>
</div>

<div id="summary">
  <table class="stbl">
    <thead>
      <tr>
        <th data-col="rank">#</th>
        <th data-col="sym">Symbol</th>
        <th data-col="name">Name</th>
        <th data-col="chg" data-num="1">Chg%</th>
        <th data-col="ltp" data-num="1">Close</th>
        <th data-col="sector">Sector</th>
      </tr>
    </thead>
    <tbody>
{table_rows}
    </tbody>
  </table>
</div>

<div id="cards">
{card_html}
</div>

<script>{_JS}</script>
</body>
</html>"""


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print enriched context only — skip HTML write",
    )
    args = parser.parse_args()

    today = datetime.now().strftime("%Y-%m-%d")
    gen_time = datetime.now().strftime("%H:%M")
    date_str = datetime.now().strftime("%d %b %Y")

    print("\n=== NSE Daily Gainers Brief ===")
    print(f"Date: {today}  Time: {gen_time}\n")

    universe = _load_universe()
    labels = _load_labels()
    print(f"Universe: {len(universe)} stocks  Labels: {len(labels)}")

    stocks = _fetch_nse_gainers()
    if not stocks:
        print("No stocks fetched — aborting.")
        return

    kg_driver = _open_kg_driver()

    print(f"\nEnriching {len(stocks)} stocks...")
    enriched = []
    for i, stock in enumerate(stocks, 1):
        sym = stock["symbol"]
        print(f"  [{i:02d}/{len(stocks)}] {sym:<18}", end=" ")
        ctx = _enrich(stock, universe, labels, kg_driver)
        card = _assemble(ctx)
        enriched.append(card)
        src = "KG" if ctx["kg_source"] else ("cache" if ctx["business"] else "—")
        print(f"src={src}")

    if kg_driver:
        kg_driver.close()

    if args.dry_run:
        print("\n--- DRY RUN: enriched context ---")
        for c in enriched:
            print(f"\n{'─'*60}")
            print(f"  {c['symbol']} ({c['change_pct']:+.1f}%) — {c['name']}")
            print(f"  Sector  : {c['sector']} · {c['industry']}")
            print(f"  Business: {c['business_text'][:120]}...")
            print(f"  Macro   : {c['macro_text'][:120]}...")
            if c["themes"]:
                print(f"  Themes  : {[t['theme'] for t in c['themes']]}")
        return

    html = _build_html(enriched, date_str, gen_time)

    _OUT_DIR.mkdir(exist_ok=True)
    dated = _OUT_DIR / f"daily_brief_{today}.html"
    dated.write_text(html, encoding="utf-8")
    _OUT_LATEST.write_text(html, encoding="utf-8")

    print(f"\n  Saved → {_OUT_LATEST}")
    print(f"  Saved → {dated}")
    print(
        f"\n  {len(enriched)} cards  |  KG: {sum(1 for c in enriched if c['kg_source'])}  |  "
        f"Cache: {sum(1 for c in enriched if not c['kg_source'] and c['business'])}  |  "
        f"Scraped: {sum(1 for c in enriched if not c['kg_source'] and not _load_cache(c['symbol']))}"
    )


if __name__ == "__main__":
    main()
