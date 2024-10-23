from persistent.pg.link import Link, LinkUsage
from infrastructure.pg.connection import sqlite_connection
from sqlalchemy import insert, select


class LinkRepository:
    def __init__(self) -> None:
        self._sessionmaker = sqlite_connection()

    async def put_link(
        self,
        short_link: str,
        long_link: str,
        created_by_ip: str,
        created_by_user_agent: str,
    ) -> None:
        stmp = insert(Link).values(
            {
                "short_link": short_link,
                "long_link": long_link,
                "created_by_ip": created_by_ip,
                "created_by_user_agent": created_by_user_agent,
            }
        )
        async with self._sessionmaker() as session:
            await session.execute(stmp)

    async def get_real_link(self, short_link: str) -> Link | None:
        stmp = select(Link).where(Link.short_link == short_link).limit(1)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)

        row = resp.fetchone()
        if row is None:
            return None

        return row[0]

    async def set_link_usage(self, link_id: str, user_ip: str, user_agent: str) -> None:
        stmp = insert(LinkUsage).values(
            {
                "link_id": link_id,
                "user_ip": user_ip,
                "user_agent": user_agent,
            }
        )
        async with self._sessionmaker() as session:
            await session.execute(stmp)
