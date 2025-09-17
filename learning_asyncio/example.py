import asyncio
import datetime
from time import sleep

a = list()


async def download_task():
    print("Downloading...")
    a.append(("download", str(datetime.datetime.now())))
    await asyncio.sleep(10)
    a.append(("download after sleep", str(datetime.datetime.now())))


async def download_file():
    await download_task()
    print("Downloading completed")


async def log_activity():
    print("Logging...")
    a.append(("logging before sleep", str(datetime.datetime.now())))
    await asyncio.sleep(2)
    a.append(("logging after sleep", str(datetime.datetime.now())))


def normal():
    for i in range(10):
        a.append((f"normal_{i}", str(datetime.datetime.now())))
        print(f"Normal-{i}.")


async def main():
    download_task = asyncio.create_task(download_file())
    log_task = asyncio.create_task(log_activity())

    await log_task
    normal()

    await download_task


if __name__ == "__main__":
    asyncio.run(main())
    for i in a:
        print(i)
