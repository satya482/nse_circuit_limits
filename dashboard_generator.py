#!/usr/bin/env python3
"""
NSE Daily Dashboard — aggregates all scan results for today.
Reads 5 markdown files, builds confluence-ranked HTML dashboard.
Output: dashboard.html
"""

import re, os
from datetime import datetime, timezone, timedelta
from collections import defaultdict

IST = timezone(timedelta(hours=5, minutes=30))
BASE = os.path.dirname(os.path.abspath(__file__))

SWING_MD       = os.path.join(BASE, "swing_scans", "swing_scans.md")
MOMENTUM_MD    = os.path.join(BASE, "momentum_scans", "momentum_scans.md")
WEEKLY_RS_MD   = os.path.join(BASE, "momentum_scans", "momentum_rs_weekly_scans.md")
EMA25_ZL_MD    = os.path.join(BASE, "ema25_zl_scans", "ema25_zl_scans.md")
EMA_MD         = os.path.join(BASE, "ema_screener_changes.md")
CIRCUIT_MD     = os.path.join(BASE, "NSE_Circuit_Limits.md")
COMPRESSION_MD = os.path.join(BASE, "ema-compression-scanner",
                               "ema_compression_scans", "ema_compression_latest.md")
DASHBOARD_HTML = os.path.join(BASE, "dashboard.html")


def read_file(path: str) -> str:
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def extract_today_block(content: str, today: str) -> str:
    """Return the first (newest) block whose heading contains today's date."""
    blocks = re.split(r'\n---\n', content)
    for block in blocks:
        if re.search(rf'^# .+{re.escape(today)}', block, re.MULTILINE):
            return block
    return ""


_ZL_DAY_RE = re.compile(r'^\d+d\+?$')

def _strip_md_link(s: str) -> str:
    """[TEXT](url) → TEXT, else return as-is."""
    m = re.match(r'\[([^\]]+)\]\([^)]+\)', s)
    return m.group(1) if m else s

def _parse_table_rows(text: str, has_signal: bool) -> list:
    """Generic row parser. has_signal=True for entry tables (6-col new / 4-col old),
    has_signal=False for turning-up tables (5-col new / 3-col old)."""
    results = []
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        header_match = ('| Signal' in line) if has_signal else ('| Day Change' in line and '| Signal' not in line)
        if '| Symbol' in line and header_match:
            i += 1
            if i < len(lines) and lines[i].strip().startswith('|---'):
                i += 1
            while i < len(lines):
                row = lines[i].strip()
                if not row.startswith('|'):
                    break
                parts = [p.strip() for p in row.split('|')]
                parts = [p for p in parts if p != '']
                if parts:
                    sym = _strip_md_link(parts[0])
                    if has_signal:
                        sig_raw = parts[1] if len(parts) > 1 else ""
                        day_chg = parts[2] if len(parts) > 2 else ""
                        # Detect new format: parts[3] looks like "5d" or "5d+"
                        if len(parts) >= 5 and _ZL_DAY_RE.match(parts[3]):
                            zl_days = parts[3]
                            zl_pct  = parts[4] if len(parts) > 4 else ""
                            circuit = parts[5] if len(parts) > 5 else ""
                        else:
                            zl_days = ""
                            zl_pct  = ""
                            circuit = parts[3] if len(parts) > 3 else ""
                        sig = ("STRONG" if "STRONG" in sig_raw
                               else "PRIMARY" if "PRIMARY" in sig_raw
                               else "DEEP PULLBACK" if "DEEP" in sig_raw
                               else sig_raw)
                        results.append({"symbol": sym, "signal": sig, "day_chg": day_chg,
                                        "zl_days": zl_days, "zl_pct": zl_pct, "circuit": circuit})
                    else:
                        day_chg = parts[1] if len(parts) > 1 else ""
                        if len(parts) >= 3 and _ZL_DAY_RE.match(parts[2]):
                            zl_days = parts[2]
                            zl_pct  = parts[3] if len(parts) > 3 else ""
                            circuit = parts[4] if len(parts) > 4 else ""
                        else:
                            zl_days = ""
                            zl_pct  = ""
                            circuit = parts[2] if len(parts) > 2 else ""
                        results.append({"symbol": sym, "day_chg": day_chg,
                                        "zl_days": zl_days, "zl_pct": zl_pct, "circuit": circuit})
                i += 1
            return results
        i += 1
    return results

