"""
reduce: a list of items reduce to one item
r = reduce(function, sequence)
"""
from functools import reduce
from range1 import range1

def add(x, y):
    return x + y


x = reduce(add, range1(100))
print(x)

x = reduce(lambda x, y: x + y, [47,11,42,13])
print(x)