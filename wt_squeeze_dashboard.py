#!/usr/bin/env python3
"""
WaveTrend Dashboard
Reads wt_bullcross_latest.md and builds wt_squeeze_dashboard.html.

Source : wt_scans/wt_bullcross_latest.md  (wt_bullcross_scanner.py)
Output : wt_squeeze_dashboard.html

Table format (13 cols):
  Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit
"""

import re
import os
import sys
from disclaimer import SEBI_HTML_FOOTER
import json
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding="utf-8")

try:
    from ohlc_db import get_names as _get_names, get_liq_labels as _get_liq_labels
except ImportError:
    _get_names = None
    _get_liq_labels = None

_NAMES: dict[str, str] = {}
_LIQ: dict[str, str] = {}

IST = timezone(timedelta(hours=5, minutes=30))
BASE = os.path.dirname(os.path.abspath(__file__))

WT_MD = os.path.join(BASE, "wt_scans", "wt_bullcross_latest.md")
TREND_MD = os.path.join(BASE, "trend_scans", "trend_scan_latest.md")
BOUNCE_RS_MD = os.path.join(BASE, "bounce_rs_scans", "bounce_rs_scan_latest.md")
OUTPUT_HTML = os.path.join(BASE, "wt_squeeze_dashboard.html")

_LABELS_FILE = os.path.join(BASE, "tools", "stock_labels.json")
_LABELS: dict = {}
if os.path.exists(_LABELS_FILE):
    with open(_LABELS_FILE, encoding="utf-8") as _f:
        _LABELS = json.load(_f)

_RANK_LABEL = {5: "OS+PPV", 4: "ANY+PPV", 3: "OVERSOLD", 2: "OS L2", 1: "ANY MID"}
_RANK_COLOR = {5: "#f97316", 4: "#eab308", 3: "#22c55e", 2: "#84cc16", 1: "#3b82f6"}


def read_file(path: str) -> str:
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def _strip_md_link(s: str) -> str:
    m = re.match(r"\[([^\]]+)\]\([^)]+\)", s)
    return m.group(1) if m else s


def _parse_sym_cell(s: str) -> tuple[str, str, str, bool]:
    """Return (symbol, weekly_zone_badge, rvol_ss_badge, rs_weekly_gate) from a symbol
    cell like '[SJVN](url)<br>📶W9 W↑12d 🚀SS·9x ★'."""
    sym = _strip_md_link(s)
    wz_m = re.search(r"W↑\d+d", s)
    rvol_m = re.search(r"🚀SS(?:·\d+x)?|RVOL\d+x", s)
    rs_weekly_gate = "📶W9" in s
    return (
        sym,
        (wz_m.group(0) if wz_m else ""),
        (rvol_m.group(0) if rvol_m else ""),
        rs_weekly_gate,
    )


# ── Parse WaveTrend markdown ──────────────────────────────────────────────────
# Table cols (13): Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit
# parts indices:     0       1      2       3        4     5     6       7     8        9        10    11        12

_SIG_RANK = {
    "OS_PPV": 5,
    "ANY_PPV": 4,
    "OVERSOLD": 3,
    "OS_L2": 2,
    "ANY": 1,
}


def _sig_to_rank(sig: str) -> int:
    for key, rank in _SIG_RANK.items():
        if key in sig:
            return rank
    return 1


