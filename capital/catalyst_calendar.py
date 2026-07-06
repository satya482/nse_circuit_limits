"""Catalyst calendar (Sec 7): days_to_results via NSE's corporate-board-meetings
API (real endpoint, verified live during planning -- returns scheduled board
meetings including their stated purpose), days_to_expiry via pure calendar math
(last Thursday of the month, the NSE stock F&O monthly expiry convention).
days_to_index_rebal is explicitly out of scope -- no verifiable NSE API exists
for Nifty index rebalance effective dates (announced via press release, not a
queryable endpoint); user decision to skip rather than guess."""

import calendar
from datetime import datetime, timedelta

import requests

NSE_HOME_URL = "https://www.nseindia.com"
BOARD_MEETINGS_URL = "https://www.nseindia.com/api/corporate-board-meetings"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
RESULTS_PURPOSE = "Financial Results"


def fetch_board_meetings(from_date: str, to_date: str) -> list[dict]:
    """from_date/to_date in DD-MM-YYYY (matches main.py's NSE API convention).
    Raises RuntimeError on failure -- Sec 0 guardrail: no silent API fallbacks."""
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})
    session.get(NSE_HOME_URL, timeout=10)
    response = session.get(
        BOARD_MEETINGS_URL,
        params={"index": "equities", "from_date": from_date, "to_date": to_date},
        timeout=10,
    )
    if response.status_code != 200:
        raise RuntimeError(f"NSE corporate-board-meetings returned {response.status_code}")
    return response.json()


def days_to_results(symbol: str, as_of: str, board_meetings: list[dict]) -> int | None:
    """Nearest upcoming 'Financial Results' board meeting date for symbol, in
    days from as_of. None if no scheduled results meeting is in board_meetings
    for this symbol -- not an error, most stocks simply have nothing scheduled
    yet (SEBI LODR only requires ~5 days' advance intimation)."""
    as_of_date = datetime.strptime(as_of, "%Y-%m-%d").date()
    candidates = []
    for row in board_meetings:
        if row.get("bm_symbol") != symbol or row.get("bm_purpose") != RESULTS_PURPOSE:
            continue
        bm_date = datetime.strptime(row["bm_date"], "%d-%b-%Y").date()
        if bm_date >= as_of_date:
            candidates.append(bm_date)
    if not candidates:
        return None
    return (min(candidates) - as_of_date).days


def _last_thursday(year: int, month: int):
    last_day = calendar.monthrange(year, month)[1]
    d = datetime(year, month, last_day).date()
    while d.weekday() != 3:  # Thursday
        d -= timedelta(days=1)
    return d


def days_to_expiry(as_of: str) -> int:
    """Days to this (or next) month's F&O monthly expiry -- last Thursday of
    the month, the NSE stock F&O convention. ponytail: does not adjust for an
    exchange holiday landing on the last Thursday (NSE shifts expiry to the
    prior trading day when that happens) -- no repo-local NSE holiday calendar
    exists to check against; accepted approximation, off by at most 1-2 days
    in rare holiday weeks."""
    as_of_date = datetime.strptime(as_of, "%Y-%m-%d").date()
    expiry = _last_thursday(as_of_date.year, as_of_date.month)
    if expiry < as_of_date:
        year, month = as_of_date.year, as_of_date.month + 1
        if month > 12:
            year, month = year + 1, 1
        expiry = _last_thursday(year, month)
    return (expiry - as_of_date).days
