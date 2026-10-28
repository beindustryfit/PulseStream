from pathlib import Path


def test_schema_files_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "schemas" / "page_view.schema.json").is_file()
    assert (root / "schemas" / "click.schema.json").is_file()
    assert (root / "producer" / "emit.py").is_file()
