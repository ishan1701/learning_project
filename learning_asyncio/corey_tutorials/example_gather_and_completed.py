import asyncio
from collections import (
    OrderedDict,  # with 3.7 version the normal dict is ordered by default
)
from datetime import datetime
from time import sleep

time_dict: OrderedDict = OrderedDict()


async def download_file(time_to_download: int = 10):
    start_time = datetime.now()
    print(f"downloading file with {time_to_download} seconds")
    await asyncio.sleep(time_to_download)
    print(f"downloaded file completed with {time_to_download}")
    end_time = datetime.now()
    time_dict[f"download_{time_to_download}"] = {"start": start_time, "end": end_time}


async def log_activity(time_to_log: int = 1):
    start_time = datetime.now()
    print(f"logging activity with {time_to_log} seconds")
    await asyncio.sleep(time_to_log)
    print(f"logged activity completed for {time_to_log}")
    end_time = datetime.now()
    time_dict[f"log_{time_to_log}"] = {"start": start_time, "end": end_time}


async def start_event_loop_with_gather():
    """
    Use when you have several independent tasks and you want to run them all together, but only care about the results once all are ready.

    Results come back in the same order you passed them.

    Example: fetch three APIs in parallel and then combine their responses.

    """
    tasks = list()
    download_task = asyncio.create_task(download_file(time_to_download=10))
    log_task_1 = asyncio.create_task(log_activity(time_to_log=10))
    log_task_2 = asyncio.create_task(log_activity(time_to_log=20))
    log_task_3 = asyncio.create_task(log_activity(time_to_log=30))

    tasks.append(download_task)
    tasks.append(log_task_1)
    tasks.append(log_task_2)
    tasks.append(log_task_3)

    await asyncio.gather(*tasks)
    print(f"started event loop")


async def start_event_loop_with_as_completed():
    """Use when you want to process results as soon as they’re ready, instead of waiting for the slowest one.

    Example: downloading 10 files and processing each immediately when it’s done."""
    tasks = list()
    download_task = asyncio.create_task(download_file(time_to_download=10))
    log_task_1 = asyncio.create_task(log_activity(time_to_log=10))
    log_task_2 = asyncio.create_task(log_activity(time_to_log=20))
    log_task_3 = asyncio.create_task(log_activity(time_to_log=30))

    tasks.append(download_task)
    tasks.append(log_task_1)
    tasks.append(log_task_2)
    tasks.append(log_task_3)

    for completed in asyncio.as_completed(tasks):
        await completed


if __name__ == "__main__":
    # asyncio.run(start_event_loop_with_gather())
    asyncio.run(start_event_loop_with_as_completed())
    print(time_dict)
