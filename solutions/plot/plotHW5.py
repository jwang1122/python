import numpy as np
import matplotlib.pyplot as plt

# Sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# green dashes, blue squares and red triangles
plt.plot(t, t, 'g--', label='y=x')
plt.plot(t, t**2, 'bs', label='y=x*x')
plt.plot(t, t**3, 'r^', label='y=x*x*x')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Multiple lines with different marks")
plt.legend()
plt.show()