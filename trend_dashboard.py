#!/usr/bin/env python3
"""
Trend Scanner Dashboard
Reads trend_scans/trend_scan_latest.md and builds trend_dashboard.html.

Source : trend_scans/trend_scan_latest.md  (trend_scanner.py)
Output : trend_dashboard.html

Groups (derived from section headers):
  🏆 LEADER_ZL   — ZLEMA25 touch + RS holds + vol dry-up  (highest conviction)
  🟢 ZL_PULLBACK  — ZLEMA25 touch + RS holds
  🔵 EMA_SUPPORT  — EMA50/100/200 bounce + RS holds
  📈 ZL_ENTRY     — ZLEMA25 touch, RS transitioning        (early watch)

Table cols (13):
  Symbol | Trap | Label | Signal | Score | RS | C/AvgC | 52W% | Vol | ZL | ZL Chg% | Day Chg | Circuit
  0        1      2       3        4       5     6        7     8    9     10        11        12
"""

import re
import os
import sys
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding="utf-8")

IST = timezone(timedelta(hours=5, minutes=30))
BASE = os.path.dirname(os.path.abspath(__file__))

TREND_MD = os.path.join(BASE, "trend_scans", "trend_scan_latest.md")
OUTPUT_HTML = os.path.join(BASE, "trend_dashboard.html")

# ── Group definitions ──────────────────────────────────────────────────────────

LEADER_ZL = "LEADER_ZL"
ZL_PULLBACK = "ZL_PULLBACK"
EMA_SUPPORT = "EMA_SUPPORT"
ZL_ENTRY = "ZL_ENTRY"

_GROUP_ORDER = [LEADER_ZL, ZL_PULLBACK, EMA_SUPPORT, ZL_ENTRY]

_EMOJI_TO_GROUP = {
    "🏆": LEADER_ZL,
    "🟢": ZL_PULLBACK,
    "🔵": EMA_SUPPORT,
    "📈": ZL_ENTRY,
}

_GROUP_META = {
    LEADER_ZL: {
        "emoji": "🏆",
        "title": "LEADER ZL — ZLEMA25 touch + RS holds + vol dry-up",
        "color": "#ffd700",
        "bg": "#1a1600",
        "desc": (
            "Stage 2 leaders resting on rising ZLEMA25 with volume drying up — "
            "energy coiling before next leg. Best risk/reward: tight stop below ZLEMA25."
        ),
    },
    ZL_PULLBACK: {
        "emoji": "🟢",
        "title": "ZL PULLBACK — ZLEMA25 touch + RS holds",
        "color": "#3fb950",
        "bg": "#0d1a0e",
        "desc": (
            "Leaders pulling back to rising ZLEMA25 with RS strength confirmed. "
            "Volume not yet dry — watch for dry-up to enter; or enter on bounce with volume."
        ),
    },
    EMA_SUPPORT: {
        "emoji": "🔵",
        "title": "EMA SUPPORT — EMA50/100/200 bounce + RS holds",
        "color": "#58a6ff",
        "bg": "#0d1220",
        "desc": (
            "Deeper pullbacks to structural EMAs. Higher risk than ZL touch. "
            "Wait for bullish close above EMA and volume confirmation before entry."
        ),
    },
    ZL_ENTRY: {
        "emoji": "📈",
        "title": "ZL ENTRY — ZLEMA25 touch, RS transitioning",
        "color": "#d29922",
        "bg": "#1a1200",
        "desc": (
            "Early-stage leaders: RS not yet confirmed strong (was recently strong, now transitioning). "
            "Smaller size. Monitor RS daily — upgrade to ZL PULLBACK when RS resumes."
        ),
    },
}


# ── Parse markdown ─────────────────────────────────────────────────────────────


def read_file(path: str) -> str:
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def _strip_md_link(s: str) -> str:
    m = re.match(r"\[([^\]]+)\]\([^)]+\)", s)
    return m.group(1) if m else s


