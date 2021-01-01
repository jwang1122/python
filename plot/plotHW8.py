from matplotlib import pyplot as plt
import numpy as np

a = 3
b = 2
x =  np.arange(-5., 5.2, 0.2)
y1 = a * x * x + b * x
y2 = a/b*x + 5

plt.plot(x, y1, label=f'y={a}*x*x +{b}*x')
plt.plot(x, y2, label=f'y={a}/{b}*x + 5')

plt.grid(linestyle='-', linewidth='0.5', color='blue')
plt.legend(loc=2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Find rough solution by cross points")
plt.show()