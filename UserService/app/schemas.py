from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
import re
from datetime import datetime

class UserBase(BaseModel):
    nickname: str
    email: EmailStr
    firstname: str
    lastname: str
    profile_picture: Optional[str] = None
    biography: Optional[str] = None

    @validator('nickname')
    def nickname_valid(cls, value):
        if not value.isalnum():
            raise ValueError("Nickname must contain only letters and numbers.")
        return value

    @validator('firstname', 'lastname')
    def name_is_alpha(cls, value):
        if not value.isalpha():
            raise ValueError("First name and last name must contain only letters.")
        return value

    @validator('biography')
    def biography_length(cls, value):
        if value and len(value) > 200:
            raise ValueError("Biography must be no longer than 200 characters.")
        return value

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: str
    nickname: str
    password: str = Field(..., min_length=8, max_length=20)

    @validator('nickname')
    def nickname_valid(cls, value):
        if not value.isalnum():
            raise ValueError("Nickname must contain only letters and numbers.")
        return value

    @validator('firstname', 'lastname')
    def name_is_alpha(cls, value):
        if not value.isalpha():
            raise ValueError("First name and last name must contain only letters.")
        return value

    @validator('password')
    def password_complexity(cls, value):
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit.")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character.")
        return value
    
class UserResponse(UserBase):
    id: int
    role: str
    created_at: datetime
    updated_at: Optional[datetime]

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    nickname: Optional[str] = None
    email: Optional[EmailStr] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    profile_picture: Optional[str] = None
    biography: Optional[str] = None

    @validator('nickname', always=True)
    def nickname_valid(cls, value):
        if value and not value.isalnum():
            raise ValueError("Nickname must contain only letters and numbers.")
        return value

    @validator('firstname', 'lastname', always=True)
    def name_is_alpha(cls, value):
        if value and not value.isalpha():
            raise ValueError("First name and last name must contain only letters.")
        return value

    @validator('biography', always=True)
    def biography_length(cls, value):
        if value and len(value) > 200:
            raise ValueError("Biography must be no longer than 200 characters.")
        return value

class ChangePassword(BaseModel):
    email: str
    old_password: str
    new_password: str = Field(..., min_length=8, max_length=20)

    @validator('new_password')
    def validate_password_complexity(cls, value):
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit.")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character.")
        return value

    class Config:
        min_anystr_length = 8
        anystr_strip_whitespace = True

class UserDelete(BaseModel):
    confirmation: bool

class ChangeAvatar(BaseModel):
    profile_picture: str

class ChangeBio(BaseModel):
    biography: str
