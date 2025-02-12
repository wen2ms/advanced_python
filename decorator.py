import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        ret = func(*args, **kwargs)

        end = time.time()
        print(end - start)

        return ret
    
    return wrapper

# foo = timer(foo)
@timer
def foo(x):
    time.sleep(x)

@timer
def add(x, y):
    return x + y

print(add(1, 2))

def advanced_timer(iteration):
    def inner(func):
        def wrapper(*args, **kwargs):
            start = time.time()

            for _ in range(iteration):
                ret = func(*args, **kwargs)

            end = time.time()
            print(end - start)

            return ret
        
        return wrapper
    
    return inner

@advanced_timer(1000)
def double(x):
    return x * 2

print(double(2))