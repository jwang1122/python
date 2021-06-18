import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.],
                 [37., 40.],
                 [29., 10.]])

cmap = plt.get_cmap("tab20c")
outer_colors = cmap([0, 4, 8])
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.pie(vals.sum(axis=1),
       radius=1,
       colors=outer_colors,
       wedgeprops={'width': size, 'edgecolor': 'white'})

ax.pie(vals.flatten(),
       radius=1-size,
       colors=inner_colors,
       wedgeprops={'width': size, 'edgecolor': 'white'})

plt.show()