#!/usr/bin/env python3
"""
discord_sync.py  —  Poll a Discord channel for HTML attachments, sync to reports/

Config:   DISCORD_BOT_TOKEN + DISCORD_CHANNEL_ID  in .env (repo root, gitignored)
State:    logs/discord_sync_state.json   — last seen message ID (local, not git)
Manifest: logs/sync_manifest.json       — filenames already synced (shared with
                                          sync_investor_stories.ps1)
"""

import json
import os
import subprocess
import sys
import requests
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).parent.parent
REPORTS_DIR = REPO / "reports"
LOGS_DIR = REPO / "logs"
MANIFEST = LOGS_DIR / "sync_manifest.json"
STATE = LOGS_DIR / "discord_sync_state.json"
API_BASE = "https://discord.com/api/v10"


# ── helpers ───────────────────────────────────────────────────────────────────


def load_env():
    env = {}
    env_file = REPO / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    for key in ("DISCORD_BOT_TOKEN", "DISCORD_CHANNEL_ID"):
        if os.environ.get(key):
            env[key] = os.environ[key]
    return env


def load_json(path, default):
    if path.exists():
        return json.loads(
            path.read_text(encoding="utf-8-sig")
        )  # handles PowerShell BOM
    return default


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


# ── Discord API ───────────────────────────────────────────────────────────────


def fetch_messages(token, channel_id, after=None):
    """Return all messages newer than `after`, oldest-first, with pagination."""
    headers = {"Authorization": f"Bot {token}"}
    all_msgs, cursor = [], after

    while True:
        params = {"limit": 100}
        if cursor:
            params["after"] = cursor
        r = requests.get(
            f"{API_BASE}/channels/{channel_id}/messages",
            headers=headers,
            params=params,
            timeout=15,
        )
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        batch = sorted(batch, key=lambda m: int(m["id"]))  # oldest-first
        all_msgs.extend(batch)
        if len(batch) < 100:
            break
        cursor = batch[-1]["id"]

    return all_msgs


def download_file(url, token, dest):
    r = requests.get(url, headers={"Authorization": f"Bot {token}"}, timeout=30)
    r.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(r.content)


# ── helpers ───────────────────────────────────────────────────────────────────


def derive_symbol(filename):
    stem = Path(filename).stem
    return stem.split("_")[0].upper()


def rebuild_index():
    result = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "generate_index.py")],
        capture_output=True,
        text=True,
    )
    out = (result.stdout + result.stderr).strip()
    if out:
        print(out)


def git_push(copied):
    subprocess.run(["git", "add", "reports/"], cwd=REPO, capture_output=True)
    staged = subprocess.run(
        ["git", "diff", "--staged", "--name-only"],
        cwd=REPO,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if not staged:
        print("Nothing staged for git.")
        return
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    msg = f"discord sync: {now} IST ({copied} new)"
    subprocess.run(["git", "commit", "-m", msg], cwd=REPO, capture_output=True)
    push = subprocess.run(["git", "push"], cwd=REPO, capture_output=True, text=True)
    if push.returncode == 0:
        print(f"Pushed: {msg}")
    else:
        print(f"Push failed: {push.stderr.strip()}")


# ── main ──────────────────────────────────────────────────────────────────────


def main():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    env = load_env()
    token = env.get("DISCORD_BOT_TOKEN", "").strip()
    channel_id = env.get("DISCORD_CHANNEL_ID", "").strip()

    if not token or not channel_id:
        print("ERROR: DISCORD_BOT_TOKEN and DISCORD_CHANNEL_ID required in .env")
        return 1

    # manifest: {filename -> entry}  (shared with sync_investor_stories.ps1)
    manifest = {e["file"]: e for e in load_json(MANIFEST, [])}
    state = load_json(STATE, {})
    last_id = state.get("last_message_id")

    print(f"Polling channel {channel_id}  (after={last_id or 'start'})...")

    try:
        messages = fetch_messages(token, channel_id, after=last_id)
    except requests.HTTPError as e:
        print(f"Discord API error: {e.response.status_code}  {e.response.text[:200]}")
        return 1

    if not messages:
        print("No new messages.")
        return 0

    copied, new_last = 0, last_id

    for msg in messages:
        new_last = msg["id"]
        for att in msg.get("attachments", []):
            fname = att["filename"]
            if not fname.lower().endswith(".html"):
                continue
            if fname in manifest:
                print(f"Skip    {fname}  (already synced)")
                continue
            symbol = derive_symbol(fname)
            dest = REPORTS_DIR / symbol / fname
            print(f"Downloading  {fname}  ->  reports/{symbol}/")
            download_file(att["url"], token, dest)
            manifest[fname] = {
                "file": fname,
                "symbol": symbol,
                "synced_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "dest": f"reports/{symbol}/{fname}",
                "source": "discord",
                "message_id": msg["id"],
            }
            copied += 1

    print(f"Files downloaded: {copied}")

    # Always advance cursor so we don't re-scan old messages next run
    if new_last and new_last != last_id:
        save_json(STATE, {"last_message_id": new_last})

    if copied == 0:
        print("No new HTML files - skipping index rebuild and git push.")
        return 0

    save_json(MANIFEST, list(manifest.values()))
    rebuild_index()
    git_push(copied)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
