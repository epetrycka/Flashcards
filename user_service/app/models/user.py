from sqlalchemy import Column, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String(10))
    fullname = Column(String(10))
    nickname = Column(String(10))

    #optional method
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
             self.name,
             self.fullname,
             self.nickname,
        )
    