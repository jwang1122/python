class Person:
    def __init__(self, name, ssn, gender, age):
        self.name = name
        self.ssn = ssn
        self.gender = gender
        self.age = age

class Student(Person):
    pass

class Teacher(Person):
    pass