"""
DELETE FROM book;
"""
from sqlalchemy import delete
from sqlalchemy.orm import Session

from database import engine, print_statement
from models import Book

query = delete(Book)
print_statement(query)
with Session(engine) as session:
    result = session.execute(query)
    session.commit()
    print(result.rowcount)
