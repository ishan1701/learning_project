# older ways
import threading
import time
from datetime import datetime
from threading import Thread
def return_dict(loop: int):
    start_time = datetime.now()
    print(f'started with thread number {loop} and the start time is {start_time} ')
    key_dict = {}
    for i in range(loop):
        key_dict[i] = i * i
    print(f'sleeping for {loop} thread for {loop} seconds and the start time is {datetime.now()} ')
    time.sleep(loop)
    print(f'waking for {loop} thread for {loop} seconds and the end time is {datetime.now()} ')
    print(key_dict)
    end_time = datetime.now()
    print(f'ended with thread number {loop} with time taken is {end_time - start_time} ')
    return key_dict


if __name__ == '__main__':
    pgm_start_time = datetime.now()
    data_list = []

    for i in range(1,5):
        data_list.append(i)

    threads = []
    for data in data_list:
        t=threading.Thread(target=return_dict, args=[data])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    pgm_end_time = datetime.now()
    print(f'total time taken by program is {pgm_end_time-pgm_start_time}')


