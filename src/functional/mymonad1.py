"""
map() function as Functor
"""
from pymonad.maybe import Maybe, Just, Nothing


x = Just(2).map(lambda x: x**2)
print(x)

x = Nothing.map(lambda x: x**2)
print(x)