def parse_signal_table(text: str) -> list:
    return _parse_table_rows(text, has_signal=True)

def parse_turning_table(text: str) -> list:
    return _parse_table_rows(text, has_signal=False)


def parse_weekly_rs_block(block: str) -> tuple:
    """Return (entry_signals, turning_signals) from a weekly RS scan block."""
    entry_m   = re.search(r'### Entry Signals\n(.*?)(?=###|\Z)', block, re.DOTALL)
    turning_m = re.search(r'### ZLEMA25 Turning Up[^\n]*\n(.*?)(?=###|\Z)', block, re.DOTALL)

    if entry_m:
        entry   = parse_signal_table(entry_m.group(1))
        turning = parse_turning_table(turning_m.group(1)) if turning_m else []
    else:
        # Old format — entire block is the entry table, no turning section
        entry   = parse_signal_table(block)
        turning = []
    return entry, turning


def parse_ema_changes(content: str) -> tuple:
    """Parse additions and deletions from ema_screener_changes.md."""
    additions, deletions = [], []

    add_m = re.search(r'## ✅ Additions.*?\n(.*?)(?=^##|\Z)', content, re.DOTALL | re.MULTILINE)
    if add_m:
        for line in add_m.group(1).splitlines():
            line = line.strip()
            if line.startswith('|') and not line.startswith('| Symbol') and not line.startswith('|---'):
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 2:
                    additions.append({"symbol": _strip_md_link(parts[0]), "day_chg": parts[1]})

    del_m = re.search(r'## ❌ Deletions.*?\n(.*?)(?=^##|\Z)', content, re.DOTALL | re.MULTILINE)
    if del_m:
        for line in del_m.group(1).splitlines():
            line = line.strip()
            if line.startswith('|') and not line.startswith('| Symbol') and not line.startswith('|---'):
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 2:
                    deletions.append({"symbol": _strip_md_link(parts[0]), "day_chg": parts[1]})

    return additions, deletions


def parse_ema_date(content: str) -> str:
    m = re.search(r'^# NSE EMA Screener — (\d{4}-\d{2}-\d{2})', content, re.MULTILINE)
    return m.group(1) if m else ""


def parse_ema25_zl(content: str, today: str) -> tuple[list, list]:
    """Parse ema25_zl_scans.md → (rising, watch) for today's block."""
    block = extract_today_block(content, today)
    if not block:
        return [], []

    def _parse_section(section_text: str) -> list:
        rows = []
        for line in section_text.splitlines():
            line = line.strip()
            if not line.startswith('|') or line.startswith('| Symbol') or line.startswith('|---'):
                continue
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) < 5:
                continue
            # New format (7 cols): Symbol Close DayChg ZLDays ZLChg% Squeeze Circuit
            # Old format (6 cols): Symbol Close DayChg ZLDays ZLChg% Circuit
            if len(parts) >= 7:
                squeeze, circuit = parts[5], parts[6]
            elif len(parts) >= 6:
                squeeze, circuit = "", parts[5]
            else:
                squeeze, circuit = "", ""
            rows.append({
                "symbol":  _strip_md_link(parts[0]),
                "close":   parts[1],
                "day_chg": parts[2],
                "zl_days": parts[3],
                "zl_pct":  parts[4],
                "squeeze": squeeze,
                "circuit": circuit,
            })
        return rows

    rising_m = re.search(r'### ZLEMA25 Rising\n(.*?)(?=###|\Z)', block, re.DOTALL)
    watch_m  = re.search(r'### ZLEMA25 Watch[^\n]*\n(.*?)(?=###|\Z)', block, re.DOTALL)

    rising = _parse_section(rising_m.group(1)) if rising_m else []
    watch  = _parse_section(watch_m.group(1))  if watch_m  else []
    return rising, watch


def parse_circuit_changes(content: str, limit: int = 12) -> list:
    changes = []
    in_table = False
    for line in content.splitlines():
        line = line.strip()
        if line.startswith('| Date'):
            in_table = True
            continue
        if line.startswith('|---'):
            continue
        if in_table and line.startswith('|'):
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 5:
                changes.append({
                    "date":   parts[0],
                    "symbol": _strip_md_link(parts[1]).replace('**', ''),
                    "name":   parts[2],
                    "from_":  parts[3],
                    "to_":    parts[4],
                })
        elif in_table and not line.startswith('|'):
            break
    return changes[:limit]


