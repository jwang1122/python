from mymath import * # import from package mymath, will load __init__.py
import mymath.triangle as triangle

r=1
x = circle_area(r) # it is because __init__.py import everything from circle.py
print(x)

p = 11
x = isPrime(p) # because __init__.py import everything from math10.py
print(x)

import mymath.linear1

x = triangle.triangle_area(3, 5) # explicitly import from mymath package
print(x)