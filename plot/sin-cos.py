"""
plot sin() and cos() wave
"""
import numpy as np
import matplotlib.pyplot as plt
from math import pi

frequency = 1
w = 2*pi*frequency
x = np.arange(0, w, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.xlabel('$\phi$')
plt.plot(x, y1, label="sin($\phi$)")
plt.plot(x, y2, label="cos($\phi$)")
plt.legend(loc=3)
plt.show()