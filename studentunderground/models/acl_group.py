from studentunderground.models.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

class AclGroupModel(Base):
    __tablename__ = 'acl_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AclGroup('%s', '%s')>" % (self.id,
                                           self.name)
