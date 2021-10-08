from math import pi
import pretty_errors

def add(x, y):
    return x + y
    
def circleArea(radius):
    if type(radius) not in [float, int]:
        raise TypeError(f"the radius must be float or integer.")
    if radius<0:
        raise ValueError(f"the radius must be positive number. You give {radius}")
    return pi*radius**2

# if __name__ == '__main__':
a = circleArea(-2) # this block of code is your test area
print(a)
print("Done.")