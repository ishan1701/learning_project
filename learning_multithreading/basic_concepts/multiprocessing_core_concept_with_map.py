import concurrent.futures
import time
from datetime import datetime


def return_dict(loop: int):
    start_time = datetime.now()
    print(f"started with thread number {loop} and the start time is {start_time} ")
    key_dict = {}
    for i in range(loop):
        key_dict[i] = i * i
    print(
        f"sleeping for {loop} thread for {loop} seconds and the start time is {datetime.now()} "
    )
    time.sleep(loop)
    print(
        f"waking for {loop} thread for {loop} seconds and the end time is {datetime.now()} "
    )
    end_time = datetime.now()
    print(
        f"ended with thread number {loop} with time taken is {end_time - start_time} "
    )
    return key_dict


if __name__ == "__main__":
    pgm_start_time = datetime.now()
    print(f"the program started at {pgm_start_time}")
    secs_to_sleep = []
    for i in range(1, 100):
        secs_to_sleep.append(i)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(return_dict, secs_to_sleep)

    for res in results:
        print(res)

    pgm_end_time = datetime.now()
    print(f"the program execution time is {pgm_end_time - pgm_start_time}")
