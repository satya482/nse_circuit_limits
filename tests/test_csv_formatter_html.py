from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_HTML = ROOT / "dashboard" / "csv.html"


def test_csv_formatter_page_exists_with_disclaimer():
    text = CSV_HTML.read_text(encoding="utf-8")

    assert "SEBI registered" in text
    assert "NSE Delivery CSV Formatter" in text


def test_file_upload_accepts_csv_and_txt_with_filereader_fallback():
    text = CSV_HTML.read_text(encoding="utf-8")

    assert 'type="file"' in text
    assert 'accept=".csv,.txt,text/csv,text/plain"' in text
    assert "FileReader" in text
    assert "readAsText" in text
    assert "file.name.toLowerCase()" in text
    assert 'endsWith(".csv")' in text
    assert 'endsWith(".txt")' in text


def test_csv_formatter_is_self_contained():
    text = CSV_HTML.read_text(encoding="utf-8")

    assert "../docs/app.js" not in text
    assert "../docs/styles.css" not in text
