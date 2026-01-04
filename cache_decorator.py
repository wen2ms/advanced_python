from functools import cache, lru_cache


@lru_cache(maxsize=5)
# @cache
def fib(num):
    if num == 0 or num == 1:
        return num
    return fib(num - 1) + fib(num - 2)


if __name__ == "__main__":
    for i in range(400):
        print(i, fib(i))
