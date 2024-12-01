import reflex as rx
from ..navigation import routes as Links
from ..components.styles import Size, MAX_WIDTH, Color, TextColor, Font


def experience() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Work Experience",
                style={"font_family": Font.TITLES.value},  # type: ignore
                font_size=Size.BIG.value,
                color=TextColor.PRIMARY.value,
            ),
            rx.text(
                "I have been working in the field of molecular biology for over 20 years. "
                "Most of my work has been in the field of bacterial pathogenesis and host-pathogen interactions. I have experience in the following areas:",
                color=TextColor.SECONDARY.value,
                padding=Size.MEDIUM.value,
                size=Size.ABIT_BIG.value,  # type: ignore
            ),
            rx.hstack(
                rx.button(
                    "Download CV",
                    on_click=rx.download(url="/downloads/Linh_Duong_CV_20241111.pdf"),
                    size="3",
                    class_name="experience-button",  # Added class for styling
                ),
                rx.button(
                    "View on",
                    rx.icon("github"),
                    rx.html(
                        ""
                        # className="fab fa-github",
                        # aria_label="GitHub Profile",
                        # style={'margin-right': '0.0rem'}  # Adds spacing between text and icon
                    ),
                    href=Links.GITHUB_URL,
                    is_external=True,
                    size="3",
                    class_name="experience-button",  # Added class for styling
                ),
            ),
        ),
        bg=Color.SECONDARY.value,
        padding=Size.BIG.value,
        border_radius="25px",
        style=MAX_WIDTH,  # type: ignore
    )
