import matplotlib.pyplot as plt


age = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102,
           110, 120, 121, 122, 130, 111, 115, 112, 80, 75,
           65, 54, 44, 43, 42, 48]

plt.boxplot(age)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)


x = np.random.normal(size=1000)

plt.boxplot(x)
plt.show()