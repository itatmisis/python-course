import random
import time


def timeit(name: str, iters: int) -> None:
    results = []
    for _ in range(iters):
        list_ = list(range(10_000))
        item = random.randint(0, 10_000)

        t0 = time.monotonic_ns()

        list_.index(item)

        results.append(time.monotonic_ns() - t0)

    avg_dur = (sum(results) / len(results)) / 1_000

    print(f"{name}: {avg_dur:.2f}ms")


timeit("Find in list", 1000)
