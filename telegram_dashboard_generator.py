"""
Telegram Themes Dashboard Generator

Reads all telegram_themes/themes_*.json files and generates
telegram_themes/index.html — a self-contained GitHub Pages-ready dashboard.

Run  : python telegram_dashboard_generator.py
Output: telegram_themes/index.html
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

_HERE    = Path(__file__).parent
_THEMES_DIR = _HERE / "telegram_themes"
_OUT     = _THEMES_DIR / "index.html"


def _tv_link(symbol: str) -> str:
    clean = re.sub(r"\.(BO|NS)$", "", symbol.upper())
    return f"https://www.tradingview.com/chart/?symbol=NSE%3A{clean}"


def _conviction_cls(conviction: str) -> str:
    c = (conviction or "").lower()
    if "high" in c:   return "conv-high"
    if "medium" in c: return "conv-med"
    return "conv-low"


def _sentiment_cls(sentiment: str) -> str:
    s = (sentiment or "").lower()
    if "bullish" in s: return "sent-bull"
    if "bearish" in s: return "sent-bear"
    return "sent-neu"


def _theme_color(idx: int) -> str:
    palette = ["#58a6ff", "#3fb950", "#a371f7", "#d29922", "#f85149",
               "#79c0ff", "#56d364", "#bc8cff", "#e3b341", "#ff7b72"]
    return palette[idx % len(palette)]


def _load_all_data() -> dict[str, list[dict]]:
    """Load all themes_*.json files. Returns {date: [reports]}."""
    data: dict[str, list[dict]] = {}
    for p in sorted(_THEMES_DIR.glob("themes_*.json"), reverse=True):
        m = re.search(r"themes_(\d{4}-\d{2}-\d{2})\.json", p.name)
        if not m:
            continue
        date = m.group(1)
        with open(p, encoding="utf-8") as fh:
            obj = json.load(fh)
        data[date] = obj.get("reports", [])
    return data


def _build_html(data: dict[str, list[dict]]) -> str:
    dates     = sorted(data.keys(), reverse=True)
    all_dates_json = json.dumps(dates)
    data_json = json.dumps(data, ensure_ascii=False)
    now       = datetime.now().strftime("%Y-%m-%d %H:%M IST")

    # ── Pre-build theme sidebar items for each date ──────────────────────────
    # (used for non-JS fallback; JS overrides at runtime)

    css = """
:root {
  --bg:#0d1117; --bg2:#161b22; --bg3:#21262d; --bd:#30363d;
  --tx:#e6edf3; --mu:#8b949e;
  --grn:#3fb950; --red:#f85149; --blu:#58a6ff; --pur:#a371f7;
  --ylw:#d29922; --gld:#ffd700;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;font-size:13px;
     background:var(--bg);color:var(--tx);height:100vh;display:flex;flex-direction:column;overflow:hidden}

/* ── Top bar ── */
#topbar{background:var(--bg2);border-bottom:1px solid var(--bd);
        padding:10px 16px;display:flex;align-items:center;gap:12px;flex-shrink:0}
#topbar h1{font-size:15px;font-weight:700;color:var(--tx);letter-spacing:.3px}
#topbar h1 span{color:var(--blu)}
#topbar .tagline{color:var(--mu);font-size:11px;margin-left:4px}
.date-tabs{display:flex;gap:6px;margin-left:auto}
.date-tab{padding:4px 10px;border-radius:20px;border:1px solid var(--bd);
          background:transparent;color:var(--mu);cursor:pointer;font-size:11px;
          font-family:inherit;transition:.15s}
.date-tab:hover{border-color:var(--blu);color:var(--blu)}
.date-tab.active{background:var(--blu);border-color:var(--blu);color:#fff;font-weight:600}
#gen-time{color:var(--mu);font-size:10px;white-space:nowrap}

/* ── Stats bar ── */
#statsbar{background:var(--bg2);border-bottom:1px solid var(--bd);
          padding:6px 16px;display:flex;gap:20px;flex-shrink:0}
