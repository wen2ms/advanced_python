def my_add(a: int, b: int) -> int:
    return a + b

print(my_add(1, 2))

class Pizza:
    type = 'pizza'

def get_type(pizza: Pizza) -> str:
    return pizza.type

print(get_type(Pizza()))

# from typing import List
# def my_sum(numbers: List[int]) -> int:

def my_sum_list(numbers: list[int]) -> int:
    total = 0

    for i in numbers:
        total += i
    
    return total

print(my_sum_list([0, 1, 2]))

from typing import Sequence

def my_num_sequence(numbers: Sequence) -> int:
    total = 0

    for i in numbers:
        total += i
    
    return total

print(my_num_sequence((1, 2, 3)))
print(my_num_sequence(b'123'))

def my_sum_dict(numbers_dictionary: dict[str, int]) -> int:
    total = 0

    for i in numbers_dictionary.values():
        total += i
    
    return total

print(my_sum_dict({'a': 1, 'b': 2, 'c': 3}))

#from typing import Optional
# def foo(x: Optional[int]) -> None:

from typing import Union

def foo(x: Union[int, None]) -> None:
    if x is None:
        print("x is a None")
    else:
        print(f"x is {x}")

foo(None)
foo(1)


