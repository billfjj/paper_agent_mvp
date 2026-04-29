from paper_agent.database.models import PaperProject


OUTLINES = {
    "IEEE": ["I. Introduction", "II. Related Work", "III. Methodology", "IV. Experiments", "V. Discussion", "VI. Conclusion"],
    "Elsevier": ["Abstract", "Keywords", "1. Introduction", "2. Literature Review", "3. Proposed Method", "4. Experimental Setup", "5. Results and Discussion", "6. Conclusion"],
    "MDPI": ["1. Introduction", "2. Related Work", "3. Materials and Methods", "4. Results", "5. Discussion", "6. Conclusions"],
}


def generate_outline(project: PaperProject, style: str) -> str:
    sections = OUTLINES.get(style, OUTLINES["IEEE"])
    lines = [f"### {style} Outline", "", f"**Title:** {project.title}", f"**Target:** {project.target_journal}", ""]
    for section in sections:
        lines.append(f"- {section}")
    lines.extend(
        [
            "",
            "### Section Logic",
            "- Introduction: background, nighttime traffic challenges, limits of prior methods, proposed idea, contributions.",
            "- Related Work: low-light enhancement, adverse-condition object detection, frequency-domain learning, physics-aware vision.",
            "- Methodology: overall architecture, frequency branch, physics-aware branch, feature fusion, losses, inference.",
            "- Experiments: datasets, settings, baselines, main results, ablations, robustness, efficiency.",
            "- Discussion: why the method works, failure cases, limitations, deployment implications.",
        ]
    )
    return "\n".join(lines)
