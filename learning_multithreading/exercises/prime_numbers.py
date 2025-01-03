import concurrent.futures
from datetime import datetime


def is_prime(n: int, value_dict):
    print(f'from inside function the dict is {value_dict}')
    if type(n) != int:
        raise TypeError(f'{n} must be an integer')
    if n <= 1:
        value_dict[n] = False
        return value_dict
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            value_dict[n] = False
            return value_dict
    value_dict[n] = True
    return value_dict


if __name__ == '__main__':

    start_time = datetime.now()
    value_dict = {}
    nums = []
    for i in range(10):
        nums.append(i)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(lambda num: is_prime(num, value_dict), nums)

    for result in results:
        print(result)
        print(type(result))
    end_time = datetime.now()

    print(f'Time taken to execute the code is {end_time - start_time}')
