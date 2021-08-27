"""
How applicative works
"""

from pymonad.tools import curry
from pymonad.operators.maybe import Just, Maybe, Nothing

@curry(2)
def add(x, y):
    return Just(x + y)

@curry(2)
def mul(x, y):
    return Just(x * y)

@curry(2)
def div(x, y):
    return Just(x / y) if y else Nothing

@curry(2)
def sub(x, y):
    return Just(x - y) 

appl = (Just(1) # Maybe.insert(1)
    .then(sub(1))
    .then(div(5))  # Returns a Nothing value
    .then(sub(5))
    .then(mul(5))
    .maybe(Nothing, lambda x: x))
print(appl)

m = Just(5).then(sub(1))
print(m)