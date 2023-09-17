import multiprocessing as mp
import random

import launcher


def launch(amount: int) -> None:
    args = [random.randint(2, 4) for _ in range(amount)]  # noqa: S311

    with mp.Pool() as p:
        p.map(launcher.launch_rocket, args)


if __name__ == "__main__":
    launch(10)
