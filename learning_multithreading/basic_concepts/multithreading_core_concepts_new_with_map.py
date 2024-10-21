import concurrent.futures
import time
from datetime import datetime


def return_dict(loop: int):
    # if loop == 2:
    #     raise ValueError('Some error')
    start_time = datetime.now()
    print(f'started with thread number {loop} and the start time is {start_time} ')
    key_dict = {}
    for i in range(loop):
        key_dict[i] = i * i
    print(f'sleeping for {loop} thread for {loop} seconds and the start time is {datetime.now()} ')
    time.sleep(loop)
    print(f'waking for {loop} thread for {loop} seconds and the end time is {datetime.now()} ')
    end_time = datetime.now()
    print(f'ended with thread number {loop} with time taken is {end_time - start_time} ')
    return key_dict


if __name__ == '__main__':
    secs = []
    start_pgm = datetime.now()
    for i in range(1, 100):
        secs.append(i)


    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(return_dict, secs)

    for result in results:
        print(result.values())

    end_pgm = datetime.now()
    print(f'the total execution time is {end_pgm - start_pgm}')
