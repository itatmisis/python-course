"""
UPDATE book
SET price = 0.7 * price;
SELECT * FROM book;
"""
from sqlalchemy import update
from sqlalchemy.orm import Session

from database import engine, print_statement
from models import Book

query = update(Book).values(price=Book.price * 0.7)
print_statement(query)
with Session(engine) as session:
    result = session.execute(query)
    session.commit()
    print(result.rowcount)
