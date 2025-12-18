from collections import deque

stack = deque()

stack.append("A")
stack.append("B")
stack.append("C")

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

queue = deque(["D", "E", "F"])

print(queue)

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())


def tail(filename, n=10):
    with open(filename) as infile:
        return deque(infile, n)


print(tail("deque_start.py"))


def roundrobin(*iterables):
    iterators = deque(map(iter, iterables))

    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            iterators.popleft()


for letter in roundrobin("ABC", "DE", "FGH"):
    print(letter)
