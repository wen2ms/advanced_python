from __future__ import annotations


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)


class Rational:
    def __init__(self, numerator: int, denominator: int) -> None:
        if numerator != 0:
            common = gcd(numerator, denominator)
            self.numerator, self.denominator = numerator // common, denominator // common
        else:
            self.numerator, self.denominator = numerator, denominator
        if self.denominator < 0:
            self.numerator, self.denominator = -self.numerator, -self.denominator

    def __add__(self, other: Rational) -> Rational:
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other: Rational) -> Rational:
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other: Rational) -> Rational:
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    # /
    def __truediv__(self, other: Rational) -> Rational:
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Rational(numerator, denominator)

    def __lt__(self, other: Rational) -> bool:
        return self.numerator * self.denominator < other.numerator - other.denominator

    def __str__(self) -> str:
        if self.denominator == 1 or self.numerator == 0:
            return str(self.numerator)
        return f"{self.numerator} / {self.denominator}"


class Foo:
    def __init__(self, text: str) -> None:
        self.text = text

    def __or__(self, other: Foo) -> MyList:
        return MyList(self, other)

    def __repr__(self) -> str:
        return f"Foo(text={self.text!r})"


class MyList:
    def __init__(self, *args) -> None:
        self.elements = list(args)

    def __or__(self, other) -> MyList:
        return MyList(*self.elements, other)

    def __repr__(self) -> str:
        return f"MyList({', '.join(map(repr, self.elements))})"


def test_operation(a, b) -> None:
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} > {b} = {a > b}")


if __name__ == "__main__":
    a = Rational(-2, 8)
    b = Rational(-2, 16)

    test_operation(a, b)

    # a = Rational(1, 8)
    # b = Rational(0, 16)

    # test_operation(a, b)

    a = Foo("a")
    b = Foo("b")
    c = Foo("c")
    print(a | b | c)
