from sqlalchemy.orm import Session
from models.user import User
from schemas.auth import UserCreate, UserLogin
from services.hashing import hash_password, verify_password
from werkzeug.exceptions import HTTPException

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    user_object = User(name=user.name, email=user.email, hashedPassword=hashed_password, nickname=user.nickname, fullname=user.fullname)
    db.add(user_object)
    db.commit()
    db.refresh(user_object)
    return user_object

def authenticate_user(db: Session, user: UserLogin):
    user_data = db.query(User).filter(User.email == user.email).first()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    hashed_password = hash_password(user.password)
    if not verify_password(user.password, user_data.hashedPassword):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    return user_data
