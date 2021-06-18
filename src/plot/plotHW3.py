import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('./plot/plotHW3.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()