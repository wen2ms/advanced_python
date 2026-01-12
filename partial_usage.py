from functools import partial


def borrow(lender, borrower):
    print(f"{borrower} borrowed from {lender}")


if __name__ == "__main__":
    borrow_from_foo = partial(borrow, "Foo")
    borrow_from_foo("Jay")
    borrow_from_foo("Ana")
