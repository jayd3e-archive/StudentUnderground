from studentunderground.models.base import Base
from studentunderground.models.assignment_content import AssignmentContentModel
from studentunderground.models.assignment_comment import AssignmentCommentModel
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class AssignmentInfoModel(Base):
    __tablename__ = 'assignment_infos'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    created = Column(DateTime)
    group_id = Column(Integer, ForeignKey('groups.id'))
    contents = relationship(AssignmentContentModel,
                            backref="info")
    comments = relationship(AssignmentCommentModel,
                            backref="info")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AssignmentInfo('%s', '%s', '%s', '%s')>" % (self.id,
                                                             self.name,
                                                             self.created,
                                                             self.group_id)
