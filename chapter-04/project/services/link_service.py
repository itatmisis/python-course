from utils.utils_random import random_alfanum


class LinkService:
    def __init__(self) -> None:
        self.short_link_to_real_link: dict[str, str] = {}

    def create_link(self, link: str) -> str:
        short_link = random_alfanum(5)
        self.short_link_to_real_link[short_link] = link

        return short_link

    def get_real_link(self, link: str) -> str | None:
        return self.short_link_to_real_link.get(link)
