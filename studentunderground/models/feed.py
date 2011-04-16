from studentunderground.models.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

class FeedModel(Base):
    __tablename__ = 'feed'

    id = Column(Integer, primary_key=True)
    model = Column(String(50))
    foreign_id = Column(Integer)
    created = Column(DateTime)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Feed('%s', '%s', '%s', '%s')>" % (self.id, 
                                                   self.model,
                                                   self.foreign_id,
                                                   self.created)
