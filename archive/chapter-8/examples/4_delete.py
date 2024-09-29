"""
DELETE FROM book;
"""

from database import engine, print_statement
from models import Book
from sqlalchemy import delete
from sqlalchemy.orm import Session

query = delete(Book)
print_statement(query)
with Session(engine) as session:
    result = session.execute(query)
    session.commit()
    print(result.rowcount)
