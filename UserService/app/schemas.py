from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    nickname: str
    email: EmailStr
    hashedPassword: str
    role: Optional[str] = None
    firstname: str
    lastname: str
    profile_picture: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    nickname: str
    email: EmailStr
    role: Optional[str] = None
    firstname: str
    lastname: str
    profile_picture: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