def parse_wt_rows(content: str) -> list[dict]:
    rows = []
    seen: set[str] = set()
    for line in content.splitlines():
        ls = line.strip()
        if not ls.startswith("|"):
            continue
        if ls.startswith("|---") or ls.startswith("| ---"):
            continue
        # preserve empty cells (Label may be empty) — [1:-1] slice, not filter
        # replace \| (escaped pipe inside label cell) before splitting on |
        parts = [p.strip() for p in ls.replace(r"\|", "\x00").split("|")][1:-1]
        if len(parts) < 13:
            continue
        sym, wz_badge, rvol_badge, rs_weekly_gate = _parse_sym_cell(parts[0])
        if not sym or sym in ("Symbol", "#"):
            continue
        if sym in seen:
            continue
        seen.add(sym)
        # ZL col: "↑6d" or "↓6d"
        zl_raw = parts[7]
        zl_dir = "↑" if zl_raw.startswith("↑") else "↓"
        zl_days = zl_raw.lstrip("↑↓").strip()
        # WT col: "41.53/40.92"
        wt_parts = parts[10].split("/")
        wt1 = wt_parts[0].strip() if wt_parts else ""
        wt2 = wt_parts[1].strip() if len(wt_parts) > 1 else ""
        # Flags col: "SQ·PV" | "SQ" | "PV" | "—"
        flags = parts[8]
        squeeze = "SQ" in flags
        ppv = "PV" in flags
        # RS col: "🔄82" | "↑82" | "↓30"
        rs_raw = parts[5]
        if rs_raw.startswith("🔄"):
            rs_state = "transition"
        elif rs_raw.startswith("↑"):
            rs_state = "strong"
        else:
            rs_state = "weak"
        rows.append(
            {
                "symbol": sym,
                "wz_badge": wz_badge,
                "rvol_badge": rvol_badge,
                "rs_weekly_gate": rs_weekly_gate,
                "trap": parts[1],
                "label": parts[2].replace("\x00", "|"),
                "signal": parts[3],
                "rank": _sig_to_rank(parts[3]),
                "earliness": parts[4],
                "rs_raw": rs_raw,
                "rs_state": rs_state,
                "cavgc": parts[6],
                "zl_dir": zl_dir,
                "zl_days": zl_days,
                "flags": flags,
                "squeeze": squeeze,
                "ppv": ppv,
                "zl_pct": parts[9],
                "wt": parts[10],
                "wt1": wt1,
                "wt2": wt2,
                "day_chg": parts[11],
                "circuit": parts[12],
            }
        )
    rows.sort(
        key=lambda r: (
            not r["rs_weekly_gate"],
            -r["rank"],
            -(
                float(r["earliness"])
                if r["earliness"].replace(".", "", 1).isdigit()
                else 0
            ),
        )
    )
    return rows


def parse_bounce_rs(content: str) -> list[dict]:
    """Parse bounce_rs_scan_latest.md's 8-col table. '*No signals.*' or an
    empty file both correctly yield []."""
    rows = []
    for line in content.splitlines():
        ls = line.strip()
        if not ls.startswith("|"):
            continue
        if ls.startswith("|---") or ls.startswith("| ---"):
            continue
        parts = [p.strip() for p in ls.split("|")][1:-1]
        if len(parts) != 8:
            continue
        sym = _strip_md_link(parts[0])
        if not sym or sym == "Symbol":
            continue
        rows.append(
            {
                "symbol": sym,
                "rs_pct": parts[1],
                "ema_type": parts[2],
                "setup": parts[3],
                "dip_low": parts[4],
                "ratio_now": parts[5],
                "bounce": parts[6],
                "score": parts[7],
            }
        )
    return rows


_BOUNCE_RS_TABLE_HDR = """    <thead><tr>
      <th>Symbol</th><th>RS Dip%</th><th>EMA Type</th><th>Setup</th>
      <th>Dip Low</th><th>Ratio Now</th><th>Bounce</th><th>Score</th>
    </tr></thead>"""


def _bounce_rs_html_row(r: dict) -> str:
    tv = f"https://in.tradingview.com/chart/?symbol=NSE:{r['symbol']}"
    return (
        f'<tr><td class="sym"><a href="{tv}" target="_blank">{r["symbol"]}</a></td>'
        f'<td class="num">{r["rs_pct"]}</td>'
        f'<td class="mu">{r["ema_type"]}</td>'
        f'<td class="mu">{r["setup"]}</td>'
        f'<td class="num">{r["dip_low"]}</td>'
        f'<td class="num">{r["ratio_now"]}</td>'
        f'<td class="num">{r["bounce"]}</td>'
        f'<td class="num">{r["score"]}</td></tr>'
    )


def _bounce_rs_section_html(rows: list[dict]) -> str:
    """Bounce-RS top-of-dashboard table. Empty string (section hidden entirely)
    when rows is empty — a dip-bounce regime is rare, no permanent placeholder."""
    if not rows:
        return ""
    rows_html = [_bounce_rs_html_row(r) for r in rows]
    return f"""
<div class="section" style="border:1px solid #f97316;border-radius:6px;padding:12px;background:#1a0f00">
  <div class="stitle" style="color:#f97316;border-color:#f97316">
    🔄 BOUNCE-RS — positive RS through breadth dip, bounce confirmed
    <span class="cnt" style="color:#f97316">({len(rows)} stocks)</span>
  </div>
  <table>
{_BOUNCE_RS_TABLE_HDR}
    <tbody>{"".join(rows_html)}</tbody>
  </table>
</div>
"""


