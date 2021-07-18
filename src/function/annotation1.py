"""
🔥Function annotation, used for specify argument type and return type.
It is usefule to avoid unexpected usage of a function.
need use: 
👉mypy annotation1.py

"""
from math import pi

def circle_area(radius:'float', output:'float'=0.0) -> float:
    return pi * radius * radius

if __name__ == '__main__':    
    a = circle_area(2.4)
    print(a)