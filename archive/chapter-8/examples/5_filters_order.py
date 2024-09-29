"""
SELECT title, author, price
FROM book
WHERE amount >= 2
ORDER BY price
"""

from database import engine, print_statement
from models import Book
from sqlalchemy import select
from sqlalchemy.orm import Session

statement = select(Book.title, Book.author, Book.price).where(Book.amount >= 2).order_by(Book.price)
print_statement(statement)

with Session(engine) as session:
    rows = session.execute(statement).all()

    for row in rows:
        print(row)
