# app/models/movie.py
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class MovieBase(SQLModel):
    name: str
    release_date: datetime
    watched: bool = False

class Movie(MovieBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="active")

class MovieCreate(MovieBase):
    pass

class MovieRead(MovieBase):
    id: int
    created_at: datetime
    updated_at: datetime
    status: str

class MovieUpdate(SQLModel):
    name: Optional[str] = None
    release_date: Optional[datetime] = None
    watched: Optional[bool] = None