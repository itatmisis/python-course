"""
SELECT title, author, price
FROM book
WHERE amount >= 2
ORDER BY price
"""
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Book
from database import engine


query = select(Book.title, Book.author, Book.price).where(Book.amount >= 2).order_by(Book.price)
print(query)
with Session(engine) as session:
    result = session.execute(query).all()
    for book in result:
        print(book)
