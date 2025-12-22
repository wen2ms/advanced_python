names: list[str] = ["Foo", "Bar", "Baz"]
upper_names = map(str.upper, names)
print(list(upper_names))
print([name.upper() for name in names])

nums = [1, 2, 3, 4, 5]
print(" ".join(map(str, nums)))
