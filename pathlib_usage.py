import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# for path in Path().iterdir():
#     print(path)

my_dir = Path("pickle_start")
my_file = Path("pathlib_usage.py")

print(my_dir.name, my_dir.suffix, my_dir.stem)
print(my_file.name, my_file.suffix, my_file.stem)

# new_file = my_dir.joinpath("new_file.txt")
new_file = my_dir / "new_file.txt"

print(new_file)

print(my_dir.exists())
print(my_file.exists())
print(new_file.exists())

print(my_dir.parent.absolute())
print(my_file.parent)
print(new_file.parent.parent)

path = Path("..").resolve()
print(path)

# rglob: recursive glob
for path in Path().glob("*usage*", case_sensitive=False):
    print(path)

with my_file.open() as infile:
    print(type(infile))
    # print(infile.read())

with open(my_file) as infile:
    print(type(infile))

path = Path("foo/bar")
path.mkdir(exist_ok=True, parents=True)

file = path / "foo.txt"
file.touch()

# path.rmdir()
shutil.rmtree(path)
