from datetime import datetime
from operator import and_
from typing import Optional, List
import reflex as rx  # type: ignore

import sqlalchemy  # type: ignore
from sqlmodel import select  # type: ignore

from .. import navigation
from ..auth.state import SessionState
from ..models import BlogPostModel, UserInfo

ARTICLE_LIST_ROUTE = navigation.routes.ARTICLE_LIST_ROUTE
if ARTICLE_LIST_ROUTE.endswith("/"):
    ARTICLE_LIST_ROUTE = ARTICLE_LIST_ROUTE[:-1]


class ArticlePublicState(SessionState):
    posts: List[BlogPostModel] = []
    post: Optional[BlogPostModel] = None
    post_content: str = ""
    post_publish_active: bool = False
    limit: int = 20
    # post_id: Optional[str] = None
    article_post_id: Optional[str] = None

    @rx.var
    def post_id(self):
        return self.router.page.params.get("post_id", "")

    @rx.var
    def post_url(self):
        if not self.post:
            return f"{ARTICLE_LIST_ROUTE}"
        return f"{ARTICLE_LIST_ROUTE}/{self.post.id}"

    # def get_post_detail(self):
    #     lookups = (
    #         (BlogPostModel.publish_active is True)
    #         & (BlogPostModel.publish_date < datetime.now())
    #         & (BlogPostModel.id == self.post_id)
    #     )
    #     with rx.session() as session:
    #         if self.post_id == "":
    #             self.post = None
    #             self.post_content = ""
    #             self.post_publish_active = False
    #             return
    #         sql_statement = (
    #             select(BlogPostModel)
    #             .options(
    #                 sqlalchemy.orm.joinedload(BlogPostModel.userinfo).joinedload(
    #                     UserInfo.user
    #                 )
    #             )
    #             .where(lookups)
    #         )
    #         result = session.exec(sql_statement).one_or_none()
    #         self.post = result
    #         if result is None:
    #             self.post_content = ""
    #             self.post_publish_active = False
    #             return
    #         self.post_content = result.content
    #         self.post_publish_active = result.publish_active
    # def get_post_detail(self):
    #     lookups = and_(
    #         BlogPostModel.publish_active.is_(True),  # Use `is_` for SQL comparison
    #         BlogPostModel.publish_date < datetime.now(),
    #         BlogPostModel.id == self.post_id
    #     )
    #     with rx.session() as session:
    #         if self.post_id == "":
    #             self.post = None
    #             self.post_content = ""
    #             self.post_publish_active = False
    #             return
    #         sql_statement = (
    #             select(BlogPostModel)
    #             .options(
    #                 sqlalchemy.orm.joinedload(BlogPostModel.userinfo).joinedload(
    #                     UserInfo.user
    #                 )
    #             )
    #             .where(lookups)
    #         )
    #         result = session.exec(sql_statement).one_or_none()
    #         self.post = result
    #         if result is None:
    #             self.post_content = ""
    #             self.post_publish_active = False
    #             return
    #         self.post_content = result.content
    #         self.post_publish_active = result.publish_active

    def get_post_detail(self):
        lookups = and_(
            BlogPostModel.publish_active.is_(  # type: ignore
                True
            ),  # Use is_() for SQL comparison # type: ignore
            BlogPostModel.publish_date < datetime.now(),  # type: ignore
            BlogPostModel.id == self.post_id,  # type: ignore
        )
        with rx.session() as session:
            if self.post_id == "":
                self.post = None
                self.post_content = ""
                self.post_publish_active = False
                return
            sql_statement = (
                select(BlogPostModel)
                .options(
                    sqlalchemy.orm.joinedload(BlogPostModel.userinfo).joinedload(
                        UserInfo.user
                    )
                )
                .where(lookups)
            )
            result = session.exec(sql_statement).one_or_none()
            self.post = result
            if result is None:
                self.post_content = ""
                self.post_publish_active = False
                return
            self.post_content = result.content if result else ""
            self.post_publish_active = result.publish_active if result else False

    def set_limit_and_reload(self, new_limit: int = 5):
        self.limit = new_limit
        self.load_posts()
        yield

    # def load_posts(self, *args, **kwargs):
    #     lookup_args = (BlogPostModel.publish_active is True) & (
    #         BlogPostModel.publish_date < datetime.now()
    #     )
    #     with rx.session() as session:
    #         result = session.exec(
    #             select(BlogPostModel)
    #             .options(sqlalchemy.orm.joinedload(BlogPostModel.userinfo))
    #             .where(lookup_args)
    #             .limit(self.limit)
    #         ).all()
    #         self.posts = list(result)
    def load_posts(self, *args, **kwargs):
        # Corrected logical operation
        lookup_args = and_(
            BlogPostModel.publish_active.is_(  # type: ignore
                True
            ),  # Use `is_` for SQL comparison # type: ignore
            BlogPostModel.publish_date.op("<")(datetime.now()),  # type: ignore
        )
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel)
                .options(sqlalchemy.orm.joinedload(BlogPostModel.userinfo))
                .where(lookup_args)
                .limit(self.limit)
            ).all()
            self.posts = list(result)

    def to_post(self):
        if not self.post:
            return rx.redirect(ARTICLE_LIST_ROUTE)
        return rx.redirect(f"{self.post_url}")

    @rx.var
    def computed_post_id(self):
        # Original logic for `post_id`
        return str(self.some_logic_to_get_post_id)

    @rx.var
    def some_logic_to_get_post_id(self) -> int:
        # Replace this logic with the actual implementation
        return 123  # Example: Replace with actual logic to determine post ID
