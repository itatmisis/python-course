"""
DELETE FROM book;
"""
from sqlalchemy import delete
from sqlalchemy.orm import Session

from models import Book
from database import engine


query = delete(Book)
print(query)
with Session(engine) as session:
    result = session.execute(query)
    session.commit()
    print(result.rowcount)
