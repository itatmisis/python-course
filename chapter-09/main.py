import requests
import time
from concurrent.futures import ThreadPoolExecutor, Future
from multiprocessing import Process, Queue
import asyncio
import httpx
import threading

urls = [
    "https://misis.ru",
    "https://edu.itatmisis.ru/",
    "https://ya.ru",
    "https://google.com",
    "https://python.org",
    "https://go.dev",
    "https://rust-lang.org/",
]

async def check(url: str) -> str:
    t0 = time.monotonic_ns()
    async with httpx.AsyncClient() as client:
        await client.head(url, timeout=10)
    total = (time.monotonic_ns() - t0) / 1_000_000

    print(f'Elapsed {url=} {total=:.2f}ms')

    if "misis" in url:
        raise Exception("ОШИБКА!")
    else: 
        return "OK"

async def main() -> None:
    tasks: list[asyncio.Task] = []

    for url in urls:
        tasks.append(asyncio.create_task(check(url)))

    results = await asyncio.gather(*tasks, return_exceptions=True)
    for result in results:
        if isinstance(result, Exception):
            print("Вернулась ошибка")
            continue

        print(f"Ошибки нет: {result}")
    


if __name__ == "__main__":
    asyncio.run(main())

    

