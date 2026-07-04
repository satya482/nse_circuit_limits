#!/usr/bin/env python3
"""Same-day backfill: patch today's already-written scanner .md Symbol cells
with the delivery% spike marker (fetch_delivery.py runs after those scanners
already produced today's output), then re-run the HTML dashboard generators
so HTML reflects it same-day too. Idempotent -- safe to re-run."""

import re
import sqlite3
import subprocess
import sys
from datetime import date
from pathlib import Path

from ohlc_db import DB_PATH, deliv_tag

BASE = Path(__file__).parent

_SYM_RE = re.compile(r"^\|\s*\[([A-Z0-9&\-]+)\]\(")
_SUB_RE = re.compile(r"<br><sub>(.*?)</sub>")
_DEL_TOKEN_RE = re.compile(r"DEL\d+%\(T-1\)")

SCANNER_MD_FILES = [
    ("wt_scans", "wt_bullcross_{date}.md", "wt_bullcross_latest.md"),
    ("ema25_zl_scans", "ema25_zl_scans_{date}.md", "ema25_zl_scans.md"),
    ("weekly_zl_scans", "weekly_zl_scans_{date}.md", "weekly_zl_scans.md"),
    ("trend_scans", "trend_scan_{date}.md", "trend_scan_latest.md"),
    ("rs_highline_scans", "rs_highline_{date}.md", "rs_highline_latest.md"),
]

HTML_GENERATORS = ["wt_squeeze_dashboard.py", "dashboard_generator.py", "trend_dashboard.py"]


def _strip_del_token(sub_content: str) -> str:
    parts = [p for p in sub_content.split(" · ") if p and not _DEL_TOKEN_RE.fullmatch(p)]
    return " · ".join(parts)


def patch_symbol_line(line: str, tagger) -> str:
    """Idempotently add/replace/remove the DEL{pct}%(T-1) token in a scanner
    markdown row's Symbol cell. Returns the line unchanged if it's not a data
    row (no leading '| [SYMBOL](')."""
    m = _SYM_RE.match(line)
    if not m:
        return line
    symbol = m.group(1)
    tag = tagger(symbol)

    sub_match = _SUB_RE.search(line)
    if sub_match:
        existing = _strip_del_token(sub_match.group(1))
        tokens = [t for t in existing.split(" · ") if t]
        if tag:
            tokens.append(tag)
        new_sub_content = " · ".join(tokens)
        if new_sub_content:
            return line[: sub_match.start()] + f"<br><sub>{new_sub_content}</sub>" + line[sub_match.end() :]
        return line[: sub_match.start()] + line[sub_match.end() :]

    if not tag:
        return line
    insert_at = line.index(")", m.end()) + 1
    rest = line[insert_at:]
    extra_bracket = re.match(r"^\s?\[[^\]]*\]", rest)
    if extra_bracket:
        insert_at += extra_bracket.end()
    return line[:insert_at] + f"<br><sub>{tag}</sub>" + line[insert_at:]


def patch_md_file(path: Path, tagger) -> int:
    """Patch every data row's Symbol cell in-place. Returns count of changed rows."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    changed = 0
    new_lines = []
    for line in lines:
        patched = patch_symbol_line(line, tagger)
        if patched != line:
            changed += 1
        new_lines.append(patched)
    path.write_text("".join(new_lines), encoding="utf-8")
    return changed


def _has_todays_delivery_data(today: str) -> bool:
    try:
        con = sqlite3.connect(DB_PATH)
        try:
            row = con.execute("SELECT 1 FROM delivery WHERE date=? LIMIT 1", (today,)).fetchone()
        finally:
            con.close()
        return row is not None
    except Exception as e:
        # Missing table / corrupt DB should be visibly distinct from the normal
        # "no delivery data yet" case -- otherwise a real upstream bug (e.g. the
        # fetch script failing to create the table) silently looks identical to
        # "just no data today" in the logs, indefinitely.
        print(f"backfill_delivery_markers: WARNING - error checking delivery data: {e}", file=sys.stderr)
        return False


def main() -> None:
    today = date.today().isoformat()
    if not _has_todays_delivery_data(today):
        print("backfill_delivery_markers: no delivery data for today, skipping")
        return

    total = 0
    for dirname, dated_tmpl, latest_name in SCANNER_MD_FILES:
        for name in (dated_tmpl.format(date=today), latest_name):
            path = BASE / dirname / name
            if path.exists():
                total += patch_md_file(path, deliv_tag)
    print(f"backfill_delivery_markers: patched {total} rows")

    for script in HTML_GENERATORS:
        subprocess.run([sys.executable, str(BASE / script)], check=True)


if __name__ == "__main__":
    main()
