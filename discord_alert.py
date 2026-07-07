#!/usr/bin/env python3
"""One-line Discord status alert, reusing DISCORD_WEBHOOK_URL from scan_status_mailer.py.

CLI: python discord_alert.py "title" "message" [color_hex]
"""

import os
import sys
from datetime import datetime, timezone

import requests


def send_discord_alert(title: str, message: str, color: int = 0x2EA44F) -> bool:
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "")
    if not webhook_url:
        return False

    embed = {
        "title": title,
        "description": message,
        "color": color,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    resp = requests.post(webhook_url, json={"embeds": [embed]}, timeout=10)
    return resp.status_code in (200, 204)


if __name__ == "__main__":
    alert_title = sys.argv[1] if len(sys.argv) > 1 else "NSE Scanner"
    alert_message = sys.argv[2] if len(sys.argv) > 2 else ""
    alert_color = int(sys.argv[3], 16) if len(sys.argv) > 3 else 0x2EA44F
    if send_discord_alert(alert_title, alert_message, alert_color):
        print("Discord alert sent.")
    else:
        print("Discord skipped — set DISCORD_WEBHOOK_URL to enable.")
