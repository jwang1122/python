import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.xticks(
    ticks = np.arange(0, 10, np.pi),
    labels = [0, '$\pi$', '$2\pi$', '$3\pi$'])

plt.tick_params(
    top=False,
    bottom=True,
    left=False,
    right=False,
    labelleft=False,
    labelbottom=True)

plt.plot(x, y, label='sin($\phi$)')
plt.legend()
plt.show()