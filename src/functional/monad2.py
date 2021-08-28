from pymonad.tools import curry
from pymonad.operators.maybe import Just, Maybe

@curry(2) # 1. tell how many arguments; 2. unbox value; 3. box result
def add(x, y):
    return x + y

@curry(2)
def mul(x, y):
    return x * y

print(add(2, 3))
print(mul(2,3))

# 最终目的是要连续执行的形式。
add2 = add * Just(2) & Just(8) # Applicative
print(add2)

x = add * Just(2)
print(f"20: {x}") # print functor
x = x & Just(8) # Just(8) is an applicative which can be applyed by functor
print(f"22: {x}")

mul2 = mul * Just(5) & Just(9)
print(mul2)

x = Maybe.apply(add).to_arguments(Just(3),Just(5)) # store function > then add arguments
print(x)
