from collections import namedtuple
from typing import NamedTuple

User = namedtuple("User", ["name", "x", "y"])
user = User("foo", 1, 2)
print(user[0], user.x, user.y)


class Point(NamedTuple):
    x: int
    y: int


point = Point(1, 2)
print(point.x, point[1])
