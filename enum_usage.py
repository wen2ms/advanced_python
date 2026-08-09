from enum import Enum, IntEnum, StrEnum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    @classmethod
    def print_members(cls):
        for member in cls:
            print(member.name, member.value)


class Light:
    def __init__(self, color: Color):
        self.color = color


light = Light(Color.RED)
print(light.color)

red1 = Color.RED
red2 = Color.RED
print(red1 is red2)

Color.print_members()

print(Color.RED == 1)


class IntColor(IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(IntColor.RED == 1)


class StrColor(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


print(StrColor.RED == "red")
