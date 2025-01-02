from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True, index=True, autoincrement=True)
    nickname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    hashedPassword = Column(String(255), nullable=False)
    role = Column(String(255), nullable=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    profile_picture = Column(String(255), nullable=True)
    created_at = Column(DateTime(), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(), nullable=True, onupdate=func.now())

    def __repr__(self):
        return f"<User(nickname='{self.nickname}', email='{self.email}')>"
