import abc

class Person(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getOccupation(self):
        raise NotImplementedError

    # can be used to override issubclass() function
    # @classmethod
    # def __subclasshook__(cls, subclass):
    #     return (hasattr(subclass, 'getOccupation') and
    #     callable(subclass.getOccupation) or 
    #     NotImplemented)

    # can be used to override issubclass() function
    # @classmethod
    # def __subclasscheck__(cls, sub):
    #     attr = getattr(cls, getOccupation)
    #     if sub in attr:
    #         return True

    
class Engineer(Person):
    def __init__(self, name):
        self.name = name

    def getOccupation(self):
        return "Engineer"

class Teacher(Person):
    def __init__(self, name):
        self.name = name

    def getOccupation(self):
        return "Teacher"

class Student(): #Python doesn't care if the Student inherits from  Person or not
    def __init__(self, name):
        self.name = name

    def getOccupation(self):
        return "Student"

def occupation(person): # polymophism(异类同功)
    print(person.getOccupation())

if __name__ == '__main__':    
    t1 = Teacher("John")
    e1 = Engineer("Terry")
    s1 = Student("Charles")
    occupation(t1)
    occupation(e1)
    occupation(s1)
    print("Teacher is subclass of Person:",issubclass(Teacher, Person))
    print("Teacher is subclass of Engineer:",issubclass(Teacher, Engineer))
    print("t1 is instance of Person:",isinstance(t1, Person))    
    print("t1 is instance of Teacher:",isinstance(t1, Teacher))
    print("t1 is instance of Engineer:",isinstance(t1, Engineer))
    print("s1 is instance of Person:",isinstance(s1, Person))