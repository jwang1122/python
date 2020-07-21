"""
plot sin() wave
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 12.7, 0.1)
y = np.sin(x)
plt.xlabel('Angle x')
plt.ylabel('Sin(x)')
plt.plot(x, y)
plt.show()