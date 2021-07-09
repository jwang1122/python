"""
__init__()
__call__()
"""

class Class1:
    def __init__(self, a, b, c): # always return an instance
        self.x=a
        self.y=b
        self.z=c

    def __call__(self, a): # make instance callable
        print(a)
        print(self.x,self.y,self.z)
        return self.x + self.y + self.z + a

class Class2:
    def __call__(self, a): # make the instance callable
        return a + 10

class Class3:   
    def __init__(self):
        pass

x = Class1(11, 2, 3)
y = x(10) # __call__ make object callable
print(y)

print()
print("Class2()")
x = Class2()
y = x(11)
print(y)

print()
x = Class3()
# x() # TypeError: 'Class3' object is not callable

print('Done')