def parse_trend_symbols(content: str) -> dict[str, str]:
    """Return {symbol: signal_tag} for every row in trend_scan_latest.md.

    signal_tag is one of: LEADER_ZL, ZL_PULLBACK, EMA_SUPPORT, ZL_ENTRY, TREND (fallback).
    Tag is derived from the ### section heading, not the Signal cell (which uses
    human-readable text and contains escaped pipes that break column-index parsing).
    """
    _SEC_MAP = (
        ("LEADER ZL", "LEADER_ZL"),
        ("ZL PULLBACK", "ZL_PULLBACK"),
        ("EMA SUPPORT", "EMA_SUPPORT"),
        ("ZL ENTRY", "ZL_ENTRY"),
    )
    result: dict[str, str] = {}
    in_table = False
    current_tag = "TREND"
    for line in content.splitlines():
        ls = line.strip()
        if ls.startswith("###"):
            in_table = False
            current_tag = "TREND"
            for key, tag in _SEC_MAP:
                if key in ls:
                    current_tag = tag
                    break
            continue
        if "| Symbol" in ls and "| Signal" in ls and "| Score" in ls:
            in_table = True
            continue
        if in_table and ls.startswith("|---"):
            continue
        if in_table and ls.startswith("|"):
            # Replace escaped pipes (\|) before splitting to avoid column shift
            parts = [
                p.strip() for p in ls.replace(r"\|", "\x00").split("|") if p.strip()
            ]
            if len(parts) < 2:
                continue
            sym = _strip_md_link(parts[0])
            if not sym or sym == "Symbol":
                continue
            result[sym] = current_tag
    return result


# ── HTML helpers ──────────────────────────────────────────────────────────────


def _tv_link(sym: str) -> str:
    co = _NAMES.get(sym, "")
    liq = _LIQ.get(sym, "")
    # Split "Company · ₹MCap" → company on line 2, ₹MCap | notionals on line 3
    _parts = co.rsplit(" · ", 1)
    if len(_parts) == 2 and _parts[1].startswith("₹"):
        name_part, mcap_part = _parts
    else:
        name_part, mcap_part = co, ""
    name_span = f'<span class="co-name">{name_part}</span>' if name_part else ""
    liq_content = f"{mcap_part} | {liq}" if mcap_part and liq else (mcap_part or liq)
    liq_span = f'<span class="liq-tag">{liq_content}</span>' if liq_content else ""
    return f'<a href="https://in.tradingview.com/chart/?symbol=NSE:{sym}" target="_blank" rel="noopener">{sym}</a>{name_span}{liq_span}'


def _desc_from_label(label: str) -> str:
    parts = label.split("<br>")
    if len(parts) == 1:
        return label  # new format: label IS description
    return parts[2] if len(parts) >= 3 else ""


def _chg_cls(v: str) -> str:
    return "pos" if v.startswith("+") else ("neg" if v.startswith("-") else "")


def _rank_badge(rank: int) -> str:
    color = _RANK_COLOR.get(rank, "#6b7280")
    label = _RANK_LABEL.get(rank, str(rank))
    return (
        f'<span style="background:{color};color:#fff;font-size:9px;'
        f'padding:1px 6px;border-radius:3px;font-weight:700">{label}</span>'
    )


def _rs_badge(rs_raw: str, rs_state: str) -> str:
    cls = (
        "gld" if rs_state == "transition" else ("pos" if rs_state == "strong" else "mu")
    )
    return f'<span class="{cls}">{rs_raw}</span>'


def _trap_html(trap: str) -> str:
    if "SAFE" in trap:
        return f'<span class="pos">{trap}</span>'
    if "CAUTION" in trap:
        return f'<span style="color:var(--ylw)">{trap}</span>'
    if "AVOID" in trap:
        return f'<span class="neg">{trap}</span>'
    return f'<span class="mu">{trap}</span>'


def _flags_html(flags: str) -> str:
    parts = []
    if "SQ" in flags:
        parts.append('<span style="color:var(--gld);font-weight:700">SQ</span>')
    if "PV" in flags:
        parts.append('<span style="color:var(--pur);font-weight:700">PV</span>')
    return "·".join(parts) if parts else '<span class="mu">—</span>'


