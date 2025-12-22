from bisect import bisect_left, bisect_right

nums = [1, 2, 3, 4, 5]

print(bisect_left(nums, 3))
print(bisect_right(nums, 3))
