### YEILD IS AN LAZY EVALUATION
Below is the best example

```aiignore
from typing import Generator
from pathlib import Path

def count_words(text: str) :
    words=text.split(' ')
    yield words  ##ths is lazy evaluated

def read_lines(file_name:str):
    with open(Path(__file__).parent.joinpath('data',file_name),'r') as file:
        for line in file:  # looping is required
            yield count_words(line.strip())  #ths is lazy evaluated


if __name__ == '__main__':
    word_count=read_lines(file_name='word_count.txt')
    num_words = 0
    for word in word_count:
        num_words += len(next(word))
    print(num_words)
```



In Python, the yield keyword is used within a function to make it a generator function, which allows the function to return an iterator. 
Unlike regular functions that return a single value and exit, a generator function can yield multiple values over time and resume from where it left off each time it's called. 
**This allows for lazy evaluation (only generating values when needed or next element is called) and is useful for dealing with large datasets or infinite sequences efficiently.**


**IN BELOW THE _generate_prime_numbers IS NOT AN INFINITE FUNCTION RATHER IT EVALUATED WHEN THE NEXT IN ITERATOR IS CALLED.**
```
def _is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def _generate_prime_numbers():
    start = 2
    while True:  # this is not an infinite loop and will be executed only when the next is called
        if _is_prime(start):
            yield start
        start+=1


if __name__ == '__main__':
    primes= _generate_prime_numbers()
    for i in range(500):
        print(next(primes))
   ```


**Yield each line without loading the whole file into memory**
```aiignore
def read_file_lazy(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()  # Yield each line without loading the whole file into memory

# Using the generator
for line in read_file_lazy('large_file.txt'):
    print(line)
```