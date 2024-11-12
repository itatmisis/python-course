from infrastructure.db.connection import create_all_tables, sqlite_connection
from persistent.db.link import Link
from sqlalchemy import insert, select


class LinkRepository:
    def __init__(self) -> None:
        self._sessionmaker = sqlite_connection()
        create_all_tables()

    async def put_link(self, short_link: str, long_link: str) -> None:
        stmp = insert(Link).values({"short_link": short_link, "long_link": long_link})

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()

    async def get_long_link(self, short_link: str) -> str | None:
        stmp = select(Link.long_link).where(Link.short_link == short_link).limit(1)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)

        row = resp.fetchone()
        if row is None:
            return None

        return row[0]