def parse_ema_compression(content: str, today: str) -> tuple[list, int, int]:
    """Parse ema_compression_latest.md → (signal_rows, total_compressed, total_signals).

    New format (single flat table):
        cols: # | Symbol | Sector | Close | Comp Days | Sqz Days | ZL | ZL Days | ZL Chg% | Score
    """
    if today not in content[:150]:
        return [], 0, 0

    total_m   = re.search(r'\*\*Compressed[^:]*:\*\* (\d+)', content)
    signals_m = re.search(r'\*\*Signals:\*\* (\d+)', content)
    total_compressed = int(total_m.group(1))   if total_m   else 0
    total_signals    = int(signals_m.group(1)) if signals_m else 0

    rows = []
    in_table = False
    for line in content.splitlines():
        ls = line.strip()
        if ls.startswith('|') and 'Symbol' in ls and 'Comp Days' in ls:
            in_table = True
            continue
        if in_table and ls.startswith('|---'):
            continue
        if in_table and ls.startswith('|'):
            parts = [p.strip() for p in ls.split('|') if p.strip()]
            # cols: 0=# 1=Symbol 2=Sector 3=Close 4=Comp Days 5=Sqz Days 6=ZL 7=ZL Days 8=ZL Chg% 9=Score
            if len(parts) >= 10 and parts[0].isdigit():
                rows.append({
                    "symbol":    _strip_md_link(parts[1]),
                    "sector":    parts[2],
                    "close":     parts[3],
                    "comp_days": parts[4],
                    "sqz_days":  parts[5],
                    "zl_dir":    parts[6],
                    "zl_days":   parts[7],
                    "zl_chg":    parts[8],
                    "score":     parts[9].replace('**', ''),
                })
        elif in_table and not ls.startswith('|'):
            break

    return rows, total_compressed, total_signals


# ── HTML helpers ──────────────────────────────────────────────────────────────

def tv_link(symbol: str) -> str:
    url = f"https://in.tradingview.com/chart/?symbol=NSE:{symbol}"
    return f'<a href="{url}" target="_blank" rel="noopener">{symbol}</a>'


def chg_cls(v: str) -> str:
    return "pos" if v.startswith('+') else ("neg" if v.startswith('-') else "")


def circuit_cls(s: str) -> str:
    if '🟨' in s: return 'ccy'
    if '🟥' in s: return 'ccr'
    if '🟩' in s: return 'ccg'
    if '🟦' in s: return 'ccb'
    return ''


def td_circ(circuit: str) -> str:
    cls = circuit_cls(circuit)
    return f'<td class="{cls}">{circuit}</td>' if cls else f'<td>{circuit}</td>'


def chg_float(s: str) -> float:
    try:
        return float(s.rstrip('%').lstrip('+'))
    except Exception:
        return 0.0


# ── Main HTML builder ─────────────────────────────────────────────────────────

