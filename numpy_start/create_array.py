import numpy as np

float_array = np.array([[1, 2, 3],
                        [4, 5, 6]], dtype=float)

int_array = np.array([[1, 2, 3],
                      [4, 5, 6]], dtype=int)

print(float_array.dtype, int_array.dtype)

zeros = np.zeros((3, 4))
ones = np.ones((3, 4), dtype=np.int32)
integers = np.arange(1, 7)

print(zeros)
print(ones)
print(integers)

integers = integers.reshape(2, 3)
print(integers)

lines = np.linspace(1, 10, 20)
print(lines)
