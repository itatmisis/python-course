from sqlalchemy import create_engine
from sqlalchemy.dialects import sqlite
from sqlalchemy.sql import Executable

SQLALCHEMY_DATABASE_URL = "sqlite:///../database.sqlite3"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


def print_statement(statement: Executable) -> None:
    print(statement.compile(dialect=sqlite.dialect(), compile_kwargs={"literal_binds": True}))
