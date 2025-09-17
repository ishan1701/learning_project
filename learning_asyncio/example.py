import asyncio
import datetime
from time import sleep

a = list()


async def download_task():
    print("Downloading...")
    a.append(("download", str(datetime.datetime.now())))
    await asyncio.sleep(50)
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

    print("Done after the download task is complete.")


# 1. The download_task will be put in the event loop and will start executing.
# 2. The log_activity will also be put in the event loop and will start executing
# 3. The normal() function will be waited until the log_activity is done.
# 4. Now the download_task may have been completed or not.
# 5. if the download_task is not completed, the next print statement will wait until it is completed.

# Below is the expected output:
# (learning-project-py3.10) ➜  learning_asyncio git:(main) ✗ poetry run  python example.py
# Downloading...
# Logging...
# Normal-0.
# Normal-1.
# Normal-2.
# Normal-3.
# Normal-4.
# Normal-5.
# Normal-6.
# Normal-7.
# Normal-8.
# Normal-9.
# Downloading completed
# Done after the download task is complete.

if __name__ == "__main__":
    asyncio.run(main())
