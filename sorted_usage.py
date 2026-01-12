word = "dcba"
letters = sorted(word)
print(type(letters))
print(letters)

nums = [-1, 0, 3, 3, -7]
print(sorted(nums))
print(sorted(nums, key=abs))

words = ["aa", "bb", "CC", "dd"]
print(sorted(words))
print(sorted(words, key=str.lower))
print(sorted(words, reverse=True))

intervals = [[1, 3], [4, 2], [2, 5]]
print(sorted(intervals))


def get_second_element(elements):
    return elements[1]


print(sorted([[1, 2], [3, 0], [4, -1]], key=get_second_element))
