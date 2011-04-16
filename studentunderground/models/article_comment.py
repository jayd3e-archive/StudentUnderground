from studentunderground.models.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

class ArticleCommentModel(Base):
    __tablename__ = 'article_comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    content = Column(String(1000))
    created = Column(DateTime)
    article_id = Column(Integer, ForeignKey('article_infos.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<ArticleComment('%s', '%s', '%s', '%s', '%s')>" % (self.id, 
                                                                   self.user_id,
                                                                   self.content,
                                                                   self.created,
                                                                   self.article_id)
