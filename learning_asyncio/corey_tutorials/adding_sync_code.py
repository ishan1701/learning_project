import asyncio
from time import sleep


async def download_file(file_id):
    print(f"Starting download for file {file_id}...")
    await asyncio.sleep(10)
    print(f"Downloading file  completed for {file_id}...")
    return f"File {file_id} content"


async def log_activity():
    for i in range(5):
        print(f"Logging activity {i + 1}...")
        await asyncio.sleep(6)  # Simulate doing some other work
        print(f"Logged activity completed for {i + 1}...")


def sync_function(msg: str):
    print(f"Syncing function started. with {msg}")
    for i in range(10000):
        pass
    print("Syncing function finished")


async def main():
    sync_function(msg="first call")
    download_task = asyncio.create_task(download_file(1))
    log_task = asyncio.create_task(log_activity())
    ## here the event loop will run both the tasks concurrently
    sync_function(msg="after starting tasks")
    await download_task
    sync_function(msg="after awaiting download task")
    await log_task

    sync_function(msg="after awaiting for logging task")

    print("All done")


if __name__ == "__main__":
    asyncio.run(main())
    sync_function(msg="final call after event loop")
