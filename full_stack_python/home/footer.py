import reflex as rx

# import ..components.links as Links
from ..components.styles import TextColor, Font, Size, Color
from ..navigation import routes
from datetime import datetime, timezone


class MomentState(rx.State):
    date_now: datetime = datetime.now(timezone.utc)

    @rx.event
    def update(self):
        self.date_now = datetime.now(timezone.utc)


def time_display() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            # Day of week
            #       rx.moment(
            #           format="dddd",  # Full day name (Monday, Tuesday, etc.)
            #           refresh=True,
            #           color=TextColor.PRIMARY.value,
            #           font_family="monospace",
            #           font_size=Size.DEFAULT.value,
            #       ),
            #       rx.text(
            #           " | ",
            #           color=TextColor.SECONDARY.value,
            #           font_size=Size.DEFAULT.value,
            #       ),
            #       # Date
            #       rx.moment(
            #           format="YYYY:MM:DD",
            #           refresh=True,
            #           color=TextColor.PRIMARY.value,
            #           font_family="monospace",
            #           font_size=Size.DEFAULT.value,
            #       ),
            #   ),
            #   rx.hstack(
            #       # Time
            #       rx.moment(
            #           format="HH:mm:ss",
            #           refresh=True,
            #           update_interval=1,
            #           color=TextColor.PRIMARY.value,
            #           font_family="monospace",
            #           font_size=Size.DEFAULT.value,
            #       ),
            #       rx.text(
            #           " | ",
            #           color=TextColor.SECONDARY.value,
            #           font_size=Size.DEFAULT.value,
            #       ),
            # Timezone
            rx.moment(
                MomentState.date_now,
                tz="Europe/Stockholm",
                refresh=True,
                color=TextColor.PRIMARY.value,
                font_family="monospace",
                font_size=Size.ABIT_BIG.value,
            ),
        ),
        align_items="start",
        spacing="1",
        padding_y="2",
    )


time_display_props = {
    "margin_top": "0em",  # Space above
    "margin_bottom": "0em",  # Space below
    "margin_x": "2em",  # Horizontal spacing
    "padding": "1em",  # Internal spacing
    "align_self": "center",  # Self alignment
    "width": "fit-content",  # Width adjustment        # Font size
}


def social_link(icon: str, url: str) -> rx.Component:
    """Create a social media link button."""
    return rx.link(
        rx.icon(
            icon,
            font_size="20px",
            color=TextColor.PRIMARY.value,
            _hover={"color": Color.ACCENT.value, "transform": "scale(1.1)"},
        ),
        href=url,
        is_external=True,
        transition="all 0.2s ease-in-out",
    )


def tech_badge(image: str, alt: str) -> rx.Component:
    """Create a technology badge."""
    return rx.image(
        src=image,
        alt=alt,
        height="30px",
        width="auto",
        opacity="0.8",
        _hover={"opacity": "1", "transform": "translateY(-2px)"},
        transition="all 0.2s ease-in-out",
    )


def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Divider line
            rx.divider(
                border_color=Color.SECONDARY.value,
                opacity="0.3",
                margin_y="1em",
            ),
            # Main footer content
            rx.hstack(
                # Left section - Copyright and Tech Stack
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "© 2024 Linh Duong",
                            font_family=Font.TITLES.value,
                            color=TextColor.PRIMARY.value,
                            font_size=Size.BIG.value,
                        ),
                        # rx.text(
                        #     " | ",
                        #     color=TextColor.SECONDARY.value,
                        #     font_size=Size.BIG.value,
                        # ),
                        rx.box(
                            time_display(),
                            **time_display_props,  # type: ignore
                        ),
                    ),
                    rx.hstack(
                        tech_badge("/techs/python.png", "Python"),
                        tech_badge("/techs/reflex.png", "Reflex"),
                        tech_badge("/techs/git.png", "Git"),
                    ),
                    align_items="start",
                    spacing="6",
                ),
                # Center section - Website info
                rx.box(
                    rx.text(
                        "Built with Reflex framework in Python",
                        color=TextColor.SECONDARY.value,
                        font_size=Size.ABIT_BIG.value,
                    ),
                    rx.link(
                        rx.hstack(
                            rx.text("View source code"),
                            rx.icon(
                                "arrow-up-right",
                                font_size=Size.ABIT_BIG.value,
                            ),
                            spacing="2",  # Added spacing
                            color=Color.ACCENT.value,
                            _hover={"text_decoration": "underline"},
                        ),
                        href=routes.PORTFOLIO_URL,
                        is_external=True,
                        font_size=Size.ABIT_BIG.value,
                    ),
                ),
                # Right section - Social links
                rx.hstack(
                    social_link("github", routes.GITHUB_URL),
                    social_link("linkedin", routes.LINKEDIN_URL),
                    social_link("twitter", routes.TWITTER_URL),
                    social_link("facebook", routes.FACEBOOK_URL),
                    spacing="2",  # Changed from "1.5em" to "4"
                ),
                justify_content="space-between",
                width="100%",
                padding_x="2",
                spacing="1",  # Added spacing
            ),
            padding_y="1",
            width="100%",
            max_width="1500px",
            margin="0 auto",
            spacing="1",  # Added spacing
        ),
        bg=Color.HOVER.value,
        border_top=f"1px solid {Color.SECONDARY.value}",
        padding_y="1",  # Reduced padding
        width="100%",
        border_radius="25px",
    )
