from sqlalchemy import Column, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    fullname = Column(String(255), nullable=False)
    nickname = Column(String(255), nullable=False)
    hashedPassword = Column(String(255), nullable=False)

    #optional method
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
             self.name,
             self.fullname,
             self.nickname,
        )
    