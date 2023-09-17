import random

import launcher


def launch(amount: int) -> None:
    for i in range(amount):
        print(f"Launched rocket {i=}")
        launcher.launch_rocket(random.randint(2, 4))  # noqa: S311


if __name__ == "__main__":
    launch(10)
