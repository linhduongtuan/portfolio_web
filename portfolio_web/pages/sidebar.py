import reflex as rx
from navbar import navbar


# Add state management for sidebar visibility
class SidebarState(rx.State):
    show_sidebar: bool = True

    def toggle_sidebar(self):
        self.show_sidebar = not self.show_sidebar


def collapsible_sidebar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Toggle button
            rx.button(
                rx.cond(
                    SidebarState.show_sidebar,
                    rx.icon("chevron-left"),
                    rx.icon("chevron-right"),
                ),
                on_click=SidebarState.toggle_sidebar,
                position="fixed",
                left=rx.cond(
                    SidebarState.show_sidebar,
                    "15em",  # When sidebar is shown
                    "1em",  # When sidebar is hidden
                ),
                top="1em",
                z_index="999",
                size="sm",
                border_radius="full",
            ),
            # Sidebar content with animation
            rx.cond(
                SidebarState.show_sidebar,
                rx.box(
                    rx.desktop_only(
                        rx.vstack(
                            # ... your existing sidebar content ...
                            sidebar_bottom_profile(),
                            width="16em",
                            height="100vh",
                            position="fixed",
                            left="0px",
                            top="0px",
                            bg=rx.color("accent", 3),
                            padding_x="1em",
                            padding_y="1.5em",
                            transition="all 0.3s ease-in-out",
                        ),
                    ),
                    rx.mobile_and_tablet(
                        # ... your existing mobile sidebar content ...
                    ),
                ),
                rx.box(
                    width="0em",
                    transition="all 0.3s ease-in-out",
                ),
            ),
        ),
        width=rx.cond(
            SidebarState.show_sidebar,
            "16em",  # Sidebar width when shown
            "0em",  # Sidebar width when hidden
        ),
        transition="all 0.3s ease-in-out",
    )


style = {
    "transition": "all 0.3s ease-in-out",
    "box-shadow": "2px 0 10px rgba(0,0,0,0.1)",
    "_hover": {
        "box-shadow": "2px 0 15px rgba(0,0,0,0.15)",
    },
}

button_style = {
    "background": "white",
    "box_shadow": "0 2px 5px rgba(0,0,0,0.1)",
    "_hover": {
        "background": rx.color("accent", 2),
        "box_shadow": "0 2px 8px rgba(0,0,0,0.15)",
    },
    "transition": "all 0.2s ease",
}


# Update your main layout
def index() -> rx.Component:
    return rx.hstack(
        collapsible_sidebar(),
        rx.box(
            # Your main content
            flex="1",
            padding="1em",
            margin_left=rx.cond(
                SidebarState.show_sidebar,
                "16em",  # Push content when sidebar is shown
                "0em",  # No margin when sidebar is hidden
            ),
            transition="all 0.3s ease-in-out",
        ),
        width="100%",
        spacing="0",
    )


def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            # style={
            #     "_hover": {
            #         "bg": rx.color("accent", 4),
            #         "color": rx.color("accent", 11),
            #     },
            #     "border-radius": "0.5em",
            # },
            # style=[style, button_style],
            style=button_style,
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", "/#"),
        sidebar_item("Projects", "square-library", "/#"),
        sidebar_item("Analytics", "bar-chart-4", "/#"),
        sidebar_item("Messages", "mail", "/#"),
        spacing="1",
        width="100%",
    )


def app_layout() -> rx.Component:
    return rx.box(
        rx.hstack(
            collapsible_sidebar(),
            rx.box(
                # Your main content components
                navbar(),
                rx.box(
                    # Page content
                    padding="2em",
                ),
                flex="1",
                margin_left=rx.cond(SidebarState.show_sidebar, "16em", "0em"),
                transition="all 0.3s ease-in-out",
            ),
            width="100%",
            spacing="0",
        ),
        width="100%",
    )


def sidebar_bottom_profile() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/avatar.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="7", weight="bold"),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                rx.spacer(),
                rx.vstack(
                    rx.vstack(
                        sidebar_item("Settings", "settings", "/#"),
                        sidebar_item("Log out", "log-out", "/#"),
                        spacing="1",
                        width="100%",
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.icon_button(
                            rx.icon("user"),
                            size="3",
                            radius="full",
                        ),
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    "My account",
                                    size="3",
                                    weight="bold",
                                ),
                                rx.text(
                                    "user@reflex.dev",
                                    size="2",
                                    weight="medium",
                                ),
                                width="100%",
                            ),
                            spacing="0",
                            align="start",
                            justify="start",
                            width="100%",
                        ),
                        padding_x="0.5rem",
                        align="center",
                        justify="start",
                        width="100%",
                    ),
                    width="100%",
                    spacing="5",
                ),
                spacing="5",
                # position="fixed",
                # left="0px",
                # top="0px",
                # z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("accent", 3),
                align="start",
                # height="100%",
                height="650px",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(rx.icon("align-justify", size=30)),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(rx.icon("x", size=30)),
                                width="100%",
                            ),
                            sidebar_items(),
                            rx.spacer(),
                            rx.vstack(
                                rx.vstack(
                                    sidebar_item(
                                        "Settings",
                                        "settings",
                                        "/#",
                                    ),
                                    sidebar_item(
                                        "Log out",
                                        "log-out",
                                        "/#",
                                    ),
                                    width="100%",
                                    spacing="1",
                                ),
                                rx.divider(margin="0"),
                                rx.hstack(
                                    rx.icon_button(
                                        rx.icon("user"),
                                        size="3",
                                        radius="full",
                                    ),
                                    rx.vstack(
                                        rx.box(
                                            rx.text(
                                                "My account",
                                                size="3",
                                                weight="bold",
                                            ),
                                            rx.text(
                                                "user@reflex.dev",
                                                size="2",
                                                weight="medium",
                                            ),
                                            width="100%",
                                        ),
                                        spacing="0",
                                        justify="start",
                                        width="100%",
                                    ),
                                    padding_x="0.5rem",
                                    align="center",
                                    justify="start",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="5",
                            ),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )


class State(rx.State):
    """Base state for the app."""

    is_sidebar_expanded: bool = True

    def toggle_sidebar(self):
        self.is_sidebar_expanded = not self.is_sidebar_expanded


def sidebar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Sidebar content
            rx.box(
                sidebar_bottom_profile(),
                width="16em",
                height="100vh",
                position="fixed",
                left=rx.cond(State.is_sidebar_expanded, "0em", "-16em"),
                top="0",
                bg=rx.color("accent", 3),
                padding_x="1em",
                padding_y="1.5em",
                transition="all 0.3s ease-in-out",
                z_index="998",
            ),
            # Toggle button
            rx.button(
                rx.cond(
                    State.is_sidebar_expanded,
                    rx.icon("chevron-left"),
                    rx.icon("chevron-right"),
                ),
                on_click=State.toggle_sidebar,
                position="fixed",
                left=rx.cond(State.is_sidebar_expanded, "15em", "1em"),
                top="5em",
                z_index="999",
                bg="white",
                shadow="lg",
                border_radius="full",
                size="sm",
            ),
        ),
    )


def layout(content: rx.Component) -> rx.Component:
    return rx.box(
        navbar(),
        rx.hstack(
            sidebar(),
            rx.box(
                content,
                width="100%",
                margin_left=rx.cond(State.is_sidebar_expanded, "16em", "0em"),
                transition="all 0.3s ease-in-out",
                min_height="100vh",
            ),
            width="100%",
            spacing="0",
        ),
    )
