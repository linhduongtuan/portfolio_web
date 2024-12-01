import reflex as rx
from ..components.styles import Size, MAX_WIDTH, Color, TextColor, Font
from ..navigation.routes import ABOUT_US_ROUTE


# HEADER, Name with photo on the side and relevant links
def header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading(
                "My name is",
                style={"font_family": Font.NOTES.value},  # type: ignore
                padding_top=Size.TINY.value,
                font_size=Size.BIG.value,
                color=TextColor.PRIMARY.value,
            ),
            rx.heading(
                "Linh Duong",
                padding_top=Size.SMALL.value,
                font_size=Size.VERY_BIG.value,
                color=TextColor.PRIMARY.value,
                class_name="animate__animated animate__heartBeat animate__slower --animate-delay: 10s",
                # Make the name appear, using Animate.css
            ),
            rx.text(
                "I want to be like a ",
                rx.link("Dolphin", href=ABOUT_US_ROUTE, is_external=False),
                " who learned to code.",
                font_size=Size.DEFAULT.value,
                padding_y=Size.DEFAULT.value,
                as_="p",
                color=TextColor.PRIMARY.value,
            ),
            rx.hstack(
                rx.text("Email:"),
                # rx.image(
                #     src='/email.png',
                #     width='auto',
                #     height=Size.DEFAULT.value
                # ),
                rx.box(  # ***I change it to an image, to avoid scavengers***
                    rx.text(" linhduongtuan@gmail.com "),
                    border=f"solid, 3px, {Color.SECONDARY.value}",
                ),
                rx.link(
                    rx.icon(
                        "copy",
                        on_click=rx.set_clipboard("linhduongtuan@gmail.com"),
                        # Copy the email to the clipboard when clicking
                    )
                ),
                color=TextColor.SECONDARY.value,
                padding_top=Size.DEFAULT.value,
            ),
            rx.hstack(
                rx.text(
                    "Download my Scientific CV",
                    font_size=Size.LIGHT_BIG.value,
                ),
                rx.link(
                    rx.icon(
                        "download",
                        on_click=rx.download(url="/Linh_Duong_CV_20241111.pdf"),
                        # Download my CV.pdf
                    )
                ),
                color=TextColor.SECONDARY.value,
                padding_top=Size.ZERO.value,
            ),
            padding_left=Size.COLOSAL.value,
        ),
        rx.image(
            # src='Linh_2540.jpg',
            # src="avatar_1.png",
            src="avatar.png",
            # width=['12em','14em','16em','18em','20em'],
            width="400px",
            height="auto",
            border_radius="5%",
        ),
        bg=Color.PRIMARY.value,
        padding=Size.BIG.value,
        border_radius="25px",
        style=MAX_WIDTH,  # type: ignore
    )
