"""
Python module: enum (enumeration)
enumeration: the act of naming things separately, one by one:
"""
from enum import Enum, auto

class Color(Enum):
    RED = 1 # RED=auto()
    GREEN = 2
    BLUE = 3

class Flag:
    def __init__(self, color):
        self.color = color # use Enum as attribute
    def __repr__(self):
        return str(self.color)

class AutoName(Enum):
    #The values are chosen by _generate_next_value_(), which can be overridden:
    def _generate_next_value_(name, start, count, last_values):
        return name

class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

if __name__ == '__main__':
    print(Color.RED)
    print(repr(Color.RED))
    print(Color.RED.value)
    x = Color.RED
    print(type(x))

    f = Flag(Color.RED) # the advantage of using Enumeration is you cannot use other color which not defined in enum
    print(f"My flag in {f} color.")

    # f=Flag(Color.BLACK) # raise AttributeError

    # get enum name and value
    member = Color.RED
    print(member.name)
    print(member.value)

    # enum is iterable
    for color in Color:
        print(color)

    for direction in Ordinal:
        print(direction.value) # make value same as name

    # Enumeration member ara hashable, can be used in dictionary or set
    apples = {} # create a dictionary
    apples[Color.RED] = 'red delicious'
    apples[Color.GREEN] = 'granny smith'
    print(apples)
    print(apples[Color.GREEN])

    flagColors = {Color.RED, Color.GREEN} # create a set
    print(flagColors)
    print(Color.BLUE in flagColors)

    # Enumeration member comparison
    red = Color.RED
    print(red==Color.RED)
    print(red is Color.BLUE)
    print(red != Color.BLUE)
    print(red==1) # return False when compare with type other than Enum

    # Enum is callable
    Animal = Enum('Animal','ANT BEE CAT DOG') # use str
    x = Animal.CAT
    print(x.name)
    print(x.value)

    Animal = Enum('Animal',('ANT','BEE','CAT','DOG')) # use tuple
    x = Animal.CAT
    print(x.name)
    print(x.value)

    Animal = Enum('Animal',{'ANT':4,'BEE':2,'CAT':10,'DOG':11}) # use dict
    x = Animal.CAT
    print(x.name)
    print(x.value)

