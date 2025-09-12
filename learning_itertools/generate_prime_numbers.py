def _is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def _generate_prime_numbers():
    start = 2
    while (
        True
    ):  # this is not an infinite loop and will be executed only when the next is called
        if _is_prime(start):
            yield start
        start += 1


if __name__ == "__main__":
    primes = _generate_prime_numbers()
    for i in range(500):
        print(next(primes))
