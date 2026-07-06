from capital import catalyst_calendar as cc


def _meetings():
    """Shape matches NSE's real corporate-board-meetings API response
    (verified live during planning) -- only the fields days_to_results reads
    are populated here, extras are what a real response also carries."""
    return [
        {
            "bm_symbol": "KARURVYSYA", "bm_date": "20-Jul-2026",
            "bm_purpose": "Financial Results",
            "bm_desc": "To consider and approve the unaudited financial results for the period ended Jun 30, 2026",
            "sm_name": "Karur Vysya Bank Limited",
        },
        {
            "bm_symbol": "KARURVYSYA", "bm_date": "20-Jul-2026",
            "bm_purpose": "Board Meeting Intimation",
            "bm_desc": "Karur Vysya Bank Limited has informed the Exchange about Board Meeting to be held on 20-Jul-2026",
            "sm_name": "Karur Vysya Bank Limited",
        },
        {
            "bm_symbol": "MAHLOG", "bm_date": "15-Jul-2026",
            "bm_purpose": "Financial Results",
            "bm_desc": "Quarterly Unaudited Financial results for the period ended June 2026",
            "sm_name": "Mahindra Logistics Limited",
        },
        {
            "bm_symbol": "MAHLOG", "bm_date": "01-Jul-2026",
            "bm_purpose": "Financial Results",
            "bm_desc": "A past meeting, already held",
            "sm_name": "Mahindra Logistics Limited",
        },
    ]


def test_days_to_results_finds_nearest_financial_results_meeting():
    assert cc.days_to_results("KARURVYSYA", "2026-07-06", _meetings()) == 14


def test_days_to_results_ignores_non_results_purpose():
    # KARURVYSYA also has a "Board Meeting Intimation" row on the same date --
    # must not double-count or pick the wrong purpose, just skip it
    result = cc.days_to_results("KARURVYSYA", "2026-07-06", _meetings())
    assert result == 14


def test_days_to_results_ignores_past_meetings():
    # MAHLOG has a past Financial Results meeting (01-Jul-2026, before as_of)
    # and a future one (15-Jul-2026) -- must pick the future one only
    assert cc.days_to_results("MAHLOG", "2026-07-06", _meetings()) == 9


def test_days_to_results_returns_none_when_symbol_not_found():
    assert cc.days_to_results("RELIANCE", "2026-07-06", _meetings()) is None


def test_days_to_results_returns_none_when_only_past_meetings_exist():
    assert cc.days_to_results("MAHLOG", "2026-07-10", [_meetings()[3]]) is None


def test_days_to_results_zero_when_meeting_is_today():
    assert cc.days_to_results("MAHLOG", "2026-07-15", _meetings()) == 0


def test_days_to_expiry_before_expiry_in_month():
    assert cc.days_to_expiry("2026-07-06") == 24


def test_days_to_expiry_on_expiry_day_itself():
    assert cc.days_to_expiry("2026-07-30") == 0


def test_days_to_expiry_after_expiry_rolls_to_next_month():
    assert cc.days_to_expiry("2026-07-31") == 27


def test_days_to_expiry_year_boundary_rollover():
    # Dec 2026's last Thursday is Dec 31 itself -- as_of Jan 1 2027 must roll
    # to Jan 2027's last Thursday (28th), not stay stuck in December
    assert cc.days_to_expiry("2027-01-01") == 27
