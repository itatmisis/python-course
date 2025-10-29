from persistent.link import Base
from settings.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


def connection() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(
        f"postgresql+asyncpg://{settings.pg.username}:{settings.pg.password}@"
        f"{settings.pg.host}:{settings.pg.port}/{settings.pg.database}"
    )

    return async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_all_tables() -> None:
    engine = create_engine(
        f"postgresql://{settings.pg.username}:{settings.pg.password}@"
        f"{settings.pg.host}:{settings.pg.port}/{settings.pg.database}"
    )

    Base.metadata.create_all(engine)
