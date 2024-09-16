from uuid import UUID, uuid4

from datetime import datetime
from pydantic import BaseModel, Field


class DiaryEntryCreate(BaseModel):
    mood: int
    note: str
    date: datetime


class DiaryEntry(DiaryEntryCreate):
    id: UUID = Field(default_factory=uuid4, alias="_id")
