import multiprocessing as mp
import random

import launcher


def launch(amount: int):
    args = [random.randint(2, 4) for _ in range(amount)]

    with mp.Pool() as p:
        p.map(launcher.launch_rocket, args)


if __name__ == "__main__":
    launch(10)
