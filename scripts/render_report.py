#!/usr/bin/env python3
"""
render_report.py  —  JSON → standalone HTML investor brief
Usage:
    python scripts/render_report.py reports/AEROFLEX/AEROFLEX_2026-05-17.json
    python scripts/render_report.py path/to/data.json [--out path/to/output.html]
"""

import json
import sys
import html
from pathlib import Path
from datetime import datetime

# ── Segment colour map (from persona doc) ─────────────────────────────────────
SEGMENT_COLORS = {
    "railways": "#1D9E75",
    "infrastructure": "#1D9E75",
    "infra": "#1D9E75",
    "aerospace": "#D85A30",
    "defence": "#D85A30",
    "defense": "#D85A30",
    "industrial": "#378ADD",
    "power": "#378ADD",
    "energy": "#3B6D11",
    "ev": "#3B6D11",
    "clean": "#3B6D11",
    "semiconductor": "#534AB7",
    "tech": "#534AB7",
    "technology": "#534AB7",
    "communications": "#BA7517",
    "telecom": "#BA7517",
    "default": "#378ADD",
}

MAGNITUDE_COLOR = {"High": "#D85A30", "Medium": "#BA7517", "Low": "#1D9E75"}


def seg_color(key: str) -> str:
    key = (key or "").lower()
    for k, v in SEGMENT_COLORS.items():
        if k in key:
            return v
    return SEGMENT_COLORS["default"]


def e(text) -> str:
    """HTML-escape a value, return empty string for None."""
    return html.escape(str(text or ""), quote=False)


