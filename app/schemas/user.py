from typing import Optional
from pydantic import BaseModel, EmailStr
from app.schemas.enums import Gender
from datetime import datetime, timezone

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    tel: str
    password: str
    role: str = "user"
    age: Optional[int] = None
    career: Optional[str] = None
    gender: Optional[Gender] = None
    hobbies: Optional[str] = None
    reason: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "tel": "1234567890",
                "password": "password123",
                "role": "user", 
                "age": 30,
                "career": "Software Engineer",
                "gender": "female",
                "hobbies": "reading, hiking, photography",
                "reason": "Interested in joining the platform"
            }
        }

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    name: str
    email: EmailStr
    tel: str
    role: str = "user"
    age: Optional[int] = None
    career: Optional[str] = None
    gender: Optional[Gender] = None
    hobbies: Optional[str] = None
    reason: Optional[str] = None

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    tel: Optional[str] = None
    age: Optional[int] = None
    career: Optional[str] = None
    gender: Optional[Gender] = None
    hobbies: Optional[str] = None
    reason: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "tel": "1234567890",
                "age": 30,
                "career": "Software Engineer",
                "gender": "male",
                "hobbies": "reading, hiking",
                "reason": "Personal development"
            }
        }