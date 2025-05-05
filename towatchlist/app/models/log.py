# app/models/log.py
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class RequestLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    method: str
    path: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)