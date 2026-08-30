from typing import NotRequired, TypedDict


class Person(TypedDict):
    name: str
    age: int
    address: str


bar: Person = {"name": "bar", "age": 10, "address": "bar"}
bar["address"] = "foo"
bar["name"] = "foo"
print(bar)


class Student(TypedDict):
    name: str
    age: int
    address: NotRequired[str]


foo: Student = {"name": "foo", "age": 10}
foo["address"] = "baz"
print(foo)
