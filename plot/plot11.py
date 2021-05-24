import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)


plt.figure(figsize=(12, 6))

plt.subplot(221)
plt.plot(x, y, label='a')
plt.legend()

plt.subplot(222)
plt.plot(x, y, label='b')
plt.legend()

plt.subplot(223)
plt.plot(x, y, label='c')
plt.legend(loc=3)

plt.subplot(224)
plt.plot(x, y, label='d')
plt.legend(loc=3)

plt.show()