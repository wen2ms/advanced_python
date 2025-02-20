from typing import TypeVar, Generic

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

AnimalType = TypeVar('AnimalType', bound=Animal)

class Store(Generic[AnimalType]):
    def __init__(self, stock: list[AnimalType]) -> None:
        self.stock = stock

    def buy(self) -> AnimalType:
        return self.stock.pop()
    
dogs_store = Store[Dog]([Dog(), Dog()])

cats_store = Store[Animal]([Cat(), Cat()])

dog_1: Animal = dogs_store.buy()
dog_2: Dog = dogs_store.buy()

cat_1: Animal = cats_store.buy()

print(dog_1, dog_2, cat_1)

integers_store = Store[int]([])

animals_store:Store[Animal] = Store[Dog]([])
