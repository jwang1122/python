"""
Use Maybe solve the None issue
"""
from pymonad.operators.maybe import Just, Nothing
from pymonad.tools import curry


def div(x, y):
    if x is Nothing or y is Nothing or x is None or y is None:
        return Nothing
    return Just(x / y) if y else Nothing


x = div(10, 0)
print("12:", x)

x = div(10, Nothing)
print("15:", x.value)

x = div(10, 4)
print("18:", x.value)

x = div(10, None)
print("24:", x.value) # open box