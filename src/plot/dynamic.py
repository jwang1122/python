import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

# Define the animation function
def update(frame):
    xdata.append(frame)
    ydata.append(np.random.rand())
    ln.set_data(xdata, ydata)
    ax.relim()
    ax.autoscale_view()
    return ln,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100),
                    blit=True, interval=50)

# Show the plot
plt.show()
