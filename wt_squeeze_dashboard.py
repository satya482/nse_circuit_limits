#!/usr/bin/env python3
"""
WaveTrend Dashboard
Reads wt_bullcross_latest.md and builds wt_squeeze_dashboard.html.

Source : wt_scans/wt_bullcross_latest.md  (wt_bullcross_scanner.py)
Output : wt_squeeze_dashboard.html
"""

import re, os, sys, json
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding="utf-8")

IST  = timezone(timedelta(hours=5, minutes=30))
BASE = os.path.dirname(os.path.abspath(__file__))

WT_MD       = os.path.join(BASE, "wt_scans", "wt_bullcross_latest.md")
OUTPUT_HTML = os.path.join(BASE, "wt_squeeze_dashboard.html")

_LABELS_FILE = os.path.join(BASE, "tools", "stock_labels.json")
_LABELS: dict = {}
if os.path.exists(_LABELS_FILE):
    with open(_LABELS_FILE, encoding="utf-8") as _f:
        _LABELS = json.load(_f)

_RANK_LABEL = {5: "OS+PPV", 4: "ANY+PPV", 3: "OVERSOLD", 2: "OS L2", 1: "ZERO"}
_RANK_COLOR = {5: "#f97316", 4: "#eab308", 3: "#22c55e", 2: "#84cc16", 1: "#3b82f6"}


def read_file(path: str) -> str:
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def _strip_md_link(s: str) -> str:
    m = re.match(r'\[([^\]]+)\]\([^)]+\)', s)
    return m.group(1) if m else s


# ── Parse WaveTrend markdown ──────────────────────────────────────────────────
# Table cols: Symbol | Label | Signal | Rank | WT1 | WT2 | ZL | ZL Days | ZL Chg% | Sqz | PPV | Day Chg | Close | Circuit

def parse_wt_rows(content: str) -> list[dict]:
    rows = []
    for line in content.splitlines():
        ls = line.strip()
        if not ls.startswith('|'):
            continue
        if ls.startswith('|---') or ls.startswith('| ---'):
            continue
        # preserve empty cells (Label may be empty) — use [1:-1] slice not if-strip filter
        parts = [p.strip() for p in ls.split('|')][1:-1]
        if len(parts) < 14:
            continue
        sym = _strip_md_link(parts[0])
        if not sym or sym in ("Symbol", "#"):
            continue
        try:
            rank = int(parts[3])
        except ValueError:
            continue
        rows.append({
            "symbol":  sym,
            "label":   parts[1],
            "signal":  parts[2],
            "rank":    rank,
            "wt1":     parts[4],
            "wt2":     parts[5],
            "zl_dir":  parts[6],
            "zl_days": parts[7],
            "zl_pct":  parts[8],
            "squeeze": parts[9],
            "ppv":     parts[10],
            "day_chg": parts[11],
            "close":   parts[12],
            "circuit": parts[13],
        })
    rows.sort(key=lambda r: (-r["rank"], float(r["wt1"]) if r["wt1"].lstrip("-").replace(".", "", 1).isdigit() else 0))
    return rows


# ── HTML helpers ──────────────────────────────────────────────────────────────

def _tv_link(sym: str) -> str:
    return f'<a href="https://in.tradingview.com/chart/?symbol=NSE:{sym}" target="_blank" rel="noopener">{sym}</a>'


def _chg_cls(v: str) -> str:
    return "pos" if v.startswith('+') else ("neg" if v.startswith('-') else "")


def _rank_badge(rank: int) -> str:
    color = _RANK_COLOR.get(rank, "#6b7280")
    label = _RANK_LABEL.get(rank, str(rank))
    return (f'<span style="background:{color};color:#fff;font-size:9px;'
            f'padding:1px 6px;border-radius:3px;font-weight:700">{label}</span>')


def _wt_html_row(r: dict) -> str:
    sym    = r["symbol"]
    zl_cls = "pos" if r["zl_dir"] == "↑" else "neg"
    sqz_cls = "sqz-on" if r["squeeze"] == "✓" else "sqz-off"
    ppv_cls = "pos" if r["ppv"] == "✓" else "mu"
    return (
        f'<tr>'
        f'<td class="sym">{_tv_link(sym)}</td>'
        f'<td class="lbl">{r["label"]}</td>'
        f'<td>{_rank_badge(r["rank"])}</td>'
        f'<td class="num">{r["wt1"]}</td>'
        f'<td class="num">{r["wt2"]}</td>'
        f'<td class="{zl_cls}">{r["zl_dir"]}</td>'
        f'<td class="mu">{r["zl_days"]}</td>'
        f'<td class="{_chg_cls(r["zl_pct"])}">{r["zl_pct"]}</td>'
        f'<td class="{sqz_cls}">{r["squeeze"]}</td>'
        f'<td class="{ppv_cls}">{r["ppv"]}</td>'
        f'<td class="{_chg_cls(r["day_chg"])}">{r["day_chg"]}</td>'
        f'<td class="num">{r["close"]}</td>'
        f'<td class="mu">{r["circuit"]}</td>'
        f'</tr>'
    )



def _rows_or_empty(rows_html: list[str], cols: int, msg: str) -> str:
    return "\n".join(rows_html) if rows_html else f'<tr><td colspan="{cols}" class="empty">{msg}</td></tr>'


# ── HTML builder ──────────────────────────────────────────────────────────────

