"""
plot sin() and cos() functions in one plot
"""
import numpy as np
import matplotlib.pyplot as plt
 
# evenly sampled time at 200ms intervals
t = np.arange(0., 6.7, 0.1)

# red dashes, blue squares and green triangles
plt.plot(t, np.sin(t), label="sin(x)")
plt.plot(t, np.cos(t), label="cos(x)")
plt.title("Sin(x) and Cos(x) Waves")
plt.xlabel("x")
plt.ylabel('f(x)')
plt.legend(loc=3)
plt.show()