def build_html(data: dict) -> str:
    sym = e(data.get("symbol", ""))
    company_name = e(data.get("company_name", sym))
    sector = e(data.get("sector", ""))
    date_str = e(data.get("date", datetime.today().strftime("%Y-%m-%d")))
    cover = data.get("cover", {})
    chs = data.get("chapters", {})
    verdict = e(data.get("verdict", ""))

    tagline = e(cover.get("tagline", ""))
    sector_cagr = e(cover.get("sector_cagr", ""))
    mcap = e(cover.get("mcap", ""))
    pe = e(cover.get("pe", ""))

    # ── Chapter 1 ──────────────────────────────────────────────────────────────
    ch1 = chs.get("ch1_context", {})
    ch1_title = e(ch1.get("title", "Context"))
    ch1_body = e(ch1.get("body", ""))

    # ── Chapter 2 ──────────────────────────────────────────────────────────────
    ch2 = chs.get("ch2_business", {})
    ch2_title = e(ch2.get("title", "The Business Model"))
    ch2_body = e(ch2.get("body", ""))
    ch2_flywheel = e(ch2.get("flywheel", ""))

    # ── Chapter 3 — Verticals ─────────────────────────────────────────────────
    verticals = chs.get("ch3_verticals", [])
    ch3_cards = ""
    for v in verticals:
        color = seg_color(v.get("color_key", ""))
        name = e(v.get("name", ""))
        cat = e(v.get("catalyst", ""))
        body = e(v.get("body", ""))
        status = e(v.get("status", ""))
        status_badge = {
            "running": ('<span class="badge badge-green">Running</span>'),
            "ramping": ('<span class="badge badge-amber">Ramping</span>'),
            "prototype": ('<span class="badge badge-gray">Prototype</span>'),
        }.get(status.lower(), f'<span class="badge badge-gray">{status}</span>')
        ch3_cards += f"""
        <div class="vertical-card" style="border-left:3px solid {color}">
          <div class="vertical-header">
            <span class="vertical-name" style="color:{color}">{name}</span>
            {status_badge}
          </div>
          <p class="vertical-catalyst"><strong>Catalyst:</strong> {cat}</p>
          <p>{body}</p>
        </div>"""

    # ── Chapter 4 ──────────────────────────────────────────────────────────────
    ch4 = chs.get("ch4_insight", {})
    ch4_title = e(ch4.get("title", "The Strategic Insight"))
    ch4_insight = e(ch4.get("insight", ""))
    ch4_analogy = e(ch4.get("analogy", ""))
    ch4_analogy_block = (
        f'<blockquote class="analogy">"{ch4_analogy}"</blockquote>'
        if ch4_analogy
        else ""
    )

    # ── Chapter 5 ──────────────────────────────────────────────────────────────
    ch5 = chs.get("ch5_numbers", {})
    ch5_title = e(ch5.get("title", "The Numbers in Context"))
    ch5_body = e(ch5.get("body", ""))
    stats_rows = ""
    for s in ch5.get("stats", []):
        stats_rows += f"""
          <div class="stat-row">
            <span class="stat-label">{e(s.get('label',''))}</span>
            <span class="stat-value">{e(s.get('value',''))}</span>
          </div>"""

    # ── Chapter 6 — Risks ─────────────────────────────────────────────────────
    risks_html = ""
    for r in chs.get("ch6_risks", []):
        mag = r.get("magnitude", "Medium")
        color = MAGNITUDE_COLOR.get(mag, "#BA7517")
        risks_html += f"""
        <div class="risk-card">
          <div class="risk-header">
            <span class="risk-icon" style="color:{color}">⚠</span>
            <span class="risk-title">{e(r.get('title',''))}</span>
            <span class="risk-mag" style="color:{color}">{e(mag)}</span>
          </div>
          <p>{e(r.get('detail',''))}</p>
          <p class="risk-signal"><strong>Signal:</strong> {e(r.get('signal',''))}</p>
        </div>"""

    # ── Chapter 7 — Watch Signals ─────────────────────────────────────────────
    watch_html = ""
    for w in chs.get("ch7_watch", []):
        watch_html += f"""
        <div class="watch-item">
          <div class="watch-dot"></div>
          <div class="watch-content">
            <p class="watch-metric"><strong>{e(w.get('metric',''))}</strong> — {e(w.get('direction',''))}</p>
            <p class="watch-redflag">Red flag: {e(w.get('red_flag',''))}</p>
          </div>
        </div>"""

    # ── Nav ───────────────────────────────────────────────────────────────────
    nav_labels = [
        ("ch1", "1 Context"),
        ("ch2", "2 Business"),
        ("ch3", "3 Verticals"),
        ("ch4", "4 Insight"),
        ("ch5", "5 Numbers"),
        ("ch6", "6 Risks"),
        ("ch7", "7 Watch"),
        ("verdict", "Verdict"),
    ]
    nav_links = "".join(
        f'<a href="#{id}" class="nav-link">{label}</a>' for id, label in nav_labels
    )

    # ── Full HTML ─────────────────────────────────────────────────────────────
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{sym} — NSE Investor Story</title>
<style>
/* ── Reset & base ─────────────────────────────── */
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#F8F6F2;--tx:#1A1A1A;--card:#FFFFFF;--border:#E8E4DC;
  --sub:#5A5A5A;--acc:#0D5C75;--inp:#f0ede7;
  --teal:#1D9E75;--coral:#D85A30;--blue:#378ADD;
  --green:#3B6D11;--purple:#534AB7;--amber:#BA7517;
}}
body.dark{{
  --bg:#0d1117;--tx:#e6edf3;--card:#161b22;--border:#30363d;
  --sub:#8b949e;--acc:#58a6ff;--inp:#21262d;
  --teal:#2dce95;--coral:#ff7a59;--blue:#6bbfff;
  --green:#6aad1e;--purple:#8b80f0;--amber:#e09a2a;
}}
html{{scroll-behavior:smooth}}
body{{
  background:var(--bg);color:var(--tx);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  font-size:17px;line-height:1.65;transition:background .2s,color .2s;
}}
a{{color:var(--acc);text-decoration:none}}
a:hover{{text-decoration:underline}}
p{{margin-bottom:1rem}}

/* ── Layout ───────────────────────────────────── */
.container{{max-width:760px;margin:0 auto;padding:1rem 1.25rem 6rem}}

/* ── Top bar ──────────────────────────────────── */
.topbar{{
  display:flex;align-items:center;justify-content:space-between;
  padding:.5rem 0 1rem;border-bottom:1px solid var(--border);margin-bottom:1.5rem;
}}
.topbar-left{{font-size:.8rem;color:var(--sub)}}
.btn{{
  background:var(--inp);border:1px solid var(--border);color:var(--tx);
  padding:.35rem .8rem;border-radius:6px;cursor:pointer;font-size:.8rem;
}}
.btn:hover{{background:var(--border)}}

