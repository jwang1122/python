import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0.0, 4*np.pi+0.1, 0.1)
y = np.sin(x)

plt.xticks(
    ticks = np.arange(0, 4*np.pi+0.1, np.pi),
    labels = [0, 'π', '2π', '3π', '4π'])

plt.tick_params(
    top=False,
    bottom=True,
    left=False,
    right=False,
    labelleft=False,
    labelbottom=True)

plt.plot(x, y, label='sin(θ)')
plt.legend()
plt.show()