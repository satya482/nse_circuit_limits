#!/usr/bin/env python3
"""
NSE Scanner Status Mailer
Checks if all scanners ran today, reads signal counts, sends email summary.

Setup: set GMAIL_APP_PASSWORD as a Windows env variable (run once as admin):
  setx GMAIL_APP_PASSWORD "your-16-char-app-password" /M
Get an app password at: myaccount.google.com/apppasswords
"""

import subprocess, smtplib, os, re, sys, requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding="utf-8")

IST       = timezone(timedelta(hours=5, minutes=30))
BASE      = os.path.dirname(os.path.abspath(__file__))
TO_EMAIL  = "satya482@gmail.com"
FROM_EMAIL= os.environ.get("GMAIL_USER", "satya482@gmail.com")

REPO      = "https://github.com/satya482/nse_circuit_limits"
BLOB      = f"{REPO}/blob/main"

SCANNER_KEYWORDS = {
    "Swing Scanner":         "swing scan",
    "Momentum Scanner":      "momentum scan",
    "Weekly RS Scanner":     "momentum rs-weekly scan",
    "EMA25 ZL Scanner":      "ema25-zl scan",
    "NSE ZL Squeeze":        "scan: zl-squeeze",
    "US ZL Squeeze":         "us-zl-squeeze",
    "EMA Screener":          "screener:",
    "Dashboard":             "dashboard",
}

SCANNER_MD_LINKS_STATIC = {
    "Swing Scanner":         f"{BLOB}/swing_scans/swing_scans.md",
    "Momentum Scanner":      f"{BLOB}/momentum_scans/momentum_scans.md",
    "Weekly RS Scanner":     f"{BLOB}/momentum_scans/momentum_rs_weekly_scans.md",
    "EMA25 ZL Scanner":      f"{BLOB}/ema25_zl_scans/ema25_zl_scans.md",
    "NSE ZL Squeeze":        f"{BLOB}/zl_squeeze_scans/zl_squeeze_scans.md",
    "US ZL Squeeze":         f"{BLOB}/us_zl_squeeze_scans/us_zl_squeeze_scans.md",
    "Dashboard":             f"{BLOB}/NSE_Circuit_Limits.md",
}


def get_scanner_md_links(today: str) -> dict:
    return {**SCANNER_MD_LINKS_STATIC,
            "EMA Screener": f"{BLOB}/ema_screener_scans/ema_screener_{today}.md"}


def today_ist() -> str:
    return datetime.now(IST).strftime("%Y-%m-%d")


def get_today_commits() -> str:
    today = today_ist()
    r = subprocess.run(
        ["git", "log", "--oneline", f"--since={today} 00:00"],
        capture_output=True, text=True, cwd=BASE
    )
    return r.stdout.lower()


