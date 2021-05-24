import matplotlib.pyplot as plt
import numpy as np


x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
e = [0.5, 1.0, 1.5, 0.7]

plt.errorbar(x, y, yerr=e, fmt='o')
plt.show()