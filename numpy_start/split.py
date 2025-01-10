import numpy as np

a = np.arange(12).reshape((3, 4))

print(a)

b = np.split(a, 3, axis=0)
c = np.split(a, 4, axis=1)

print(b)
print(c)

d = np.hsplit(a, 2)
e = np.vsplit(a, 3)

print(d)
print(e)
