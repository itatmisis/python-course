from utils.utils_random import random_alfanum
from repository.link_repository import LinkRepository


class ShortLinkService:
    def __init__(self) -> None:
        self.link_repository = LinkRepository()

    async def put_link(
        self,
        long_link: str,
        created_by_ip: str,
        created_by_user_agent: str,
    ) -> str:
        short_link = random_alfanum(10)

        await self.link_repository.put_link(
            short_link=short_link,
            long_link=long_link,
            created_by_ip=created_by_ip,
            created_by_user_agent=created_by_user_agent,
        )

        return short_link

    async def get_real_link(
        self,
        short_link: str,
        user_ip: str,
        user_agent: str,
    ) -> str | None:
        link = await self.link_repository.get_real_link(short_link=short_link)

        if link is not None:
            await self.link_repository.set_link_usage(link_id=link.id, user_ip=user_ip, user_agent=user_agent)

            return str(link.long_link)

        return None
