import os
import time
from pathlib import Path


def pow_ten(v: int) -> None:
    for i in range(10):
        path = Path(f"/tmp/{v}_{i}.txt")  # noqa: S108
        try:  # noqa: SIM105
            os.unlink(path)
        except Exception:
            ...

        with open(path, "w") as f:
            f.write("Hi!")

        os.unlink(path)


amount = 5000
print_step = 500


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
