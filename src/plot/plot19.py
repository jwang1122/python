import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.grid(True)

plt.plot(x, y, label='sin(x)')
plt.show()


x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.grid(alpha=0.2)

plt.plot(x, y, label='sin(x)')
plt.show()