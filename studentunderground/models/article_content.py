from studentunderground.models.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

class ArticleContentModel(Base):
    __tablename__ = 'article_contents'

    id = Column(Integer, primary_key=True)
    content = Column(String(2000))
    edited = Column(DateTime)
    article_id = Column(Integer, ForeignKey('article_infos.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<ArticleContent('%s', '%s', '%s', '%s')>" % (self.id,
                                                             self.content,
                                                             self.edited,
                                                             self.article_id)