_TREND_TAG_LABEL = {
    "LEADER_ZL": "🏆 LEADER ZL",
    "ZL_PULLBACK": "ZL PULL",
    "EMA_SUPPORT": "EMA SUP",
    "ZL_ENTRY": "ZL ENTRY",
    "TREND": "TREND",
}


def _wt_html_row(r: dict, trend_info: "dict | None" = None) -> str:
    sym = r["symbol"]
    zl_cls = "pos" if r["zl_dir"] == "↑" else "neg"
    cavgc_cls = "pos" if r["cavgc"].startswith("↑") else "mu"
    badges = []
    if r.get("rs_weekly_gate"):
        badges.append('<span style="font-weight:700;color:#38bdf8">📶W9</span>')
    wz = r.get("wz_badge", "")
    if wz:
        badges.append(f'<span class="mu">{wz}</span>')
    rv = r.get("rvol_badge", "")
    if rv:
        badges.append(
            f'<span style="font-weight:700;color:var(--org,#e08300)">{rv}</span>'
        )
    if trend_info and sym in trend_info:
        lbl = _TREND_TAG_LABEL.get(trend_info[sym], trend_info[sym])
        badges.append(f'<span style="font-weight:700;color:#86efac">{lbl}</span>')
    badge_line = (
        f'<span style="display:block;font-size:9px;white-space:nowrap">{" · ".join(badges)}</span>'
        if badges
        else ""
    )
    return (
        f"<tr>"
        f'<td class="sym">{_tv_link(sym)}{badge_line}</td>'
        f'<td style="font-size:10px;white-space:nowrap">{_trap_html(r.get("trap","n/a"))}</td>'
        f'<td class="lbl">{_desc_from_label(r["label"])}</td>'
        f'<td>{_rank_badge(r["rank"])}</td>'
        f'<td class="num">{r["earliness"]}</td>'
        f'<td style="text-align:center">{_rs_badge(r["rs_raw"], r["rs_state"])}</td>'
        f'<td class="{cavgc_cls}">{r["cavgc"]}</td>'
        f'<td class="{zl_cls}">{r["zl_dir"]}{r["zl_days"]}</td>'
        f'<td style="text-align:center">{_flags_html(r["flags"])}</td>'
        f'<td class="{_chg_cls(r["zl_pct"])}">{r["zl_pct"]}</td>'
        f'<td class="num">{r["wt"]}</td>'
        f'<td class="{_chg_cls(r["day_chg"])}">{r["day_chg"]}</td>'
        f'<td class="mu">{r["circuit"]}</td>'
        f"</tr>"
    )


def _rows_or_empty(rows_html: list[str], cols: int, msg: str) -> str:
    return (
        "\n".join(rows_html)
        if rows_html
        else f'<tr><td colspan="{cols}" class="empty">{msg}</td></tr>'
    )


def _tv_watchlist_csv(rows: list[dict]) -> str:
    return ",".join(f"NSE:{r['symbol']}" for r in rows)


