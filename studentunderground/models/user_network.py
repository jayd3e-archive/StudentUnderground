from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from studentunderground.models.base import Base


UserNetworkModel = Table('users_networks', Base.metadata,
                       Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
                       Column('network_id', Integer, ForeignKey('networks.id'), primary_key=True)
)
