from database import engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)  # noqa: A003
    name = Column(String(50))


Base.metadata.create_all(bind=engine)
