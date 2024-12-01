import reflex as rx
from typing import List, Dict
from ..components.styles import Size, MAX_WIDTH, Color, TextColor, Font
from ..navigation import routes as Links


class ProjectState(rx.State):
    """State management for the project carousel."""

    current_index: int = 0

    # Define projects as a class variable
    projects: List[Dict[str, str]] = [
        {
            "id": "portfolio",
            "title": "Portfolio Website",
            "tech": "Built with Python using Reflex framework",
            "description": "A personal portfolio website showcasing my work as a developer, research experience, and completed projects.",
            "link": "https://github.com/linhduongtuan/portfolio_web",
            "image": "/avatar_1.png",
        },
        {
            "id": "bioimage",
            "title": "Biomedical Image Analysis",
            "tech": "Built with Python using PyTorch and TensorFlow",
            "description": "Deep learning models for biomedical image analysis, including cell segmentation and classification.",
            "link": "https://github.com/linhduongtuan/bioimage-analysis",
            "image": "/avatar.png",
        },
    ]

    def next_project(self):
        """Move to next project."""
        if self.current_index < len(self.projects) - 1:
            self.current_index += 1
        else:
            self.current_index = 0

    def prev_project(self):
        """Move to previous project."""
        if self.current_index > 0:
            self.current_index -= 1
        else:
            self.current_index = len(self.projects) - 1

    @rx.var
    def current_title(self) -> str:
        return self.projects[self.current_index]["title"]

    @rx.var
    def current_tech(self) -> str:
        return self.projects[self.current_index]["tech"]

    @rx.var
    def current_description(self) -> str:
        return self.projects[self.current_index]["description"]

    @rx.var
    def current_link(self) -> str:
        return self.projects[self.current_index]["link"]

    @rx.var
    def current_image(self) -> str:
        return self.projects[self.current_index]["image"]


def project() -> rx.Component:
    """Render the project carousel."""
    return rx.box(
        rx.vstack(
            # Header
            rx.hstack(
                rx.heading(
                    "Projects and Research",
                    style={"font_family": Font.TITLES.value},  # type: ignore
                    font_size=Size.BIG.value,
                    color=TextColor.PRIMARY.value,
                ),
                rx.spacer(),
                rx.link(
                    rx.button("View all projects"),
                    href=Links.PROJECTS_ROUTE,
                    is_external=False,
                ),
                width="100%",
                padding_bottom="4",
            ),
            # Carousel
            rx.hstack(
                rx.button(
                    rx.icon("chevron-left", size=20),
                    on_click=ProjectState.prev_project,
                    variant="ghost",
                ),
                rx.box(
                    rx.vstack(
                        rx.image(
                            src=ProjectState.current_image,
                            width="100%",
                            height="auto",
                            border_radius="md",
                        ),
                        rx.heading(
                            ProjectState.current_title,
                            size="lg",  # type: ignore
                            margin_y="4",
                        ),
                        rx.text(
                            ProjectState.current_tech, color=TextColor.SECONDARY.value
                        ),
                        rx.text(ProjectState.current_description),
                        rx.link(
                            rx.button("View Project"),
                            href=ProjectState.current_link,
                            is_external=True,
                        ),
                        padding="4",
                        spacing="4",
                        align_items="start",
                    ),
                    width="100%",
                    padding_x="4",
                ),
                rx.button(
                    rx.icon("chevron-right", size=20),
                    on_click=ProjectState.next_project,
                    variant="ghost",
                ),
                width="100%",
                align_items="center",
            ),
        ),
        bg=Color.SECONDARY.value,
        padding=Size.BIG.value,
        border_radius="25px",
        style=MAX_WIDTH,  # type: ignore
        margin_top="2em",
        margin_x="auto",
        width="100%",
    )
