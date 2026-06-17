"""
Telegram Equity Insights Ingester

Connects to a Telegram channel, fetches new messages since last run,
downloads PDF/image attachments to telegram_themes/raw/, and writes
a manifest of today's messages to telegram_themes/.today_messages.json.

Run  : python telegram_ingest.py
Needs: telethon, python-dotenv
Creds: fundamental_context/.env  (TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_CHANNEL)

First run triggers interactive Telethon login (phone + OTP) — subsequent
runs reuse the .telegram_session file silently.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from datetime import timezone
from pathlib import Path

from dotenv import load_dotenv

try:
    from telethon import TelegramClient
    from telethon.tl.types import MessageMediaDocument, MessageMediaPhoto
except ImportError:
    print("[TELEGRAM] ERROR: telethon not installed. Run: pip install telethon")
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV = _HERE / "fundamental_context" / ".env"
load_dotenv(_ENV)

API_ID = int(os.getenv("TELEGRAM_API_ID", "0"))
API_HASH = os.getenv("TELEGRAM_API_HASH", "")
CHANNEL = os.getenv("TELEGRAM_CHANNEL", "Equity_Insights")

_SESSION_FILE = _HERE / ".telegram_session"
_STATE_FILE = _HERE / ".telegram_state.json"
_RAW_DIR = _HERE / "telegram_themes" / "raw"
_MANIFEST_FILE = _HERE / "telegram_themes" / ".today_messages.json"

_DOWNLOAD_EXTS = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".webp"}


def _load_state() -> dict:
    if _STATE_FILE.exists():
        with open(_STATE_FILE, encoding="utf-8") as fh:
            return json.load(fh)
    return {"last_message_id": 0}


def _save_state(state: dict) -> None:
    with open(_STATE_FILE, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2)


def _today_prefix() -> str:
    from datetime import datetime

    return datetime.now().strftime("%Y%m%d")


async def ingest() -> list[dict]:
    """Fetch new messages from Telegram channel and download attachments."""
    if not API_ID or not API_HASH:
        print(
            "[TELEGRAM] ERROR: TELEGRAM_API_ID and TELEGRAM_API_HASH not set.\n"
            "           Add them to fundamental_context/.env and retry."
        )
        sys.exit(1)

    _RAW_DIR.mkdir(parents=True, exist_ok=True)
    _MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)

    state = _load_state()
    last_id = state.get("last_message_id", 0)
    prefix = _today_prefix()

    print(f"[TELEGRAM] Channel: {CHANNEL}  |  fetching after msg_id={last_id}")

    messages_out: list[dict] = []
    max_id_seen = last_id

    async with TelegramClient(str(_SESSION_FILE), API_ID, API_HASH) as client:
        channel = await client.get_entity(CHANNEL)

        # iter_messages returns newest-first; min_id excludes that id and below
        async for msg in client.iter_messages(channel, min_id=last_id, limit=200):
            if msg.id <= last_id:
                continue
            max_id_seen = max(max_id_seen, msg.id)

            msg_date = msg.date.astimezone(timezone.utc).strftime("%Y-%m-%d")
            msg_text = msg.text or msg.message or ""
            files_downloaded: list[str] = []

            if msg.media:
                if isinstance(msg.media, MessageMediaDocument):
                    doc = msg.media.document
                    fname = None
                    for attr in doc.attributes:
                        if hasattr(attr, "file_name") and attr.file_name:
                            fname = attr.file_name
                            break
                    if not fname:
                        mime = getattr(doc, "mime_type", "")
                        ext = ".pdf" if "pdf" in mime else ".bin"
                        fname = f"{prefix}_{msg.id}{ext}"
                    ext = Path(fname).suffix.lower()
                    if ext in _DOWNLOAD_EXTS:
                        dest = _RAW_DIR / f"{prefix}_{msg.id}{ext}"
                        if not dest.exists():
                            await client.download_media(msg, file=str(dest))
                            print(f"[TELEGRAM] Downloaded: {dest.name}")
                        files_downloaded.append(str(dest))

                elif isinstance(msg.media, MessageMediaPhoto):
                    dest = _RAW_DIR / f"{prefix}_{msg.id}.jpg"
                    if not dest.exists():
                        await client.download_media(msg, file=str(dest))
                        print(f"[TELEGRAM] Downloaded photo: {dest.name}")
                    files_downloaded.append(str(dest))

            messages_out.append(
                {
                    "msg_id": msg.id,
                    "date": msg_date,
                    "text": msg_text,
                    "files": files_downloaded,
                }
            )

    print(f"[TELEGRAM] {len(messages_out)} new messages fetched")

    with open(_MANIFEST_FILE, "w", encoding="utf-8") as fh:
        json.dump(messages_out, fh, indent=2, ensure_ascii=False)

    if max_id_seen > last_id:
        _save_state({"last_message_id": max_id_seen})
        print(f"[TELEGRAM] State updated: last_message_id={max_id_seen}")

    return messages_out


def main() -> None:
    messages = asyncio.run(ingest())
    print(f"[TELEGRAM] Manifest written: {_MANIFEST_FILE} ({len(messages)} messages)")


if __name__ == "__main__":
    main()
