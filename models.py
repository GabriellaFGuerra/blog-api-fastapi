from typing import List
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from database_setup import Base


# SQLAlchemy model for posts
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    tags = Column(String)  # Store tags as a comma-separated string
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# Pydantic model for posts
class PostModel(BaseModel):
    title: str
    content: str
    tags: List[str]  # Use a list of strings for tags

    class Config:
        orm_mode = True  # Enable ORM mode for Pydantic model


# Helper functions for tag conversion
def list_to_str(tags: List[str]):
    return ",".join(filter(None, tags))  # Use filter to remove empty tags


def str_to_list(tags_str: str):
    return [
        tag.strip() for tag in tags_str.split(",") if tag.strip()
    ]  # Strip whitespace from tags

