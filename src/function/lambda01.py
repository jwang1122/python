"""
The basic syntax of a lambda expression is:

lambda arguments: expression

"""

double = lambda x: x * 2 # assign a name to an anonymous function

print(double(5))

def double(x): # override previous function definition
    return x**2

print(double(5))