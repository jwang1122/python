import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 6))

ax[0,0].plot(x, y, label='sin(ϕ)')
ax[0,1].plot(x, y, label='b')
ax[1,0].plot(x, y, label='c')
ax[1,1].plot(x, y, label='d')

plt.subplots_adjust(
    left = 0.125,  # the left side of the subplots of the figure
    right = 0.9,   # the right side of the subplots of the figure
    bottom = 0.1,  # the bottom of the subplots of the figure
    top = 0.9,     # the top of the subplots of the figure
    wspace = 0.5,  # the amount of width reserved for space between subplots,
                   # expressed as a fraction of the average axis width
    hspace = 0.5,  # the amount of height reserved for space between subplots,
                   # expressed as a fraction of the average axis height
)
for chart in ax.ravel():
    chart.legend(loc=3)

plt.show()