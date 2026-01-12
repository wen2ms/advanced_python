nums = list(range(5))
nums.reverse()
print(nums)

word = "abcdefg"
rev = word[::-1]
print(rev)

nums = "12345"
reversed_iter = reversed(nums)
print(type(reversed_iter))
print("".join(reversed_iter))
