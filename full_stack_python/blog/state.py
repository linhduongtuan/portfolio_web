from datetime import datetime
from typing import Optional
from sqlalchemy import select
import sqlalchemy.orm
from typing import List
import reflex as rx

import sqlalchemy
from sqlmodel import select  # noqa: F811
from sqlmodel import Field, Relationship

from .. import navigation
from ..auth.state import SessionState
from ..models import BlogPostModel, UserInfo

BLOG_POSTS_ROUTE = navigation.routes.BLOG_POSTS_ROUTE
if BLOG_POSTS_ROUTE.endswith("/"):
    BLOG_POSTS_ROUTE = BLOG_POSTS_ROUTE[:-1]


class BlogPostState(SessionState):
    posts: List["BlogPostModel"] = []
    post: Optional["BlogPostModel"] = None
    post_content: str = ""
    post_publish_active: bool = False
    userinfo: Optional["UserInfo"] = Relationship()
    id: Optional[int] = Field(default=None, primary_key=True)

    userinfo_id: Optional[int] = Field(default=None, foreign_key="userinfo.id")

    userinfo: Optional["UserInfo"] = Relationship(back_populates="blog_posts")
    # set_post_publish_active: Optional[bool] = Field(default=False)

    @rx.var
    def blog_post_id(self):
        return self.router.page.params.get("blog_id", "")

    @rx.var
    def blog_post_url(self):
        if not self.post:
            return f"{BLOG_POSTS_ROUTE}"
        return f"{BLOG_POSTS_ROUTE}/{self.post.id}"

    @rx.var
    def blog_post_edit_url(self) -> str:
        if not self.post:
            return f"{BLOG_POSTS_ROUTE}"
        return f"{BLOG_POSTS_ROUTE}/{self.post.id}/edit"

    def get_post_detail(self) -> None:
        """Retrieve details for a specific blog post and update instance attributes xxxxxx."""
        if self.my_userinfo_id is None:
            self._reset_post_attributes()
            return

        if not self.blog_post_id:
            self.post = None
            return

        lookups = (BlogPostModel.userinfo_id == self.my_userinfo_id) & (
            BlogPostModel.id == self.blog_post_id
        )

        with rx.session() as session:
            sql_statement = (
                select(BlogPostModel)
                .options(
                    sqlalchemy.orm.joinedload(BlogPostModel.userinfo).joinedload(  # type: ignore
                        UserInfo.user  # type: ignore
                    )
                )
                .where(lookups)
            )
            self.post = session.exec(sql_statement).one_or_none()

            if self.post is None:
                self._reset_post_attributes()
                return

            if self.post.userinfo:
                self.post.userinfo.user  # Eager load user data

            self.post_content = self.post.content
            self.post_publish_active = self.post.publish_active

    def _reset_post_attributes(self) -> None:
        """Reset post-related instance attributes to default values."""
        self.post = None
        self.post_content = ""
        self.post_publish_active = False

    def load_posts(self, published_only: bool = False) -> None:
        """Load all blog posts for the user with optional published-only filter."""
        query = (
            select(BlogPostModel)
            .options(sqlalchemy.orm.joinedload(BlogPostModel.userinfo))  # type: ignore
            .where(BlogPostModel.userinfo_id == self.my_userinfo_id)
        )

        if published_only:
            query = query.where(
                (BlogPostModel.publish_active)
                & (BlogPostModel.publish_date < datetime.now())
            )

        with rx.session() as session:
            self.posts = list(session.exec(query).all())
        # return

    def add_post(self, form_data: dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            # print("adding", post)
            session.add(post)
            session.commit()
            session.refresh(post)  # post.id
            # print("added", post)
            self.post = post

    def save_post_edits(self, post_id: int, updated_data: dict):
        with rx.session() as session:
            post = session.exec(
                select(BlogPostModel).where(BlogPostModel.id == post_id)
            ).one_or_none()
            if post is None:
                return
            for key, value in updated_data.items():
                setattr(post, key, value)
            session.add(post)
            session.commit()
            session.refresh(post)
            self.post = post

    def to_blog_post(self, edit_page=False):
        if not self.post:
            return rx.redirect(BLOG_POSTS_ROUTE)
        if edit_page:
            return rx.redirect(f"{self.blog_post_edit_url}")
        return rx.redirect(f"{self.blog_post_url}")


class BlogAddPostFormState(BlogPostState):
    form_data: dict = {}

    def handle_submit(self, form_data):
        data = form_data.copy()
        if self.my_userinfo_id is not None:
            data["userinfo_id"] = self.my_userinfo_id
        self.form_data = data
        self.add_post(data)
        return self.to_blog_post(edit_page=True)


class BlogEditFormState(BlogPostState):
    form_data: dict = {}
    # post_content: str = ""

    @rx.var
    def publish_display_date(self) -> str:
        # return "2023-12-01" # YYYY-MM-DD
        if not self.post:
            return datetime.now().strftime("%Y-%m-%d")
        if not self.post.publish_date:
            return datetime.now().strftime("%Y-%m-%d")
        return self.post.publish_date.strftime("%Y-%m-%d")

    @rx.var
    def publish_display_time(self) -> str:
        if not self.post:
            return datetime.now().strftime("%H:%M:%S")
        if not self.post.publish_date:
            return datetime.now().strftime("%H:%M:%S")
        return self.post.publish_date.strftime("%H:%M:%S")

    def handle_submit(self, form_data):
        self.form_data = form_data
        post_id = form_data.pop("post_id")
        publish_date = None
        if "publish_date" in form_data:
            publish_date = form_data.pop("publish_date")
        publish_time = None
        if "publish_time" in form_data:
            publish_time = form_data.pop("publish_time")
        publish_input_string = f"{publish_date} {publish_time}"
        try:
            final_publish_date = datetime.strptime(
                publish_input_string, "%Y-%m-%d %H:%M:%S"
            )
        except ValueError:
            final_publish_date = None
        publish_active = False
        if "publish_active" in form_data:
            publish_active = form_data.pop("publish_active") == "on"
        updated_data = {**form_data}
        updated_data["publish_active"] = publish_active
        updated_data["publish_date"] = final_publish_date
        self.save_post_edits(post_id, updated_data)
        return self.to_blog_post()
