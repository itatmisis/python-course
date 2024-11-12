from repository.link_repository import LinkRepository
from utils.utils_random import random_alfanum


class ShortLinkService:
    def __init__(self) -> None:
        self.link_repository = LinkRepository()

    async def put_link(self, long_link: str) -> str:
        short_link = random_alfanum(10)

        await self.link_repository.put_link(short_link=short_link, long_link=long_link)

        return short_link

    async def get_real_link(self, short_link: str) -> str | None:
        return await self.link_repository.get_long_link(short_link=short_link)
