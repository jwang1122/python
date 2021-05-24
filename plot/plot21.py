import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available)
# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight',
#  'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark',
#  'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
#  'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white',
#  'seaborn-whitegrid', 'tableau-colorblind10']

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.style.use('dark_background')

plt.plot(x, y, label='sin(x)')
plt.show()