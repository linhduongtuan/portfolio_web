import reflex as rx
from portfolio_web.components import styles
from portfolio_web.components.styles import Size
from portfolio_web.pages.navbar import navbar
from portfolio_web.pages.footer import footer
from portfolio_web.pages.header import header
from portfolio_web.pages.bio import bio
from portfolio_web.pages.technologies import technologies
from portfolio_web.pages.experience import experience
from portfolio_web.pages.skills import skills
from portfolio_web.pages.projects import project
from portfolio_web.pages.publications import publications_view
from portfolio_web.pages.research import research_view
from portfolio_web.pages.about_me import about_me, education
from portfolio_web.pages.blog_page import blog_page
from portfolio_web.pages.blog_post_page import blog_post_page


def index() -> rx.Component:
    return rx.box(
        navbar(),
        # test_table(),
        rx.center(
            rx.vstack(header(), bio(), technologies(), experience()),
        ),
        rx.spacer(padding=styles.Size.VERY_BIG),
        skills(),
        rx.spacer(padding=styles.Size.VERY_BIG),
        rx.center(project()),
        rx.spacer(padding=styles.Size.VERY_BIG),
        footer(),
    )


def research():
    return rx.box(
        navbar(),
        rx.center(
            research_view(),
        ),
        rx.spacer(padding=Size.VERY_BIG.value),
        footer(),
    )


def publications():
    return rx.box(
        navbar(),
        rx.center(
            publications_view(),
        ),
        rx.spacer(padding=Size.VERY_BIG.value),
        footer(),
    )


def about():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                about_me(),
                education(),
            ),
        ),
        rx.spacer(padding=styles.Size.VERY_BIG),
        footer(),
    )


@rx.page(route="/blog")
def personal_blog():
    return rx.box(
        navbar(),
        rx.center(
            blog_page(),
        ),
        rx.spacer(padding=styles.Size.VERY_BIG),
        footer(),
    )


app = rx.App(
    # state=BlogState,
    stylesheets=styles.STYLE_SHEET,
    style=styles.BASE_STYLE,
)

app.add_page(
    index,
    route="/",
    title="Linh Duong - PORTFOLIO",
    description="Linh Duong's Portfolio website",
)

app.add_page(
    blog_post_page,
    route="/blog/post/[id]",
    title="Blog Post",
    description="Detailed blog post",
)
app.add_page(personal_blog, route="/blog")

app.add_page(research, route="/research")
app.add_page(publications, route="/publications")
app.add_page(about, route="/about")