/* ── Cover card ───────────────────────────────── */
.cover{{
  background:var(--card);border:1px solid var(--border);border-radius:10px;
  padding:1.5rem;margin-bottom:1.5rem;
}}
.cover-eyebrow{{font-size:.75rem;color:var(--sub);margin-bottom:.4rem;text-transform:uppercase;letter-spacing:.06em}}
.cover-symbol{{font-size:2rem;font-weight:700;line-height:1.1}}
.cover-name{{font-size:1rem;color:var(--sub);margin:.2rem 0 .8rem}}
.cover-tagline{{font-size:1.05rem;font-style:italic;color:var(--acc);margin-bottom:1rem}}
.cover-meta{{display:flex;flex-wrap:wrap;gap:.5rem}}
.cover-chip{{
  background:var(--inp);border:1px solid var(--border);border-radius:20px;
  padding:.2rem .7rem;font-size:.78rem;
}}

/* ── Chapter nav ──────────────────────────────── */
.chapter-nav{{
  display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1.75rem;
}}
.nav-link{{
  background:var(--inp);border:1px solid var(--border);border-radius:5px;
  padding:.25rem .6rem;font-size:.75rem;color:var(--tx);
  white-space:nowrap;
}}
.nav-link:hover{{background:var(--border);text-decoration:none}}

/* ── Chapter articles ─────────────────────────── */
article{{
  background:var(--card);border:1px solid var(--border);border-radius:10px;
  padding:1.5rem;margin-bottom:1.25rem;
}}
.ch-eyebrow{{font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;color:var(--sub);margin-bottom:.3rem}}
.ch-title{{font-size:1.2rem;font-weight:700;margin-bottom:1rem}}

