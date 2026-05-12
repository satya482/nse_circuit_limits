"""
Telegram Theme Parser

Reads today's message manifest (telegram_themes/.today_messages.json),
extracts text from PDF/image files via pdfplumber / Claude Vision API,
then calls Claude Haiku to extract structured equity theme data per report.
Writes output to telegram_themes/themes_YYYY-MM-DD.md.

Run (from Telegram manifest):  python telegram_parser.py
Run (from local folder)     :  python telegram_parser.py --folder C:/path/to/pdfs/

Needs: anthropic, pdfplumber, python-dotenv
Creds: fundamental_context/.env  (ANTHROPIC_API_KEY)
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

try:
    import anthropic
except ImportError:
    print("[PARSER] ERROR: anthropic not installed. Run: pip install anthropic")
    sys.exit(1)

try:
    import pdfplumber
    _PDF_OK = True
except ImportError:
    _PDF_OK = False
    print("[PARSER] WARNING: pdfplumber not installed — PDF parsing disabled. Run: pip install pdfplumber")

from telegram_symbol_resolver import Resolver as _Resolver
_resolver = _Resolver()

# ── Config ────────────────────────────────────────────────────────────────────
_HERE  = Path(__file__).parent
_ENV   = _HERE / "fundamental_context" / ".env"
load_dotenv(_ENV)

ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")
HAIKU_MODEL   = "claude-haiku-4-5-20251001"

_MANIFEST  = _HERE / "telegram_themes" / ".today_messages.json"
_CACHE     = _HERE / "telegram_themes" / ".telegram_parsed_cache.json"
_OUT_DIR   = _HERE / "telegram_themes"

_IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
_PDF_EXTS   = {".pdf"}

# ── Claude prompts ────────────────────────────────────────────────────────────
_SYSTEM = (
    "You are Vikram Iyer, a 30-year veteran Indian equity research analyst. "
    "Extract structured information from an equity research report or message. "
    "Return ONLY valid JSON — no prose, no markdown code blocks, no explanation."
)

_SCHEMA = """{
  "date": "<YYYY-MM-DD or null>",
  "source": "Equity_Insights",
  "themes": ["<theme name>"],
  "companies": [
    {"symbol": "<NSE symbol or best guess>", "name": "<company name>", "sentiment": "<bullish|bearish|neutral>"}
  ],
  "key_points": ["<concise insight>"],
  "catalysts": ["<catalyst name>"],
  "time_horizon": "<short-term|6-12M|2Y+|not mentioned>",
  "conviction": "<High|Medium|Low|not mentioned>",
  "summary": "<2-3 sentence summary>"
}"""


# ── Cache helpers ─────────────────────────────────────────────────────────────
def _load_cache() -> set[str]:
    if _CACHE.exists():
        with open(_CACHE, encoding="utf-8-sig") as fh:  # utf-8-sig strips BOM if present
            return set(json.load(fh).get("processed", []))
    return set()


def _save_cache(processed: set[str]) -> None:
    with open(_CACHE, "w", encoding="utf-8") as fh:
        json.dump({"processed": sorted(processed)}, fh, indent=2)


def _file_key(path: str) -> str:
    """Content-based cache key: same bytes → same key regardless of path or filename."""
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return "f:" + h.hexdigest()

def _msg_key(msg_id: str) -> str:
    return "m:" + hashlib.md5(str(msg_id).encode()).hexdigest()[:12]


# ── Content extractors ────────────────────────────────────────────────────────
def _pdf_text(path: str) -> str:
    if not _PDF_OK:
        return ""
    try:
        pages: list[str] = []
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                pages.append(page.extract_text() or "")
        return "\n\n".join(pages).strip()
    except Exception as exc:
        print(f"[PARSER] PDF error {Path(path).name}: {exc}")
        return ""


def _image_text(path: str, client: anthropic.Anthropic) -> str:
    mime_map = {
        ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".png": "image/png", ".gif": "image/gif", ".webp": "image/webp",
    }
    mime = mime_map.get(Path(path).suffix.lower(), "image/jpeg")
    try:
        with open(path, "rb") as fh:
            data = base64.standard_b64encode(fh.read()).decode()
        resp = client.messages.create(
            model=HAIKU_MODEL,
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": mime, "data": data}},
                    {"type": "text", "text": "Extract all text from this image verbatim. Output only the extracted text, nothing else."},
                ],
            }],
        )
        return resp.content[0].text.strip()
    except Exception as exc:
        print(f"[PARSER] Image OCR error {Path(path).name}: {exc}")
        return ""


# ── Claude theme extraction ───────────────────────────────────────────────────
def _extract_themes(content: str, client: anthropic.Anthropic, today: str) -> dict | None:
    if not content.strip():
        return None
    user_msg = (
        f"Today's date: {today}\n\n"
        f"Extract all fields from this equity report.\n"
        f"Return JSON matching this schema exactly:\n{_SCHEMA}\n\n"
        f"REPORT:\n{content[:20000]}"
    )
    try:
        resp = client.messages.create(
            model=HAIKU_MODEL,
            max_tokens=2048,
            system=_SYSTEM,
            messages=[{"role": "user", "content": user_msg}],
        )
        raw = resp.content[0].text.strip()
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        data = json.loads(raw)
        # Resolve each company's symbol to a canonical NSE code
        if isinstance(data.get("companies"), list):
            data["companies"] = [_resolver.resolve_company(c) for c in data["companies"]]
        return data
    except json.JSONDecodeError as exc:
        print(f"[PARSER] JSON parse error: {exc}")
        return None
    except Exception as exc:
        print(f"[PARSER] Claude API error: {exc}")
        return None


# ── Markdown renderer ─────────────────────────────────────────────────────────
def _render_report(idx: int, msg: dict, ex: dict, source: str) -> str:
    themes    = ", ".join(ex.get("themes") or []) or "—"
    catalysts = ", ".join(ex.get("catalysts") or []) or "—"
    horizon   = ex.get("time_horizon") or "—"
    conviction = ex.get("conviction") or "—"
    summary   = ex.get("summary") or "—"
    companies = ex.get("companies") or []
    key_pts   = ex.get("key_points") or []

    lines = [
        f"## Report {idx} — {themes}",
        f"**Source**: `{Path(source).name}`  |  **Date**: {msg.get('date', '—')}",
        f"**Themes**: {themes}",
        f"**Time horizon**: {horizon}  |  **Conviction**: {conviction}",
        "",
        f"> {summary}",
        "",
    ]
    if companies:
        lines += [
            "### Companies mentioned",
            "| Symbol | Name | Sentiment |",
            "|--------|------|-----------|",
        ]
        for c in companies:
            lines.append(f"| {c.get('symbol','—')} | {c.get('name','—')} | {c.get('sentiment','—')} |")
        lines.append("")
    if key_pts:
        lines.append("### Key points")
        for pt in key_pts:
            lines.append(f"- {pt}")
        lines.append("")
    if ex.get("catalysts"):
        lines.append(f"**Catalysts**: {catalysts}")
        lines.append("")
    lines += ["---", ""]
    return "\n".join(lines)


def _header(today: str, n: int) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M IST")
    return f"# Telegram Equity Insights — {today}\n_Fetched {now} | {n} report(s) parsed_\n\n---\n\n"


# ── Core processing ───────────────────────────────────────────────────────────
def _process_messages(
    messages: list[dict],
    client: anthropic.Anthropic,
    cache: set[str],
    today: str,
    out_path: Path,
    append: bool = False,
) -> tuple[int, list[dict]]:
    """Process a list of message dicts, write/append markdown. Returns (count, data_records)."""
    reports: list[tuple[dict, dict, str]] = []

    for msg in messages:
        text  = msg.get("text") or ""
        files = msg.get("files") or []

        if files:
            for fpath in files:
                try:
                    cache_key = _file_key(fpath)
                except OSError:
                    print(f"[PARSER] Skip (unreadable): {Path(fpath).name}")
                    continue
                if cache_key in cache:
                    print(f"[PARSER] Skip (already parsed): {Path(fpath).name}")
                    continue

                ext = Path(fpath).suffix.lower()
                if ext in _PDF_EXTS:
                    content = _pdf_text(fpath)
                elif ext in _IMAGE_EXTS:
                    content = _image_text(fpath, client)
                else:
                    print(f"[PARSER] Skip unsupported: {Path(fpath).name}")
                    continue

                if text:
                    content = f"{text}\n\n{content}"

                if not content.strip():
                    print(f"[PARSER] Empty content: {Path(fpath).name}")
                    cache.add(cache_key)
                    continue

                print(f"[PARSER] Extracting themes: {Path(fpath).name}")
                ex = _extract_themes(content, client, today)
                if ex:
                    reports.append((msg, ex, fpath))
                    cache.add(cache_key)
                else:
                    print(f"[PARSER] Extraction failed: {Path(fpath).name}")

        elif text.strip():
            cache_key = _msg_key(msg['msg_id'])
            if cache_key in cache:
                continue
            print(f"[PARSER] Extracting themes from text msg id={msg['msg_id']}")
            ex = _extract_themes(text, client, today)
            if ex:
                reports.append((msg, ex, f"msg_{msg['msg_id']}"))
                cache.add(cache_key)

    if not reports:
        return 0, []

    # Determine start index if appending to an existing file
    start_idx = 1
    if append and out_path.exists():
        existing = out_path.read_text(encoding="utf-8")
        start_idx = len(re.findall(r"^## Report \d+", existing, re.MULTILINE)) + 1
        md = existing.rstrip() + "\n\n"
    else:
        md = _header(today, len(reports))

    data_records: list[dict] = []
    for idx, (msg, ex, src) in enumerate(reports, start=start_idx):
        md += _render_report(idx, msg, ex, src)
        data_records.append({**ex, "source": Path(src).name, "date": msg.get("date", today)})

    out_path.write_text(md, encoding="utf-8")
    return len(reports), data_records


def _folder_to_messages(folder: Path) -> list[dict]:
    """Build a synthetic message list from all PDFs/images in a folder."""
    supported = _PDF_EXTS | _IMAGE_EXTS
    files = sorted(p for p in folder.iterdir() if p.suffix.lower() in supported and p.is_file())
    if not files:
        print(f"[PARSER] No supported files found in {folder}")
        return []
    today = datetime.now().strftime("%Y-%m-%d")
    messages = []
    for i, f in enumerate(files):
        messages.append({
            "msg_id":  f"folder_{i}",
            "date":    today,
            "text":    "",
            "files":   [str(f)],
        })
    print(f"[PARSER] Folder mode: {len(files)} file(s) found in {folder}")
    return messages


# ── JSON output ───────────────────────────────────────────────────────────────
def _merge_json(json_path: Path, new_records: list[dict], today: str) -> None:
    """Merge new records into today's JSON file, deduplicating by source filename."""
    existing: list[dict] = []
    if json_path.exists():
        with open(json_path, encoding="utf-8") as fh:
            existing = json.load(fh).get("reports", [])
    seen_sources = {r.get("source") for r in existing}
    merged = existing + [r for r in new_records if r.get("source") not in seen_sources]
    out = {"date": today, "generated": datetime.now().strftime("%Y-%m-%d %H:%M IST"), "reports": merged}
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
    print(f"[PARSER] JSON saved: {json_path} ({len(merged)} total reports)")


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(description="Telegram equity theme parser")
    parser.add_argument(
        "--folder", "-f", metavar="PATH",
        help="Parse all PDFs/images in this local folder instead of the Telegram manifest",
    )
    args = parser.parse_args()

    if not ANTHROPIC_KEY:
        print("[PARSER] ERROR: ANTHROPIC_API_KEY not set in fundamental_context/.env")
        sys.exit(1)

    today    = datetime.now().strftime("%Y-%m-%d")
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = _OUT_DIR / f"themes_{today}.md"
    client   = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    cache    = _load_cache()

    json_path = _OUT_DIR / f"themes_{today}.json"

    if args.folder:
        # ── Manual folder mode ────────────────────────────────────────────────
        folder = Path(args.folder)
        if not folder.is_dir():
            print(f"[PARSER] ERROR: not a directory: {folder}")
            sys.exit(1)
        messages = _folder_to_messages(folder)
        if not messages:
            sys.exit(0)
        append = out_path.exists()
        n, records = _process_messages(messages, client, cache, today, out_path, append=append)
        _save_cache(cache)
        if n:
            _merge_json(json_path, records, today)
            print(f"[PARSER] Written: {out_path} ({n} reports from folder)")
        else:
            print("[PARSER] No new reports from folder")
    else:
        # ── Telegram manifest mode ────────────────────────────────────────────
        if not _MANIFEST.exists():
            print(f"[PARSER] Manifest not found at {_MANIFEST} — run telegram_ingest.py first")
            sys.exit(0)
        with open(_MANIFEST, encoding="utf-8") as fh:
            messages = json.load(fh)
        if not messages:
            print("[PARSER] Empty manifest — nothing to parse")
            sys.exit(0)
        n, records = _process_messages(messages, client, cache, today, out_path)
        _save_cache(cache)
        if n:
            _merge_json(json_path, records, today)
            print(f"[PARSER] Written: {out_path} ({n} reports)")
        else:
            print("[PARSER] No new reports — nothing written")


if __name__ == "__main__":
    main()