def read_file(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def parse_signal_count(md: str, today: str) -> str:
    blocks = re.split(r'\n---\n', md)
    for block in blocks:
        if today in block:
            rows = [l for l in block.splitlines()
                    if l.strip().startswith('|') and not l.strip().startswith('| Symbol') and '|---' not in l]
            return str(len(rows))
    return "—"


def parse_ema25_zl_counts(md: str, today: str) -> tuple[str, str]:
    m = re.search(rf'\*\*ZLEMA25 Rising: (\d+)\*\*.*?\*\*ZLEMA25 Watch: (\d+)\*\*', md)
    if m and today in md[:200]:
        return m.group(1), m.group(2)
    return "—", "—"


def parse_screener_counts(md: str, today: str) -> tuple[str, str]:
    if today not in md[:100]:
        return "—", "—"
    adds = re.search(r'## ✅ Additions.*?\((\d+)\)', md)
    dels = re.search(r'## ❌ Deletions.*?\((\d+)\)', md)
    return (adds.group(1) if adds else "0"), (dels.group(1) if dels else "0")


def parse_zl_squeeze_count(md: str, today: str) -> str:
    if today not in md[:80]:
        return "—"
    m = re.search(r'\*\*(\d+) stocks: ZLEMA25 Rising \+ Squeeze ON\*\*', md)
    return (m.group(1) + " signals") if m else "—"


def parse_compression_counts(md: str, today: str) -> tuple[str, str]:
    if today not in md[:100]:
        return "—", "—"
    compressed = re.search(r'\*\*Compressed.*?:\*\* (\d+)', md)
    signals    = re.search(r'\*\*Signals:\*\* (\d+)', md)
    return (compressed.group(1) if compressed else "—"), (signals.group(1) if signals else "—")


def get_scan_details(today: str) -> dict:
    swing_md    = read_file(os.path.join(BASE, "swing_scans", "swing_scans.md"))
    mom_md      = read_file(os.path.join(BASE, "momentum_scans", "momentum_scans.md"))
    weekly_md   = read_file(os.path.join(BASE, "momentum_scans", "momentum_rs_weekly_scans.md"))
    zl25_md     = read_file(os.path.join(BASE, "ema25_zl_scans", "ema25_zl_scans.md"))
    nse_zl_md   = read_file(os.path.join(BASE, "zl_squeeze_scans", "zl_squeeze_scans.md"))
    us_zl_md    = read_file(os.path.join(BASE, "us_zl_squeeze_scans", "us_zl_squeeze_scans.md"))
    screener_md = read_file(os.path.join(BASE, "ema_screener_scans", f"ema_screener_{today}.md"))
    zl_rising, zl_watch = parse_ema25_zl_counts(zl25_md, today)
    ema_adds, ema_dels  = parse_screener_counts(screener_md, today)

    return {
        "Swing Scanner":    parse_signal_count(swing_md,  today) + " signals",
        "Momentum Scanner": parse_signal_count(mom_md,    today) + " signals",
        "Weekly RS Scanner":parse_signal_count(weekly_md, today) + " signals",
        "EMA25 ZL Scanner": f"Rising {zl_rising} / Watch {zl_watch}",
        "NSE ZL Squeeze":   parse_zl_squeeze_count(nse_zl_md, today),
        "US ZL Squeeze":    parse_zl_squeeze_count(us_zl_md,  today),
        "EMA Screener":     f"+{ema_adds} adds / -{ema_dels} exits",
        "Dashboard":        "generated",
    }


def build_html_email(today: str, status: dict, details: dict, all_ok: bool,
                     scanner_links: dict) -> str:
    color  = "#2ea44f" if all_ok else "#d73a49"
    header = "All scanners OK" if all_ok else "Scanner issues detected"

    rows = ""
    for name, ok in status.items():
        icon   = "✅" if ok else "❌"
        detail = details.get(name, "—")
        bg     = "#f6fff8" if ok else "#fff6f6"
        link   = scanner_links.get(name)
        label  = (f'<a href="{link}" style="color:#0366d6;text-decoration:none">{name}</a>'
                  if link else name)
        rows += f"""
        <tr style="background:{bg}">
          <td style="padding:8px 12px;border-bottom:1px solid #e1e4e8">{icon} {label}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #e1e4e8;color:#586069">{detail}</td>
        </tr>"""

    failed_note = ""
    if not all_ok:
        failed = [n for n, ok in status.items() if not ok]
        failed_note = f'<p style="color:#d73a49;margin-top:12px">Missing: {", ".join(failed)}</p>'

    return f"""
<html><body style="font-family:Segoe UI,sans-serif;font-size:14px;color:#24292e;max-width:600px;margin:0 auto;padding:20px">
  <h2 style="color:{color};margin-bottom:4px">NSE + US Scanners — {header}</h2>
  <p style="color:#586069;margin-top:0">{today} · Generated {datetime.now(IST).strftime('%H:%M IST')}</p>
  <table style="width:100%;border-collapse:collapse;border:1px solid #e1e4e8;border-radius:6px;overflow:hidden">
    <thead>
      <tr style="background:#f6f8fa">
        <th style="padding:8px 12px;text-align:left;color:#586069;font-size:12px">Scanner</th>
        <th style="padding:8px 12px;text-align:left;color:#586069;font-size:12px">Result</th>
      </tr>
    </thead>
    <tbody>{rows}</tbody>
  </table>
  {failed_note}
  <p style="color:#959da5;font-size:11px;margin-top:16px">
    <a href="{REPO}" style="color:#959da5">{REPO}</a>
  </p>
</body></html>"""


def send_discord(today: str, status: dict, details: dict, all_ok: bool,
                 scanner_links: dict) -> bool:
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "")
    if not webhook_url:
        return False

    color = 0x2ea44f if all_ok else 0xd73a49

    fields = []
    for name, ok in status.items():
        icon   = "✅" if ok else "❌"
        detail = details.get(name, "—")
        link   = scanner_links.get(name)
        value  = f"[{detail}]({link})" if link else detail
        fields.append({"name": f"{icon} {name}", "value": value, "inline": True})

    embed = {
        "title":     f"NSE + US Scanners — {'All OK' if all_ok else 'Issues Detected'}",
        "color":     color,
        "fields":    fields,
        "footer":    {"text": f"satya482@gmail.com · {today}"},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    if not all_ok:
        failed = [n for n, ok in status.items() if not ok]
        embed["description"] = f"⚠️ Missing: {', '.join(failed)}"

    resp = requests.post(webhook_url, json={"embeds": [embed]}, timeout=10)
    return resp.status_code in (200, 204)


def send_email(subject: str, html: str) -> bool:
    app_pass = os.environ.get("GMAIL_APP_PASSWORD", "")
    if not app_pass:
        print("  [email] GMAIL_APP_PASSWORD not set.")
        print("  Run: setx GMAIL_APP_PASSWORD \"your-app-password\" /M")
        print("  Get one at: myaccount.google.com/apppasswords")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = FROM_EMAIL
    msg["To"]      = TO_EMAIL
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(FROM_EMAIL, app_pass)
        s.send_message(msg)
    return True


def main():
    today   = today_ist()
    commits = get_today_commits()

    status = {
        name: keyword in commits
        for name, keyword in SCANNER_KEYWORDS.items()
    }
    details = get_scan_details(today)
    all_ok  = all(status.values())

    print(f"\nNSE Scanner Status — {today}")
    print("=" * 50)
    for name, ok in status.items():
        icon   = "OK  " if ok else "MISS"
        detail = details.get(name, "")
        print(f"  [{icon}] {name:<22}  {detail}")
    print("=" * 50)
    if all_ok:
        print("  All scanners completed.\n")
    else:
        failed = [n for n, ok in status.items() if not ok]
        print(f"  Missing: {', '.join(failed)}\n")

    icon    = "OK" if all_ok else "ALERT"
    subject = f"[NSE+US {icon}] Scanners {today} — {'All OK' if all_ok else 'Issues'}"
    html    = build_html_email(today, status, details, all_ok, get_scanner_md_links(today))

    if send_email(subject, html):
        print(f"  Email sent to {TO_EMAIL}")
    else:
        print("  Email skipped — set GMAIL_APP_PASSWORD to enable.")

    links = get_scanner_md_links(today)
    if send_discord(today, status, details, all_ok, links):
        print("  Discord notification sent.")
    else:
        print("  Discord skipped — set DISCORD_WEBHOOK_URL to enable.")


if __name__ == "__main__":
    main()