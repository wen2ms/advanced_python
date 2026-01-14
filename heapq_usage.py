import heapq


class Person:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __repr__(self) -> str:
        return f"{self.name}"


if __name__ == "__main__":
    persons = [Person("a", 2), Person("b", 1), Person("c", 4), Person("d", 5), Person("e", -1)]

    heap = [(person.priority, person) for person in persons]
    heapq.heapify(heap)
    print(heap)
    print(heap[0])

    heapq.heappush(heap, (7, Person("f", 7)))
    print(heap)
    print(heapq.heappop(heap))

    heap = [-1, -2, -3, -4]
    heapq.heapify(heap)
    print(heap)
