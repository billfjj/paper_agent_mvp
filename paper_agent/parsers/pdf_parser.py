from pathlib import Path

import fitz


def extract_pdf_text(path: str | Path, max_pages: int | None = None) -> str:
    doc = fitz.open(path)
    pages = doc if max_pages is None else doc[:max_pages]
    return "\n\n".join(page.get_text("text") for page in pages)
