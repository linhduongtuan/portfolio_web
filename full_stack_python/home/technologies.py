import reflex as rx
from typing import List
from ..components.styles import Size, Color, TextColor, Font


# Class to add images of the technologies I know
class ForeachState(rx.State):
    frontend: List[str] = ["reflex"]

    backend: List[str] = [
        "Python",
        "R",
    ]

    tools: List[str] = [
        "Markdown",
        "Git",
        "GitHub",
    ]


# Creates the boxes with the images of each list
def logos(logo: str):
    return rx.card(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(src=f"techs/{logo}.png", width="60px", height="auto"),
                    rx.text.strong(logo, color="#000000"),
                    align="center",
                ),
                bg_color=Color.TERTIARY.value,
                height="100px",
                width="100px",
                border_radius="25%",
            )
        ),
        padding=Size.DEFAULT.value,
        variant="ghost",
    )


# Function that is sent to the main to execute, contains the logos
def technologies():
    return rx.vstack(
        rx.heading(
            "Technologies",
            style={"font_family": Font.TITLES.value},  # type: ignore
            font_size=Size.VERY_BIG.value,
            padding_top=Size.BIG.value,
            padding_bottom=Size.SMALL.value,
            color=TextColor.TERTIARY.value,
        ),
        rx.text("Backend & Database:", color=TextColor.TERTIARY.value),
        rx.grid(
            rx.foreach(ForeachState.backend, logos),
            columns=rx.breakpoints(initial="3", xs="4", sm="5", md="8", lg="9"),
        ),
        rx.text("Frontend:", color=TextColor.TERTIARY.value),
        rx.grid(
            rx.foreach(ForeachState.frontend, logos),
            columns=rx.breakpoints(initial="3", xs="4", sm="5", md="8", lg="9"),
        ),
        rx.text("Tools & Methodologies:", color=TextColor.TERTIARY.value),
        rx.grid(
            rx.foreach(ForeachState.tools, logos),
            columns=rx.breakpoints(initial="3", xs="4", sm="5", md="8", lg="9"),
        ),
        padding_bottom=Size.COLOSAL.value,
    )
