import matplotlib.pyplot as plt
import numpy as np


x = [1, 3, 5, 7, 9]
y = [2, 3, 4, 3, 4]

# calculate the trendline
model = np.polyfit(x, y, 1)
trend = np.poly1d(model)

plt.plot(x, y, label='data')
plt.plot(x, trend(x), color='red', linestyle='--', label='trend')
plt.show()

x = np.linspace(0, 10, 1000)
y = np.sin(x)

model = np.polyfit(x, y, 5)
trend = np.poly1d(model)

plt.plot(x, y, label='sin(x)')
plt.plot(x, trend(x), color='red', linestyle='--', label='trend')
plt.show()