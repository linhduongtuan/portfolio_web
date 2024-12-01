import reflex as rx
from ..components.styles import Size, MAX_WIDTH, Color, TextColor, Font
from ..navigation.routes import ABOUT_US_ROUTE


def bio() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Header Section
            rx.hstack(
                rx.heading(
                    "MY BRIEF BIOGRAPHY",
                    style={"font_family": Font.TITLES.value},  # type: ignore
                    font_size=Size.BIG.value,
                    color=TextColor.PRIMARY.value,
                ),
                rx.spacer(),
                rx.link(
                    rx.button(
                        "Tell me more...",
                        rx.icon("book-open"),
                    ),
                    color=TextColor.SECONDARY.value,
                    href=ABOUT_US_ROUTE,
                    is_external=False,
                ),
                #   href=Links.GOOGLE_SCHOLAR_URL,
                padding_right=Size.BIG.value,
                width="100%",
            ),
            # Introduction Text
            rx.text(
                "I am Linh Duong, a Ph.D. in Biotechnology currently working as a postdoctoral researcher at KTH Royal Institute of Technolog. "
                "My passion lies in understanding the molecular mechanisms of bacterial pathogenesis and host-pathogen interactions.",
                color=TextColor.SECONDARY.value,
                padding_lseft=Size.MEDIUM.value,
                style={"list_style_type": "disc"},  # type: ignore
                font_size=Size.ABIT_BIG.value,
            ),
            # Subheading: Research Interests
            rx.heading(
                "My Research Interests:",
                font_size=Size.LIGHT_BIG.value,
                color=TextColor.PRIMARY.value,
                padding_top=Size.SMALL.value,
            ),
            # Bullet List of Research Interests
            rx.unordered_list(
                rx.list_item("Investigating bacterial virulence factors"),
                rx.list_item("Studying bacterial and cellular physiology"),
                rx.list_item("Exploring cellular signaling pathway interactions"),
                rx.list_item("Elucidating the microbiome's role in health and disease"),
                color=TextColor.SECONDARY.value,
                padding_lseft=Size.MEDIUM.value,
                style={"list_style_type": "disc"},  # type: ignore
                font_size=Size.ABIT_BIG.value,
            ),
            # Subheading: Computational Biology Leveraging
            rx.heading(
                "Computational Biology Expertise:",
                font_size=Size.LIGHT_BIG.value,
                color=TextColor.PRIMARY.value,
                padding_top=Size.SMALL.value,
            ),
            # Bullet List of Computational Biology Applications
            rx.unordered_list(
                rx.list_item("Analyzing genetic data"),
                rx.list_item("Developing predictive models"),
                rx.list_item("Studying non-communicable diseases"),
                rx.list_item(
                    "Applying machine learning to biological data and medical images"
                ),
                color=TextColor.SECONDARY.value,
                padding_lseft=Size.MEDIUM.value,
                style={"list_style_type": "disc"},  # type: ignore
                font_size=Size.ABIT_BIG.value,
            ),
            # Subheading: Data Science Applications
            rx.heading(
                "Data analysis:",
                font_size=Size.LIGHT_BIG.value,
                color=TextColor.PRIMARY.value,
                padding_top=Size.SMALL.value,
            ),
            # Bullet List of Computational Biology Applications
            rx.unordered_list(
                rx.list_item("Conducting epidemiological data analysis"),
                rx.list_item("Developing time-series prediction models"),
                rx.list_item("Researching communicable diseases"),
                rx.list_item("Implementing deep learning for bio-image analysis"),
                color=TextColor.SECONDARY.value,
                padding_lseft=Size.MEDIUM.value,
                style={"list_style_type": "disc"},  # type: ignore
                font_size=Size.ABIT_BIG.value,
            ),
        ),
        bg=Color.SECONDARY.value,
        padding=Size.BIG.value,
        border_radius="25px",
        style=MAX_WIDTH,  # type: ignore
    )