.stat{display:flex;align-items:center;gap:5px}
.stat-val{font-size:13px;font-weight:700;color:var(--tx)}
.stat-lbl{font-size:10px;color:var(--mu);text-transform:uppercase;letter-spacing:.4px}
.stat-dot{width:6px;height:6px;border-radius:50%}

/* ── Main layout ── */
#main{display:flex;flex:1;overflow:hidden}

/* ── Sidebar ── */
#sidebar{width:240px;background:var(--bg2);border-right:1px solid var(--bd);
         overflow-y:auto;flex-shrink:0;padding:8px 0}
.sidebar-section{padding:4px 12px;font-size:10px;color:var(--mu);
                 text-transform:uppercase;letter-spacing:.5px;margin-top:8px}
.theme-item{padding:8px 14px;cursor:pointer;border-left:3px solid transparent;
            transition:.12s;display:flex;align-items:flex-start;gap:8px}
.theme-item:hover{background:var(--bg3)}
.theme-item.active{background:var(--bg3)}
.theme-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;margin-top:3px}
.theme-name{font-size:12px;color:var(--tx);line-height:1.4;font-weight:500}
.theme-sub{font-size:10px;color:var(--mu);margin-top:1px}
.theme-conv{font-size:9px;padding:1px 5px;border-radius:8px;
            margin-left:auto;flex-shrink:0;font-weight:600}

/* ── Detail panel ── */
#detail{flex:1;overflow-y:auto;padding:20px 24px}
#detail-inner{max-width:900px}

.detail-header{margin-bottom:16px}
.detail-title{font-size:20px;font-weight:700;color:var(--tx);line-height:1.3;margin-bottom:8px}
.detail-meta{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.badge{padding:3px 8px;border-radius:10px;font-size:10px;font-weight:600;letter-spacing:.2px}
.conv-high{background:rgba(63,185,80,.15);border:1px solid rgba(63,185,80,.3);color:var(--grn)}
.conv-med {background:rgba(210,153,34,.15);border:1px solid rgba(210,153,34,.3);color:var(--ylw)}
.conv-low {background:rgba(139,148,158,.15);border:1px solid rgba(139,148,158,.3);color:var(--mu)}
.badge-horizon{background:rgba(88,166,255,.1);border:1px solid rgba(88,166,255,.25);color:var(--blu)}
.badge-src{background:transparent;border:1px solid var(--bd);color:var(--mu);font-weight:400}

.summary-box{background:var(--bg2);border:1px solid var(--bd);border-left:3px solid var(--blu);
             border-radius:6px;padding:12px 14px;margin:16px 0;
             font-size:13px;color:var(--tx);line-height:1.6}

.section{margin:20px 0}
.section-title{font-size:10px;color:var(--mu);text-transform:uppercase;letter-spacing:.5px;
               font-weight:600;margin-bottom:10px;padding-bottom:6px;border-bottom:1px solid var(--bd)}

/* ── Companies table ── */
.co-table{width:100%;border-collapse:collapse;border:1px solid var(--bd);border-radius:6px;overflow:hidden}
.co-table th{background:var(--bg3);color:var(--mu);font-size:10px;text-transform:uppercase;
             letter-spacing:.5px;padding:7px 10px;text-align:left;font-weight:600}
.co-table td{padding:8px 10px;border-top:1px solid var(--bd);vertical-align:middle}
.co-table tr:hover td{background:var(--bg3)}
.sym-link{font-family:monospace;font-size:12px;font-weight:700;color:var(--blu);
          text-decoration:none;letter-spacing:.3px}
.sym-link:hover{text-decoration:underline}
.co-name{font-size:12px;color:var(--tx)}
.sent-bull{color:var(--grn);font-size:11px;font-weight:600}
.sent-bear{color:var(--red);font-size:11px;font-weight:600}
.sent-neu {color:var(--mu);font-size:11px}
.res-badge{display:inline-block;margin-left:4px;padding:1px 5px;border-radius:6px;
           font-size:9px;font-weight:700;vertical-align:middle;letter-spacing:.3px}
.res-ok{background:rgba(63,185,80,.15);border:1px solid rgba(63,185,80,.3);color:var(--grn)}
.res-fz{background:rgba(210,153,34,.12);border:1px solid rgba(210,153,34,.3);color:var(--ylw)}

/* ── Key points ── */
.kp-list{list-style:none;display:flex;flex-direction:column;gap:6px}
.kp-list li{padding:7px 10px 7px 14px;background:var(--bg2);border:1px solid var(--bd);
            border-radius:4px;border-left:3px solid var(--pur);
            font-size:12px;color:var(--tx);line-height:1.5;position:relative}

/* ── Catalysts ── */
.catalysts{display:flex;flex-wrap:wrap;gap:6px}
.catalyst{padding:4px 10px;background:rgba(163,113,247,.1);
          border:1px solid rgba(163,113,247,.25);border-radius:10px;
          font-size:11px;color:var(--pur)}

/* ── Empty state ── */
.empty{text-align:center;padding:60px 20px;color:var(--mu)}
.empty-icon{font-size:40px;margin-bottom:12px}

/* ── Scrollbars ── */
::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bd);border-radius:3px}

