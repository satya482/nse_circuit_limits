#!/usr/bin/env python3
"""
Kite Connect daily access token refresh.
Automates browser login using TOTP and updates .env with the new access token.
Run once daily before any scanner — scheduled at 8:00 AM Mon-Fri.
"""

import os, sys, requests, pyotp
from urllib.parse import urlparse, parse_qs
from kiteconnect import KiteConnect
from pathlib import Path
from datetime import datetime, timedelta

ENV_FILE       = Path(__file__).parent / ".env"
TOKEN_STAMP    = Path(__file__).parent / ".kite_token_stamp"
TOKEN_MAX_AGE  = timedelta(hours=16)   # refreshed ~4 PM, valid until 8 AM next day


def load_env() -> dict:
    env = {}
    with open(ENV_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def update_env_token(new_token: str):
    lines = ENV_FILE.read_text(encoding="utf-8").splitlines()
    updated = [
        f"KITE_ACCESS_TOKEN={new_token}" if l.startswith("KITE_ACCESS_TOKEN=") else l
        for l in lines
    ]
    ENV_FILE.write_text("\n".join(updated) + "\n", encoding="utf-8")


def fetch_access_token(api_key, api_secret, user_id, password, totp_secret) -> str:
    s = requests.Session()
    s.headers.update({"X-Kite-Version": "3"})

    # Step 1: password login
    r = s.post("https://kite.zerodha.com/api/login",
               data={"user_id": user_id, "password": password})
    r.raise_for_status()
    body = r.json()
    if body.get("status") != "success":
        raise RuntimeError(f"Login failed: {body}")
    request_id = body["data"]["request_id"]

    # Step 2: TOTP
    otp = pyotp.TOTP(totp_secret).now()
    r = s.post("https://kite.zerodha.com/api/twofa",
               data={"user_id": user_id, "request_id": request_id,
                     "twofa_value": otp, "twofa_type": "totp"})
    r.raise_for_status()
    body = r.json()
    if body.get("status") != "success":
        raise RuntimeError(f"TOTP failed: {body}")

    # Step 3: follow Kite's internal redirects, stop at the localhost callback
    r = s.get(f"https://kite.zerodha.com/connect/login?api_key={api_key}&v=3",
              allow_redirects=False)
    location = r.headers.get("Location", "")
    while r.status_code in (301, 302, 303, 307, 308):
        if not location:
            break
        if "127.0.0.1" in location or "localhost" in location:
            break  # reached callback — don't try to connect to localhost
        r = s.get(location, allow_redirects=False)
        location = r.headers.get("Location", "")

    if not location:
        raise RuntimeError("No redirect to callback URL from Kite Connect")
    params = parse_qs(urlparse(location).query)
    if "request_token" not in params:
        raise RuntimeError(f"request_token missing in redirect: {location}")
    request_token = params["request_token"][0]

    # Step 4: exchange request_token for access_token
    kite = KiteConnect(api_key=api_key)
    session = kite.generate_session(request_token, api_secret=api_secret)
    return session["access_token"]


def _token_is_fresh() -> bool:
    """Return True if the token was written less than TOKEN_MAX_AGE ago."""
    if not TOKEN_STAMP.exists():
        return False
    try:
        stamped = datetime.fromisoformat(TOKEN_STAMP.read_text().strip())
        return datetime.now() - stamped < TOKEN_MAX_AGE
    except Exception:
        return False


def main():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if _token_is_fresh():
        stamped = TOKEN_STAMP.read_text().strip()
        print(f"[{ts}] Token still fresh (refreshed {stamped}) — skipping.")
        sys.exit(0)

    print(f"[{ts}] Kite token refresh starting...")

    env = load_env()
    try:
        token = fetch_access_token(
            api_key     = env["KITE_API_KEY"],
            api_secret  = env["KITE_API_SECRET"],
            user_id     = env["KITE_USER_ID"],
            password    = env["KITE_PASSWORD"],
            totp_secret = env["KITE_TOTP_SECRET"],
        )
        update_env_token(token)
        TOKEN_STAMP.write_text(datetime.now().isoformat(timespec="seconds"))
        print(f"  Token refreshed: {token[:8]}...{token[-4:]}")

        # Verify
        kite = KiteConnect(api_key=env["KITE_API_KEY"])
        kite.set_access_token(token)
        profile = kite.profile()
        print(f"  Verified: {profile['user_name']} | {profile['email']}")
        print(f"  Broker: {profile['broker']}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Done.")

    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()