def parse_trend_rows(content: str) -> dict:
    """Returns {group_key: [row_dict, ...]} in score-desc order within each group."""
    groups: dict = {k: [] for k in _GROUP_ORDER}
    current_group = None
    seen: set = set()

    for line in content.splitlines():
        ls = line.strip()

        # Section header detection
        if ls.startswith("### "):
            for emoji, grp in _EMOJI_TO_GROUP.items():
                if emoji in ls:
                    current_group = grp
                    break
            continue

        if current_group is None:
            continue
        if not ls.startswith("|"):
            continue
        if ls.startswith("|---") or ls.startswith("| ---"):
            continue

        parts = [p.strip() for p in ls.split("|")][1:-1]
        if len(parts) < 13:
            continue
        sym = _strip_md_link(parts[0])
        if not sym or sym in ("Symbol", "#"):
            continue
        if sym in seen:
            continue
        seen.add(sym)

        # Score
        try:
            score = int(parts[4])
        except ValueError:
            score = 0

        # RS: "🔄82" | "↑99" | "↓78"
        rs_raw = parts[5]
        if rs_raw.startswith("🔄"):
            rs_state = "transition"
        elif rs_raw.startswith("↑"):
            rs_state = "strong"
        else:
            rs_state = "weak"

        # Vol: "🔵0.39x" = dry-up | "0.69x" | "3.58x"
        vol_raw = parts[8]
        vol_dry = vol_raw.startswith("🔵")

        # ZL: "↑57d" | "↓10d"
        zl_raw = parts[9]
        zl_dir = "↑" if zl_raw.startswith("↑") else "↓"
        zl_days_str = re.sub(r"[↑↓d\s]", "", zl_raw)
        try:
            zl_days = int(zl_days_str)
        except ValueError:
            zl_days = 0

        groups[current_group].append(
            {
                "symbol": sym,
                "trap": parts[1],
                "label": parts[2],
                "signal": parts[3],
                "score": score,
                "rs_raw": rs_raw,
                "rs_state": rs_state,
                "cavgc": parts[6],
                "w52": parts[7],
                "vol_raw": vol_raw,
                "vol_dry": vol_dry,
                "zl_dir": zl_dir,
                "zl_days": zl_days,
                "zl_pct": parts[10],
                "day_chg": parts[11],
                "circuit": parts[12],
            }
        )

    # Already score-sorted by trend_scanner.py, but enforce within each group
    for grp in groups:
        groups[grp].sort(key=lambda r: -r["score"])

    return groups


# ── HTML helpers ───────────────────────────────────────────────────────────────


def _tv_link(sym: str) -> str:
    return (
        f'<a href="https://in.tradingview.com/chart/?symbol=NSE:{sym}" '
        f'target="_blank" rel="noopener">{sym}</a>'
    )


def _chg_cls(v: str) -> str:
    return "pos" if v.startswith("+") else ("neg" if v.startswith("-") else "")


def _trap_html(trap: str) -> str:
    if "SAFE" in trap:
        return f'<span class="pos">{trap}</span>'
    if "CAUTION" in trap:
        return f'<span style="color:var(--ylw)">{trap}</span>'
    if "AVOID" in trap:
        return f'<span class="neg">{trap}</span>'
    return f'<span class="mu">{trap}</span>'


def _score_html(score: int) -> str:
    if score >= 75:
        color = "#ffd700"
    elif score >= 60:
        color = "#3fb950"
    elif score >= 45:
        color = "#d29922"
    else:
        color = "#8b949e"
    return f'<span style="font-weight:700;color:{color}">{score}</span>'


def _rs_html(rs_raw: str, rs_state: str) -> str:
    cls = (
        "gld" if rs_state == "transition" else ("pos" if rs_state == "strong" else "mu")
    )
    return f'<span class="{cls}">{rs_raw}</span>'


def _cavgc_html(v: str) -> str:
    cls = "pos" if v.startswith("↑") else "mu"
    return f'<span class="{cls}">{v}</span>'


def _w52_html(w52: str) -> str:
    try:
        pct = int(w52.rstrip("%"))
        color = "#ffd700" if pct >= 95 else ("#3fb950" if pct >= 80 else "#d29922")
    except ValueError:
        color = "#8b949e"
    return f'<span style="color:{color}">{w52}</span>'


