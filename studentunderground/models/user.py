from studentunderground.models.base import Base
from studentunderground.models.user_network import UserNetworkModel
from studentunderground.models.user_group import UserGroupModel
from studentunderground.models.group import GroupModel
from studentunderground.models.network import NetworkModel
from studentunderground.models.profile import ProfileModel
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    acl_user_id = Column(Integer, ForeignKey('acl_users.id'))
    groups = relationship(GroupModel,
                          secondary=UserGroupModel,
                          backref="users")
    networks = relationship(NetworkModel,
                            secondary=UserNetworkModel,
                            backref="users")
    profile = relationship(ProfileModel,
                           backref="user",
                           uselist=False)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<User('%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                         self.email,
                                                         self.first_name,
                                                         self.last_name,
                                                         self.acl_user_id)
