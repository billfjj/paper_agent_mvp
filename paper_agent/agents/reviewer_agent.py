def review_section(section_text: str) -> str:
    text = (section_text or "").strip()
    if not text:
        return "请先粘贴需要审查的论文段落。"

    return f"""### Simulated Review

**Major Concerns**

1. Novelty should be stated as a technical difference, not only as a combination of popular modules.
2. Each causal claim needs either a citation, an ablation, or a clearly marked hypothesis.
3. The section should clarify whether improvements come from architecture, training data, loss design, or post-processing.

**Minor Concerns**

1. Avoid broad claims such as "significantly improves" until exact metrics are inserted.
2. Check that every placeholder citation is later backed by a real BibTeX entry.
3. Keep terminology consistent across frequency branch, physics-aware branch, and fusion module.

**Suggested Revision Strategy**

1. Add one sentence that defines the exact research gap.
2. Add one sentence that explains why existing enhancement-first pipelines are insufficient.
3. Insert citation placeholders only where a claim needs support.
4. Reserve numerical claims for the final version after table verification.

**Reviewed Text Length**

{len(text.split())} words
"""