@media(max-width:700px){
  #sidebar{display:none}
  #detail{padding:12px}
}
"""

    js = f"""
const ALL_DATA = {data_json};
const ALL_DATES = {all_dates_json};

let currentDate = ALL_DATES[0] || '';
let currentIdx  = 0;

const PALETTE = ['#58a6ff','#3fb950','#a371f7','#d29922','#f85149',
                 '#79c0ff','#56d364','#bc8cff','#e3b341','#ff7b72'];

function tvLink(co) {{
  // Use resolver-verified nse_code when confidence >= 0.60; fall back to raw symbol
  const conf = co.res_conf || 0;
  const sym  = (conf >= 0.60 && co.nse_code && co.nse_code !== 'null')
               ? co.nse_code
               : (co.symbol || '');
  if(!sym || sym === '—') return null;
  const clean = sym.replace(/\\.(BO|NS|NSE|BSE)$/i,'').toUpperCase();
  if(!clean) return null;
  return `https://www.tradingview.com/chart/?symbol=NSE%3A${{clean}}`;
}}

function confBadge(co) {{
  const conf = co.res_conf || 0;
  const method = co.res_method || '';
  if(method === 'non_nse' || method === 'unresolved' || method === 'no_universe') return '';
  if(conf >= 0.85) return '<span class="res-badge res-ok" title="Exact/high-confidence NSE match">NSE</span>';
  if(conf >= 0.60) return '<span class="res-badge res-fz" title="Fuzzy NSE match">~NSE</span>';
  return '';
}}

function convClass(c) {{
  const l = (c||'').toLowerCase();
  if(l.includes('high'))   return 'conv-high';
  if(l.includes('medium')) return 'conv-med';
  return 'conv-low';
}}

function sentClass(s) {{
  const l = (s||'').toLowerCase();
  if(l.includes('bull')) return 'sent-bull';
  if(l.includes('bear')) return 'sent-bear';
  return 'sent-neu';
}}

