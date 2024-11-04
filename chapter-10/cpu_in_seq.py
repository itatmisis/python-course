import math
import time


def pow_ten(v: int) -> float:
    vsum = 0
    for _ in range(100_000):
        vsum += math.sin(math.sqrt((v + 100) ** 10))

    return vsum


amount = 50
print_step = 5


def main():
    t0 = time.monotonic()
    for i in range(amount):
        pow_ten(i)

        if i % print_step == 0:
            print(f"{i} done")

    dur = (time.monotonic() - t0) * 1000
    print(f"Executed in {dur:.5f}ms, {dur/amount:.5f}ms per func")


if __name__ == "__main__":
    main()
