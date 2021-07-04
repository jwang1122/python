"""
if you donot use 
if __name__ == '__main__":
condition, you will have the output as below👇

12.566370614359172
Done.
32.169908772759484

this is due to the import line.
"""
from circle import circle_area

area = circle_area(3.2)
print(area)