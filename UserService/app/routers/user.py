from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app import schemas, models
from app.services import auth
from app.services.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
import re
from app.services.auth import create_refresh_token
import asyncio
import websockets
from app.config import settings

router = APIRouter(prefix="/user", tags=["User"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    if db.query(models.User).filter(models.User.nickname == user.nickname).first():
        raise HTTPException(status_code=400, detail="Nickname already taken")
    
    if not re.match(r'^[a-zA-Z0-9]+$', user.nickname):
        raise HTTPException(status_code=400, detail="Nickname must contain only letters and numbers.")
    
    new_user = models.User(
        nickname=user.nickname,
        email=user.email,
        hashedPassword=auth.hash_password(user.password),
        firstname=user.firstname,
        lastname=user.lastname
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Login user and generate JWT
@router.post("/login")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db), response: Response = None):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashedPassword):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        
    access_token = create_refresh_token(data={"sub": db_user.email})
    response.set_cookie(key="access_token", value=access_token, httponly=True)

    return {"message": "Login successful", "access_token": access_token}

# Get user profile
@router.get("/profile", response_model=schemas.UserResponse)
def get_profile(current_user: models.User = Depends(get_current_user)):
    return current_user

@router.delete("/delete", response_model=schemas.UserResponse)
def delete_user(user_id: int, confirmation: schemas.UserDelete, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if not confirmation.confirmation:
        raise HTTPException(status_code=400, detail="Deletion not confirmed")
    
    if current_user.id != user_id:
        raise HTTPException(status_code=400, detail="You can only delete your own account")
    
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()

    return user

# @router.post("/change-password")
# def change_password(change_data: schemas.ChangePassword, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == change_data.email).first()
    
#     if not user or not auth.verify_password(change_data.old_password, user.hashedPassword):
#         raise HTTPException(status_code=400, detail="Incorrect old password")

#     hashed_new_password = auth.hash_password(change_data.new_password)

#     user.hashedPassword = hashed_new_password
#     db.commit()
#     db.refresh(user)
    
#     return {"message": "Password updated successfully"}

# @router.put("/change-avatar", response_model=schemas.UserResponse)
# def change_avatar(user_id: int, avatar_data: schemas.ChangeAvatar, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     user.profile_picture = avatar_data.profile_picture
#     db.commit()
#     db.refresh(user)
#     return user

# @router.put("/change-bio", response_model=schemas.UserResponse)
# def change_bio(user_id: int, bio_data: schemas.ChangeBio, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     user.biography = bio_data.biography
#     db.commit()
#     db.refresh(user)
#     return user

