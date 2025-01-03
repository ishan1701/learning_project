def _get_next_fib(prev, current):
    return current + prev


def _create_fibonacci_sequence():
    start_elements = [0, 1]
    prev, current = start_elements[0], start_elements[-1]
    yield from start_elements

    while True:  # this is not an infinite loop and will be executed only when the next is called
        next = _get_next_fib(prev=prev, current=current)
        yield next
        prev = current
        current = next



if __name__ == '__main__':
    series = _create_fibonacci_sequence()
    for i in range(7):
        print(next(series),end=' ')
