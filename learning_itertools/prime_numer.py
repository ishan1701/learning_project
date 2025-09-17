def if_pn(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primenumbers():
    start = 1
    while True:
        if if_pn(start):
            yield start
        start += 1


if __name__ == "__main__":
    primes = get_primenumbers()
    print(next(primes), end=" ")
    print(next(primes), end=" ")
    print(next(primes), end=" ")
    print(next(primes), end=" ")
    print(next(primes), end=" ")
    print(next(primes), end=" ")
    print(next(primes), end=" ")

    for i in range(100):
        print(next(primes))
