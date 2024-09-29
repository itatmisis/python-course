"""
SELECT author, title, price FROM book
"""

from database import engine, print_statement
from models import Book
from sqlalchemy import select
from sqlalchemy.orm import Session

query = select(Book)
print("multiple rows")
print_statement(query)
with Session(engine) as session:
    rows = session.execute(query).scalars()

    for book in rows:
        print(book.id, book.title, book.price)


print("single row")
with Session(engine) as session:
    row = session.execute(select(Book).limit(1)).scalar()
    if row is None:
        print("Not found")
    else:
        print(row.id, row.title, row.price)
