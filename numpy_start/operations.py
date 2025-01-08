import numpy as np

array_a = np.ones(4, dtype=int)
array_b = np.arange(4)

print(array_a)
print(array_b)

print(f"a + b = {array_a + array_b}")
print(f"a * b = {array_a * array_b}")
print(f"a^2 = {array_b ** 2}")
print(f"sin(a) = {np.sin(array_a)}")

print(array_b > 2)

array_b = array_b.reshape(4, 1)
print(array_b)

array_c = np.dot(array_a, array_b)
array_c_dot = array_a.dot(array_b)

print(array_c)
print(array_c_dot)

randoms = np.random.random((2, 4))

print(randoms)
print(np.max(randoms))
print(randoms.min())

array_b = array_b.reshape(2, 2)
print(array_b)
print(np.sum(array_b))
print(np.max(array_b, axis=1))