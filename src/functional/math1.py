"""
Functor: apply a function to a wrapped value
"""
from pymonad.operators.maybe import Just, Nothing

def add3(x):
    return Just(x + 3)

def sub5(x):
    return Just(x - 5)

def mul7(x):
    return Just(x * 7)

def div9(x):
    return Just(x / 9)

if __name__ == '__main__':
    f = lambda x: Just(x) >> add3 >> sub5 >> mul7 >> div9
    print(f(20)) # return boxed value
    print(f(20).value) # open box