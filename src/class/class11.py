"""
Don't use class level variables for instance attributes.
"""
class Dog:
    tricks = ['bark'] # class level attribute

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick, tricks=None):
        if tricks==None:
            self.tricks = []
        self.tricks.append(trick) # confuse, use self.tricks but put in class level attributes

class Student:
    name = None # confuse yourself, name_

    def __init__(self, name):
        self.name = name # self.__name

    def __str__(self):
        return self.name

if __name__ == "__main__":
    fido = Dog("Fido")
    buddy = Dog("Buddy")
    fido.add_trick("roll over") # modify same class level attribute
    buddy.add_trick("play dead") # modify same class level attribute
    print(f"what fido can do: {fido.tricks}")
    print(f"what buddy can do: {buddy.tricks}")
    print(Dog.tricks)
    fido.add_trick("pass bridge", fido.tricks)
    print(f"what fido can do: {fido.tricks}")


    s1 = Student("Amy")
    print(s1)
    print(Student.name)