def build_html(today: str, now_str: str,
               swing: list, momentum: list,
               weekly_entry: list, weekly_turning: list,
               zl25_rising: list, zl25_watch: list,
               ema_adds: list, ema_dels: list, ema_date: str,
               circuit_changes: list,
               compression_rows: list, total_compressed: int, total_zl_rising: int) -> str:

    # Build unified confluence map
    scanner_map: dict = defaultdict(set)
    signal_map:  dict = {}
    day_chg_map: dict = {}
    circuit_map: dict = {}
    zl_days_map: dict = {}
    zl_pct_map:  dict = {}

    def register(rows, tag):
        for r in rows:
            s = r["symbol"]
            scanner_map[s].add(tag)
            signal_map.setdefault(s, r.get("signal", ""))
            if not day_chg_map.get(s):
                day_chg_map[s] = r.get("day_chg", "")
            if not circuit_map.get(s):
                circuit_map[s] = r.get("circuit", "")
            if not zl_days_map.get(s) and r.get("zl_days"):
                zl_days_map[s] = r.get("zl_days", "")
                zl_pct_map[s]  = r.get("zl_pct", "")

    register(swing,        "Swing")
    register(momentum,     "Momentum")
    register(weekly_entry, "WeeklyRS")

    all_syms = sorted(
        scanner_map.keys(),
        key=lambda s: (len(scanner_map[s]), chg_float(day_chg_map.get(s, "0"))),
        reverse=True,
    )

    triple = sum(1 for s in scanner_map if len(scanner_map[s]) == 3)
    double = sum(1 for s in scanner_map if len(scanner_map[s]) == 2)

    # Unified table rows
    u_rows = []
    for sym in all_syms:
        tags = scanner_map[sym]
        n    = len(tags)
        if n == 3:
            stars = '<span class="s3">★★★</span>'
            rcls  = ' class="r3"'
        elif n == 2:
            stars = '<span class="s2">★★</span>'
            rcls  = ' class="r2"'
        else:
            stars = '<span class="s1">★</span>'
            rcls  = ''

        badges = "".join(
            f'<span class="b b-{t.lower()}">{t}</span>'
            for t in sorted(tags)
        )
        sig  = signal_map.get(sym, "")
        chg  = day_chg_map.get(sym, "")
        circ = circuit_map.get(sym, "")
        sig_cls = "ss" if sig == "STRONG" else ("sp" if sig == "PRIMARY" else "sd")

        zld  = zl_days_map.get(sym, "")
        zlp  = zl_pct_map.get(sym, "")
        u_rows.append(
            f'<tr{rcls}>'
            f'<td>{stars}</td>'
            f'<td class="sym">{tv_link(sym)}</td>'
            f'<td>{badges}</td>'
            f'<td class="{sig_cls}">{sig}</td>'
            f'<td class="{chg_cls(chg)}">{chg}</td>'
            f'<td class="zld">{zld}</td>'
            f'<td class="{chg_cls(zlp)}">{zlp}</td>'
            f'{td_circ(circ)}'
            f'</tr>'
        )

    # Turning table rows
    t_rows = [
        f'<tr>'
        f'<td class="sym">{tv_link(r["symbol"])}</td>'
        f'<td class="{chg_cls(r["day_chg"])}">{r["day_chg"]}</td>'
        f'<td class="zld">{r.get("zl_days","")}</td>'
        f'<td class="{chg_cls(r.get("zl_pct",""))}">{r.get("zl_pct","")}</td>'
        f'{td_circ(r["circuit"])}</tr>'
        for r in weekly_turning
    ]

    # EMA25 ZL rows
    def _zl_row(r):
        sqz = r.get("squeeze", "")
        sqz_cls = "sqz-on" if sqz == "✓" else "sqz-off"
        return (
            f'<tr><td class="sym">{tv_link(r["symbol"])}</td>'
            f'<td class="num">{r["close"]}</td>'
            f'<td class="{chg_cls(r["day_chg"])}">{r["day_chg"]}</td>'
            f'<td class="zld">{r["zl_days"]}</td>'
            f'<td class="{chg_cls(r["zl_pct"])}">{r["zl_pct"]}</td>'
            f'<td class="{sqz_cls}">{sqz if sqz else "—"}</td>'
            f'{td_circ(r["circuit"])}</tr>'
        )
    zr_rows = [_zl_row(r) for r in zl25_rising[:20]]
    zw_rows = [_zl_row(r) for r in zl25_watch[:15]]

    # EMA adds / dels
    ea_rows = [
        f'<tr><td class="sym">{tv_link(r["symbol"])}</td>'
        f'<td class="{chg_cls(r["day_chg"])}">{r["day_chg"]}</td></tr>'
        for r in ema_adds[:12]
    ]
    ed_rows = [
        f'<tr><td class="sym">{tv_link(r["symbol"])}</td>'
        f'<td class="{chg_cls(r["day_chg"])}">{r["day_chg"]}</td></tr>'
        for r in ema_dels[:12]
    ]

    # Circuit change rows
    cc_rows = []
    for r in circuit_changes:
        cls = circuit_cls(r["to_"])
        cc_rows.append(
            f'<tr><td>{r["date"]}</td>'
            f'<td class="sym">{tv_link(r["symbol"])}</td>'
            f'<td class="nm">{r["name"]}</td>'
            f'<td>{r["from_"]}</td>'
            f'<td class="{cls}">{r["to_"]}</td></tr>'
        )

    def table_or_empty(rows, cols, empty_msg):
        if rows:
            return "\n".join(rows)
        return f'<tr><td colspan="{cols}" class="empty">{empty_msg}</td></tr>'

    # EMA Compression rows
    comp_rows_html = []
    for r in compression_rows[:20]:
        zld = r["zl_days"]
        zlc = r["zl_chg"]
        comp_rows_html.append(
            f'<tr>'
            f'<td class="sym">{tv_link(r["symbol"])}</td>'
            f'<td class="num">{r["close"]}</td>'
            f'<td class="zld">{r["comp_days"]}</td>'
            f'<td class="zld">{r.get("sqz_days", "—")}</td>'
            f'<td class="num">{r["score"]}</td>'
            f'<td class="zld">{zld}</td>'
            f'<td class="{chg_cls(zlc)}">{zlc}</td>'
            f'</tr>'
        )

    compression_section = ""
    if compression_rows or total_compressed:
        compression_section = f"""
<div class="section">
  <div class="stitle">EMA Compression + BB Squeeze — top {len(compression_rows[:20])} signals &nbsp;|&nbsp; {total_compressed} compressed &nbsp;|&nbsp; {total_zl_rising} passed all gates</div>
  <table>
    <thead><tr><th>Symbol</th><th>Close</th><th>Comp Days</th><th>Sqz Days</th><th>Score</th><th>ZL Days</th><th>ZL Chg%</th></tr></thead>
    <tbody>{table_or_empty(comp_rows_html, 7, "No signals today")}</tbody>
  </table>
</div>"""

    ema_label = f"EMA Screener ({ema_date})" if ema_date and ema_date != today else "EMA Screener — Today"

    turning_section = ""
    if weekly_turning:
        turning_section = f"""
<div class="section">
  <div class="stitle">ZLEMA25 Turning Up — early entries ({len(weekly_turning)})</div>
  <table>
    <thead><tr><th>Symbol</th><th>Day Chg</th><th>ZL Days</th><th>ZL Chg%</th><th>Circuit</th></tr></thead>
    <tbody>{table_or_empty(t_rows, 5, "No ZLEMA25 turns today")}</tbody>
  </table>
</div>"""

    zl25_section = ""
    if zl25_rising or zl25_watch:
        zl25_section = f"""
<div class="two">
  <div class="section">
    <div class="stitle">EMA25 ZL Rising — RS-filtered ({len(zl25_rising)} stocks, top 20)</div>
    <table>
      <thead><tr><th>Symbol</th><th>Close</th><th>Day Chg</th><th>ZL Days</th><th>ZL Chg%</th><th>Squeeze</th><th>Circuit</th></tr></thead>
      <tbody>{table_or_empty(zr_rows, 7, "No ZL rising stocks")}</tbody>
    </table>
  </div>
  <div class="section">
    <div class="stitle">EMA25 ZL Watch — RS-filtered ({len(zl25_watch)} stocks, top 15)</div>
    <table>
      <thead><tr><th>Symbol</th><th>Close</th><th>Day Chg</th><th>ZL Days</th><th>ZL Chg%</th><th>Squeeze</th><th>Circuit</th></tr></thead>
      <tbody>{table_or_empty(zw_rows, 7, "No ZL watch stocks")}</tbody>
    </table>
  </div>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NSE Dashboard — {today}</title>
<style>
:root{{
  --bg:#0d1117;--bg2:#161b22;--bg3:#21262d;
  --bd:#30363d;--tx:#e6edf3;--mu:#8b949e;
  --gld:#ffd700;--grn:#3fb950;--red:#f85149;--blu:#58a6ff;--pur:#a371f7;
  --ylw:#d29922;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--tx);font-family:'Segoe UI',system-ui,sans-serif;font-size:13px;padding:16px;line-height:1.4}}
h1{{font-size:1.25rem;color:var(--blu);margin-bottom:3px}}
.sub{{color:var(--mu);font-size:11px;margin-bottom:16px}}

.bar{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px}}
.stat{{background:var(--bg2);border:1px solid var(--bd);border-radius:6px;padding:7px 14px;text-align:center;min-width:70px}}
.sv{{font-size:1.5rem;font-weight:700;line-height:1.1}}
.sl{{color:var(--mu);font-size:10px;text-transform:uppercase;letter-spacing:.5px}}
.gld{{color:var(--gld)}}.grn{{color:var(--grn)}}.red{{color:var(--red)}}.blu{{color:var(--blu)}}.pur{{color:var(--pur)}}

.section{{margin-bottom:18px}}
.stitle{{font-size:.78rem;font-weight:600;color:var(--mu);text-transform:uppercase;letter-spacing:.7px;margin-bottom:6px;border-bottom:1px solid var(--bd);padding-bottom:3px}}

table{{width:100%;border-collapse:collapse;background:var(--bg2);border-radius:6px;overflow:hidden;font-size:12px}}
th{{background:var(--bg3);color:var(--mu);font-size:10px;text-transform:uppercase;letter-spacing:.5px;padding:5px 9px;text-align:left;border-bottom:1px solid var(--bd)}}
td{{padding:4px 9px;border-bottom:1px solid var(--bd);vertical-align:middle}}
tr:last-child td{{border-bottom:none}}
tr:hover td{{background:var(--bg3)}}

.r3{{background:rgba(255,215,0,.07)}}.r3:hover td{{background:rgba(255,215,0,.13)}}
.r2{{background:rgba(88,166,255,.05)}}

.s3{{color:var(--gld);font-size:13px}}.s2{{color:var(--blu)}}.s1{{color:var(--mu)}}

.sym{{font-weight:600;font-family:monospace;font-size:12px}}
.sym a{{color:inherit;text-decoration:none}}.sym a:hover{{text-decoration:underline;color:var(--blu)}}
.zld{{color:var(--mu);font-size:11px}}
.nm{{font-size:11px;color:var(--mu)}}
.num{{font-family:monospace;font-size:12px;color:var(--mu)}}
.pos{{color:var(--grn)}}.neg{{color:var(--red)}}.sqz-on{{color:var(--grn);font-weight:600;text-align:center}}.sqz-off{{color:var(--mu);text-align:center;font-size:11px}}

.b{{display:inline-block;font-size:9px;padding:1px 5px;border-radius:3px;font-weight:700;color:#fff;margin-right:2px}}
.b-swing{{background:#1f6feb}}.b-momentum{{background:#388bfd}}.b-weeklyrs{{background:#7c3aed}}

.ss{{color:var(--grn)}}.sp{{color:var(--blu)}}.sd{{color:var(--ylw)}}

.ccy{{color:var(--ylw)}}.ccr{{color:var(--red)}}.ccg{{color:var(--grn)}}.ccb{{color:var(--blu)}}

.two{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.empty{{color:var(--mu);font-style:italic;text-align:center;padding:8px}}

@media(max-width:800px){{.two{{grid-template-columns:1fr}}}}
</style>
</head>
<body>

<h1>NSE Daily Dashboard — {today}</h1>
<div class="sub">Generated {now_str}</div>

<div class="bar">
  <div class="stat"><div class="sv gld">{triple}</div><div class="sl">★★★ Triple</div></div>
  <div class="stat"><div class="sv blu">{double}</div><div class="sl">★★ Double</div></div>
  <div class="stat"><div class="sv grn">{len(swing)}</div><div class="sl">Swing</div></div>
  <div class="stat"><div class="sv grn">{len(momentum)}</div><div class="sl">Momentum</div></div>
  <div class="stat"><div class="sv grn">{len(weekly_entry)}</div><div class="sl">Weekly RS</div></div>
  <div class="stat"><div class="sv blu">{len(weekly_turning)}</div><div class="sl">ZL Turning</div></div>
  <div class="stat"><div class="sv grn">{len(zl25_rising)}</div><div class="sl">ZL25 Rising</div></div>
  <div class="stat"><div class="sv pur">{len(zl25_watch)}</div><div class="sl">ZL25 Watch</div></div>
  <div class="stat"><div class="sv grn">{len(ema_adds)}</div><div class="sl">EMA Adds</div></div>
  <div class="stat"><div class="sv red">{len(ema_dels)}</div><div class="sl">EMA Exits</div></div>
  <div class="stat"><div class="sv pur">{total_compressed}</div><div class="sl">Compressed</div></div>
  <div class="stat"><div class="sv gld">{total_zl_rising}</div><div class="sl">Squeeze+RS</div></div>
</div>

<div class="section">
  <div class="stitle">Unified Entry Signals — sorted by confluence ({len(all_syms)} stocks)</div>
  <table>
    <thead><tr><th width="60">Conf</th><th>Symbol</th><th>Scanners</th><th>Signal</th><th>Day Chg</th><th>ZL Days</th><th>ZL Chg%</th><th>Circuit</th></tr></thead>
    <tbody>{table_or_empty(u_rows, 8, "No signals today")}</tbody>
  </table>
</div>

{turning_section}

{zl25_section}

{compression_section}

<div class="two">
  <div class="section">
    <div class="stitle">{ema_label} — Additions ({len(ema_adds)})</div>
    <table>
      <thead><tr><th>Symbol</th><th>Day Chg</th></tr></thead>
      <tbody>{table_or_empty(ea_rows, 2, "No additions")}</tbody>
    </table>
  </div>
  <div class="section">
    <div class="stitle">{ema_label} — Exits ({len(ema_dels)})</div>
    <table>
      <thead><tr><th>Symbol</th><th>Day Chg</th></tr></thead>
      <tbody>{table_or_empty(ed_rows, 2, "No exits")}</tbody>
    </table>
  </div>
</div>

<div class="section">
  <div class="stitle">Recent Circuit Limit Changes — watchlist</div>
  <table>
    <thead><tr><th>Date</th><th>Symbol</th><th>Name</th><th>From</th><th>To</th></tr></thead>
    <tbody>{table_or_empty(cc_rows, 5, "No recent changes")}</tbody>
  </table>
</div>

</body>
</html>
"""


