import numpy as np

a = np.zeros((3, 4), dtype=int)

print(a)

b = a
c = a.copy()

a[0] = [1, 2, 3, 4]

print(b)
print(c)