def _vol_html(vol_raw: str, vol_dry: bool) -> str:
    if vol_dry:
        v = vol_raw.lstrip("🔵").strip()
        return f'<span style="color:var(--gld);font-weight:600" title="Volume dry-up">🔵{v}</span>'
    try:
        ratio = float(vol_raw.rstrip("x"))
        cls = "neg" if ratio >= 2.0 else ("pos" if ratio >= 1.2 else "mu")
    except ValueError:
        cls = "mu"
    return f'<span class="{cls}">{vol_raw}</span>'


def _zl_html(zl_dir: str, zl_days: int) -> str:
    if zl_dir == "↑":
        color = (
            "#ffd700" if zl_days <= 3 else ("#3fb950" if zl_days <= 7 else "#8b949e")
        )
        title = (
            "Very fresh turn"
            if zl_days <= 3
            else ("Fresh" if zl_days <= 7 else "Aging")
        )
        return f'<span style="color:{color};font-weight:600" title="{title}">↑{zl_days}d</span>'
    return f'<span class="neg">↓{zl_days}d</span>'


def _signal_chips(signal: str, group: str) -> str:
    meta = _GROUP_META.get(group, {})
    grp_color = meta.get("color", "#8b949e")
    chips = []

    if "vol dry-up" in signal:
        chips.append(("DRY-UP", "#ffd700"))
    if "EMA20 ↑" in signal:
        chips.append(("EMA20↑", grp_color))
    if "RS holds" in signal:
        chips.append(("RS✓", "#3fb950"))
    if "RS transitioning" in signal:
        chips.append(("RS~", "#d29922"))
    if "EMA200" in signal:
        chips.append(("EMA200", "#f85149"))
    elif "EMA100" in signal:
        chips.append(("EMA100", "#a371f7"))
    elif "EMA50" in signal:
        chips.append(("EMA50", "#58a6ff"))

    parts = []
    for label, c in chips:
        parts.append(
            f'<span style="background:{c}22;color:{c};font-size:9px;'
            f"padding:1px 5px;border-radius:3px;font-weight:600;"
            f'border:1px solid {c}44">{label}</span>'
        )
    return "&nbsp;".join(parts) if parts else '<span class="mu">—</span>'


def _trend_row(r: dict, group: str) -> str:
    sym = r["symbol"]
    return (
        "<tr>"
        f'<td class="sym">{_tv_link(sym)}</td>'
        f'<td style="font-size:10px;white-space:nowrap">{_trap_html(r["trap"])}</td>'
        f'<td class="lbl">{r["label"]}</td>'
        f'<td style="white-space:nowrap">{_signal_chips(r["signal"], group)}</td>'
        f'<td style="text-align:center">{_score_html(r["score"])}</td>'
        f'<td style="text-align:center">{_rs_html(r["rs_raw"], r["rs_state"])}</td>'
        f'<td style="text-align:center">{_cavgc_html(r["cavgc"])}</td>'
        f'<td style="text-align:center">{_w52_html(r["w52"])}</td>'
        f'<td style="text-align:center">{_vol_html(r["vol_raw"], r["vol_dry"])}</td>'
        f'<td style="text-align:center">{_zl_html(r["zl_dir"], r["zl_days"])}</td>'
        f'<td class="{_chg_cls(r["zl_pct"])}">{r["zl_pct"]}</td>'
        f'<td class="{_chg_cls(r["day_chg"])}">{r["day_chg"]}</td>'
        f'<td class="mu">{r["circuit"]}</td>'
        "</tr>"
    )


def _copy_btn(rows: list) -> str:
    if not rows:
        return ""
    syms = ",".join(f"NSE:{r['symbol']}" for r in rows)
    return (
        f'<button class="copy-btn" data-syms="{syms}">'
        f"📋 Copy TV List ({len(rows)})</button>"
    )


_TABLE_HDR = """    <thead><tr>
      <th>Symbol</th><th>Trap</th><th>Label</th><th>Signal</th>
      <th>Score</th><th>RS</th><th>C/AvgC</th><th>52W%</th><th>Vol</th>
      <th>ZL↑ Days</th><th>ZL Chg%</th><th>Day Chg</th><th>Circuit</th>
    </tr></thead>"""


