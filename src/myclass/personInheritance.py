"""
__init__, __str__
"""
class Person:
    def __init__(self, name="Guest", ssn="999-99-9999", gender=None, age=0, occupation=None):
        self.name = name
        self.ssn = ssn
        self.gender = gender
        self.age = age
        self.occupation = occupation

    def __str__(self):
        return f"Name: {self.name}; Ocupation: {self.occupation}"

class Student(Person):
    pass

class Teacher(Person):
    pass

class Employee(Person):
    pass

class Manager(Employee):
    pass

if __name__ == '__main__':
    s = Student("Amy Lee", occupation="student")
    print(type(s))
    print(s)
    t = Teacher("John Wang", occupation="teacher")
    print(type(t))
    print(t)
    e = Employee("Lee Robertson", occupation="employee")
    print(type(e))
    print(e)
    m = Manager("David Johnson", occupation="manager")
    print(type(m))
    print(m)

