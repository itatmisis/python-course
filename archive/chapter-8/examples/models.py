"""
CREATE TABLE book(
    id INTEGER,  --PRIMARY KEY AUTOINCREMENT
    title  VARCHAR(50),
    author  VARCHAR(30),
    price  DECIMAL(8, 2),
    amount  INT
)
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)  # noqa: A003
    title = Column(String(50))
    author = Column(String(30))
    price = Column(Integer)
    amount = Column(Integer)
