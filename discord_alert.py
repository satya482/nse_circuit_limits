#!/usr/bin/env python3
"""One-line Discord status alert, reusing DISCORD_WEBHOOK_URL from scan_status_mailer.py.

CLI: python discord_alert.py "title" "message" [color_hex]
"""

import argparse
import os
from datetime import datetime, timezone
from collections.abc import Sequence

import requests


def send_discord_alert(
    title: str,
    message: str,
    color: int = 0x2EA44F,
    fields: Sequence[tuple[str, str]] | None = None,
) -> bool:
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "")
    if not webhook_url:
        return False

    embed = {
        "title": title,
        "description": message,
        "color": color,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    if fields:
        embed["fields"] = [{"name": k, "value": v, "inline": True} for k, v in fields]

    resp = requests.post(webhook_url, json={"embeds": [embed]}, timeout=10)
    return resp.status_code in (200, 204)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Post a one-line Discord status alert.")
    parser.add_argument("title")
    parser.add_argument("message")
    parser.add_argument("--color", help="Hex color, e.g. 2EA44F")
    parser.add_argument(
        "--field", action="append", default=[], metavar="NAME=VALUE",
        help="Embed field, repeatable",
    )
    args = parser.parse_args()

    fields = [tuple(f.split("=", 1)) for f in args.field]
    color = int(args.color, 16) if args.color else 0x2EA44F
    if send_discord_alert(args.title, args.message, color, fields):
        print("Discord alert sent.")
    else:
        print("Discord skipped — set DISCORD_WEBHOOK_URL to enable.")
