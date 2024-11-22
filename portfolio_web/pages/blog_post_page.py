# portfolio_web/pages/blog_post_page.py
import reflex as rx
from typing import Optional
from portfolio_web.components.styles import TextColor
from portfolio_web.pages.blog_page import BlogPost
from portfolio_web.pages.navbar import navbar
from portfolio_web.pages.footer import footer
from portfolio_web.data.contents import blog_posts
from portfolio_web.pages.state import enhanced_comment_section
from portfolio_web.data.contents import blog_posts, BlogPost
from portfolio_web.pages.state import enhanced_comment_section


class BlogState(rx.State):
    """State for blog functionality."""

    current_id: Optional[str] = None  # Changed from post_id to current_id

    def get_post(self) -> Optional[BlogPost]:
        """Get the current blog post."""
        if not self.current_id:
            return None
        return next((post for post in blog_posts if post.id == self.current_id), None)

    def set_current_id(self, id: str):
        """Set the current post ID."""
        self.current_id = id


@rx.page(route="/blog/post/[id]")  # Changed from post_id to id
def blog_post_page(id: Optional[str] = None) -> rx.Component:  # Changed parameter name
    """Display a single blog post."""
    # Find the post directly
    post = next((p for p in blog_posts if p.id == id), None)

    if not post:
        return rx.box(
            navbar(),
            rx.center(
                rx.vstack(
                    rx.heading(
                        "Select a Blog Post", size="xl", color=TextColor.PRIMARY.value
                    ),
                    rx.text(
                        "Choose from our available posts:",
                        color=TextColor.SECONDARY.value,
                    ),
                    rx.vstack(
                        *[
                            rx.link(
                                f"• {p.title}",
                                href=f"/blog/post/{p.id}",
                                color=TextColor.SECONDARY.value,
                                _hover={"color": TextColor.PRIMARY.value},
                            )
                            for p in blog_posts
                        ],
                        rx.divider(margin_y="8"),
                        # comment_section(),  # or
                        enhanced_comment_section(),
                        align_items="start",
                        margin_top="1",
                        spacing="1",
                    ),
                    padding="2em",
                ),
            ),
            footer(),
        )

    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading(
                    post.title,
                    size="xl",
                    color=TextColor.PRIMARY.value,
                ),
                rx.hstack(
                    rx.text(
                        f"📅 {post.date}",
                        color=TextColor.SECONDARY.value,
                        font_size="sm",
                    ),
                    rx.text(
                        f"☕ {post.reading_time}",
                        color=TextColor.SECONDARY.value,
                        font_size="sm",
                    ),
                    spacing="4",
                ),
                rx.wrap(
                    *[
                        rx.badge(
                            tag,
                            color_scheme="teal",
                            variant="soft",
                            margin="2px",
                        )
                        for tag in post.tags
                    ],
                ),
                rx.box(
                    rx.markdown(post.content),
                    width="100%",
                    padding_y="2em",
                ),
                *[
                    rx.code_block(
                        block.code,
                        language=block.language,
                        theme="dark",
                    )
                    for block in post.code_blocks
                ],
                width="100%",
                max_width="800px",
                padding="2em",
                spacing="4",
            ),
        ),
        footer(),
    )


def blog_post_item(post: BlogPost) -> rx.Component:
    """Create a blog post preview item."""
    return rx.link(
        rx.box(
            rx.vstack(
                rx.heading(post.title),
                rx.text(post.preview),
                rx.wrap(
                    *[
                        rx.badge(
                            tag,
                            color_scheme="teal",
                            variant="soft",
                            margin="2px",
                        )
                        for tag in post.tags
                    ],
                ),
                align_items="start",
                padding="1",
            ),
            _hover={"bg": "rgba(255, 255, 255, 0.1)"},
        ),
        href=f"/blog/post/{post.id}",
        key=post.id,
    )
