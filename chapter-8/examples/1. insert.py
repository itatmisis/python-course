"""
INSERT INTO tableName (col1, col2, ...colN) VALUES (val1, val2, ...valN)
"""
from sqlalchemy import insert
from sqlalchemy.orm import Session

from models import Book
from database import engine

query = insert(Book).values(title='Мастер и Маргарита', author='Булгаков М.А.',
                            price=670.99, amount=3)
print(query)
with Session(engine) as session:
    result = session.execute(query)
    print(result.inserted_primary_key)
    session.commit()
