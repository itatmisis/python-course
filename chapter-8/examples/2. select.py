"""
SELECT author, title, price FROM book
"""
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Book
from database import engine


query = select(Book)
print(query)
with Session(engine) as session:
    result = session.execute(query).all()
    for book in result:
        print(book[0].book_id, book[0].title)
