from math import pi

def circle_area(radius):
    return pi * radius**2

r = 1
a = circle_area(r)
print(f"The circle area with radius={r} is {a:.3f}")