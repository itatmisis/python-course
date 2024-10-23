from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import asyncio


def sqlite_connection() -> async_sessionmaker[AsyncSession]:
    url = "sqlite+aiosqlite:///sql_app.db"

    engine = create_async_engine(url, connect_args={"check_same_thread": False})
    return async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
