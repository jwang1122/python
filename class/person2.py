"""
class attribute and function with classmethod decorator
"""


class Person:
    totalObjects = 0

    def __init__(self, name="Guest", ssn="999-99-9999", gender=None, age=0):
        self.name = name
        self.ssn = ssn
        self.gender = gender
        self.age = age
        Person.totalObjects += 1

    @classmethod
    def showcount(cls): # cls class decorator representitive
        print("Total objects: ",cls.totalObjects)

p1 = Person("John")
p2 = Person("Charles")
p3 = Person("Ethan")
print("Total objects", Person.totalObjects)
Person.showcount()
