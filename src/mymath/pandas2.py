"""
Understand pandas DataFrame
"""
import pandas as pd
import numpy as np

# use dictionary to create pandas DataFrame
d = {'col1': [1, 2, 3], 'col2': [1, 8, 27]}
df = pd.DataFrame(data=d)

print(df)
print(df.dtypes)

df.plot(x ='col1', y='col2', kind = 'line')

df = pd.DataFrame(data=d, dtype=np.int8) # force short integer
print(type(df))

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
print(df2)

from dataclasses import make_dataclass
Point = make_dataclass("Point", [("x", int), ("y", int)])
df3 = pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
print(df3)
print(df3.dtypes)

import matplotlib.pyplot as plt
plt.show()
