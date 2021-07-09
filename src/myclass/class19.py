"""
Python supports a form of multiple inheritanc.
"""
class Base1:
    def __init__(self, name):
        self.name = name
    def add(self, x, y):
        return x+y

class Base2:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    
    def mul(self, x, y):
        return x * y

    def __repr__(self):
        return self.name

class Subclass(Base2, Base1): # choose first class function if both have same
    pass

x = Subclass("Sub class")
print(x)
x = Subclass("John", 13)
print(x)
print(x.add(6,7))
print(x.mul(4,5))