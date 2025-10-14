from persistent.db.base import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

_url = "/sql_app.db"


def sqlite_connection() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(f"sqlite+aiosqlite://{_url}", connect_args={"check_same_thread": False})

    return async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_all_tables() -> None:
    engine = create_engine(f"sqlite://{_url}", connect_args={"check_same_thread": False})

    Base.metadata.create_all(engine)
