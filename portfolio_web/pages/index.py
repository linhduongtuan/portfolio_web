import reflex as rx


class BlogPost:
    def __init__(self, id: str, title: str, preview: str, content: str):
        self.id = id
        self.title = title
        self.preview = preview
        self.content = content


# Sample blog posts
blog_posts = [
    BlogPost(
        "1",
        "Deep Learning in Biomedicine",
        "A preview of deep learning applications...",
        "Full content about deep learning in biomedicine...",
    ),
    BlogPost(
        "2",
        "AI in Drug Discovery",
        "How AI is revolutionizing drug discovery...",
        "Detailed content about AI in drug discovery...",
    ),
]


def blog_preview(post: BlogPost):
    return rx.box(
        rx.heading(post.title, size="lg"),
        rx.text(post.preview),
        rx.link(
            "Read more",
            href=f"/blog/{post.id}",
            color="blue.500",
        ),
        padding="4",
        border="1px solid",
        border_radius="md",
        margin_y="2",
    )


def index():
    return rx.box(
        rx.heading("My Research Blog"),
        rx.vstack(
            *[blog_preview(post) for post in blog_posts],
            spacing="4",
            align="stretch",
        ),
        max_width="800px",
        margin="auto",
        padding="4",
    )


def blog_index():
    return rx.box(
        rx.heading("Blog Posts"),
        rx.vstack(
            [
                rx.link(
                    rx.card(rx.text(post.title), rx.text(post.preview)),
                    href=f"/blog/{post.id}",
                )
                for post in blog_posts
            ]
        ),
    )
