from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from studentunderground.models.base import Base

AclUserGroupModel = Table('acl_users_groups', Base.metadata,
                       Column('acl_user_id', Integer, ForeignKey('acl_users.id'), primary_key=True),
                       Column('acl_group_id', Integer, ForeignKey('acl_groups.id'), primary_key=True)
)
