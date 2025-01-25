def foo(number):
    while number > 0:
        yield number

        number -= 1

    return -1

generator_foo = foo(5)

try:
    for number in generator_foo:
        print(number)
        next(generator_foo)
except StopIteration as e:
    print(e.value)

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            
            node = node.next

head = Node('head')
node_1 = Node('node_1')
node_2 = Node('node_2')

head.next = node_1
node_1.next = node_2

print()

for node in head:
    print(node.name)

def bar(number):
    while number > 0:
        send_value = yield number

        if send_value is not None:
            number = send_value
        
        number -= 1

generator_bar = bar(5)

# first = generator_bar.send(None)
first = next(generator_bar)

print(f"send: {generator_bar.send(10)}")

for i in generator_bar:
    print(i)
