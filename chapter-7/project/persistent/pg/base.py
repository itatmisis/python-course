from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, Double, MetaData, Text
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()
Base.metadata = MetaData(schema="public")


class WithId:
    __abstract__ = True

    id = Column(Text, default=uuid.uuid4, primary_key=True)


class WithCreatedAt:
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)


class WithUpdatedAt:
    __abstract__ = True

    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
