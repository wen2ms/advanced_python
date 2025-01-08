import numpy as np

array = np.arange(10).reshape((2, 5))

print(array)

min_index = array.argmin()
max_index = np.max(array)
print(min_index, max_index)

mean = np.mean(array)
print(mean)

median = np.median(array)
print(median)

print(np.cumsum(array))
print(np.diff(array))

nonzeros_rows, nonzeros_columns = np.nonzero(array)
nonzeros = [array[row][column] for row, column in zip(nonzeros_rows, nonzeros_columns)]
print(nonzeros)

print(np.sort(array)[:, ::-1])

print(np.transpose(array))
print((array.T).dot(array))

print(np.clip(array, 2, 7))