from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from database import engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


Base.metadata.create_all(bind=engine)
