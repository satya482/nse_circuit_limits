import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
from wt_squeeze_dashboard import parse_bounce_rs
from wt_squeeze_dashboard import _bounce_rs_section_html, build_html  # noqa: E402
from run_bounce_rs_scanner import build_markdown  # noqa: E402
from scanners.bounce_rs_scanner import OUTPUT_COLUMNS  # noqa: E402


def test_parse_bounce_rs_basic():
    md = (
        "# Bounce-RS Scanner — 2026-07-05\n\n"
        "| Symbol | RS Dip% | EMA Type | Setup | Dip Low | Ratio Now | Bounce | Score |\n"
        "|--------|--------:|:--------:|-------|--------:|----------:|-------:|------:|\n"
        "| [SBIN](https://in.tradingview.com/chart/?symbol=NSE:SBIN) | 8.23 | A | POCKET_PIVOT "
        "| 0.55 | 0.85 | 0.30 | 14.50 |\n"
    )
    rows = parse_bounce_rs(md)
    assert len(rows) == 1
    assert rows[0]["symbol"] == "SBIN"
    assert rows[0]["ema_type"] == "A"
    assert rows[0]["setup"] == "POCKET_PIVOT"
    assert rows[0]["score"] == "14.50"


def test_parse_bounce_rs_no_signals_returns_empty():
    md = "# Bounce-RS Scanner — 2026-07-05\n\n*No signals.*\n"
    assert parse_bounce_rs(md) == []


def test_parse_bounce_rs_empty_content_returns_empty():
    assert parse_bounce_rs("") == []


def test_parse_bounce_rs_multiple_rows_preserves_order():
    md = (
        "| Symbol | RS Dip% | EMA Type | Setup | Dip Low | Ratio Now | Bounce | Score |\n"
        "|--------|--------:|:--------:|-------|--------:|----------:|-------:|------:|\n"
        "| [AAA](url) | 10.0 | A | POCKET_PIVOT | 0.5 | 0.9 | 0.4 | 18.0 |\n"
        "| [BBB](url) | 2.0 | B | NONE | 0.6 | 0.8 | 0.2 | 5.0 |\n"
    )
    rows = parse_bounce_rs(md)
    assert [r["symbol"] for r in rows] == ["AAA", "BBB"]


_SAMPLE_ROW = {
    "symbol": "SBIN",
    "rs_pct": "8.23",
    "ema_type": "A",
    "setup": "POCKET_PIVOT",
    "dip_low": "0.55",
    "ratio_now": "0.85",
    "bounce": "0.30",
    "score": "14.50",
}


def test_bounce_rs_section_hidden_when_empty():
    assert _bounce_rs_section_html([]) == ""


def test_bounce_rs_section_shows_row_when_present():
    html = _bounce_rs_section_html([_SAMPLE_ROW])
    assert "SBIN" in html
    assert "POCKET_PIVOT" in html
    assert "(1 stocks)" in html


def test_build_html_includes_bounce_rs_section_when_rows_present():
    html = build_html(
        "2026-07-05", "2026-07-05 17:35 IST", [], bounce_rs_rows=[_SAMPLE_ROW]
    )
    assert "BOUNCE-RS" in html
    assert "SBIN" in html


def test_build_html_omits_bounce_rs_section_when_no_rows():
    html = build_html("2026-07-05", "2026-07-05 17:35 IST", [])
    assert "BOUNCE-RS" not in html


def test_build_html_bounce_rs_section_appears_before_wt_bar():
    """Topmost placement: bounce-rs section text appears before the stat bar's
    'WT Bull Cross' label, confirming it renders above every other section."""
    html = build_html(
        "2026-07-05", "2026-07-05 17:35 IST", [], bounce_rs_rows=[_SAMPLE_ROW]
    )
    assert html.index("BOUNCE-RS") < html.index("WT Bull Cross")


def test_build_markdown_round_trips_through_parse_bounce_rs():
    """Verify that build_markdown()'s real output parses back correctly
    through parse_bounce_rs(), with no column misalignment or data loss."""
    # Create a DataFrame with exact OUTPUT_COLUMNS and realistic sample data
    df = pd.DataFrame(
        [
            {
                "symbol": "SBIN",
                "rs_during_dip_%": 8.23,
                "ema_type": "A",
                "setup": "POCKET_PIVOT",
                "dip_low_ratio": 0.55,
                "ratio_5d_now": 0.85,
                "bounce_mag": 0.30,
                "score": 14.50,
            },
            {
                "symbol": "INFY",
                "rs_during_dip_%": 2.67,
                "ema_type": "B",
                "setup": "NR7",
                "dip_low_ratio": 0.62,
                "ratio_5d_now": 0.78,
                "bounce_mag": 0.16,
                "score": 7.33,
            },
        ],
        columns=OUTPUT_COLUMNS,
    )

    # Generate markdown using build_markdown()
    md = build_markdown(df, "2026-07-05", "2026-07-05 17:35 IST")

    # Parse it back using parse_bounce_rs()
    parsed_rows = parse_bounce_rs(md)

    # Assert row count preserved
    assert len(parsed_rows) == 2

    # Assert first row
    assert parsed_rows[0]["symbol"] == "SBIN"
    assert parsed_rows[0]["rs_pct"] == "8.23"
    assert parsed_rows[0]["ema_type"] == "A"
    assert parsed_rows[0]["setup"] == "POCKET_PIVOT"
    assert parsed_rows[0]["dip_low"] == "0.55"
    assert parsed_rows[0]["ratio_now"] == "0.85"
    assert parsed_rows[0]["bounce"] == "0.30"
    assert parsed_rows[0]["score"] == "14.50"

    # Assert second row
    assert parsed_rows[1]["symbol"] == "INFY"
    assert parsed_rows[1]["rs_pct"] == "2.67"
    assert parsed_rows[1]["ema_type"] == "B"
    assert parsed_rows[1]["setup"] == "NR7"
    assert parsed_rows[1]["dip_low"] == "0.62"
    assert parsed_rows[1]["ratio_now"] == "0.78"
    assert parsed_rows[1]["bounce"] == "0.16"
    assert parsed_rows[1]["score"] == "7.33"
