"""Build the standalone ZL breadth table from the sector-rotation report."""

import re
from html import escape
from pathlib import Path
from datetime import datetime

from dashboard_generator import parse_sector_rotation
from disclaimer import SEBI_HTML_BANNER, SEBI_HTML_FOOTER
from cluster_membership import read_json, COVERAGE_FILE, IST

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "sector_rotation_scans" / "sector_rotation_latest.md"
OUTPUT = ROOT / "cluster.html"


def build_html(content: str, coverage: dict | None = None) -> str:
    date = re.search(r"^# Sector Rotation .+?(\d{4}-\d{2}-\d{2})", content, re.M)
    if not date or "## ZL Breadth per Group" not in content:
        raise ValueError("Sector rotation report has no dated ZL breadth section")
    groups = parse_sector_rotation(content)[3]
    columns = ("label", "zl_rising", "breadth", "avg_days", "avg_pct", "cluster", "members")
    rows = "\n".join(
        '<tr data-group>' + ''.join(f'<td>{escape(group[key])}</td>' for key in columns) + '</tr>'
        for group in groups
    )
    if not groups:
        rows = '<tr><td colspan="7">No groups with ≥40% ZL rising.</td></tr>'
    title = f"ZL Breadth per Group ({len(groups)} groups ≥40% rising)"
    coverage_html = ''
    if coverage is not None:
        pending = coverage['pending']
        pending_rows = ''.join('<tr>' + ''.join(f'<td>{escape(str(row[key]))}</td>'
                               for key in ('symbol', 'name', 'reason')) + '</tr>' for row in pending)
        changes = coverage.get('changes', {})
        added = ', '.join(changes.get('added', [])) or 'None'
        removed = ', '.join(changes.get('removed', [])) or 'None'
        moved = '; '.join(f"{r['symbol']}: {r['from']} → {r['to']}" for r in changes.get('moved', [])) or 'None'
        discovered = coverage.get('discovered_at', '')
        try:
            discovered = datetime.fromisoformat(discovered).astimezone(IST).strftime('%Y-%m-%d %H:%M IST')
        except ValueError:
            pass
        retry = ', '.join(coverage.get('description_failures', [])) or 'None'
        coverage_html = f'''<section aria-label="Universe coverage">
<h2>Universe coverage</h2>
<p>NSE common equities including IPOs · Price &gt;₹25 · Market cap ₹1,000 crore–₹5 lakh crore</p>
<p>{coverage['eligible']} eligible · {coverage['ready']} ready · {len(pending)} pending</p>
<p class="meta">Price data: {escape(coverage.get('price_date', ''))}</p>
<p class="meta">Discovered: {escape(discovered)} · Groups updated: {escape(coverage.get('groups_updated', ''))} · Descriptions refreshed: {escape(coverage.get('descriptions_updated') or 'Pending')}</p>
<details><summary>Description fetches awaiting retry ({len(coverage.get('description_failures', []))})</summary><p>{escape(retry)}</p></details>
<details><summary>Pending stocks ({len(pending)})</summary>
<div class="table-wrap"><table aria-label="Pending stocks"><thead><tr><th>Symbol</th><th>Company</th><th>Reason</th></tr></thead><tbody>{pending_rows or '<tr><td colspan="3">None</td></tr>'}</tbody></table></div></details>
<details><summary>Last weekly membership changes</summary>
<p>Added: {escape(added)}</p><p>Removed: {escape(removed)}</p><p>Moved: {escape(moved)}</p></details></section>'''
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Cluster</title>
<style>
:root{{color-scheme:dark}}*{{box-sizing:border-box}}body{{margin:0;background:#0d1117;color:#e6edf3;font:14px/1.6 system-ui,sans-serif}}
main{{max-width:1600px;margin:auto;padding:24px}}a{{color:#79c0ff}}h1{{font-size:clamp(20px,3vw,30px);line-height:1.3}}
.meta{{color:#9ba8b8}}.table-wrap{{overflow-x:auto;border:1px solid #30363d;border-radius:8px;margin-top:24px}}
table{{width:100%;border-collapse:collapse;min-width:950px}}th,td{{padding:14px 16px;text-align:left;vertical-align:top;border-bottom:1px solid #30363d}}
th{{background:#161b22;white-space:nowrap}}tbody tr:hover{{background:#161b22}}td:nth-child(3){{color:#56d49b;font-weight:700}}
td:nth-child(6){{color:#e3b341}}td:first-child{{min-width:180px;font-weight:600}}td:nth-child(6),td:nth-child(7){{min-width:240px}}
</style></head><body><main>
{SEBI_HTML_BANNER}
<a href="dashboard.html">← NSE Dashboard</a>
<h1>{title}</h1>
<p class="meta">Source report: {date.group(1)} · All qualifying groups shown</p>
<p>⚡ = coordinated cluster (≥2 members turned ZL within ±2 bars).</p>
<div class="table-wrap"><table aria-label="ZL Breadth per Group">
<thead><tr><th scope="col">Group</th><th scope="col">ZL Rising</th><th scope="col">Breadth</th><th scope="col">Avg ZL Days</th><th scope="col">Avg ZL Chg%</th><th scope="col">⚡ Cluster</th><th scope="col">Members</th></tr></thead>
<tbody>{rows}</tbody></table></div>
{coverage_html}
{SEBI_HTML_FOOTER}
</main></body></html>
'''


def generate(source: Path = SOURCE, output: Path = OUTPUT) -> None:
    page = build_html(source.read_text(encoding="utf-8"), read_json(COVERAGE_FILE))
    temporary = output.with_suffix('.html.tmp')
    temporary.write_text(page, encoding="utf-8")
    temporary.replace(output)
    print(f"Written: {output}")


if __name__ == "__main__":
    generate()
