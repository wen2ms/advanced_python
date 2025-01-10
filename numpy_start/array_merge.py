import numpy as np

a = np.array([1, 1, 1])
b = np.array([2, 2, 2])

c = np.vstack((a, b))
d = np.hstack((a, b))

print(c)
print(d)

a = a[:, np.newaxis]
b = b[:, np.newaxis]

print(a)
print(b)

c = np.vstack((a, b))
d = np.hstack((a, b))

print(c)
print(d)

e = np.concatenate((a, b, a), axis=0)
f = np.concatenate((a, b, b), axis=1)
print(e)
print(f)