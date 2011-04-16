from studentunderground.models.base import Base
from studentunderground.models.assignment_info import AssignmentInfoModel
from studentunderground.models.article_info import ArticleInfoModel
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class GroupModel(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    created = Column(DateTime)
    edited = Column(DateTime)
    network_id = Column(Integer, ForeignKey('networks.id'))
    assignments = relationship(AssignmentInfoModel,
                               backref="group")
    articles = relationship(ArticleInfoModel,
                            backref="group")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Group('%s', '%s', '%s', '%s', '%s')>" % (self.id, 
                                                          self.name,
                                                          self.created,
                                                          self.edited,
                                                          self.network_id)
