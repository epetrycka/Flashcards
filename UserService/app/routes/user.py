from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import UserCreate, UserResponse
from app.models import User
from app.services.database import get_db
from app.services.rabbitmq import publish_event
from app.services.auth import hash_password

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    hashed_pwd = hash_password(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_pwd)
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    # await publish_event("user.registered", {"user_id": new_user.id, "email": new_user.email})
    
    return new_user