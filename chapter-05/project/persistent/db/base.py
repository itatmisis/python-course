import uuid

from sqlalchemy import Column, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()
# Base.metadata = MetaData(schema="public")


def _uuid4_as_str() -> str:
    return str(uuid.uuid4())


class WithId:
    __abstract__ = True

    id = Column(Text, default=_uuid4_as_str, primary_key=True)
