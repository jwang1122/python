class Person:
    numOfPersons = 0 # class level attributes

    def __init__(self, name, age): # name, age are function local variables
        self.name = name # create instance attribute self.name
        self.age = age
        Person.numOfPersons += 1

    @classmethod
    def getNumOfPersons(cls): # cls and self just a argument name, can be anything you want. but better use cls
        return cls.numOfPersons

    @staticmethod
    def add(x, y): # no self argument needed, since it does NOT modify any instance level attribute
        return x + y

if __name__ == '__main__':
    p1 = Person("John", 14)
    print(Person.numOfPersons) # access class level variable attributes
    p1 = Person("Jim", 14)
    print(Person.numOfPersons)

    Person.getNumOfPersons() ## call class level function

    # p1.sayHello() # AttributeError: 'Person' object has no attribute 'sayHello'

    print(f'Person can do simple math: {Person.add(3,4)}')