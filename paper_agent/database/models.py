from dataclasses import dataclass


@dataclass
class PaperProject:
    title: str
    target_journal: str
    research_topic: str
    method_summary: str
    contribution: str
    status: str = "draft"


@dataclass
class PaperCard:
    title: str
    venue_year: str
    problem: str
    method: str
    novelty: str
    datasets: str
    metrics: str
    limitations: str
    useful_for: str

    def to_markdown(self) -> str:
        return f"""### Paper Card

| Field | Content |
| --- | --- |
| Title | {self.title} |
| Venue / Year | {self.venue_year} |
| Problem | {self.problem} |
| Method | {self.method} |
| Key novelty | {self.novelty} |
| Dataset | {self.datasets} |
| Metrics | {self.metrics} |
| Limitations | {self.limitations} |
| Useful for | {self.useful_for} |
"""
