class Dog:
    # class variable
    dog_book = {'yellow': 30, 'black': 20, 'white': 10}

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

        self.dog_book[color] += 1
    
    # instance method
    def bark(self):
        print(f'{self.name} is barking...')

    @classmethod
    def dogs_number(cls):
        number = 0

        for color_dogs_number in cls.dog_book.values():
            number += color_dogs_number

        return number
    
    # static method can be separated from the class and cannot access class or instance variables
    @staticmethod
    def total_weights(dogs):
        total = 0

        for dog in dogs:
            total += dog.weight
        
        return total

print(f'The total of dogs = {Dog.dogs_number()}')

dog_1 = Dog('biye', 'yellow', 10)

dog_1.bark()

print(f'The total of weights = {Dog.total_weights([dog_1])}')

print(Dog.dog_book)