from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from app.schemas.question import QuestionResponse

class LevelBase(BaseModel):
    boss_name: str
    boss_image_s3: Optional[str] = None
    background_image_s3: Optional[str] = None
    boss_hp: int = 100
    boss_attack: int = 10
    question_ids: List[str] = []

class LevelCreate(LevelBase):
    level: int = 1

class LevelUpdate(BaseModel):
    boss_name: Optional[str] = None
    boss_image_s3: Optional[str] = None
    background_image_s3: Optional[str] = None
    boss_hp: Optional[int] = None
    boss_attack: Optional[int] = None
    question_ids: Optional[List[str]] = None

class LevelResponse(LevelBase):
    level: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class LevelWithQuestionsResponse(LevelResponse):
    questions: List[QuestionResponse] = []
    
    class Config:
        orm_mode = True 