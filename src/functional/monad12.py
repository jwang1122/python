"""
Maybe.maybe() function
"""
from pymonad.maybe import Maybe, Just, Nothing

x = Just(1).maybe(Nothing, lambda x: str(x))

print(type(x))
print(x)

x = Nothing.maybe('a', lambda x: str(x)) # use default value
print(x)