def _copy_btn(rows: list[dict]) -> str:
    if not rows:
        return ""
    return f'<button class="copy-btn" data-syms="{_tv_watchlist_csv(rows)}">📋 Copy TV List ({len(rows)})</button>'


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
.co-name{display:block;font-size:10px;color:var(--mu);font-weight:normal;line-height:1.2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:160px}
.liq-tag{display:block;font-size:9px;color:#6b9aaa;font-family:monospace;font-weight:600;line-height:1.3;letter-spacing:0.02em}
.lbl{font-size:11px;color:var(--mu);max-width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.mu{color:var(--mu);font-size:11px}
.num{font-family:monospace;font-size:12px;color:var(--mu)}
.pos{color:var(--grn)}.neg{color:var(--red)}
.sqz-hi{color:var(--gld);font-weight:700;text-align:center}
.sqz-on{color:var(--grn);font-weight:600;text-align:center}
.sqz-off{color:var(--mu);text-align:center;font-size:11px}
.empty{color:var(--mu);font-style:italic;text-align:center;padding:10px}

.copy-btn{margin-left:auto;background:var(--bg3);border:1px solid var(--bd);color:var(--tx);
  font-size:10px;padding:3px 9px;border-radius:4px;cursor:pointer;text-transform:none;letter-spacing:0;font-weight:600}
.copy-btn:hover{background:var(--bd);border-color:var(--blu)}
.copy-btn.copied{background:var(--grn);border-color:var(--grn);color:#0d1117}
.trend-tag{display:inline-block;font-size:8px;background:#14532d;color:#86efac;
  padding:1px 5px;border-radius:3px;font-weight:700;letter-spacing:.4px;margin-top:2px;white-space:nowrap}
"""


_TABLE_HDR = """    <thead><tr>
      <th>Symbol</th><th>Trap</th><th>Label</th><th>WT Signal</th>
      <th>Erly</th><th>RS</th><th>C/AvgC</th><th>ZL</th><th>Flags</th>
      <th>ZL Chg%</th><th>WT1/WT2</th><th>Day Chg</th><th>Circuit</th>
    </tr></thead>"""


def build_html(
    today: str,
    now_str: str,
    wt_rows: list,
    trend_info: "dict | None" = None,
    bounce_rs_rows: "list | None" = None,
) -> str:
    trend_info = trend_info or {}
    bounce_rs_section = _bounce_rs_section_html(bounce_rs_rows or [])
    sqz_rows = [r for r in wt_rows if r["squeeze"]]
    other_rows = [r for r in wt_rows if not r["squeeze"]]
    # Trend × WT confluence — all WT rows also in trend scanner, rank desc
    conf_rows = [r for r in wt_rows if r["symbol"] in trend_info]
    # RS-Confirmed — informational subset, additive (every row also appears above/below)
    rs_rows = [r for r in wt_rows if r["rs_state"] != "weak"]
    wt_html = [_wt_html_row(r, trend_info) for r in other_rows]
    sqz_html = [_wt_html_row(r, trend_info) for r in sqz_rows]
    rs_html = [_wt_html_row(r, trend_info) for r in rs_rows]
    n_os_plus = sum(1 for r in wt_rows if r["rank"] >= 3)
    n_ppv = sum(1 for r in wt_rows if r["ppv"])
    n_sqz = len(sqz_rows)
    n_conf = len(conf_rows)
    n_rs = len(rs_rows)

    conf_html = [_wt_html_row(r, trend_info) for r in conf_rows]
    conf_section = ""
    if conf_rows:
        conf_section = f"""
<div class="section" style="border:1px solid #16a34a;border-radius:6px;padding:12px;background:#071a0f">
  <div class="stitle" style="color:#4ade80;border-color:#16a34a">
    🏆 TREND × WT BULLCROSS — Stage-2 leader in pullback + WT signal firing now
    <span class="cnt" style="color:#4ade80">({n_conf} stocks)</span>
    {_copy_btn(conf_rows)}
  </div>
  <p style="font-size:11px;color:#86efac;margin-bottom:8px;opacity:.85">
    These stocks passed the trend scanner (Stage-2 leader, RS ≥60, ZLEMA25 rising, near key support)
    AND have a WT bull cross today. Highest-rank WT signals first.
    🏆 LEADER ZL = ZLEMA25 touch + RS holds + vol dry-up (best setup).
  </p>
  <table>
{_TABLE_HDR}
    <tbody>{"".join(conf_html)}</tbody>
  </table>
</div>
"""

    wg_rows = [r for r in wt_rows if r["rs_weekly_gate"]]
    wg_html = [_wt_html_row(r, trend_info) for r in wg_rows]
    n_wg = len(wg_rows)
    wg_section = ""
    if wg_rows:
        wg_section = f"""
<div class="section" style="border:1px solid #38bdf8;border-radius:6px;padding:12px;background:#001a26">
  <div class="stitle" style="color:#38bdf8;border-color:#38bdf8">
    📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400
    <span class="cnt" style="color:#38bdf8">({n_wg} of {len(wt_rows)})</span>
    {_copy_btn(wg_rows)}
  </div>
  <p style="font-size:11px;color:#7dd3fc;margin-bottom:8px;opacity:.85">
    Informational, not a filter — every row here also appears in its rank/squeeze section below.
  </p>
  <table>
{_TABLE_HDR}
    <tbody>{"".join(wg_html)}</tbody>
  </table>
</div>
"""

    rs_section = ""
    if rs_rows:
        rs_section = f"""
<div class="section" style="border:1px solid #38bdf8;border-radius:6px;padding:12px;background:#001a26">
  <div class="stitle" style="color:#38bdf8;border-color:#38bdf8">
    📶 RS-CONFIRMED — RS strong or transitioning vs NIFTY MIDSML 400
    <span class="cnt" style="color:#38bdf8">({n_rs} of {len(wt_rows)})</span>
    {_copy_btn(rs_rows)}
  </div>
  <p style="font-size:11px;color:#7dd3fc;margin-bottom:8px;opacity:.85">
    Informational, not a filter — every row here also appears in its rank/squeeze section below.
  </p>
  <table>
{_TABLE_HDR}
    <tbody>{"".join(rs_html)}</tbody>
  </table>
</div>
"""

    sqz_section = ""
    if sqz_rows:
        sqz_section = f"""
<div class="section" style="border:1px solid var(--gld);border-radius:6px;padding:12px;background:#1a1600">
  <div class="stitle" style="color:var(--gld);border-color:var(--gld)">
    🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze
    <span class="cnt" style="color:var(--gld)">({n_sqz} highest conviction)</span>
    {_copy_btn(sqz_rows)}
  </div>
  <p style="font-size:11px;color:#b8a000;margin-bottom:8px">
    BB-KC squeeze (energy coiling) + WT bull cross (momentum turning up) = spring loaded → fires UP.
    Oversold cross inside squeeze = maximum compression + mean-reversion force.
  </p>
  <table>
{_TABLE_HDR}
    <tbody>{"".join(sqz_html)}</tbody>
  </table>
</div>
"""

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
  Erly = earliness score (higher = earlier entry) &nbsp;|&nbsp;
  RS = 🔄transition / ↑strong / ↓weak vs NIFTY MIDSML 400 &nbsp;|&nbsp;
  Flags = SQ (BB-KC squeeze ON) · PV (Pocket Pivot Volume) &nbsp;|&nbsp;
  Sorted: rank desc → earliness desc
</div>
{bounce_rs_section}
<div class="bar">
  <div class="stat"><div class="sv grn">{n_conf}</div><div class="sl">🏆 Trend×WT</div></div>
  <div class="stat"><div class="sv gld">{n_sqz}</div><div class="sl">🎯 Squeeze Break</div></div>
  <div class="stat"><div class="sv" style="color:#38bdf8">{n_wg}</div><div class="sl">📶 Weekly RS Gate</div></div>
  <div class="stat"><div class="sv" style="color:#38bdf8">{n_rs}</div><div class="sl">RS-Confirmed</div></div>
  <div class="stat"><div class="sv ora">{len(wt_rows)}</div><div class="sl">WT Bull Cross</div></div>
  <div class="stat"><div class="sv grn">{n_os_plus}</div><div class="sl">Oversold+ (rank≥3)</div></div>
  <div class="stat"><div class="sv pur">{n_ppv}</div><div class="sl">PPV confirmed</div></div>
</div>

{wg_section}
{conf_section}
{rs_section}
{sqz_section}
<div class="section">
  <div class="stitle">
    Other WT Bull Crosses — no active squeeze
    <span class="cnt">({len(other_rows)} signals — sorted rank desc, deeper oversold first)</span>
    {_copy_btn(other_rows)}
  </div>
  <table>
{_TABLE_HDR}
    <tbody>{_rows_or_empty(wt_html, 13, "No other WT bull crosses today")}</tbody>
  </table>
</div>

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
{SEBI_HTML_FOOTER}
</body>
</html>"""


def main():
    global _NAMES, _LIQ
    if _get_names:
        _NAMES = _get_names()
    if _get_liq_labels:
        _LIQ = _get_liq_labels(symbols=list(_NAMES.keys()) if _NAMES else None)

    now_ist = datetime.now(IST)
    today = now_ist.strftime("%Y-%m-%d")
    now_str = now_ist.strftime("%Y-%m-%d %H:%M IST")

    print(f"[{now_str}] Building WaveTrend + Squeeze Dashboard...")

    wt_rows = parse_wt_rows(read_file(WT_MD))
    print(f"  WT bull crosses : {len(wt_rows)}")

    trend_info = parse_trend_symbols(read_file(TREND_MD))
    conf_count = sum(1 for r in wt_rows if r["symbol"] in trend_info)
    print(
        f"  Trend leaders   : {len(trend_info)}  |  Trend×WT confluence: {conf_count}"
    )

    bounce_rs_rows = parse_bounce_rs(read_file(BOUNCE_RS_MD))
    print(f"  Bounce-RS       : {len(bounce_rs_rows)}")

    html = build_html(today, now_str, wt_rows, trend_info, bounce_rs_rows)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Written → {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
