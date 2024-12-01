import reflex as rx
from ..components.styles import Size, TextColor


def button_menu(icon: str, name: str, url: str, ext: bool) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.box(
                # class_name=f"fa fa-{icon}",
                display=["flex", "flex", "flex", "flex", "flex"]
                if ext
                else ["flex", "flex", "none", "flex", "flex"],
                margin_right="0.5rem",
            ),
            rx.text(
                name.upper(),
                display=["none", "none", "none", "flex", "flex"]
                if ext
                else ["none", "none", "flex", "flex", "flex"],
            ),
        ),
        href=url,
        is_external=ext,
        class_name="navbar-item",
        style=rx.Style(
            {
                "text-decoration": "none",
                "color": TextColor.PRIMARY.value,
                "padding": "0.5rem",
                "border-radius": "5px",
            },
        ),
    )


# Create the footer buttons
def button_footer(icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.box(class_name=f"fa fa-{icon}"),
        href=url,
        is_external=True,
        size="8",
        # class_name='shake',
        color=TextColor.PRIMARY.value,
        padding_right=Size.SMALL.value,
    )
