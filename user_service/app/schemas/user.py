from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column('name', String(), nullable=False),
    Column('fullname', String(), nullable=False),
    Column('nickname', String(), unique=True, nullable=False),
    Column("email", String, unique=True, nullable=False),
    Column("hashed_password", String, nullable=False),
)