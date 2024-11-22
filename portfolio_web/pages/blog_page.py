from dataclasses import dataclass
import reflex as rx
from portfolio_web.components.styles import Size, Color, TextColor
from portfolio_web.data.contents import blog_posts, BlogPost
from typing import List, Dict
import datetime


class BlogState(rx.State):
    """State for managing blog interactions."""

    show_content: dict[str, bool] = {}

    def toggle_content(self, post_id: str):
        """Toggle the visibility of a post's content."""
        self.show_content[post_id] = not self.show_content.get(post_id, False)


def giscus_comments() -> rx.Component:
    return rx.box(
        rx.script(
            {
                "src": "https://giscus.app/client.js",
                "data-repo": "YOUR_USERNAME/YOUR_REPO",  # e.g., "linh/portfolio"
                "data-repo-id": "YOUR_REPO_ID",  # Get from giscus.app
                "data-category": "Announcements",  # Choose your category
                "data-category-id": "YOUR_CATEGORY_ID",  # Get from giscus.app
                "data-mapping": "pathname",
                "data-strict": "0",
                "data-reactions-enabled": "1",
                "data-emit-metadata": "0",
                "data-input-position": "bottom",
                "data-theme": "preferred_color_scheme",
                "data-lang": "en",
                "crossorigin": "anonymous",
                "async": True,
            }
        ),
        margin_top="2em",
        width="100%",
    )


class CommentState(rx.State):
    comments: Dict[str, List[Dict]] = {}  # Store comments by post_id
    new_comment: str = ""

    def add_comment(self, post_id: str):
        if not self.new_comment.strip():
            return

        if post_id not in self.comments:
            self.comments[post_id] = []

        self.comments[post_id].append(
            {
                "text": self.new_comment,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
        )
        self.new_comment = ""  # Clear input


def comment_section(post_id: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Comments",
            size="lg",
            margin_top="2em",
            color=TextColor.FEATURED.value,
        ),
        rx.divider(),
        rx.foreach(
            CommentState.comments[post_id],
            lambda comment: rx.box(
                rx.text(comment["text"]),
                rx.text(
                    comment["date"],
                    font_size="sm",
                    color="gray",
                ),
                padding="1em",
                border="1px solid",
                border_color="gray.200",
                border_radius="md",
                margin_y="0.5em",
            ),
        ),
        rx.form(
            rx.text_area(
                value=CommentState.new_comment,
                on_change=CommentState.set_new_comment,
                placeholder="Add a comment...",
                width="100%",
            ),
            rx.button(
                "Submit",
                type_="submit",
                on_click=lambda: CommentState.add_comment(post_id),
            ),
            width="100%",
        ),
        width="100%",
        max_width="800px",
        padding="2em",
    )


def disqus_comments(post_id: str) -> rx.Component:
    disqus_shortname = "your-shortname"  # Replace with your shortname

    return rx.box(
        rx.html(
            f"""
          <div id="disqus_thread"></div>
          <script>
              var disqus_config = function () {{
                  this.page.url = window.location.href;
                  this.page.identifier = "{post_id}";
                  this.page.title = "{post_id}";
              }};

              function loadDisqus() {{
                  var d = document, s = d.createElement('script');
                  s.src = 'https://{disqus_shortname}.disqus.com/embed.js';
                  s.setAttribute('data-timestamp', +new Date());
                  (d.head || d.body).appendChild(s);
              }}

              // Load Disqus when the div is visible
              var observer = new IntersectionObserver(function(entries) {{
                  if(entries[0].isIntersecting) {{
                      loadDisqus();
                      observer.disconnect();
                  }}
              }}, {{ threshold: [0] }});

              observer.observe(document.getElementById('disqus_thread'));

              // Error handling
              window.addEventListener('message', function(e) {{
                  if (e.data.type === 'dsq.timeout') {{
                      document.getElementById('disqus_thread').innerHTML = 
                          'Comments failed to load. Please check your internet connection or try again later.';
                  }}
              }});
          </script>
          <noscript>
              Please enable JavaScript to view the comments.
          </noscript>
          """
        ),
        margin_top="2em",
        width="100%",
        min_height="200px",
    )


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
        href=f"/blog/post/{post.id}",  # Updated href
        text_decoration="none",
        width="100%",
    )


@rx.page(route="/blog")
def blog_page() -> rx.Component:
    """Display the blog listing page."""
    return rx.box(
        rx.vstack(
            rx.heading(
                "RESEARCH BLOG",
                size=Size.BIG.value,
                color=TextColor.PRIMARY.value,
                margin_bottom="0.5em",
                font_size="3em",
                font_weight="bold",
                align_self="center",
                padding_top="1em",
            ),
            *[blog_post_item(post) for post in blog_posts],
            rx.divider(),
            rx.heading("Comments", size="lg"),
            disqus_comments(id) if id else rx.text("No comments available"),
            width="100%",
            max_width="800px",
            padding="2em",
            spacing="4",
        ),
    )
