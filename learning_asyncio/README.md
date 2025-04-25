
## what is asyncio
asyncio module is python module to run the program in an **event loop**. When I say event loop it means its an 
loop which takes multiple routines or await task at a time and run them in a loop. Now it doesnt means that I run once after another.
Lets say all the routines has the wait condition where it waits for an IO operation to get completed. 
lets say download a file from s3 bucket.

```for example
    a = asyncio.create_task(run_task_a(30))
    print_number()
    b = asyncio.create_task(run_task_b(20))
    print_number()
    c = asyncio.create_task(run_task_c(10))
    print_number()
   ```
a, b and c will be started and the print statements will be executed. Because no await has come yet.

Now,
```    
    a_return = await a
    print_number(caller='after A')

    b_return = await b

    print_number(caller='after B')
    c_return = await c
    print_number(caller='after C')
   ```

all the print statements will be waited until await completes

## how it is different from multithreading
* Multithreading is a concept to run multiple threads in a single process sharing the same memory space.
* the context will be switched between the threads. So only one thread will be running at a time
* The  variable like dict can be shared which require thread safe.
* 
* However, asyncio should be used where ever possible as compared to threads.

## how its different to multiprocessing

## how spark beam is multiprocessing
Multiprocessing in distributed systems like Apache Spark and Apache Beam refers to executing multiple independent processes concurrently to process large datasets in parallel. These processes typically run on multiple CPU cores or machines in a cluster, with each process handling a portion of the data. Unlike multithreading, which shares memory within a single process, multiprocessing uses separate processes with isolated memory, enabling true parallelism even for CPU-bound tasks.
* Data Partitioning: Spark divides data into partitions (logical chunks of an RDD or DataFrame) distributed across nodes in a cluster.
* Executor Processes: Spark runs executors, which are standalone JVM processes, typically one per node or allocated CPU cores. Each executor can process multiple partitions in parallel.
* Task Parallelism: Spark’s scheduler breaks jobs into stages and tasks. Each task processes one partition and runs in a separate process within an executor. Multiple tasks run concurrently across executors, leveraging multiprocessing.
* Cluster Manager: A cluster manager (e.g., YARN, Kubernetes, or Spark’s standalone mode) allocates resources and schedules tasks across nodes, ensuring tasks run in parallel processes on different machines or cores.
* Example: If you have a 1TB dataset split into 100 partitions on a 10-node cluster, Spark assigns partitions to executors. Each executor runs tasks as separate processes to process its partitions, achieving parallelism across nodes
## main asyncio commands

### async 
This keyword is used to declare a function as subroutine

### await
This keyword is used to wait the subroutine to complete. 
Note that to await should be used with async defined.

```aiignore
    async def run_task_c(sleep_time: int) -> str:
    start_time = datetime.now()
    print(f'Running task c at {start_time}')
    await asyncio.sleep(sleep_time)
    finish_time = datetime.now()
    print(f'Finished task c at {finish_time}')
    return f'{start_time} and  {finish_time}'
```
it will also be used in the event loop function
a_return = await a
### create_task()
it is used to summit a task to eventloop

### gather()
This is one line statement to put tasks to event loop

so in place of below
```    
    a = asyncio.create_task(run_task_a(30))
    b = asyncio.create_task(run_task_b(20))
    c = asyncio.create_task(run_task_c(10))
   ```
I can put a single gather statement
```aiignore

    (a_return, b_return, c_return)= await asynco.gather(run_task_a(30), run_task_b(20), run_task_c(10))
```

### runs()
its used inside normal function to all subroute.
so lets say if i have the below 
```aiignore

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
    b = asyncio.create_task(run_task_b(20))
    c = asyncio.create_task(run_task_c(10))
```

now this routine submits other subroutines. I need to call this like below
```aiignore
    
    if __name__ == '__main__':
    asyncio.run(run_tasks())
    
```


### sleep()
its a method inside the asyncio package. Its is used to sleep the subroute. However, it returns
return await future

It should be used rather than normal sleep.

### wait()

### wait_for()

### as_completed()

### TimeoutError

### to_thread()

### run_in_executor()

### to_thread()


