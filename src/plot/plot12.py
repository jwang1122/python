import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 6))

ax[0,0].plot(x, y, label='a')
ax[0,1].plot(x, y, label='b')
ax[1,0].plot(x, y, label='c')
ax[1,1].plot(x, y, label='d')

for chart in ax.ravel():
    chart.legend(loc=3)


plt.show()