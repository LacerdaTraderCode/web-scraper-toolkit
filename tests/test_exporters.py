import polars as pl

from utils.exporters import export_all, export_to_csv, export_to_json, export_to_parquet

DATA = [
    {"text": "First quote", "author": "Author A", "tags": "life, love"},
    {"text": "Second quote", "author": "Author B", "tags": "books"},
]


def test_export_to_csv_roundtrip(tmp_path):
    path = tmp_path / "quotes.csv"

    export_to_csv(DATA, str(path))

    assert pl.read_csv(path).to_dicts() == DATA


def test_export_to_parquet_roundtrip(tmp_path):
    path = tmp_path / "quotes.parquet"

    export_to_parquet(DATA, str(path))

    assert pl.read_parquet(path).to_dicts() == DATA


def test_export_to_json_writes_data(tmp_path):
    path = tmp_path / "quotes.json"

    export_to_json(DATA, str(path))

    content = path.read_text(encoding="utf-8")
    assert "First quote" in content
    assert "Author B" in content


def test_export_creates_missing_directories(tmp_path):
    path = tmp_path / "nested" / "output" / "quotes.csv"

    export_to_csv(DATA, str(path))

    assert path.exists()


def test_export_all_writes_every_format(tmp_path):
    export_all(DATA, str(tmp_path / "out" / "quotes"))

    produced = sorted(file.name for file in (tmp_path / "out").iterdir())
    assert produced == ["quotes.csv", "quotes.json", "quotes.parquet"]
