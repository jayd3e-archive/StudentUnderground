from studentunderground.models.base import Base
from studentunderground.models.article_content import ArticleContentModel
from studentunderground.models.article_comment import ArticleCommentModel
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class ArticleInfoModel(Base):
    __tablename__ = 'article_infos'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    created = Column(DateTime)
    group_id = Column(Integer, ForeignKey('groups.id'))
    contents = relationship(ArticleContentModel,
                            backref="info")
    comments = relationship(ArticleCommentModel,
                            backref="info")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<ArticleInfo('%s', '%s', '%s', '%s')>" % (self.id,
                                                          self.name,
                                                          self.created,
                                                          self.group_id)
