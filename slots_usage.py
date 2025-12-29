import time


class Point:
    __slots__ = ("x",)


class Num:
    pass


point = Point()
num = Num()

start = time.time()
for _ in range(10000000):
    point.x = 1
end = time.time()
print(end - start)

start = time.time()
for _ in range(10000000):
    num.x = 1
end = time.time()
print(end - start)

point.y = 1