def _section_html(group: str, rows: list) -> str:
    meta = _GROUP_META[group]
    color = meta["color"]
    bg = meta["bg"]
    rows_html = [_trend_row(r, group) for r in rows]
    body = (
        "\n".join(rows_html)
        if rows_html
        else '<tr><td colspan="13" class="empty">No signals today.</td></tr>'
    )
    avg_score = (
        f" &nbsp;·&nbsp; avg score {sum(r['score'] for r in rows) // len(rows)}"
        if rows
        else ""
    )
    return f"""
<div class="section" style="border:1px solid {color};border-radius:6px;padding:12px;background:{bg}">
  <div class="stitle" style="color:{color};border-color:{color}55">
    {meta["title"]}
    <span class="cnt" style="color:{color}">({len(rows)} signals{avg_score})</span>
    {_copy_btn(rows)}
  </div>
  <p style="font-size:11px;color:{color}99;margin-bottom:8px">{meta["desc"]}</p>
  <table>
{_TABLE_HDR}
    <tbody>{body}</tbody>
  </table>
</div>"""


# ── CSS ────────────────────────────────────────────────────────────────────────

CSS = """
:root{
  --bg:#0d1117;--bg2:#161b22;--bg3:#21262d;
  --bd:#30363d;--tx:#e6edf3;--mu:#8b949e;
  --gld:#ffd700;--grn:#3fb950;--red:#f85149;--blu:#58a6ff;--pur:#a371f7;
  --ylw:#d29922;--ora:#f97316;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--tx);font-family:'Segoe UI',system-ui,sans-serif;
     font-size:13px;padding:16px;line-height:1.4}
h1{font-size:1.2rem;color:var(--grn);margin-bottom:3px}
.sub{color:var(--mu);font-size:11px;margin-bottom:16px}
.nav{font-size:11px;margin-bottom:12px}
.nav a{color:var(--blu);text-decoration:none;margin-right:12px}

.bar{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px}
.stat{background:var(--bg2);border:1px solid var(--bd);border-radius:6px;
      padding:7px 14px;text-align:center;min-width:70px}
.sv{font-size:1.5rem;font-weight:700;line-height:1.1}
.sl{color:var(--mu);font-size:10px;text-transform:uppercase;letter-spacing:.5px}
.gld{color:var(--gld)}.grn{color:var(--grn)}.red{color:var(--red)}
.blu{color:var(--blu)}.ora{color:var(--ora)}.pur{color:var(--pur)}

.section{margin-bottom:22px}
.stitle{font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.7px;
        margin-bottom:6px;border-bottom:1px solid;padding-bottom:3px;
        display:flex;align-items:center;gap:8px}
.stitle .cnt{font-size:.85rem}

table{width:100%;border-collapse:collapse;background:var(--bg2);
      border-radius:6px;overflow:hidden;font-size:12px}
th{background:var(--bg3);color:var(--mu);font-size:10px;text-transform:uppercase;
   letter-spacing:.5px;padding:5px 9px;text-align:left;border-bottom:1px solid var(--bd)}
td{padding:4px 9px;border-bottom:1px solid var(--bd);vertical-align:middle}
tr:last-child td{border-bottom:none}
tr:hover td{background:var(--bg3)}

.sym{font-weight:600;font-family:monospace;font-size:12px}
.sym a{color:inherit;text-decoration:none}.sym a:hover{text-decoration:underline;color:var(--blu)}
.lbl{font-size:11px;color:var(--mu);max-width:180px;overflow:hidden;
     text-overflow:ellipsis;white-space:nowrap}
.mu{color:var(--mu);font-size:11px}
.num{font-family:monospace;font-size:12px;color:var(--mu)}
.pos{color:var(--grn)}.neg{color:var(--red)}
.empty{color:var(--mu);font-style:italic;text-align:center;padding:10px}

.copy-btn{margin-left:auto;background:var(--bg3);border:1px solid var(--bd);
  color:var(--tx);font-size:10px;padding:3px 9px;border-radius:4px;cursor:pointer;
  letter-spacing:0;font-weight:600}
.copy-btn:hover{background:var(--bd);border-color:var(--blu)}
.copy-btn.copied{background:var(--grn);border-color:var(--grn);color:#0d1117}
"""


# ── Build HTML ─────────────────────────────────────────────────────────────────


