from pydantic import BaseModel, Field
from typing import Optional
import uuid
from datetime import datetime, timezone

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    publication_year: int
    price: float

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    publication_year: Optional[int] = None
    price: Optional[float] = None

class Book(BookBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True 