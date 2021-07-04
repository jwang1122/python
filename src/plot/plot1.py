"""
plot sin() wave
"""
import numpy as np
import matplotlib.pyplot as plt
from math import pi

frequency = 2
w = 2*pi*frequency
x = np.arange(0, w, 0.1)
y = np.sin(x)
plt.xlabel('Angle(θ)')
plt.ylabel('sin(θ)')
plt.plot(x, y)
plt.title('Sine Wave')
plt.show()