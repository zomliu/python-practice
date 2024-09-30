# basic concept of inheritance

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

def inheritance_demo1():
    stu = Student('Bob', 'MIT')
    print(stu.name)

    print(isinstance(stu, Person))      # True
    print(isinstance(stu, Student))     # True
    print(issubclass(Student, Person))  # True