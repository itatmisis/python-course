from persistent.db.base import Base, WithId
from sqlalchemy import Column, Text


class Link(Base, WithId):
    __tablename__ = "link"

    short_link = Column(Text, nullable=False, unique=True)
    long_link = Column(Text, nullable=False)
