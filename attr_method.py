str = "abc"

print(hasattr(str, "split"))
print(hasattr(str, "readlines"))


class Foo:
    def __init__(self):
        self.one = 1


foo = Foo()
print(getattr(foo, "one", 0))
print(getattr(foo, "two", 0))

setattr(foo, "two", 2)
print(foo.two)

delattr(foo, "one")
print(hasattr(foo, "one"))
