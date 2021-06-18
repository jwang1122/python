"""
numpy.ndarray
underatand numpy array
"""
import inspect
f = inspect.currentframe()

import numpy as np
from numpy import pi

a1 = np.arange(10, 30, 5)
print(f"{inspect.getframeinfo(f).lineno}:{a1}")

# Create an one dimentional array
a1 = np.array([6, 7, 8])
print(f"{inspect.getframeinfo(f).lineno}:{a1}")

a1 = np.linspace(0,2,9) # 9 numbers from 9 to 2
print(f"{inspect.getframeinfo(f).lineno}:{a1}")

a1 = np.linspace(0,2*pi,100) # 9 numbers from 9 to 2
print(f"{inspect.getframeinfo(f).lineno}:{a1}")

a1 = np.array((6.2, 7.1, 8.5))
print(f"{inspect.getframeinfo(f).lineno}:{a1}")

# Create 2 dimentional array
a2 = np.arange(15).reshape(3, 5)
print(f"{inspect.getframeinfo(f).lineno}:{type(a2)}")
print(f"{inspect.getframeinfo(f).lineno}:{a2.shape}")
print(f"{inspect.getframeinfo(f).lineno}:{a2.dtype}")
print(f"{inspect.getframeinfo(f).lineno}:{a2.ndim}")
print(f"{inspect.getframeinfo(f).lineno}:{a2}")

a2 = np.array([(1.5, 2, 3), (4, 5, 6)])
print(f"{inspect.getframeinfo(f).lineno}:{a2}")

a2 = np.array([[1, 2+1j], [3, 4+2j]]) # force all values to be complex number
print(f"{inspect.getframeinfo(f).lineno}:{a2}")

a2 = np.array([[1, 2], [3, 4]], dtype=complex)
print(f"{inspect.getframeinfo(f).lineno}:{a2}")

# Create all 0 3D array
a3 = np.zeros((3, 4))
print(f"{inspect.getframeinfo(f).lineno}:{a3}")

a3 = np.ones((3,3), dtype=np.int16)
print(f"{inspect.getframeinfo(f).lineno}:{a3}")

a3 = np.ones((2, 3, 3), dtype=np.int16)
print(f"{inspect.getframeinfo(f).lineno}:{a3}")
