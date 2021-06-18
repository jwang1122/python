"""
Python supports a form of multiple inheritanc.
"""
class Base1:
    def __init__(self, name):
        self.name = name

class Base2:
    def __repr__(self):
        return self.name

class Subclass(Base1, Base2):
    pass

x = Subclass("Sub class")
print(x)
