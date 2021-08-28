"""
applicative handle error
"""
from pymonad.tools import curry
from pymonad.operators.maybe import Just, Nothing

@curry(2) #打包功能块
def div(x, y):
    return x/y if y else Nothing

x = div(10, 0) # Return a normal int
print("09:",x)
x=div * Just(10) & Just(4) # Applicative 打包功能作用于打包变量
print("11:",x)

# x=div(Just(10), Just(4)) # don't know how to calculate Just divided by Just
# print(x)

x=div(10, 4) # nomal way to call, no box
print(x)