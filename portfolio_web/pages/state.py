# In states.py
from typing import List, Dict
from datetime import datetime
import reflex as rx
from typing import List, Dict, Optional
from datetime import datetime
import reflex as rx
# from portfolio_web.database.database import get_session
# from portfolio_web.database.models import Post, CodeSnippet

# class State(rx.State):
#   """The app state."""
#   current_post: Optional[Dict] = None

#   def get_all_posts(self) -> List[Dict]:
#       """Get all blog posts."""
#       session = next(get_session())
#       try:
#           posts = session.query(Post).order_by(Post.date.desc()).all()
#           return [
#               {
#                   "slug": post.slug,
#                   "title": post.title,
#                   "date": post.date.strftime("%B %d, %Y"),
#                   "preview": post.preview,
#                   "tags": post.tags,
#                   "reading_time": post.reading_time
#               }
#               for post in posts
#           ]
#       finally:
#           session.close()

#   def get_post(self, slug: str) -> Optional[Dict]:
#       """Get a specific blog post."""
#       session = next(get_session())
#       try:
#           post = session.query(Post).filter(Post.slug == slug).first()
#           if post:
#               return {
#                   "slug": post.slug,
#                   "title": post.title,
#                   "date": post.date.strftime("%B %d, %Y"),
#                   "content": post.content,
#                   "tags": post.tags,
#                   "reading_time": post.reading_time,
#                   "code_blocks": [
#                       {
#                           "code": block.code,
#                           "language": block.language
#                       }
#                       for block in post.code_blocks
#                   ]
#               }
#           return None
#       finally:
#           session.close()


comment_styles = dict(
    box=dict(
        bg="white",
        shadow="sm",
        border_radius="md",
        padding="4",
        _hover=dict(
            shadow="md",
        ),
    ),
    input=dict(
        border="1px solid",
        border_color="gray.200",
        _focus=dict(
            border_color="blue.500",
            shadow="outline",
        ),
    ),
    button=dict(
        bg="blue.500",
        color="white",
        _hover=dict(
            bg="blue.600",
        ),
    ),
)


class State(rx.State):
    """The app state."""

    comments: List[Dict] = []
    new_comment: str = ""
    user_name: str = ""
    user_email: str = ""

    def handle_submit(self):
        """Handle the form submission."""
        if self.new_comment.strip() and self.user_name.strip():
            new_comment = {
                "text": self.new_comment,
                "author": self.user_name,
                "email": self.user_email,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "id": len(self.comments),
            }
            self.comments = self.comments + [new_comment]
            # Clear form
            self.new_comment = ""
            self.user_name = ""
            self.user_email = ""


def enhanced_comment_section() -> rx.Component:
    #   return rx.vstack(
    #       rx.heading("Comments", size="lg"),

    #       # Comment form
    #       rx.form(
    #           rx.vstack(
    #               rx.hstack(
    #                   rx.input(
    #                       placeholder="Your Name",
    #                       value=State.user_name,
    #                       on_change=State.set_user_name,
    #                       required=True,
    #                       style=comment_styles["input"],
    #                       id="name",
    #                       name="name",
    #                   ),
    #                   rx.input(
    #                       placeholder="Email (optional)",
    #                       type_="email",
    #                       value=State.user_email,
    #                       on_change=State.set_user_email,
    #                       style=comment_styles["input"],
    #                       id="email",
    #                       name="email",
    #                   ),
    #                   width="100%",
    #               ),
    #               rx.text_area(
    #                   placeholder="Write a comment...",
    #                   value=State.new_comment,
    #                   on_change=State.set_new_comment,
    #                   required=True,
    #                   min_height="200px",
    #                   min_width="600px",
    #                   style=comment_styles["input"],
    #                   id="comment",
    #                   name="comment",
    #               ),
    #               rx.button(
    #                   "Post Comment",
    #                   type_="submit",
    #                   style=comment_styles["button"],
    #               ),
    #               align_items="flex-start",
    #           ),
    #           on_submit=State.handle_submit,
    #       ),

    #       # Comments display
    #       rx.vstack(
    #           rx.foreach(
    #               State.comments,
    #               lambda comment: rx.box(
    #                   rx.vstack(
    #                       rx.hstack(
    #                           rx.heading(
    #                               comment["author"],
    #                               size="sm",
    #                           ),
    #                           rx.spacer(),
    #                           rx.text(
    #                               comment["date"],
    #                               font_size="sm",
    #                               color="gray.500",
    #                           ),
    #                       ),
    #                       rx.text(comment["text"]),
    #                       align_items="flex-start",
    #                       style=comment_styles["box"],
    #                   ),
    #               ),
    #           ),
    #           width="100%",
    #           spacing="4",
    #       ),
    #       width="100%",
    #       spacing="6",
    #   )
    return rx.popover.root(
        rx.popover.trigger(
            rx.button("Comment", variant="soft"),
        ),
        rx.popover.content(
            rx.flex(
                rx.avatar("2", fallback="RX", radius="full"),
                rx.box(
                    rx.text_area(
                        placeholder="Write a comment…",
                        style={"height": 80},
                    ),
                    rx.flex(
                        rx.checkbox("Send to group"),
                        rx.popover.close(rx.button("Comment", size="1")),
                        spacing="3",
                        margin_top="12px",
                        justify="between",
                    ),
                    flex_grow="1",
                ),
                spacing="3",
            ),
            style={"width": 360},
        ),
    )
