import reflex as rx
from portfolio_web.components.styles import TextColor
from portfolio_web.pages.navbar import navbar
from portfolio_web.pages.footer import footer
from portfolio_web.data.contents import blog_posts


def blog_post():
    """Display a single blog post based on the id."""
    post_id = rx.get_query_params().get("id", "")
    # Find the post with the matching id
    post = next((p for p in blog_posts if p.id == post_id), None)
    if not post:
        return rx.box(
            navbar(),
            rx.center(
                rx.text("Post not found", color=TextColor.PRIMARY.value),
                padding="2em",
            ),
            footer(),
        )
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading(
                    post.title,
                    font_weight="bold",
                    font_size="2em",
                    color=TextColor.PRIMARY.value,
                    align_self="center",
                    padding_top="1em",
                ),
                rx.text(
                    f"Date: {post.date} | Reading Time: {post.reading_time}",
                    color=TextColor.SECONDARY.value,
                    font_size="0.9em",
                    align_self="center",
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
                    align_self="center",
                ),
                # Full content
                rx.text(
                    post.content,
                    color=TextColor.PRIMARY.value,
                    font_size="1em",
                    padding_top="1em",
                ),
            ),
            padding="2em",
        ),
        footer(),
    )
