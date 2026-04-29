from pathlib import Path

from paper_agent.parsers.pdf_parser import extract_pdf_text
from paper_agent.rag.chunker import chunk_text


def ingest_pdf(path: str | Path) -> list[str]:
    text = extract_pdf_text(path)
    return chunk_text(text)
