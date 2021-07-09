""" 
Function defined outside the class
"""
def f1(self, x, y): # it has self argument
    return min(x, x+y)
            
class A:
    f = f1
    def g(self):
        return 'hello world'

    h = g # give another function name
        
class C:
    f = f1 # both A and C can have same function
    def add(self, x, y):
        return x + y

x = A()
y = x.f(3,-2)
print(y)
print(x.h())
print(f1(None, 2, 3)) # f1 still can be used, but ignore first argument
c=C()
y = c.f(5, 1)
print(y)