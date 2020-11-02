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
        return self.naself

if __name__ == '__main__':
    p1 = Person("Charles Wang", age='13')
    print(p1)