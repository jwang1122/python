import pandas as pd
import matplotlib.pyplot as plt

d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['a', 'b', 'c'])
print(ser)

plt.plot(ser)
plt.show()

ser = pd.Series(data=d, index=['x', 'y', 'z'])
print(ser)
ser.plot()
plt.show()

r = [1, 2]
ser = pd.Series(r, copy=False)
ser.iloc[0] = 999
print(ser)