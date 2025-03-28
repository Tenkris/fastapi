from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class QuestionType(str, Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    SINGLE_CHOICE = "single_choice"

class QuestionBase(BaseModel):
    question: str
    type: QuestionType
    time_countdown: int
    answer: str

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(BaseModel):
    question: Optional[str] = None
    type: Optional[QuestionType] = None
    time_countdown: Optional[int] = None
    answer: Optional[str] = None

class QuestionResponse(QuestionBase):
    question_id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True 