"""
Universal Functions
"""
import numpy as np

a = np.arange(5)
print(a)

x = np.exp(a) # e to each element of a array, return new array
print(x)

x = np.sqrt(a) # square root of each element of a array
print(x)

b = np.array([2.,-1,4,3,5])
x = np.add(a,b)
print(x)
