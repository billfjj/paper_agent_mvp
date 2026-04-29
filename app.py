from pathlib import Path

import streamlit as st
import yaml

from paper_agent.agents.novelty_agent import analyze_novelty
from paper_agent.agents.outline_agent import generate_outline
from paper_agent.agents.paper_reader_agent import build_paper_card_from_text
from paper_agent.agents.reviewer_agent import review_section
from paper_agent.agents.section_writer_agent import write_section
from paper_agent.database.db import init_db
from paper_agent.database.models import PaperProject
from paper_agent.parsers.pdf_parser import extract_pdf_text


ROOT = Path(__file__).parent
CONFIG = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))


def main() -> None:
    st.set_page_config(page_title=CONFIG["app"]["name"], layout="wide")
    init_db(CONFIG["app"]["database_path"])

    st.title("Paper Agent MVP")
    st.caption("科研论文工作流 Copilot：文献卡片、创新点、大纲、章节初稿与模拟审稿。")

    tabs = st.tabs(["Project", "Paper Card", "Novelty", "Outline", "Write", "Review"])

    with tabs[0]:
        st.subheader("论文项目")
        title = st.text_input("Title", "Frequency and Physics-Aware Dual-Branch Framework for Nighttime Road Object Detection")
        target = st.text_input("Target venue", "IEEE T-ITS")
        topic = st.text_area("Research topic", "Nighttime road object detection with frequency-domain enhancement and physics-aware degradation priors.")
        method = st.text_area("Method summary", "A dual-branch framework combines frequency-aware restoration with physics-guided representation learning for robust traffic object detection.")
        contribution = st.text_area("Contributions", "1. Frequency-aware feature enhancement.\n2. Physics-aware degradation modeling.\n3. Robust nighttime traffic detection benchmarks.")
        project = PaperProject(
            title=title,
            target_journal=target,
            research_topic=topic,
            method_summary=method,
            contribution=contribution,
            status="draft",
        )
        st.session_state["project"] = project
        st.success("项目上下文已更新。")

    with tabs[1]:
        st.subheader("文献阅读与 Paper Card")
        uploaded = st.file_uploader("Upload a PDF", type=["pdf"])
        raw_text = st.text_area("Or paste paper text / abstract", height=180)
        if uploaded is not None:
            pdf_path = ROOT / "data" / "uploads" / uploaded.name
            pdf_path.parent.mkdir(parents=True, exist_ok=True)
            pdf_path.write_bytes(uploaded.getbuffer())
            raw_text = extract_pdf_text(pdf_path, max_pages=5)
            st.info(f"已解析前 5 页：{pdf_path.name}")
        if st.button("Generate Paper Card"):
            card = build_paper_card_from_text(raw_text)
            st.session_state["paper_card"] = card
            st.markdown(card.to_markdown())

    with tabs[2]:
        st.subheader("创新点分析")
        project = st.session_state.get("project")
        related = st.text_area("Related methods", "Low-light enhancement, domain adaptation, physics-based image degradation, nighttime object detection.")
        results = st.text_area("Key results", "The proposed method improves mAP and robustness under low illumination and adverse visibility.")
        if st.button("Analyze Novelty") and project:
            st.markdown(analyze_novelty(project, related, results))

    with tabs[3]:
        st.subheader("论文大纲")
        style = st.selectbox("Style", ["IEEE", "Elsevier", "MDPI"])
        project = st.session_state.get("project")
        if st.button("Generate Outline") and project:
            st.markdown(generate_outline(project, style))

    with tabs[4]:
        st.subheader("分章节写作")
        section = st.selectbox("Section", ["Abstract", "Introduction", "Related Work", "Methodology", "Experiments", "Discussion", "Conclusion"])
        project = st.session_state.get("project")
        paper_card = st.session_state.get("paper_card")
        if st.button("Draft Section") and project:
            st.markdown(write_section(section, project, paper_card))

    with tabs[5]:
        st.subheader("模拟审稿")
        section_text = st.text_area("Paste section text", height=260)
        if st.button("Review Section"):
            st.markdown(review_section(section_text))


if __name__ == "__main__":
    main()
