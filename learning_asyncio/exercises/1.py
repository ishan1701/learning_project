import asyncio
from random import randint
from datetime import datetime


async def run_task_a(sleep_time: int) -> str:
    start_time = datetime.now()
    print(f'Running task a at {start_time}')
    await asyncio.sleep(sleep_time)
    finish_time = datetime.now()
    print(f'Finished task a at {finish_time}')
    return f'{start_time} and  {finish_time}'


async def run_task_b(sleep_time: int) -> str:
    start_time = datetime.now()
    print(f'Running task b at {start_time}')
    await asyncio.sleep(sleep_time)
    finish_time = datetime.now()
    print(f'Finished task b at {finish_time}')
    return f'{start_time} and  {finish_time}'


async def run_task_c(sleep_time: int) -> str:
    start_time = datetime.now()
    print(f'Running task c at {start_time}')
    await asyncio.sleep(sleep_time)
    finish_time = datetime.now()
    print(f'Finished task c at {finish_time}')
    return f'{start_time} and  {finish_time}'


def print_number(caller: str = None):
    if caller is not None:
        print(caller)
    start_time = datetime.now()
    for i in range(2):
        print(i)
    end_time = datetime.now()
    print(f'loop started at {start_time}and finished at {end_time}')


async def run_tasks():
    '''
    Explanations:
        Here the a, b and c will go in the event loop
        now 3 print statements before the first await a statement will be executed, Because the other parts of
        code will be executed until the await tasks

        1. c task will be complete but the print statements will not be executed, why beacue event loop is still running?
        2. Once all the await tasks will be completed, print_number(caller='after A') after B and after c

        Then the pgm will continue as normal

    '''
    a = asyncio.create_task(run_task_a(30))
    print_number()
    b = asyncio.create_task(run_task_b(20))
    print_number()
    c = asyncio.create_task(run_task_c(10))
    print_number()

    a_return = await a
    print_number(caller='after A')

    b_return = await b

    print_number(caller='after B')
    c_return = await c
    print_number(caller='after C')

    print_number()
    print('after all the await')
    print_number()

    for a in (a_return, b_return, c_return):
        print(a)


if __name__ == '__main__':
    asyncio.run(run_tasks())
