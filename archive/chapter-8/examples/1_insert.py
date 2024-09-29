"""
INSERT INTO tableName (col1, col2, ...colN) VALUES (val1, val2, ...valN)
"""

import random

from database import engine, print_statement
from models import Book
from sqlalchemy import insert
from sqlalchemy.orm import Session

titles = [
    ("I Know Why The Caged Bird Sings", "Maya Angelou"),
    ("East of Eden", "John Steinbeck"),
    ("The Sun Also Rises", "Ernest Hemingway"),
    ("Do Androids Dream of Electric Sheep?", "Philip K. Dick"),
    ("The Curious Incident of the Dog in the Night-Time", "Mark Haddon"),
    ("Cloudy with a Chance of Meatballs", "Judi Barrett"),
    ("Pride and Prejudice and Zombies", "Seth Grahame-Smith"),
    ("The House of Mirth", "Edith Wharton"),
    ("Are You There, Vodka? It's Me, Chelsea", "Chelsea Handler"),
    ("And Then There Were None", "Agatha Christie"),
    ("Their Eyes Were Watching God", "Zora Neale Hurston"),
    ("The Devil Wears Prada", "Lauren Weisberger"),
    ("Brave New World", "Aldous Huxley"),
    ("Bury My Heart at Wounded Knee", "Dee Brown"),
    ("The Man Who Was Thursday", "G.K. Chesterton"),
]

with Session(engine) as session:
    for _ in range(random.randint(10, 30)):  # noqa: S311
        book, author = random.choice(titles)  # noqa: S311
        statement = insert(Book).values(
            title=book,
            author=author,
            price=random.randint(100, 1000),  # noqa: S311
            amount=random.randint(0, 20),  # noqa: S311
        )
        print_statement(statement)
        result = session.execute(statement)
        print(result.inserted_primary_key)
        session.commit()
