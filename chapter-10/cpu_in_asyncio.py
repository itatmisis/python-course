import asyncio
import math
import time


async def pow_ten(v: int) -> float:
    vsum = 0
    for _ in range(100_000):
        vsum += math.sin(math.sqrt((v + 100) ** 10))

    return vsum


amount = 50
print_step = 5


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
