import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.xlim(-0.0, 10.0)
plt.ylim(-2.0, 2.0)

plt.plot(x, y, label='sin(θ)')
plt.legend()
plt.show()