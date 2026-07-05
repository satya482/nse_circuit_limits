import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from wt_squeeze_dashboard import parse_bounce_rs
from wt_squeeze_dashboard import _bounce_rs_section_html, build_html  # noqa: E402


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
