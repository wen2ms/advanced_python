print(isinstance(5, str))
print(isinstance(5, int))
print(isinstance(5, (str, int)))

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Human):
    def __init__(self, student_id, student_class, name, age):
        self.student_id = student_id
        self.student_class = student_class
        super().__init__(name, age)


class Teacher(Human):
    def __init__(self, teacher_id, salary, name, age):
        self.teacher_id = teacher_id
        self.salary = salary
        super().__init__(name, age)


human = Human("Jucy", 18)
student = Student("201801", "01", "Jucy", 18)
teacher = Teacher("s1101", 7000, "Jucy", 18)
print(isinstance(human, Human), type(human))
# inherit
print(isinstance(student, Human), isinstance(student, Teacher))

print(type(print))