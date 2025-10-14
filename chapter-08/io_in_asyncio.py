import asyncio
import time
from pathlib import Path

import aiofiles  # pip install aiofiles
from aiofiles import os


async def pow_ten(v: int) -> None:
    for i in range(10):
        path = Path(f"/tmp/{v}_{i}.txt")  # noqa: S108
        try:  # noqa: SIM105
            await os.unlink(path)
        except Exception:
            ...

        async with aiofiles.open(path, "w") as f:
            await f.write("Hi!")

        await os.unlink(path)


amount = 5000
print_step = 500


async def main():
    t0 = time.monotonic()
    futures: list[asyncio.Future] = []
    for i in range(amount):
        futures.append(asyncio.create_task(pow_ten(i)))

    dur = (time.monotonic() - t0) * 1000
    print(f"Submited in {dur:.5f}ms, {dur/amount:.5f}ms per func")

    t0 = time.monotonic()
    await asyncio.gather(*futures)

    dur = (time.monotonic() - t0) * 1000
    print(f"Executed in {dur:.5f}ms, {dur/amount:.5f}ms per func")


if __name__ == "__main__":
    asyncio.run(main())
