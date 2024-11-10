from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.types import String
from app.database import Base
from enum import Enum as PyEnum

#relations not implemented

class UserRole(PyEnum):
    STANDARD = "Standard"
    PRO = "Pro"

class StatusInvitation(PyEnum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole))
    first_name = Column(String)
    last_name = Column(String)
    profile_picture = Column(String) 
    created_at = Column(Date)
    updated_at = Column(Date)

    #folders = relationship("Folder", back_populates="owner")

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), index=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)

class Friend(Base):
    __tablename__ = "friends"

    user_id = Column(Integer, ForeignKey("users.id"),index=True)
    friend_id = Column(Integer, ForeignKey("users.id"),index=True)
    updated_at = Column(Date)

class GroupInvitation(Base):
    __tablename__ = "groups-invitations"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"), index=True)
    sender_id = Column(Integer, ForeignKey("users.id"),index=True)
    recipient_id = Column(Integer, ForeignKey("users.id"),index=True)
    status = Column(Enum(StatusInvitation))
    sent_at = Column(Date)

class FriendInvitation(Base):
    __tablename__ = "friends-invitations"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"),index=True)
    recipient_id = Column(Integer, ForeignKey("users.id"),index=True)
    status = Column(Enum(StatusInvitation))
    sent_at = Column(Date)

# class GroupMembers(Base):
# in-progress project

class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String)
    image_url = Column(String)
    is_public = Column(Boolean, default=False)
    created_at = Column(Date)
    updated_at = Column(Date)
        
    #owner = relationship("User", back_populates="folders")

class SharedFolders(Base):
    __tablename__ = "shared-folders"

    id = Column(Integer, primary_key=True, index=True)
    folder_id = Column(Integer, ForeignKey("folders.id"), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), index=True)
    friend_id = Column(Integer, ForeignKey("users.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))
    created_at = Column(Date)

class Set(Base):
    __tablename__ = "sets"

    id = Column(Integer, primary_key=True, index=True)
    folder_id = Column(Integer, ForeignKey("folders.id"))
    onwer_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    description = Column(String)
    image_url = Column(String)
    is_public = Column(Boolean, default=False)
    created_at = Column(Date)
    updated_at = Column(Date)

class Flashcard(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True, index=True)
    set_id = Column(Integer, ForeignKey("sets.id"))
    question = Column(String)
    answer = Column(String)
    image_url = Column(String)
    animation_url = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    feedback_text = Column(String)
    feedback_type = Column(String)
    created_at = Column(Date)