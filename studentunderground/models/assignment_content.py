from studentunderground.models.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

class AssignmentContentModel(Base):
    __tablename__ = 'assignment_contents'

    id = Column(Integer, primary_key=True)
    content = Column(String(2000))
    edited = Column(DateTime)
    assignment_id = Column(Integer, ForeignKey('assignment_infos.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AssignmentContent('%s', '%s', '%s', '%s')>" % (self.id, 
                                                         self.content,
                                                         self.edited,
                                                         self.assignment_id)
