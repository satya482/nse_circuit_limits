#!/usr/bin/env python3
"""
Generate 8-word business labels for all stocks in .company_cache/.

Uses Claude haiku to produce a crisp label per stock:
  "Pharma APIs & xanthine intermediates, India exporter"
  "Wind turbine manufacturer & renewable energy solutions"

Output:
  - Adds `short_label` to each .company_cache/{SYMBOL}.json (in-place)
  - Writes tools/stock_labels.json → {symbol: label} flat lookup

Usage:
    python tools/generate_stock_labels.py                         # all stale/missing
    python tools/generate_stock_labels.py --symbols KRN ICICIBANK  # specific stocks
    python tools/generate_stock_labels.py --force                 # regenerate all
"""

import argparse
import json
import sys
import time
from pathlib import Path

import os

import anthropic

sys.stdout.reconfigure(encoding="utf-8")

# Load .env from ema-compression-scanner/ (where project secrets live)
_ENV_FILE = Path(__file__).parent.parent / "ema-compression-scanner" / ".env"
if _ENV_FILE.exists() and not os.environ.get("ANTHROPIC_API_KEY"):
    for line in _ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("ANTHROPIC_API_KEY="):
            os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip()
            break

REPO_DIR    = Path(__file__).parent.parent
CACHE_DIR   = REPO_DIR / ".company_cache"
TOOLS_DIR   = Path(__file__).parent
LABELS_FILE = TOOLS_DIR / "stock_labels.json"

MODEL = "claude-haiku-4-5-20251001"

SYSTEM = (
    "You generate ultra-concise stock labels for Indian equity traders. "
    "Respond with ONLY the label — no quotes, no explanation, no punctuation at the end."
)

USER_TMPL = """\
Describe this company in 7-9 words capturing: core product/service, sector, and end-market.
Be specific. No filler words (India's leading, etc.). Use plain English.

Company: {name}
Description: {desc}"""


# ── Claude call ────────────────────────────────────────────────────────────────

_client: anthropic.Anthropic | None = None

def _get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic()
    return _client


def generate_label(name: str, description: str) -> str:
    desc_snippet = description[:500].strip()
    msg = _get_client().messages.create(
        model=MODEL,
        max_tokens=40,
        system=SYSTEM,
        messages=[{"role": "user", "content": USER_TMPL.format(name=name, desc=desc_snippet)}],
    )
    label = msg.content[0].text.strip().strip('"').strip("'")
    # Truncate to 12 words max as safety
    words = label.split()
    if len(words) > 12:
        label = " ".join(words[:10])
    return label


# ── Cache helpers ──────────────────────────────────────────────────────────────

def _load_cache(symbol: str) -> dict | None:
    p = CACHE_DIR / f"{symbol}.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def _save_cache(data: dict):
    sym = data["symbol"]
    p   = CACHE_DIR / f"{sym}.json"
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def _has_label(data: dict) -> bool:
    return bool(data.get("short_label", "").strip())


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbols", nargs="+", help="Specific symbols to process")
    parser.add_argument("--force",   action="store_true", help="Regenerate even if label exists")
    args = parser.parse_args()

    if args.symbols:
        symbols = args.symbols
    else:
        symbols = sorted(p.stem for p in CACHE_DIR.glob("*.json"))

    print(f"Processing {len(symbols)} stocks...")

    labels: dict[str, str] = {}
    if LABELS_FILE.exists():
        try:
            labels = json.loads(LABELS_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass

    generated = 0
    skipped   = 0
    errors    = 0

    for i, sym in enumerate(symbols, 1):
        data = _load_cache(sym)
        if data is None:
            errors += 1
            continue

        if not args.force and _has_label(data):
            labels[sym] = data["short_label"]
            skipped += 1
            continue

        desc = data.get("combined_description", "").strip()
        if not desc:
            desc = f"{data.get('name', sym)}"

        name = data.get("name", sym)

        try:
            label = generate_label(name, desc)
            data["short_label"] = label
            _save_cache(data)
            labels[sym] = label
            generated += 1
            print(f"[{i}/{len(symbols)}] {sym}: {label}")
        except Exception as e:
            print(f"[{i}/{len(symbols)}] {sym}: ERROR — {e}")
            errors += 1

        time.sleep(0.1)

    # Write flat lookup
    LABELS_FILE.write_text(
        json.dumps(dict(sorted(labels.items())), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\nDone. Generated={generated}  Skipped={skipped}  Errors={errors}")
    print(f"Written: {LABELS_FILE}  ({len(labels)} labels)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