/* ── Vertical cards ───────────────────────────── */
.vertical-card{{
  background:var(--inp);border-radius:8px;padding:1rem;margin-bottom:.85rem;
}}
.vertical-header{{display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem}}
.vertical-name{{font-weight:700;font-size:.95rem}}
.vertical-catalyst{{font-size:.9rem;margin-bottom:.5rem}}
.badge{{
  font-size:.68rem;padding:.15rem .5rem;border-radius:20px;font-weight:600;
}}
.badge-green{{background:#d1fae5;color:#065f46}}
body.dark .badge-green{{background:#064e3b;color:#6ee7b7}}
.badge-amber{{background:#fef3c7;color:#92400e}}
body.dark .badge-amber{{background:#451a03;color:#fcd34d}}
.badge-gray{{background:var(--border);color:var(--sub)}}

/* ── Flywheel ─────────────────────────────────── */
.flywheel{{
  background:var(--inp);border-left:3px solid var(--acc);border-radius:0 8px 8px 0;
  padding:.75rem 1rem;margin:1rem 0;font-style:italic;font-size:.95rem;
}}

/* ── Strategic insight ────────────────────────── */
.insight-box{{
  background:var(--inp);border-left:4px solid var(--amber);border-radius:0 8px 8px 0;
  padding:1rem 1.25rem;margin-bottom:1rem;font-size:1rem;line-height:1.6;
}}
blockquote.analogy{{
  border-left:3px solid var(--border);padding:.5rem 1rem;
  color:var(--sub);font-style:italic;margin:1rem 0;
}}

/* ── Stats ────────────────────────────────────── */
.stats-grid{{display:grid;grid-template-columns:1fr;gap:0;margin:1rem 0}}
@media(min-width:520px){{.stats-grid{{grid-template-columns:1fr 1fr}}}}
.stat-row{{
  display:flex;justify-content:space-between;align-items:baseline;
  padding:.55rem 0;border-bottom:1px solid var(--border);
}}
.stat-row:last-child{{border-bottom:none}}
.stat-label{{font-size:.85rem;color:var(--sub)}}
.stat-value{{font-weight:600;font-size:.95rem}}

/* ── Risks ────────────────────────────────────── */
.risk-card{{
  border:1px solid var(--border);border-radius:8px;padding:1rem;margin-bottom:.85rem;
}}
.risk-header{{display:flex;align-items:center;gap:.5rem;margin-bottom:.5rem}}
.risk-icon{{font-size:1.1rem}}
.risk-title{{font-weight:600;flex:1}}
.risk-mag{{font-size:.78rem;font-weight:700}}
.risk-signal{{font-size:.85rem;color:var(--sub)}}

/* ── Watch signals ────────────────────────────── */
.watch-item{{display:flex;gap:.75rem;margin-bottom:1rem;align-items:flex-start}}
.watch-dot{{
  width:10px;height:10px;border-radius:50%;background:var(--teal);
  margin-top:.45rem;flex-shrink:0;
}}
.watch-metric{{margin-bottom:.2rem}}
.watch-redflag{{font-size:.85rem;color:var(--sub)}}

/* ── Verdict ──────────────────────────────────── */
#verdict{{
  background:var(--card);border:2px solid var(--acc);border-radius:10px;
  padding:1.5rem;margin-bottom:1.25rem;
}}
.verdict-label{{
  font-size:.7rem;text-transform:uppercase;letter-spacing:.1em;
  color:var(--acc);font-weight:700;margin-bottom:.5rem;
}}
.verdict-body{{font-size:.98rem;line-height:1.7}}

/* ── TTS bar ──────────────────────────────────── */
.tts-bar{{
  position:fixed;bottom:0;left:0;right:0;
  background:var(--card);border-top:1px solid var(--border);
  padding:.6rem 1rem;display:flex;align-items:center;gap:.5rem;
  z-index:100;
}}
.tts-bar .btn{{padding:.4rem .9rem}}
.tts-progress{{
  flex:1;font-size:.75rem;color:var(--sub);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
}}

/* ── Print ────────────────────────────────────── */
@media print{{
  .topbar button,.chapter-nav,.tts-bar{{display:none!important}}
  body{{font-size:12pt;color:#000;background:#fff}}
  .cover,.container{{max-width:100%!important}}
  article,#verdict{{break-inside:avoid}}
}}
</style>
</head>
<body>
<div class="container">

  <!-- Top bar -->
  <div class="topbar">
    <span class="topbar-left">NSE · {sector} · {date_str}</span>
    <button class="btn" id="toggle" onclick="toggleTheme()">🌙 Dark</button>
  </div>

  <!-- Cover -->
  <div class="cover" role="banner">
    <p class="cover-eyebrow">NSE:{sym} · Investor Story</p>
    <div class="cover-symbol">{sym}</div>
    <div class="cover-name">{company_name}</div>
    <p class="cover-tagline">{tagline}</p>
    <div class="cover-meta">
      {f'<span class="cover-chip">Sector CAGR: {sector_cagr}</span>' if sector_cagr else ''}
      {f'<span class="cover-chip">MCap: {mcap}</span>' if mcap else ''}
      {f'<span class="cover-chip">PE: {pe}</span>' if pe else ''}
      <span class="cover-chip">{date_str}</span>
    </div>
  </div>

  <!-- Chapter nav -->
  <nav class="chapter-nav" aria-label="Chapters">
    {nav_links}
  </nav>

  <main id="report-content">

    <!-- Chapter 1: Context -->
    <article id="ch1" aria-labelledby="ch1-title">
      <p class="ch-eyebrow">Chapter 1</p>
      <h2 class="ch-title" id="ch1-title">{ch1_title}</h2>
      <p>{ch1_body}</p>
    </article>

    <!-- Chapter 2: Business Model -->
    <article id="ch2" aria-labelledby="ch2-title">
      <p class="ch-eyebrow">Chapter 2</p>
      <h2 class="ch-title" id="ch2-title">{ch2_title}</h2>
      <p>{ch2_body}</p>
      {f'<div class="flywheel">{ch2_flywheel}</div>' if ch2_flywheel else ''}
    </article>

    <!-- Chapter 3: Verticals -->
    <article id="ch3" aria-labelledby="ch3-title">
      <p class="ch-eyebrow">Chapter 3</p>
      <h2 class="ch-title" id="ch3-title">The Vertical Stories</h2>
      {ch3_cards}
    </article>

    <!-- Chapter 4: Strategic Insight -->
    <article id="ch4" aria-labelledby="ch4-title">
      <p class="ch-eyebrow">Chapter 4 · The One Thing to Understand</p>
      <h2 class="ch-title" id="ch4-title">{ch4_title}</h2>
      <div class="insight-box">{ch4_insight}</div>
      {ch4_analogy_block}
    </article>

    <!-- Chapter 5: Numbers -->
    <article id="ch5" aria-labelledby="ch5-title">
      <p class="ch-eyebrow">Chapter 5</p>
      <h2 class="ch-title" id="ch5-title">{ch5_title}</h2>
      <p>{ch5_body}</p>
      <div class="stats-grid">{stats_rows}</div>
    </article>

    <!-- Chapter 6: Risks -->
    <article id="ch6" aria-labelledby="ch6-title">
      <p class="ch-eyebrow">Chapter 6 · Eyes Open</p>
      <h2 class="ch-title" id="ch6-title">Risks</h2>
      {risks_html}
    </article>

    <!-- Chapter 7: Watch Signals -->
    <article id="ch7" aria-labelledby="ch7-title">
      <p class="ch-eyebrow">Chapter 7</p>
      <h2 class="ch-title" id="ch7-title">Watch Signals</h2>
      {watch_html}
    </article>

    <!-- Verdict -->
    <section id="verdict" aria-label="Verdict">
      <p class="verdict-label">Verdict</p>
      <p class="verdict-body">{verdict}</p>
    </section>

  </main>
</div>

<!-- TTS bar -->
<div class="tts-bar" aria-label="Text to speech controls">
  <button class="btn" id="tts-play" onclick="ttsPlay()">🔊 Read</button>
  <button class="btn" id="tts-pause" onclick="ttsPause()" style="display:none">⏸ Pause</button>
  <button class="btn" onclick="ttsStop()">⏹ Stop</button>
  <span class="tts-progress" id="tts-progress">Ready to read aloud</span>
</div>

<script>
// ── Theme ─────────────────────────────────────────────────────────────────────
(function(){{
  var t=localStorage.getItem('theme');
  if(t==='dark'){{document.body.classList.add('dark');document.getElementById('toggle').textContent='☀ Light';}}
}})();
function toggleTheme(){{
  var d=document.body.classList.toggle('dark');
  localStorage.setItem('theme',d?'dark':'light');
  document.getElementById('toggle').textContent=d?'☀ Light':'🌙 Dark';
}}

// ── TTS ───────────────────────────────────────────────────────────────────────
var _utt=null,_paused=false,_paragraphs=[],_idx=0;
function _buildParagraphs(){{
  var nodes=document.getElementById('report-content').querySelectorAll('p,h2');
  _paragraphs=[];
  nodes.forEach(function(n){{
    var t=n.innerText.trim();
    if(t) _paragraphs.push(t);
  }});
}}
function _speak(idx){{
  if(idx>=_paragraphs.length){{ttsStop();return;}}
  _idx=idx;
  var prog=document.getElementById('tts-progress');
  prog.textContent=_paragraphs[idx].substring(0,60)+'…';
  _utt=new SpeechSynthesisUtterance(_paragraphs[idx]);
  _utt.rate=0.92;_utt.lang='en-IN';
  _utt.onend=function(){{_speak(idx+1);}};
  window.speechSynthesis.speak(_utt);
}}
function ttsPlay(){{
  if(!('speechSynthesis' in window)){{
    document.getElementById('tts-progress').textContent='TTS not supported in this browser';return;
  }}
  if(_paused){{window.speechSynthesis.resume();_paused=false;}}
  else{{
    window.speechSynthesis.cancel();
    _buildParagraphs();
    _speak(0);
  }}
  document.getElementById('tts-play').style.display='none';
  document.getElementById('tts-pause').style.display='';
}}
function ttsPause(){{
  window.speechSynthesis.pause();_paused=true;
  document.getElementById('tts-play').style.display='';
  document.getElementById('tts-pause').style.display='none';
}}
function ttsStop(){{
  window.speechSynthesis.cancel();_paused=false;_idx=0;
  document.getElementById('tts-play').style.display='';
  document.getElementById('tts-pause').style.display='none';
  document.getElementById('tts-progress').textContent='Ready to read aloud';
}}
</script>
</body>
</html>"""


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Render investor story JSON to HTML")
    parser.add_argument("json_file", help="Path to the JSON data file")
    parser.add_argument(
        "--out", help="Output HTML path (default: same dir, .html extension)"
    )
    args = parser.parse_args()

    json_path = Path(args.json_file)
    if not json_path.exists():
        print(f"Error: {json_path} not found", file=sys.stderr)
        sys.exit(1)

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    if args.out:
        out_path = Path(args.out)
    else:
        # Same directory, replace .json with .html, prefix symbol if not already
        stem = json_path.stem
        sym = data.get("symbol", "")
        if sym and not stem.startswith(sym):
            stem = f"{sym}_{stem}"
        out_path = json_path.with_name(stem + ".html")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    html_content = build_html(data)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Rendered -> {out_path}")
    return str(out_path)


if __name__ == "__main__":
    main()
