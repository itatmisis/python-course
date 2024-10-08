from utils.utils_random import random_alfanum


class ShortLinkService:
    def __init__(self) -> None:
        self.our_link_to_real_link: dict[str, str] = {}

    def put_link(self, link: str) -> str:
        short_link = random_alfanum(10)
        self.our_link_to_real_link[short_link] = link

        return short_link

    def get_real_link(self, link: str) -> str | None:
        return self.our_link_to_real_link.get(link)
