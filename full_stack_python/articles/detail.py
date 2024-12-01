import reflex as rx

from ..ui.base import base_page

from . import state

from ..blog.notfound import blog_post_not_found


def article_detail_page() -> rx.Component:
    my_child = rx.cond(
        state.ArticlePublicState.post,
        rx.vstack(
            rx.hstack(
                rx.heading(state.ArticlePublicState.post.title, size="9"), # type: ignore
                align="end",  # type: ignore
            ),
            rx.text("By ", state.ArticlePublicState.post.userinfo.user.username),  # type: ignore
            rx.text(state.ArticlePublicState.post.publish_date),  # type: ignore
            rx.text(state.ArticlePublicState.post.content, white_space="pre-wrap"),  # type: ignore
            spacing="5",
            align="center",
            min_height="85vh",
        ),
        blog_post_not_found(),
    )
    return base_page(my_child)
