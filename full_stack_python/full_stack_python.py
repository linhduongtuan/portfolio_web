"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_local_auth

from .ui.base import base_page

from .auth.pages import my_login_page, my_register_page, my_logout_page
from .auth.state import SessionState


from .articles.detail import article_detail_page
from .articles.list import article_public_list_page
from .articles.state import ArticlePublicState

from . import blog, contact, navigation, home
from .components import styles


# def index() -> rx.Component:
#     return base_page(
#         rx.cond(
#             SessionState.is_authenticated,
#             pages.dashboard_component(),
#             pages.landing_component(),
#         )
#     )


def index() -> rx.Component:
    return base_page(
        rx.box(
            # pages.navbar(),
            rx.center(
                rx.vstack(
                    home.header(), home.bio(), home.technologies(), home.experience()
                ),
            ),
            rx.spacer(padding=styles.Size.VERY_BIG),
            home.skills(),
            rx.spacer(padding=styles.Size.VERY_BIG),
            rx.center(home.project()),
            rx.spacer(padding=styles.Size.VERY_BIG),
            home.footer(),
        )
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        panel_background="solid",
        scaling="90%",
        radius="medium",
        accent_color="sky",
    )
)
app.add_page(index, on_load=ArticlePublicState.load_posts)
# reflex_local_auth pages
app.add_page(
    my_login_page,
    # pages.navbar(),
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    my_register_page,
    # pages.navbar(),
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)

app.add_page(
    my_logout_page,
    route=navigation.routes.LOGOUT_ROUTE,
    title="Logout",
)

app.add_page(home.research_view, route=navigation.routes.RESEARCH_ROUTE)

app.add_page(home.publications_view, route=navigation.routes.RESEARCH_ROUTE)

# my pages
app.add_page(home.about_page, route=navigation.routes.ABOUT_US_ROUTE)

app.add_page(home.protected_page, route="/protected/", on_load=SessionState.on_load)


app.add_page(
    article_public_list_page,
    route=navigation.routes.ARTICLE_LIST_ROUTE,
    on_load=ArticlePublicState.load_posts,
)


app.add_page(
    article_detail_page,
    # route=f"{navigation.routes.ARTICLE_LIST_ROUTE}/[post_id]",
    route=f"{navigation.routes.ARTICLE_LIST_ROUTE}/[article_id]",
    on_load=ArticlePublicState.get_post_detail,
)


app.add_page(
    blog.blog_post_list_page,
    route=navigation.routes.BLOG_POSTS_ROUTE,
    on_load=blog.BlogPostState.load_posts,
)

app.add_page(blog.blog_post_add_page, route=navigation.routes.BLOG_POST_ADD_ROUTE)

app.add_page(
    blog.blog_post_detail_page,
    route="/blog/[blog_id]",
    on_load=blog.BlogPostState.get_post_detail,
)

app.add_page(
    blog.blog_post_edit_page,
    route="/blog/[blog_id]/edit",
    on_load=blog.BlogPostState.get_post_detail,
)

app.add_page(contact.contact_page, route=navigation.routes.CONTACT_US_ROUTE)
app.add_page(
    contact.contact_entries_list_page,
    route=navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries,
)
app.add_page(home.pricing_page, route=navigation.routes.PRICING_ROUTE)
