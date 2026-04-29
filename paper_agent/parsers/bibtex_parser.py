from pathlib import Path

import bibtexparser


def load_bibtex(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as handle:
        database = bibtexparser.load(handle)
    return list(database.entries)
