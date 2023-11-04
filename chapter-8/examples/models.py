"""
CREATE TABLE book(
    book_id INTEGER,  --PRIMARY KEY AUTOINCREMENT
    title  VARCHAR(50),
    author  VARCHAR(30),
    price  DECIMAL(8, 2),
    amount  INT
)
"""
from sqlalchemy import Column, Integer, String, Numeric

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    author = Column(String(30))
    price = Column(Numeric(8, 2))
    amount = Column(Integer)


Base.metadata.create_all(bind=engine)


