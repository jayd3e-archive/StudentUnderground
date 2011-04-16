from studentunderground.models.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

class ProfileModel(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created = Column(DateTime)
    edited = Column(DateTime)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Profile('%s', '%s', '%s')>" % (self.id,
                                                self.created,
                                                self.edited)
