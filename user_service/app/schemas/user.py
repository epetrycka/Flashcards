User.__table__  
Table('users', MetaData(),
            Column('id', Integer(), table='users', primary_key=True, nullable=False),
            Column('name', String(), table='users'),
            Column('fullname', String(), table='users'),
            Column('nickname', String(), table='users'), schema=None)