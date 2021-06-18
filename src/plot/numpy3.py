"""
Arithmetic operators on arrays apply elementwise.
"""
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

a = np.array([20, 30, 40, 50])
b = np.array((1,2,3,4))
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)

x = 10 * np.linspace(0.5,2*pi,5)
print(x)

y = x < 30
print(y)

y = x.sum()
print(y)

print(x.max())