function renderSidebar(date) {{
  const reports = ALL_DATA[date] || [];
  const el = document.getElementById('sidebar');
  if(!reports.length) {{ el.innerHTML='<div style="padding:20px;color:var(--mu);text-align:center">No reports</div>'; return; }}

  let html = '<div class="sidebar-section">Themes</div>';
  reports.forEach((r, i) => {{
    const themes = (r.themes||[]).join(', ') || 'Unknown';
    const shortTheme = themes.length > 32 ? themes.slice(0,30)+'…' : themes;
    const cos = (r.companies||[]).map(c=>{{
      const conf = c.res_conf||0;
      return (conf>=0.60 && c.nse_code && c.nse_code!=='null') ? c.nse_code : (c.symbol||'—');
    }}).join(', ') || '—';
    const shortCo = cos.length > 28 ? cos.slice(0,26)+'…' : cos;
    const color  = PALETTE[i % PALETTE.length];
    const cc     = convClass(r.conviction);
    const cls    = i === currentIdx ? 'theme-item active' : 'theme-item';
    html += `<div class="${{cls}}" onclick="selectTheme(${{i}})" style="border-left-color:${{i===currentIdx?color:'transparent'}}">
      <span class="theme-dot" style="background:${{color}}"></span>
      <div>
        <div class="theme-name">${{shortTheme}}</div>
        <div class="theme-sub">${{shortCo}}</div>
      </div>
      <span class="badge theme-conv ${{cc}}">${{r.conviction||'—'}}</span>
    </div>`;
  }});
  el.innerHTML = html;
}}

function renderDetail(date, idx) {{
  const reports = ALL_DATA[date] || [];
  const el = document.getElementById('detail-inner');
  if(!reports.length) {{
    el.innerHTML = '<div class="empty"><div class="empty-icon">📭</div><div>No reports for this date</div></div>';
    return;
  }}
  const r = reports[idx] || reports[0];
  const color = PALETTE[idx % PALETTE.length];
  const themes = (r.themes||[]).join(' · ') || 'Unknown Theme';
  const cc = convClass(r.conviction);

  // Companies
  const cos = r.companies||[];
  let coHtml = '';
  if(cos.length) {{
    coHtml = `<table class="co-table">
      <thead><tr><th>Symbol</th><th>Company</th><th>Sentiment</th></tr></thead><tbody>`;
    cos.forEach(c => {{
      const sc   = sentClass(c.sentiment);
      const sent = (c.sentiment||'—').charAt(0).toUpperCase()+(c.sentiment||'—').slice(1);
      const conf = c.res_conf || 0;
      const dispSym = (conf >= 0.60 && c.nse_code && c.nse_code !== 'null')
                      ? c.nse_code : (c.symbol||'—');
      const link = tvLink(c);
      const symHtml = link
        ? `<a class="sym-link" href="${{link}}" target="_blank">${{dispSym}}</a>${{confBadge(c)}}`
        : `<span style="color:var(--mu)">${{dispSym}}</span>`;
      coHtml += `<tr>
        <td>${{symHtml}}</td>
        <td><span class="co-name">${{c.name||'—'}}</span></td>
        <td><span class="${{sc}}">${{sent}}</span></td>
      </tr>`;
    }});
    coHtml += '</tbody></table>';
  }}

  // Key points
  const kps = r.key_points||[];
  let kpHtml = '';
  if(kps.length) {{
    kpHtml = '<ul class="kp-list">' + kps.map(k=>`<li>${{k}}</li>`).join('') + '</ul>';
  }}

  // Catalysts
  const cats = r.catalysts||[];
  let catHtml = '';
  if(cats.length) {{
    catHtml = '<div class="catalysts">' + cats.map(c=>`<span class="catalyst">${{c}}</span>`).join('') + '</div>';
  }}

  el.innerHTML = `
    <div class="detail-header">
      <div class="detail-title" style="border-left:3px solid ${{color}};padding-left:10px">${{themes}}</div>
      <div class="detail-meta">
        <span class="badge ${{cc}}">${{r.conviction||'—'}} Conviction</span>
        <span class="badge badge-horizon">⏱ ${{r.time_horizon||'—'}}</span>
        <span class="badge badge-src">📄 ${{r.source||'—'}}</span>
        <span class="badge badge-src">📅 ${{r.date||date}}</span>
      </div>
    </div>
    <div class="summary-box">${{r.summary||'No summary available.'}}</div>
    ${{cos.length ? `<div class="section"><div class="section-title">Companies</div>${{coHtml}}</div>` : ''}}
    ${{kps.length ? `<div class="section"><div class="section-title">Key Points</div>${{kpHtml}}</div>` : ''}}
    ${{cats.length ? `<div class="section"><div class="section-title">Catalysts</div>${{catHtml}}</div>` : ''}}
  `;
}}

