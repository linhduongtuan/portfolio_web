import reflex as rx
from reflex.style import set_color_mode, color_mode

# import ..components.links as Links
from ..navigation import routes as Links
from ..components.styles import Color, Size, TextColor
# from reflex.style import toggle_color_mode


background_base_style = dict(
    bg=rx.color_mode_cond(light=Color.FEATURED.value, dark=Color.HOVER.value),
)

background_button_style = dict(
    bg=rx.color_mode_cond(light=Color.FEATURED.value, dark=Color.HOVER.value),
    color=rx.color_mode_cond(
        light=TextColor.SECONDARY.value, dark=TextColor.SECONDARY.value
    ),
    box_shadow=rx.color_mode_cond(
        light="2px 2px 4px #c5c5c5,-2px -2px 4px #ffffff",
        dark="2px 2px 4px #000,-2px -2px 4px #222222",
    ),
    _hover={
        "border_style": "solid",
        "border_width": "1px",
        "border_color": Color.PRIMARY.value,
        "text_decoration": "none",
    },
)


def is_current_page(page_route: str) -> rx.Var:
    """Check if the given route is currently active."""
    return rx.State.router.page.path == page_route  # type: ignore


def dark_mode_toggle() -> rx.Component:
    return rx.segmented_control.root(
        rx.segmented_control.item(
            rx.icon(tag="monitor", size=20),
            value="system",
        ),
        rx.segmented_control.item(
            rx.icon(tag="sun", size=20),
            value="light",
        ),
        rx.segmented_control.item(
            rx.icon(tag="moon", size=20),
            value="dark",
        ),
        on_change=set_color_mode,
        variant="classic",
        radius="large",
        value=color_mode,
    )


def contact_menu_item(icon: str, text: str, href: str) -> rx.Component:
    """Create a contact menu item with hover effects."""
    return rx.menu.item(
        rx.link(
            rx.hstack(
                rx.icon(icon),
                rx.text(text),
            ),
            href=href,
            is_external=True,
            width="100%",
            text_decoration="none",
            color=TextColor.HOVER.value,
            _hover={
                "color": TextColor.FEATURED.value,
                "background": Color.SECONDARY.value,
            },
        ),
    )


def highlighted_button_menu(
    icon: str, text: str, route: str, is_external: bool
) -> rx.Component:
    """Create a button with highlight effect for active page."""
    button_content = rx.hstack(
        rx.icon(icon),
        rx.text(text) if text else rx.fragment(),
    )

    if is_external:
        return rx.link(
            button_content,
            href=route,
            is_external=True,
            text_decoration="none",
            _hover={
                "text_decoration": "none",
                "transform": "scale(1.05)",
            },
        )

    return rx.cond(
        is_current_page(route),
        rx.button(
            button_content,
            variant="solid",
            size="4",
            bg=Color.ACCENT.value,
            color=TextColor.SECONDARY.value,
            on_click=rx.redirect(route),
            _hover={
                "bg": Color.HOVER.value,
                "transform": "scale(1.05)",
            },
        ),
        rx.button(
            button_content,
            variant="soft",
            size="4",
            bg="transparent",
            color=TextColor.PRIMARY.value,
            on_click=rx.redirect(route),
            _hover={
                "bg": Color.HOVER.value,
                "transform": "scale(1.05)",
            },
        ),
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.avatar(
                src="/avatar.png",
                fallback="GSA",
                color_scheme="indigo",
                radius="full",
                border=f"solid, 2px, {Color.PRIMARY.value}",
                size="3",
                spacing="3",
            ),
            rx.heading(
                "Linh Duong's portfolio",
                color=TextColor.PRIMARY.value,
            ),
            rx.spacer(),
            highlighted_button_menu("HOME", "HOME", Links.HOME_ROUTE, False),
            highlighted_button_menu(
                "layout-dashboard", "RESEARCH", Links.RESEARCH_ROUTE, False
            ),
            highlighted_button_menu(
                "book", "PUBLICATION", Links.PUBLICATIONS_ROUTE, False
            ),
            highlighted_button_menu("pen", "BLOG", Links.BLOG, False),
            highlighted_button_menu("user", "ABOUT", Links.ABOUT_US_ROUTE, False),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("CONTACT ME", variant="soft", size="4"),
                ),
                rx.menu.content(
                    contact_menu_item("github", "GITHUB", Links.GITHUB_URL),
                    contact_menu_item(
                        "graduation-cap", "GOOGLE SCHOLAR", Links.GOOGLE_SCHOLAR_URL
                    ),
                    contact_menu_item(
                        "book-open", "RESEARCHGATE", Links.RESEARCHGATE_URL
                    ),
                    contact_menu_item("fingerprint", "ORCID", Links.ORCID_URL),
                    contact_menu_item("linkedin", "LINKEDIN", Links.LINKEDIN_URL),
                    contact_menu_item("twitter", "TWITTER/X", Links.TWITTER_URL),
                    contact_menu_item("facebook", "FACEBOOK", Links.FACEBOOK_URL),
                    contact_menu_item("mail", "EMAIL", Links.EMAIL_URL),
                    padding="0.5em",
                ),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Search ...",
                type="search",
                size="3",
                justify="end",
            ),
            dark_mode_toggle(),
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        padding_x=Size.MEDIUM.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        border=f"3px solid {Color.SECONDARY.value}",
        top="0",
        width="100%",
    )
