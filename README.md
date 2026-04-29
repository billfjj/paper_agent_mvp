# Paper Agent MVP

本项目是一个本地科研论文写作 Copilot MVP，面向 AI、交通、遥感、语义分割、深度估计、可见度预测等论文工作流。

第一版目标不是全自动写论文，而是提供：

- 论文项目管理
- PDF / BibTeX 文献入库
- Paper Card 结构化整理
- 创新点分析
- 论文大纲生成
- 分章节初稿生成
- 模拟审稿意见

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Project Layout

```text
paper_agent/
├── agents/
├── database/
├── parsers/
├── rag/
├── templates/
│   └── prompts/
└── tools/
```

## Notes

- `data/paper_agent.sqlite3` 会在首次运行时自动创建。
- 当前 MVP 默认生成可编辑草稿，不会自动联网检索文献。
- 后续可以在 `paper_agent/tools/` 中接入 Semantic Scholar、arXiv、Crossref 和 Zotero。
