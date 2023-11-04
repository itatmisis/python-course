from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///../database.sqlite3"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
