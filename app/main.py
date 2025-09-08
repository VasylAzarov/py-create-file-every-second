from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour:02}_{now.minute:02}_{now.second:02}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
