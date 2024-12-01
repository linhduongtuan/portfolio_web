import reflex as rx
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum
from ..components.styles import Color, TextColor, Size
from ..ui.base import base_page


class OutputType(Enum):
    PAPER = "paper"
    PATENT = "patent"
    SOFTWARE = "software"
    AWARD = "award"


@dataclass
class Output:
    """Research output (paper, patent, software, award)"""

    type: OutputType
    title: str
    description: str
    url: Optional[str] = None
    year: Optional[int] = None


@dataclass
class Research:
    """Research project information"""

    title: str
    aims: str
    year_start: int
    year_end: Optional[int] = None
    sponsor: str = ""
    sponsor_url: str = ""
    budget: str = ""
    outputs: List[Output] = None  # type: ignore

    def __post_init__(self):
        self.outputs = self.outputs or []
        self.year_end = self.year_end or self.year_start


def research_output_item(output: Output) -> rx.Component:
    """Create a research output item."""
    icon_map = {
        OutputType.PAPER: "📄",
        OutputType.PATENT: "📋",
        OutputType.SOFTWARE: "💻",
        OutputType.AWARD: "🏆",
    }

    return rx.hstack(
        rx.text(icon_map[output.type], font_size="1.2em"),
        rx.vstack(
            rx.text(output.title, font_weight="medium"),
            rx.text(
                output.description,
                font_style="italic",
                color=TextColor.SECONDARY.value,
            ),
            rx.link(
                output.url,
                href=output.url,
                color=Color.ACCENT.value,
                is_external=True,
            )
            if output.url
            else rx.box(),
            align_items="start",
        ),
        width="100%",
        spacing="3",
    )


def research_item(proj: Research) -> rx.Component:
    """Create a research project item."""
    sponsor_badge = (
        rx.link(
            rx.badge(
                proj.sponsor,
                color_scheme="green",
                text_size=Size.ABIT_BIG.value,
                color=TextColor.PRIMARY.value,
                _hover={
                    "transform": "scale(1.05)",
                    "transition": "transform 0.2s",
                },
            ),
            href=proj.sponsor_url,
            is_external=True,
        )
        if (proj.sponsor and proj.sponsor_url)
        else rx.badge(
            proj.sponsor,
            color_scheme="green",
            text_size=Size.ABIT_BIG.value,
            color=TextColor.PRIMARY.value,
        )
        if proj.sponsor
        else rx.box()
    )
    return rx.vstack(
        # Project header
        rx.hstack(
            rx.vstack(
                rx.heading(
                    proj.title,
                    size=Size.COLOSAL.value,  # type: ignore
                    color=TextColor.PRIMARY.value,  # type: ignore
                ),
                rx.text(
                    f"{proj.year_start}-{proj.year_end}",
                    color=TextColor.SECONDARY.value,
                ),
                align_items="start",
            ),
            rx.spacer(),
            sponsor_badge,
            width="100%",
        ),
        # Project aims
        rx.accordion.root(
            rx.accordion.item(
                header="Project Aims",
                content=rx.text(
                    proj.aims,
                    color=TextColor.PRIMARY.value,  # type: ignore
                ),
                bg=Color.SECONDARY.value,  # type: ignore
                padding="1em",
            ),
            collapsible=True,
            width="100%",
        ),
        # Outputs section
        rx.vstack(
            rx.heading(
                "Outputs",
                size=Size.LIGHT_BIG.value,  # type: ignore
                color=TextColor.PRIMARY.value,  # type: ignore
            ),
            *[research_output_item(output) for output in proj.outputs],
            align_items="start",
            padding="1em",
            bg="whiteAlpha.100",
            border_radius="md",
        )
        if proj.outputs
        else rx.box(),
        align_items="start",
        width="100%",
        spacing="4",
        padding="2em",
        border="1px solid",
        border_color=Color.PRIMARY.value,
        border_radius="5%",
        # color=TextColor.TERTIARY.value,
    )


@rx.page(route="/research")
def research_view() -> rx.Component:
    """Create the research page view."""
    my_child = rx.box(
        rx.vstack(
            rx.heading(
                "PROJECTS & RESEARCH",
                size=Size.BIG.value,  # type: ignore
                color=TextColor.TERTIARY.value,
                margin_bottom="0.5em",  # Space below the heading
                font_size="3em",  # Or use direct size
                font_weight="bold",  # Optional: make it bolder
                align_self="center",  # Center it horizontally
                # Or align_self="flex-start" for left alignment
                # Or align_self="flex-end" for right alignment
                padding_top="1em",  # Space above the heading
            ),
            *[research_item(proj) for proj in RESEARCH_PROJECTS],
            align_items="start",
            spacing="4",
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding="2em",
            # color=TextColor.TERTIARY.value,
        ),
        id="my-child",
    )
    return base_page(my_child)


