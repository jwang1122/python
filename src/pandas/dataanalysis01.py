import pandas as pd
from matplotlib import pyplot as plt

x = (1, 2, 3, 4)
y = (1, 4, 9, 16)
z = (15, 10, 5, 0)
plt.plot(x, y) # plotting
plt.plot(x, z)
plt.title("square of number") # add title
plt.xlabel("x") # add x-axis label
plt.ylabel('y and z') # add y-axis label
plt.legend(["this is y", "this is z"])

# Add grid lines
plt.grid(True, which='major', linestyle='-', linewidth='0.5', color='gray')
plt.grid(True, which='minor', linestyle=':', linewidth='0.5', color='red')

# Set minor grid interval
plt.minorticks_on()
plt.grid(True, which='minor', linestyle=':', linewidth='0.5', color='red', alpha=0.5)

plt.show()     # display the chart