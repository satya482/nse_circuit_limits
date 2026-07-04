import sqlite3

import backfill_delivery_markers
from backfill_delivery_markers import _has_todays_delivery_data, patch_md_file, patch_symbol_line


def _tagger(spikes):
    return lambda symbol: spikes.get(symbol, "")


def test_patch_symbol_line_adds_tag_no_existing_sub():
    line = "| [RELIANCE](https://tv.example/RELIANCE) | 3d | +1.2% |\n"
    out = patch_symbol_line(line, _tagger({"RELIANCE": "DEL68%(T-1)"}))
    assert out.startswith(
        "| [RELIANCE](https://tv.example/RELIANCE)<br><sub>DEL68%(T-1)</sub>"
    )


def test_patch_symbol_line_appends_to_existing_sub():
    line = "| [RELIANCE](https://tv.example/RELIANCE)<br><sub>↑CMF3d</sub> | 3d |\n"
    out = patch_symbol_line(line, _tagger({"RELIANCE": "DEL68%(T-1)"}))
    assert "<sub>↑CMF3d · DEL68%(T-1)</sub>" in out


def test_patch_symbol_line_idempotent_rerun():
    line = "| [RELIANCE](https://tv.example/RELIANCE) | 3d |\n"
    tagger = _tagger({"RELIANCE": "DEL68%(T-1)"})
    once = patch_symbol_line(line, tagger)
    twice = patch_symbol_line(once, tagger)
    assert once == twice


def test_patch_symbol_line_removes_stale_tag_when_no_longer_spiking():
    line = "| [RELIANCE](https://tv.example/RELIANCE)<br><sub>DEL68%(T-1)</sub> | 3d |\n"
    out = patch_symbol_line(line, _tagger({}))
    assert "DEL" not in out
    assert "<sub>" not in out


def test_patch_symbol_line_handles_rs_highline_extra_bracket():
    line = "| [RELIANCE](https://tv.example/RELIANCE) [20% ] | 150.00 |\n"
    out = patch_symbol_line(line, _tagger({"RELIANCE": "DEL68%(T-1)"}))
    assert out.startswith(
        "| [RELIANCE](https://tv.example/RELIANCE) [20% ]<br><sub>DEL68%(T-1)</sub>"
    )


def test_patch_symbol_line_ignores_non_data_rows():
    header = "| Symbol | Days |\n"
    assert patch_symbol_line(header, _tagger({"RELIANCE": "DEL68%(T-1)"})) == header


def test_patch_md_file_idempotent(tmp_path):
    p = tmp_path / "sample.md"
    p.write_text("| [RELIANCE](https://tv.example/RELIANCE) | 3d |\n", encoding="utf-8")
    tagger = _tagger({"RELIANCE": "DEL68%(T-1)"})

    n1 = patch_md_file(p, tagger)
    content_once = p.read_text(encoding="utf-8")
    n2 = patch_md_file(p, tagger)
    content_twice = p.read_text(encoding="utf-8")

    assert n1 == 1
    assert n2 == 0
    assert content_once == content_twice


def test_has_todays_delivery_data_true_when_row_for_today(tmp_path, monkeypatch):
    db_path = tmp_path / "market.db"
    con = sqlite3.connect(db_path)
    con.execute("CREATE TABLE delivery (symbol TEXT, date TEXT, deliv_pct REAL)")
    con.execute("INSERT INTO delivery VALUES ('RELIANCE', '2026-07-04', 55.0)")
    con.commit()
    con.close()
    monkeypatch.setattr(backfill_delivery_markers, "DB_PATH", db_path)

    assert _has_todays_delivery_data("2026-07-04") is True


def test_has_todays_delivery_data_false_when_only_older_dates(tmp_path, monkeypatch):
    db_path = tmp_path / "market.db"
    con = sqlite3.connect(db_path)
    con.execute("CREATE TABLE delivery (symbol TEXT, date TEXT, deliv_pct REAL)")
    con.execute("INSERT INTO delivery VALUES ('RELIANCE', '2026-07-01', 55.0)")
    con.commit()
    con.close()
    monkeypatch.setattr(backfill_delivery_markers, "DB_PATH", db_path)

    assert _has_todays_delivery_data("2026-07-04") is False


def test_has_todays_delivery_data_false_when_table_missing(tmp_path, monkeypatch):
    db_path = tmp_path / "market.db"
    sqlite3.connect(db_path).close()  # fresh, empty DB file -- no CREATE TABLE run
    monkeypatch.setattr(backfill_delivery_markers, "DB_PATH", db_path)

    assert _has_todays_delivery_data("2026-07-04") is False