def main():
    now_ist = datetime.now(IST)
    today   = now_ist.strftime("%Y-%m-%d")
    now_str = now_ist.strftime("%Y-%m-%d %H:%M IST")

    print(f"[{now_str}] Building dashboard for {today}…")

    swing_content       = read_file(SWING_MD)
    momentum_content    = read_file(MOMENTUM_MD)
    weekly_content      = read_file(WEEKLY_RS_MD)
    zl25_content        = read_file(EMA25_ZL_MD)
    ema_content         = read_file(EMA_MD)
    circuit_content     = read_file(CIRCUIT_MD)
    compression_content = read_file(COMPRESSION_MD)

    swing_block    = extract_today_block(swing_content,    today)
    momentum_block = extract_today_block(momentum_content, today)
    weekly_block   = extract_today_block(weekly_content,   today)

    swing_signals    = parse_signal_table(swing_block)
    momentum_signals = parse_signal_table(momentum_block)
    weekly_entry, weekly_turning = parse_weekly_rs_block(weekly_block)

    zl25_rising, zl25_watch = parse_ema25_zl(zl25_content, today)
    ema_adds, ema_dels = parse_ema_changes(ema_content)
    ema_date = parse_ema_date(ema_content)
    circuit_changes = parse_circuit_changes(circuit_content)
    compression_rows, total_compressed, total_zl_rising = parse_ema_compression(compression_content, today)

    html = build_html(
        today=today, now_str=now_str,
        swing=swing_signals, momentum=momentum_signals,
        weekly_entry=weekly_entry, weekly_turning=weekly_turning,
        zl25_rising=zl25_rising, zl25_watch=zl25_watch,
        ema_adds=ema_adds, ema_dels=ema_dels, ema_date=ema_date,
        circuit_changes=circuit_changes,
        compression_rows=compression_rows,
        total_compressed=total_compressed,
        total_zl_rising=total_zl_rising,
    )

    with open(DASHBOARD_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Written: {DASHBOARD_HTML}")
    print(f"  Swing:{len(swing_signals)} Momentum:{len(momentum_signals)} WeeklyRS:{len(weekly_entry)} Turning:{len(weekly_turning)}")
    print(f"  ZL25 Rising:{len(zl25_rising)} Watch:{len(zl25_watch)}")
    print(f"  EMA Compression: {total_compressed} compressed, {total_zl_rising} ZL rising")
    print(f"  EMA adds:{len(ema_adds)} dels:{len(ema_dels)} Circuit changes:{len(circuit_changes)}")
    triple = sum(1 for s in {r['symbol'] for r in swing_signals} &
                              {r['symbol'] for r in momentum_signals} &
                              {r['symbol'] for r in weekly_entry})
    if triple:
        print(f"  Triple confluence (3 scanners): {triple} stocks")


if __name__ == "__main__":
    main()