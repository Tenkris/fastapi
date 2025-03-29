from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime, timezone

class UserCreate(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    password: str
    level_id: Optional[int] = 1
    user_image: Optional[str] = None
    attack: Optional[float] = 10.0
    defense: Optional[float] = 10.0
    speed: Optional[float] = 10.0
    critical: Optional[float] = 5.0
    hp: Optional[float] = 100.0

    class Config:
        json_schema_extra = {
            "example": {
                "email": "john@example.com",
                "name": "John Doe",
                "password": "password123",
                "level_id": 1,
                "user_image": "https://s3.amazonaws.com/bucket/image.jpg",
                "attack": 10.0,
                "defense": 10.0,
                "speed": 10.0,
                "critical": 5.0,
                "hp": 100.0
            }
        }

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    level_id: int
    user_image: Optional[str] = None
    attack: float
    defense: float
    speed: float
    critical: float
    hp: float

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    level_id: Optional[int] = None
    user_image: Optional[str] = None
    attack: Optional[float] = None
    defense: Optional[float] = None
    speed: Optional[float] = None
    critical: Optional[float] = None
    hp: Optional[float] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Smith",
                "level_id": 2,
                "user_image": "https://s3.amazonaws.com/bucket/updated-image.jpg",
                "attack": 15.0,
                "defense": 12.0,
                "speed": 11.0,
                "critical": 6.0,
                "hp": 120.0
            }
        }