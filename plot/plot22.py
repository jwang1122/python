import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 1000)
y = x - x.mean()
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'Serif'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['figure.figsize'] = (9, 6)
plt.style.use('fivethirtyeight')
plt.yscale('linear')

plt.plot(x, y)
plt.show()

# x = np.linspace(0, 10, 1000)
# y = x - x.mean()

plt.yscale('log')

plt.plot(x, y)
plt.show()

plt.yscale('logit')

plt.plot(x, y)
plt.show()