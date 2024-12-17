from core.database import engine
from models.user import Base, User 
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Jan", fullname="Marcin", nickname="wolder")
session.add(new_user)

User.__table__.drop(engine)

session.commit()

session.close()

print("Tabele zostały utworzone, a dane zostały zapisane.")
