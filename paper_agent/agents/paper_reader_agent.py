from paper_agent.database.models import PaperCard


def build_paper_card_from_text(text: str) -> PaperCard:
    cleaned = " ".join((text or "").split())
    title = cleaned[:120] if cleaned else "Untitled paper"
    abstract_hint = cleaned[:600] if cleaned else "No text was provided."
    return PaperCard(
        title=title,
        venue_year="To be completed",
        problem=_infer_problem(abstract_hint),
        method="Identify the main architecture, training strategy, and inference pipeline from the full paper.",
        novelty="Summarize the claimed difference from prior work after reading introduction and method sections.",
        datasets="Extract dataset names from experiments section.",
        metrics="Extract metrics such as mAP, mIoU, F1, RMSE, AbsRel, or visibility accuracy.",
        limitations="Check failure cases, missing ablations, domain limitations, and compute cost.",
        useful_for="Introduction, Related Work, Methodology motivation, and Discussion.",
    )


def _infer_problem(text: str) -> str:
    if not text:
        return "The paper problem is not available yet."
    return f"Initial reading focus: {text[:260]}..."
