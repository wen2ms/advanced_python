from dataclasses import dataclass, field


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}, name = {self.name}, age = {self.age}"


# frozen: member variables are immutable
@dataclass(frozen=True)
class Toy:
    name: str
    age: int = 0
    nums: list[int] = field(default_factory=list, repr=False)


if __name__ == "__main__":
    student = Student("foo", 18)
    print(student)

    toy = Toy("bar", 7)
    print(toy)
