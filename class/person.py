"""
Inheritence

"""
class Person:
    def __init__(self, name="Guest", ssn="999-99-9999", gender=None, age=0):
        self.name = name
        self.ssn = ssn
        self.gender = gender
        self.age = age

class Student(Person):
    pass

class Teacher(Person):
    pass