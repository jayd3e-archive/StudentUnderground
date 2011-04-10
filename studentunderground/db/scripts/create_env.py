from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from studentunderground.db.config import DbConfig
from studentunderground.db.config import TestConfig

class CreateEnv(object):
    def __init__(self):
        pass

    def create_db(self, config):
        create = config.engine + '://'

        if config.user:
            create += config.user
        elif config.file:
            create += config.file

        if config.pw:
            create += ':' + config.pw
        if config.host:
            create += '@' + config.host
        if config.db:
            create += '/' + config.db

        self.db = create_engine(create, pool_recycle=3600)

    def create_schema(self):
        metadata = MetaData(self.db)

        users  = Table('users', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('email', String(50)),
                      Column('first_name', String(50)),
                      Column('last_name', String(50)),
                      Column('password', String(40)),
                      mysql_engine='InnoDB',
                      mysql_charset='utf8'
        )

        groups = Table('groups', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('name', String(50)),
                       mysql_engine='InnoDB',
                       mysql_charset='utf8'
        )

        profiles = Table('user_profiles', metadata,
                         Column('id', Integer, primary_key=True),
                         Column('created', DateTime),
                         Column('edited', DateTime),
                         mysql_engine='InnoDB',
                         mysql_charset='utf8'
        )

        networks = Table('networks', metadata,
                         Column('id', Integer, primary_key=True),
                         Column('name', String(100)),
                         Column('created', DateTime),
                         Column('edited', DateTime),
                         mysql_engine='InnoDB',
                         mysql_charset='utf8'

        )

        classes = Table('classes', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String(100)),
                        Column('created', DateTime),
                        Column('edited', DateTime),
                        mysql_engine='InnoDB',
                        mysql_charset='utf8'

        )

        assignment_infos = Table('assignment_infos', metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('name', String(100)),
                                 Column('created', DateTime),
                                 mysql_engine='InnoDB',
                                 mysql_charset='utf8'

        )

        assignment_contents = Table('assignment_contents', metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('content', String(2000)),
                                    Column('edited', DateTime),
                                    mysql_engine='InnoDB',
                                    mysql_charset='utf8'
        )

        assignment_comments = Table('assignment_comments', metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('user_id', Integer),
                                    Column('content', String(1000)),
                                    Column('created', DateTime),
                                    mysql_engine='InnoDB',
                                    mysql_charset='utf8'
        )

        article_infos = Table('article_infos', metadata,
                              Column('id', Integer, primary_key=True),
                              Column('name', String(100)),
                              Column('created', DateTime),
                              mysql_engine='InnoDB',
                              mysql_charset='utf8'

        )

        article_contents = Table('article_contents', metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('content', String(2000)),
                                 Column('edited', DateTime),
                                 mysql_engine='InnoDB',
                                 mysql_charset='utf8'

        )

        article_comments = Table('article_comments', metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('user_id', Integer),
                                 Column('content', String(1000)),
                                 Column('created', DateTime),
                                 mysql_engine='InnoDB',
                                 mysql_charset='utf8'
        )

        users.create()
        groups.create()
        profiles.create()
        networks.create()
        classes.create()
        assignment_infos.create()
        assignment_contents.create()
        assignment_comments.create()
        article_infos.create()
        article_contents.create()
        article_comments.create()

if __name__ == '__main__':
    c = CreateEnv()
    c.create_db(DbConfig)
    c.create_schema()
