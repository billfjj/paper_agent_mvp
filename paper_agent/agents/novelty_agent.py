from paper_agent.database.models import PaperProject


def analyze_novelty(project: PaperProject, related_methods: str, results: str) -> str:
    return f"""### 创新点分析

**核心问题**

{project.research_topic}

**本文方法**

{project.method_summary}

**与已有方法的可能区别**

1. 是否不仅做低照度增强，而是把频域增强与检测任务端到端关联。
2. 是否不仅引入物理先验，而是让先验约束特征、损失或退化建模过程。
3. 是否在夜间道路场景中证明了检测性能、鲁棒性和泛化能力的共同提升。

**需要警惕的审稿质疑**

1. 频域分支是否只是常规增强模块，缺少必要性证明。
2. 物理先验是否真正参与学习，还是只作为叙述性动机。
3. 对比方法是否公平，尤其是增强后检测、低照度检测和恶劣天气检测方法。
4. 提升是否只来自更多参数或训练技巧。

**建议补充实验**

1. 去除频域分支、去除物理先验、替换融合策略的消融实验。
2. 不同照度、噪声、雾霾或曝光条件下的分组评估。
3. 参数量、FLOPs、FPS 和显存占用对比。
4. 可视化频域响应、注意力图、失败案例与跨数据集泛化。

**可写入 Introduction 的贡献表述**

We propose a frequency and physics-aware dual-branch framework for nighttime road object detection, where frequency-domain representations enhance low-light discriminative cues and physics-guided priors regularize degradation-aware feature learning. Extensive experiments demonstrate consistent improvements over enhancement-based and detection-oriented baselines under challenging nighttime traffic conditions.

**输入的已有方法**

{related_methods}

**输入的实验结果**

{results}
"""