def build_html(today: str, now_str: str, groups: dict, scan_date: str) -> str:
    total = sum(len(v) for v in groups.values())
    n_leader = len(groups[LEADER_ZL])
    n_pullback = len(groups[ZL_PULLBACK])
    n_ema = len(groups[EMA_SUPPORT])
    n_entry = len(groups[ZL_ENTRY])

    all_rows = [r for grp in _GROUP_ORDER for r in groups[grp]]
    avg_leader_score = (
        sum(r["score"] for r in groups[LEADER_ZL]) // n_leader if n_leader else 0
    )
    n_dry = sum(1 for r in all_rows if r["vol_dry"])
    n_fresh_zl = sum(1 for r in all_rows if r["zl_dir"] == "↑" and r["zl_days"] <= 5)

    sections = "\n".join(_section_html(g, groups[g]) for g in _GROUP_ORDER)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Trend Scanner Dashboard — {today}</title>
<style>{CSS}</style>
</head>
<body>

<div class="nav">
  <a href="dashboard.html">← Main Dashboard</a>
  <a href="wt_squeeze_dashboard.html">WT + Squeeze →</a>
</div>

<h1>📈 Trend Scanner Dashboard — {today}</h1>
<div class="sub">
  Scan date: {scan_date} &nbsp;|&nbsp; Generated: {now_str}
  &nbsp;|&nbsp; Leaders in Stage 2 uptrends pulling back to ZLEMA25 or structural EMAs
  &nbsp;|&nbsp; Score = RS%×0.35 + vol dry-up(20) + 52W proximity(20) + RS holds(15) + ZL fresh(10)
  &nbsp;|&nbsp; ZL↑ color: <span style="color:#ffd700">≤3d=new</span> · <span style="color:#3fb950">≤7d=fresh</span> · <span style="color:#8b949e">&gt;7d=aging</span>
  &nbsp;|&nbsp; Vol: <span style="color:#ffd700">🔵 = dry-up (below 20d avg × 0.7)</span>
</div>

<div class="bar">
  <div class="stat"><div class="sv gld">{n_leader}</div><div class="sl">🏆 Leader ZL</div></div>
  <div class="stat"><div class="sv grn">{n_pullback}</div><div class="sl">🟢 ZL Pullback</div></div>
  <div class="stat"><div class="sv blu">{n_ema}</div><div class="sl">🔵 EMA Support</div></div>
  <div class="stat"><div class="sv ora">{n_entry}</div><div class="sl">📈 ZL Entry</div></div>
  <div class="stat"><div class="sv" style="color:var(--tx)">{total}</div><div class="sl">Total</div></div>
  <div class="stat"><div class="sv gld">{n_dry}</div><div class="sl">Vol Dry-up</div></div>
  <div class="stat"><div class="sv" style="color:#3fb950">{n_fresh_zl}</div><div class="sl">ZL ≤5d Fresh</div></div>
  <div class="stat"><div class="sv" style="color:#ffd700">{avg_leader_score}</div><div class="sl">Leader Avg Score</div></div>
</div>

{sections}

<script>
document.querySelectorAll('.copy-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    navigator.clipboard.writeText(btn.dataset.syms).then(() => {{
      const orig = btn.textContent;
      btn.textContent = '✓ Copied!';
      btn.classList.add('copied');
      setTimeout(() => {{ btn.textContent = orig; btn.classList.remove('copied'); }}, 1500);
    }});
  }});
}});
</script>

</body>
</html>"""


# ── Entry point ────────────────────────────────────────────────────────────────


def _extract_scan_date(content: str) -> str:
    m = re.search(r"Trend Scanner.*?(\d{4}-\d{2}-\d{2})", content)
    return m.group(1) if m else "—"


def main():
    now_ist = datetime.now(IST)
    today = now_ist.strftime("%Y-%m-%d")
    now_str = now_ist.strftime("%Y-%m-%d %H:%M IST")

    print(f"[{now_str}] Building Trend Scanner Dashboard...")

    content = read_file(TREND_MD)
    if not content:
        print(f"  ERROR: {TREND_MD} not found")
        return

    scan_date = _extract_scan_date(content)
    groups = parse_trend_rows(content)

    for grp in _GROUP_ORDER:
        print(f"  {_GROUP_META[grp]['emoji']} {grp}: {len(groups[grp])} rows")

    html = build_html(today, now_str, groups, scan_date)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Written → {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
