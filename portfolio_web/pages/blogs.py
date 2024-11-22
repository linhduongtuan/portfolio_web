# pages/blogs.py
import reflex as rx
from portfolio_web.components.styles import TextColor


def blog_post_item(post: BlogPost) -> rx.Component:
    """Create a blog post item with link to full post."""
    return rx.link(
        rx.box(
            rx.hstack(
                rx.text("•", color=TextColor.PRIMARY.value),
                rx.vstack(
                    # Date and reading time
                    rx.hstack(
                        rx.text(
                            post.date,
                            color=TextColor.SECONDARY.value,
                            font_size="0.9em",
                        ),
                        rx.spacer(),
                        rx.text(
                            f"☕ {post.reading_time} read",
                            color=TextColor.SECONDARY.value,
                            font_size="0.9em",
                        ),
                    ),
                    # Title
                    rx.heading(
                        post.title,
                        font_weight="bold",
                        color=TextColor.PRIMARY.value,
                        font_size="1.2em",
                    ),
                    # Tags
                    rx.hstack(
                        *[
                            rx.badge(
                                tag,
                                color_scheme="teal",
                                variant="soft",
                                margin="2px",
                            )
                            for tag in post.tags
                        ],
                        spacing="2",
                        flex_wrap="wrap",
                    ),
                    # Preview text
                    rx.text(
                        post.preview,
                        color=TextColor.SECONDARY.value,
                        font_style="italic",
                    ),
                    align_items="start",
                    width="100%",
                ),
                width="100%",
            ),
            padding="1em",
            border_radius="0.5em",
            _hover={
                "bg": "rgba(255, 255, 255, 0.1)",
                "transform": "translateY(-2px)",
            },
            transition="all 0.2s ease-in-out",
        ),
        href=f"/blog/{post.id}",
        text_decoration="none",
        width="100%",
    )
