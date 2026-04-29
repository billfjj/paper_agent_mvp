from pathlib import Path
import sqlite3


SCHEMA = """
CREATE TABLE IF NOT EXISTS papers (
    id INTEGER PRIMARY KEY,
    title TEXT,
    authors TEXT,
    year INTEGER,
    venue TEXT,
    doi TEXT,
    abstract TEXT,
    pdf_path TEXT,
    bibtex TEXT,
    keywords TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS paper_cards (
    id INTEGER PRIMARY KEY,
    paper_id INTEGER,
    problem TEXT,
    method TEXT,
    novelty TEXT,
    datasets TEXT,
    metrics TEXT,
    limitations TEXT,
    useful_for TEXT
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    title TEXT,
    target_journal TEXT,
    research_topic TEXT,
    method_summary TEXT,
    contribution TEXT,
    status TEXT
);

CREATE TABLE IF NOT EXISTS drafts (
    id INTEGER PRIMARY KEY,
    project_id INTEGER,
    section_name TEXT,
    content TEXT,
    version INTEGER,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""


def init_db(database_path: str) -> None:
    path = Path(database_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as conn:
        conn.executescript(SCHEMA)
