import uuid

from sqlalchemy import Column, MetaData
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()
Base.metadata = MetaData(schema="public")


class WithId:
    __abstract__ = True

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
