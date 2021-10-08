"""
if you donot use 
if __name__ == '__main__":
condition, you will have the output as below👇

12.566370614359172
Done.
32.169908772759484

this is due to the import line.
"""
from circle import circleArea # load whole module, only circleArea can be used

area = circleArea(3.2)
print(area)

import circle # same module only load one time

r = 6.1
area = circle.circleArea(r)
print(f"The circle area with radius={r} is {area:.3f}.")

a = circle.add(4,5)
print(a)