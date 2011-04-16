from studentunderground.models.base import Base
from studentunderground.models.user import UserModel
from studentunderground.models.acl_group import AclGroupModel
from studentunderground.models.acl_user_group import AclUserGroupModel
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

class AclUserModel(Base):
    __tablename__ = 'acl_users'

    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    identifier = Column(String(50))
    password = Column(String(40))
    acl_groups = relationship(AclGroupModel,
                              secondary=AclUserGroupModel,
                              backref="acl_users")
    user = relationship(UserModel,
                        backref="acl_user",
                        uselist=False)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AclUser('%s', '%s', '%s', '%s')>" % (self.id,
                                                      self.email,
                                                      self.identifier,
                                                      self.password)
