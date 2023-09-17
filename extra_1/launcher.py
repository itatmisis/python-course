import time


def launch_rocket(minus_t: int) -> None:
    for count in range(minus_t, 0, -1):
        print(f"{count=}")
        time.sleep(1)
    print("Start!")


if __name__ == "__main__":
    launch_rocket(4)
