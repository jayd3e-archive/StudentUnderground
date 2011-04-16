from studentunderground.models.base import Base
from studentunderground.models.group import GroupModel
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

class NetworkModel(Base):
    __tablename__ = 'networks'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    created = Column(DateTime)
    edited = Column(DateTime)
    groups = relationship(GroupModel,
                          backref="network")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Network('%s', '%s', '%s', '%s')>" % (self.id,
                                                      self.name,
                                                      self.created,
                                                      self.edited)
