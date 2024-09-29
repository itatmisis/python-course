from collections.abc import Generator

from settings import settings
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///../database.sqlite3"
SQLALCHEMY_DATABASE_URL = f"postgresql://db_main:db_main@{settings.db_host}:5432/db_main"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


def get_db() -> Generator[Session, None, None]:
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)  # noqa: A003
    name = Column(String(50))
