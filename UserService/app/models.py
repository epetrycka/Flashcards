from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func, Text

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nickname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    hashedPassword = Column(String(255), nullable=False)
    role = Column(String(20), nullable=True, default="student")
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    profile_picture = Column(String(255), nullable=True)
    biography = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=True, onupdate=func.now())

    def __repr__(self):
        return f"<User(nickname='{self.nickname}', email='{self.email}')>"
