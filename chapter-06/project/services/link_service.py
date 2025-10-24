from repositories.link_repository import LinkRepository
from utils.utils_random import random_alfanum


class LinkService:
    def __init__(self) -> None:
        self._link_repository = LinkRepository()

    async def create_link(self, real_link: str) -> str:
        short_link = random_alfanum(5)

        await self._link_repository.create_link(short_link, real_link)

        return short_link

    async def get_real_link(self, short_link: str) -> str | None:
        link = await self._link_repository.get_link(short_link=short_link)
        if link is None:
            return None

        return str(link.real_link)
