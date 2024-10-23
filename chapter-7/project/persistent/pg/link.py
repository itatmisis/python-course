from persistent.pg.base import WithId, WithCreatedAt, WithUpdatedAt, Base
from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, Double, MetaData, Text
from sqlalchemy.orm import declarative_base


class Link(Base, WithId, WithCreatedAt, WithUpdatedAt):
    __tablename__ = "link"

    short_link = Column(Text, nullable=False, unique=True)
    long_link = Column(Text, nullable=False)

    created_by_ip = Column(Text, nullable=False)
    created_by_user_agent = Column(Text, nullable=False)


class LinkUsage(Base, WithId, WithCreatedAt):
    __tablename__ = "link_usage"

    link_id = Column(Text, nullable=False)

    user_ip = Column(Text, nullable=False)
    user_agent = Column(Text, nullable=False)
