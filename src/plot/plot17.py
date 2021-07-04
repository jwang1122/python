import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)
labels = [0, 'π', '2π', '3π']
major_ticks = np.arange(0, 10, np.pi)
minor_ticks = np.arange(0, 10, 1)

ax = plt.gca() # get current axes
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_xticklabels(labels)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)
ax.tick_params(which='major', width=2, length=8, color='red')
ax.tick_params(which='minor', width=0.5, length=4, color='#00000088')
ax.set_xlim(-0.0, 10.0)
ax.set_ylim(-2, 2)
ax.set_xlabel('ϕ')
plt.plot(x, y, label='sin(ϕ)')
plt.legend(loc=3)
plt.show()