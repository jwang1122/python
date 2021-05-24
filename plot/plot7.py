import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)


a = np.random.normal(size=1000)
b = np.random.normal(size=1000)
c = np.random.normal(size=1000)
d = np.random.normal(size=1000)
data = [a, b, c, d]

plt.boxplot(data)
plt.show()