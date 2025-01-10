import numpy as np

array = np.arange(10)

print(array)

print(array[5])

array = array.reshape((2, 5))
print(array)

print(array[1])

print(array[1][0])

print(array[1, 0])

print(array[1, :3])

for column in array.T:
    print(column)

print(array.flatten())

# flat provides a iterator of array flatten
for item in array.flat:
    print(item)
