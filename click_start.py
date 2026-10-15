import click


@click.command()
@click.option("--name", default="anonymous", help="Enter your name")
@click.option("--count", type=int, required=True, help="Enter count times")
def foo(name: str, count: int) -> None:
    for _ in range(count):
        print(f"Hello {name}")


if __name__ == "__main__":
    foo()
