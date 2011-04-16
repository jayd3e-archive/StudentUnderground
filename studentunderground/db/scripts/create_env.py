from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
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

        users_groups = Table('users_groups', metadata,
                             Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
                             Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True)
        )
        
        users_networks = Table('users_networks', metadata,
                             Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
                             Column('network_id', Integer, ForeignKey('networks.id'), primary_key=True)
        )

        acl_users_groups = Table('acl_users_groups', metadata,
                             Column('acl_user_id', Integer, ForeignKey('acl_users.id'), primary_key=True),
                             Column('acl_group_id', Integer, ForeignKey('acl_groups.id'), primary_key=True)
        )

        acl_users  = Table('acl_users', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('email', String(50)),
                      Column('identifier', String(50)),
                      Column('password', String(40)),
                      mysql_engine='InnoDB',
                      mysql_charset='utf8'
        )

        acl_groups = Table('acl_groups', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('name', String(50)),
                       mysql_engine='InnoDB',
                       mysql_charset='utf8'
        )

        users = Table('users', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('email', String(50)),
                      Column('first_name', String(50)),
                      Column('last_name', String(50)),
                      Column('acl_user_id', Integer)
        )

        profiles = Table('user_profiles', metadata,
                         Column('id', Integer, primary_key=True),
                         Column('created', DateTime),
                         Column('edited', DateTime),
                         Column('user_id', Integer),
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

        groups = Table('groups', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String(100)),
                        Column('created', DateTime),
                        Column('edited', DateTime),
                        Column('network_id', Integer),
                        mysql_engine='InnoDB',
                        mysql_charset='utf8'

        )

        feed = Table('feed', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('model', String(100)),
                     Column('foreign_id', Integer),
                     Column('created', DateTime)
        )

        assignment_infos = Table('assignment_infos', metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('name', String(100)),
                                 Column('created', DateTime),
                                 Column('group_id', Integer),
                                 mysql_engine='InnoDB',
                                 mysql_charset='utf8'

        )

        assignment_contents = Table('assignment_contents', metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('content', String(2000)),
                                    Column('edited', DateTime),
                                    Column('assignment_id', Integer),
                                    mysql_engine='InnoDB',
                                    mysql_charset='utf8'
        )

        assignment_comments = Table('assignment_comments', metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('user_id', Integer),
                                    Column('content', String(1000)),
                                    Column('created', DateTime),
                                    Column('assignment_id', Integer),
                                    mysql_engine='InnoDB',
                                    mysql_charset='utf8'
        )

        article_infos = Table('article_infos', metadata,
                              Column('id', Integer, primary_key=True),
                              Column('name', String(100)),
                              Column('created', DateTime),
                              Column('group_id', Integer),
                              mysql_engine='InnoDB',
                              mysql_charset='utf8'
        )

        article_contents = Table('article_contents', metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('content', String(2000)),
                                 Column('edited', DateTime),
                                 Column('assignment_id', Integer),
                                 mysql_engine='InnoDB',
                                 mysql_charset='utf8'
        )

        article_comments = Table('article_comments', metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('user_id', Integer),
                                 Column('content', String(1000)),
                                 Column('created', DateTime),
                                 Column('assignment_id', Integer),
                                 mysql_engine='InnoDB',
                                 mysql_charset='utf8'
        )

        acl_users_groups.create()
        users_groups.create()
        users_networks.create()
        acl_users.create()
        acl_groups.create()
        users.create()
        profiles.create()
        networks.create()
        groups.create()
        feed.create()
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
