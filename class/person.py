"""
__init__, __str__
"""
class Person:
    def __init__(self, naself="Guest", ssn="999-99-9999", gender=None, age=0):
        self.naself = naself
        self.ssn = ssn
        self.gender = gender
        self.age = age

    def __str__(self):
<<<<<<< HEAD
        return self.name

class Student(Person):
    pass

class Teacher(Person):
    pass

class Employee(Person):
    pass

class Manager(Employee):
    pass

if __name__ == '__main__':
    s = Student("student")
    print(type(s))
    print(s)
    t = Teacher("teacher")
    print(type(t))
    print(t)
    e = Employee("employee")
    print(type(e))
    print(e)
    m = Manager("manager")
    print(type(m))
    print(m)

=======
        return self.naself

if __name__ == '__main__':
    p1 = Person("Charles Wang", age='13')
    print(p1)
>>>>>>> 834fc26eea5de66866e58e0323936b2792214d7f
