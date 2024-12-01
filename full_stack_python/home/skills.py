import reflex as rx
from typing import List
from ..components.styles import (
    Size,
    MAX_WIDTH_SKILLS,
    Color,
    TextColor,
    Font,
)


# Class to add each soft skill's images and descriptions
class ForeachState(rx.State):
    softskills: dict[str, str] = {
        # I can put all this text in a txt, so as not to leave it in code
        "teamwork": "First of all, I need a long text where I talk about how that softskill was used in a previous experience, such as in a project or in a job and if I have/use/possess it,",
        "leadership": "two, I need a long text where I talk about how that softskill was used in a previous experience, such as in a project or in a job and if I have/use/possess it",
        "conflict_management": "three, I need a long text where I talk about how that softskill was used in a previous experience, such as in a project or in a job and if I have/use/possess it",
        "time_management": "four, I need a long text where I talk about how that softskill was used in a previous experience, such as in a project or in a job and if I have/use/possess it",  # time normalization with three point estimation
        "adaptability": "five, I need a long text where I talk about how that softskill was used in a previous experience previous, such as in a project or in a job and that if I have/use/possess it",
        "communication": "six, I need a long text where I talk about how that softskill was used in a previous experience, such as in a project or in a job and that if I have/use/possess it",
        "continuos_learning": "seven, I need a long text where I talk about how that softskill was used in a previous experience, such as in a project or in a job and that if I have/use/possess it",
        "creativity": "eight, I need a long text where I talk about how that softskill was used in a previous experience, such as in a project or in a job and that if I have/use/possess it",
        "problem_solving": "nine, I need a long text where I talk about how that softskill was used in a previous experience, such as in a project or in a job and that if I have/use/possess it",
        # 'critical_thinking'
    }


# Create the list boxes passing the dict as a list.
def grid_dict(skill: List):
    return rx.box(
        rx.hstack(
            rx.image(
                src=f"/skills/{skill[0]}.png",
                width=rx.breakpoints(
                    xs=Size.VERY_BIG.value,
                    md=Size.GARGANTUAL.value,
                    lg=Size.COLOSAL.value,
                ),
                height="auto",
            ),
            rx.text(skill[1]),
        ),
        padding=Size.DEFAULT.value,
    )


# Function that is sent to the main to execute, Contains the logos and description
def skills():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Abilities & Softskills",
                    style={"font_family": Font.TITLES.value},  # type: ignore
                    font_size=Size.VERY_BIG.value,
                    padding_top=Size.DEFAULT.value,
                ),
                rx.grid(
                    rx.foreach(ForeachState.softskills, grid_dict),
                    columns=rx.breakpoints(xs="1", md="2", lg="3"),
                ),
                rx.hstack(
                    rx.spacer(),
                    rx.text(
                        "*This section has been designed using resources from Flaticon.com",
                        color=TextColor.SECONDARY.value,
                        padding_y=Size.DEFAULT.value,
                    ),
                    width="100%",
                ),
                style=MAX_WIDTH_SKILLS,  # type: ignore
            )
        ),
        bg=Color.TERTIARY.value,
        padding=Size.DEFAULT.value,
        width="100%",
        border_radius="25px",
    )
