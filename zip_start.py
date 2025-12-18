foo = [1, 2, 3]
bar = ["a", "b", "c"]
print(list(zip(foo, bar)))

pairs = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print(nums)
print(letters)
