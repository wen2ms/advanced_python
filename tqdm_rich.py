from tqdm import tqdm
from rich.progress import track
from rich.progress import Progress
from tqdm import trange
from time import sleep

# for _ in tqdm(range(1000)):
#     sleep(0.001)

for _ in trange(1000, desc="Sleeping"):
    sleep(0.001)

students = ["Foo", "Bar", "Foobar", "Quz", "Corge", "Fred", "Qux"]
for student in tqdm(students, desc="students"):
    sleep(0.1)

def generator(iteration):
    for i in range(iteration):
        yield i

for _ in tqdm(generator(50), total=50):
    sleep(0.01)

with tqdm(total=100, leave=False) as process_bar:
    process_bar.update(20)
    sleep(2)
    process_bar.update(30)
    sleep(1)
    process_bar.update(50)

for _ in track(range(1000), description="Sleeping"):
    sleep(0.001)

with Progress() as progress:
    task1 = progress.add_task("[red]Downloading", total=10)
    task2 = progress.add_task("[green]Processing", total=10)
    task3 = progress.add_task("[yellow]Saving", total=10)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.2)
        progress.update(task3, advance=0.1)
        sleep(0.1)