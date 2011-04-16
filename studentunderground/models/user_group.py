from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from studentunderground.models.base import Base


UserGroupModel = Table('users_groups', Base.metadata,
                       Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
                       Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True)
)