function renderStats(date) {{
  const reports = ALL_DATA[date] || [];
  const themes  = new Set(reports.flatMap(r=>r.themes||[]));
  const cos     = new Set(reports.flatMap(r=>(r.companies||[]).map(c=>{{
    const conf = c.res_conf||0;
    return (conf>=0.60 && c.nse_code && c.nse_code!=='null') ? c.nse_code : c.symbol;
  }})));
  const highs   = reports.filter(r=>(r.conviction||'').toLowerCase().includes('high')).length;
  document.getElementById('stat-reports').textContent = reports.length;
  document.getElementById('stat-themes').textContent  = themes.size;
  document.getElementById('stat-cos').textContent     = cos.size;
  document.getElementById('stat-high').textContent    = highs;
}}

function renderDateTabs() {{
  const el = document.getElementById('date-tabs');
  el.innerHTML = ALL_DATES.map(d =>
    `<button class="date-tab${{d===currentDate?' active':''}}" onclick="switchDate('${{d}}')">${{d}}</button>`
  ).join('');
}}

function switchDate(date) {{
  currentDate = date;
  currentIdx  = 0;
  renderDateTabs();
  renderSidebar(date);
  renderStats(date);
  renderDetail(date, 0);
}}

function selectTheme(idx) {{
  currentIdx = idx;
  renderSidebar(currentDate);
  renderDetail(currentDate, idx);
  document.getElementById('detail').scrollTop = 0;
}}

// Init
renderDateTabs();
renderSidebar(currentDate);
renderStats(currentDate);
renderDetail(currentDate, 0);
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Telegram Equity Insights</title>
<style>{css}</style>
</head>
<body>

<div id="topbar">
  <h1>📊 <span>Telegram</span> Equity Insights</h1>
  <span class="tagline">— research themes & coverage</span>
  <div class="date-tabs" id="date-tabs"></div>
  <span id="gen-time">Updated {now}</span>
</div>

<div id="statsbar">
  <div class="stat">
    <span class="stat-dot" style="background:var(--blu)"></span>
    <span class="stat-val" id="stat-reports">—</span>
    <span class="stat-lbl">Reports</span>
  </div>
  <div class="stat">
    <span class="stat-dot" style="background:var(--pur)"></span>
    <span class="stat-val" id="stat-themes">—</span>
    <span class="stat-lbl">Themes</span>
  </div>
  <div class="stat">
    <span class="stat-dot" style="background:var(--grn)"></span>
    <span class="stat-val" id="stat-cos">—</span>
    <span class="stat-lbl">Companies</span>
  </div>
  <div class="stat">
    <span class="stat-dot" style="background:var(--gld)"></span>
    <span class="stat-val" id="stat-high">—</span>
    <span class="stat-lbl">High Conviction</span>
  </div>
</div>

<div id="main">
  <nav id="sidebar"></nav>
  <div id="detail">
    <div id="detail-inner"></div>
  </div>
</div>

<script>{js}</script>
</body>
</html>"""

    return html


def main() -> None:
    data = _load_all_data()
    if not data:
        print(f"[DASH] No themes_*.json files found in {_THEMES_DIR}")
        print("       Run telegram_parser.py first to generate JSON data.")
        return

    _THEMES_DIR.mkdir(parents=True, exist_ok=True)
    html = _build_html(data)
    _OUT.write_text(html, encoding="utf-8")

    total_reports = sum(len(v) for v in data.values())
    print(f"[DASH] Generated: {_OUT}")
    print(f"       {len(data)} date(s) | {total_reports} total report(s)")


if __name__ == "__main__":
    main()
