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
    print(key_dict)
    end_time = datetime.now()
    print(
        f"ended with thread number {loop} with time taken is {end_time - start_time} "
    )
    return key_dict


if __name__ == "__main__":
    start_pgm = datetime.now()
    print(start_pgm)
    secs = [1, 2, 3, 3, 2, 1]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(return_dict, loop) for loop in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    for result in results:
        print(result.result())

    end_pgm = datetime.now()
    print(f"the total execution time is {end_pgm - start_pgm}")

    print("________________________________________")

    # via map method

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(return_dict, secs)

    for result in results:
        print(result.values())
    print("second values")

    # The below code do not work
    # for f in concurrent.futures.as_completed(results):
    #     print(f)

    end_pgm = datetime.now()
    print(f"the total execution time is {end_pgm - start_pgm}")
