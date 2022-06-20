"""
everythin in Python is class
"""

from class01 import Robot
from math import pi
from turtle import Turtle

x = Robot()
print(type(x))
print(f'the class Robot module name is: {x.__module__}')

x = 5
print(type(x))
print(f'4 is an instance of {type(4)}')

print(type(pi))

t = Turtle()
print(type(t))

s = "John"
print(type(s))