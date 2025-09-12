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
    secs_to_sleep = [3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 60]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(return_dict, sec) for sec in secs_to_sleep]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    pgm_end_time = datetime.now()
    print(f"the program execution time is {pgm_end_time - pgm_start_time}")