CSS = """
:root{
  --bg:#0d1117;--bg2:#161b22;--bg3:#21262d;
  --bd:#30363d;--tx:#e6edf3;--mu:#8b949e;
  --gld:#ffd700;--grn:#3fb950;--red:#f85149;--blu:#58a6ff;--pur:#a371f7;
  --ylw:#d29922;--ora:#f97316;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--tx);font-family:'Segoe UI',system-ui,sans-serif;font-size:13px;padding:16px;line-height:1.4}
h1{font-size:1.2rem;color:var(--blu);margin-bottom:3px}
.sub{color:var(--mu);font-size:11px;margin-bottom:16px}
.nav{font-size:11px;margin-bottom:12px}
.nav a{color:var(--blu);text-decoration:none}

.bar{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px}
.stat{background:var(--bg2);border:1px solid var(--bd);border-radius:6px;padding:7px 14px;text-align:center;min-width:70px}
.sv{font-size:1.5rem;font-weight:700;line-height:1.1}
.sl{color:var(--mu);font-size:10px;text-transform:uppercase;letter-spacing:.5px}
.gld{color:var(--gld)}.grn{color:var(--grn)}.red{color:var(--red)}.blu{color:var(--blu)}.ora{color:var(--ora)}.pur{color:var(--pur)}

.section{margin-bottom:22px}
.stitle{font-size:.78rem;font-weight:600;color:var(--mu);text-transform:uppercase;letter-spacing:.7px;
        margin-bottom:6px;border-bottom:1px solid var(--bd);padding-bottom:3px;display:flex;align-items:center;gap:8px}
.stitle .cnt{color:var(--tx);font-size:.85rem}

table{width:100%;border-collapse:collapse;background:var(--bg2);border-radius:6px;overflow:hidden;font-size:12px}
th{background:var(--bg3);color:var(--mu);font-size:10px;text-transform:uppercase;letter-spacing:.5px;
   padding:5px 9px;text-align:left;border-bottom:1px solid var(--bd)}
td{padding:4px 9px;border-bottom:1px solid var(--bd);vertical-align:middle}
tr:last-child td{border-bottom:none}
tr:hover td{background:var(--bg3)}

.sym{font-weight:600;font-family:monospace;font-size:12px}
.sym a{color:inherit;text-decoration:none}.sym a:hover{text-decoration:underline;color:var(--blu)}
.lbl{font-size:11px;color:var(--mu);max-width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.mu{color:var(--mu);font-size:11px}
.num{font-family:monospace;font-size:12px;color:var(--mu)}
.pos{color:var(--grn)}.neg{color:var(--red)}
.sqz-hi{color:var(--gld);font-weight:700;text-align:center}
.sqz-on{color:var(--grn);font-weight:600;text-align:center}
.sqz-off{color:var(--mu);text-align:center;font-size:11px}
.empty{color:var(--mu);font-style:italic;text-align:center;padding:10px}
"""


def build_html(today: str, now_str: str, wt_rows: list) -> str:
    wt_html   = [_wt_html_row(r) for r in wt_rows]
    n_os_plus = sum(1 for r in wt_rows if r["rank"] >= 3)
    n_ppv     = sum(1 for r in wt_rows if r["ppv"] == "✓")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>WaveTrend Dashboard — {today}</title>
<style>{CSS}</style>
</head>
<body>

<div class="nav"><a href="dashboard.html">← Main Dashboard</a></div>

<h1>WaveTrend Bull Cross — {today}</h1>
<div class="sub">
  Generated {now_str} &nbsp;|&nbsp;
  🔥 MAJOR = PPV confirmed &nbsp;|&nbsp;
  🟢 OVERSOLD = cross below −53/−60 &nbsp;|&nbsp;
  📈 ABOVE ZERO = WT1 crossed zero
</div>

<div class="bar">
  <div class="stat"><div class="sv ora">{len(wt_rows)}</div><div class="sl">WT Bull Cross</div></div>
  <div class="stat"><div class="sv grn">{n_os_plus}</div><div class="sl">Oversold+ (rank≥3)</div></div>
  <div class="stat"><div class="sv pur">{n_ppv}</div><div class="sl">PPV confirmed</div></div>
</div>

<div class="section">
  <div class="stitle">
    WaveTrend Bull Cross
    <span class="cnt">({len(wt_rows)} signals — sorted rank desc, deeper oversold first)</span>
  </div>
  <table>
    <thead><tr>
      <th>Symbol</th><th>Label</th><th>WT Signal</th>
      <th>WT1</th><th>WT2</th><th>ZL</th><th>ZL Days</th><th>ZL Chg%</th>
      <th>Sqz</th><th>PPV</th><th>Day Chg</th><th>Close</th><th>Circuit</th>
    </tr></thead>
    <tbody>{_rows_or_empty(wt_html, 13, "No WaveTrend bull crosses today — run wt_bullcross_scanner.py first")}</tbody>
  </table>
</div>

</body>
</html>"""


def main():
    now_ist = datetime.now(IST)
    today   = now_ist.strftime("%Y-%m-%d")
    now_str = now_ist.strftime("%Y-%m-%d %H:%M IST")

    print(f"[{now_str}] Building WaveTrend + Squeeze Dashboard...")

    wt_rows = parse_wt_rows(read_file(WT_MD))
    print(f"  WT bull crosses : {len(wt_rows)}")

    html = build_html(today, now_str, wt_rows)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Written → {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
