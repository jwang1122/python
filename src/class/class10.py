"""
override __new__()
"""

from enum import Enum

class Sample(object):
    def __str__(self):
        return "SAMPLE"

class A(object):
    def __new__(cls):
        return Sample()

class B(object): # different way to write __new__()
    def __new__(cls):
        return super(B, cls).__new__(Sample)

#
class Coordinate(bytes, Enum):
    """
    Coordinate with binary codes that can be indexed by the int code.
    """
    def __new__(cls, value, label, unit): # override __new__()
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        obj.unit = unit
        return obj
    PX = (0, 'P.X', 'km') # position X
    PY = (1, 'P.Y', 'km') # position Y
    VX = (2, 'V.X', 'km/s') # velocity X
    VY = (3, 'V.Y', 'km/s') # Velocity Y


if __name__ == '__main__':
    a = A()
    print(a)
    print(type(a))
    b = B()
    print(b)
    print(type(b))

    vx = Coordinate.VX
    print(Coordinate['PY'])
    print(f"label: {vx.label}")
    print(f"value: {vx.value}")
    print(f"unit: {vx.unit}")
