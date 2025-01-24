from collections import abc

# With __iter__ method
print(isinstance([], abc.Iterable))

# With __iter__ and __next__ methods
print(isinstance([], abc.Iterator))

numbers = iter(list(range(5)))

next(numbers)

print(next(numbers), '\n')

import random

generate_random = lambda: random.randint(1, 6)

for number in iter(generate_random, 5):
    print(number)