import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)

ax = plt.gca()
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(True)

plt.plot(x, y, label='sin(x)')
plt.show()