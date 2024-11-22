from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel


class CodeSnippet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str
    language: str
    post_id: Optional[int] = Field(default=None, foreign_key="post.id")
    post: Optional["Post"] = Relationship(back_populates="code_blocks")


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    slug: str = Field(index=True, unique=True)
    title: str
    date: datetime
    preview: str
    content: str
    tags: List[str] = Field(default_factory=list, sa_column_kwargs={"type_": "JSON"})
    reading_time: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    code_blocks: List[CodeSnippet] = Relationship(back_populates="post")
