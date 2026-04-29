from paper_agent.database.models import PaperCard, PaperProject


def write_section(section: str, project: PaperProject, paper_card: PaperCard | None = None) -> str:
    if section == "Abstract":
        return _abstract(project)
    if section == "Introduction":
        return _introduction(project)
    if section == "Related Work":
        card_note = paper_card.to_markdown() if paper_card else "No paper card has been selected."
        return _related_work(project, card_note)
    if section == "Methodology":
        return _method(project)
    if section == "Experiments":
        return _experiments(project)
    if section == "Discussion":
        return _discussion(project)
    return _conclusion(project)


def _abstract(project: PaperProject) -> str:
    return f"""### Abstract Draft

Nighttime road object detection is essential for intelligent transportation systems, yet it remains challenging because low illumination, sensor noise, glare, and visibility degradation suppress discriminative visual cues. This paper presents **{project.title}**, a framework designed to improve object detection in challenging nighttime traffic scenes. The proposed method integrates frequency-aware representation learning with physics-guided degradation modeling, enabling the detector to recover informative structures while maintaining task-relevant semantics. Experiments on nighttime road benchmarks should compare the proposed framework with enhancement-based, detection-oriented, and adverse-condition baselines. The final abstract should report exact numerical gains, efficiency, and robustness results after the experimental tables are fixed.
"""


def _introduction(project: PaperProject) -> str:
    return f"""### Introduction Draft

Road object detection is a fundamental component of intelligent transportation systems, supporting autonomous driving, traffic monitoring, and safety-critical perception. Although modern detectors have achieved strong performance in well-lit daytime scenes, their reliability often degrades sharply at night due to weak illumination, complex light sources, motion blur, and reduced object-background contrast \\cite{{night_detection_placeholder}}.

Existing studies mainly address this problem from two perspectives. Image enhancement methods improve visual quality before detection, but perceptual enhancement does not always preserve task-discriminative features. Detection-oriented adaptation methods improve robustness by modifying the detector or training strategy, yet they may underuse the physical characteristics of nighttime degradation and frequency-level cues \\cite{{low_light_placeholder, adverse_detection_placeholder}}.

To address these limitations, this paper studies {project.research_topic}. We propose {project.method_summary} The key idea is to jointly exploit frequency-domain information and physics-aware priors so that the model can enhance robust structures while learning degradation-aware semantic representations.

The main contributions are summarized as follows:

{project.contribution}
"""


def _related_work(project: PaperProject, card_note: str) -> str:
    return f"""### Related Work Draft

#### Low-Light Image Enhancement

Low-light enhancement methods attempt to improve visibility by adjusting illumination, contrast, or noise distribution. These methods are useful for human perception, but their outputs may introduce artifacts or remove subtle object cues required by downstream detectors.

#### Object Detection in Adverse Traffic Scenes

Adverse-condition object detection focuses on robust perception under nighttime, fog, rain, glare, and sensor noise. Existing approaches include domain adaptation, feature alignment, data augmentation, and task-specific detector redesign. However, many methods treat degradation as a generic domain gap and do not explicitly model frequency-level or physics-guided cues.

#### Frequency and Physics-Aware Vision

Frequency-domain learning can expose structural patterns that are less visible in the spatial domain, while physics-aware modeling provides interpretable constraints for degradation formation. For {project.title}, the related work should emphasize how these two lines of research are complementary.

#### Available Paper Card Context

{card_note}
"""


def _method(project: PaperProject) -> str:
    return f"""### Methodology Draft

The proposed framework consists of three components: a frequency-aware branch, a physics-aware branch, and a task-oriented fusion module. Given a nighttime road image, the frequency-aware branch extracts degradation-robust structural cues, while the physics-aware branch estimates representations associated with illumination and visibility degradation. The fused representation is then passed to the detection head for object classification and localization.

This section should define the input image, branch functions, fusion operator, and loss terms in LaTeX. It should also clarify whether the framework is detector-agnostic or tied to a specific backbone.
"""


def _experiments(project: PaperProject) -> str:
    return f"""### Experiments Draft

The experiments should evaluate {project.title} from accuracy, robustness, ablation, and efficiency perspectives. Recommended subsections include datasets, implementation details, comparison methods, main results, ablation studies, robustness analysis, visualization, and computational cost. All reported improvements should include exact metrics and the same training protocol for fair comparison.
"""


def _discussion(project: PaperProject) -> str:
    return f"""### Discussion Draft

The discussion should explain why frequency-aware and physics-aware modeling improves nighttime detection, where the method still fails, and how deployment constraints affect practical use. It should avoid overclaiming and explicitly distinguish validated conclusions from plausible hypotheses.
"""


def _conclusion(project: PaperProject) -> str:
    return f"""### Conclusion Draft

This paper presented {project.title}, a framework for nighttime road object detection that combines frequency-aware representation learning with physics-guided degradation modeling. The final conclusion should summarize the verified empirical gains, highlight the most important ablation findings, and discuss future work such as broader weather conditions, cross-camera generalization, and real-time deployment.
"""