RESEARCH_PROJECTS = [
    Research(
        title="AI-Powered Medical Image Analysis for Early Disease Detection",
        aims="Develop and validate deep learning models for automated detection of diseases from various medical imaging modalities, focusing on tuberculosis, COVID-19, and breast cancer screening.",
        year_start=2023,
        year_end=2025,
        sponsor="European Research Council",
        sponsor_url="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en",
        budget="€750,000",
        outputs=[
            Output(
                type=OutputType.PAPER,
                title="Detection of tuberculosis from chest X-ray images: Boosting performance with Vision Transformer",
                description="Published in Expert Systems with Applications (Impact Factor: 8.665)",
                url="https://doi.org/10.1016/j.eswa.2021.115519",
                year=2023,
            ),
            Output(
                type=OutputType.SOFTWARE,
                title="MedicalVisionAI",
                description="Open-source medical image analysis toolkit with 1000+ GitHub stars",
                url="https://github.com/medicalvisionai",
                year=2023,
            ),
            Output(
                type=OutputType.AWARD,
                title="Best Paper Award",
                description="MICCAI 2023 Conference - Medical Image Computing and Computer Assisted Intervention",
                year=2023,
            ),
        ],
    ),
    Research(
        title="Generative AI for Drug Discovery",
        aims="Leverage large language models and generative AI to accelerate drug discovery process by predicting protein structures and generating novel molecular compounds.",
        year_start=2022,
        year_end=2024,
        sponsor="Horizon Europe",
        sponsor_url="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en",
        budget="€1,200,000",
        outputs=[
            Output(
                type=OutputType.PAPER,
                title="ProteinGPT: Large Language Models for Protein Structure Prediction",
                description="Published in Nature Machine Intelligence",
                url="https://doi.org/example",
                year=2023,
            ),
            Output(
                type=OutputType.PATENT,
                title="Method for Generating Novel Molecular Compounds Using AI",
                description="Patent No. EP123456",
                url="https://patent.example",
                year=2023,
            ),
            Output(
                type=OutputType.SOFTWARE,
                title="MoleculeGen",
                description="AI-powered molecular generation platform",
                url="https://github.com/moleculegen",
                year=2023,
            ),
        ],
    ),
    Research(
        title="Multimodal Learning for Healthcare",
        aims="Develop innovative multimodal learning approaches combining medical imaging, clinical notes, and genomic data for personalized medicine.",
        year_start=2021,
        year_end=2024,
        sponsor="National Science Foundation",
        sponsor_url="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en",
        budget="€500,000",
        outputs=[
            Output(
                type=OutputType.PAPER,
                title="MultiHealth: A Multimodal Deep Learning Framework for Healthcare",
                description="Published in Nature Methods",
                url="https://doi.org/example2",
                year=2022,
            ),
            Output(
                type=OutputType.SOFTWARE,
                title="HealthFusion",
                description="Framework for multimodal medical data fusion",
                url="https://github.com/healthfusion",
                year=2022,
            ),
            Output(
                type=OutputType.AWARD,
                title="Innovation Award",
                description="European Healthcare Innovation Awards 2022",
                year=2022,
            ),
        ],
    ),
    Research(
        title="Federated Learning for Privacy-Preserving Healthcare AI",
        aims="Design and implement federated learning systems for training medical AI models across multiple institutions while preserving patient privacy.",
        year_start=2020,
        year_end=2023,
        sponsor="EU Privacy Tech Grant",
        sponsor_url="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en",
        budget="€650,000",
        outputs=[
            Output(
                type=OutputType.PAPER,
                title="SecureHealth: Privacy-Preserving Federated Learning in Healthcare",
                description="Published in IEEE Transactions on Medical Imaging",
                url="https://doi.org/example3",
                year=2022,
            ),
            Output(
                type=OutputType.SOFTWARE,
                title="FedHealth",
                description="Open-source federated learning framework for healthcare",
                url="https://github.com/fedhealth",
                year=2021,
            ),
            Output(
                type=OutputType.PATENT,
                title="System for Privacy-Preserving Medical AI Training",
                description="Patent No. US987654",
                url="https://patent.example2",
                year=2022,
            ),
        ],
    ),
    Research(
        title="Explainable AI for Clinical Decision Support",
        aims="Develop interpretable AI models that provide transparent and explainable recommendations for clinical decision support systems.",
        year_start=2019,
        year_end=2022,
        sponsor="Medical Research Council",
        sponsor_url="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en",
        budget="€450,000",
        outputs=[
            Output(
                type=OutputType.PAPER,
                title="XAI-Med: Explainable AI Framework for Medical Decision Support",
                description="Published in JAMA Network Open",
                url="https://doi.org/example4",
                year=2021,
            ),
            Output(
                type=OutputType.SOFTWARE,
                title="ExplainMed",
                description="Toolkit for medical AI model interpretation",
                url="https://github.com/explainmed",
                year=2020,
            ),
            Output(
                type=OutputType.AWARD,
                title="Clinical Impact Award",
                description="International Conference on Healthcare Informatics 2021",
                year=2021,
            ),
        ],
    ),
]
