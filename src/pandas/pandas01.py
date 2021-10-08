"""
Create DataFrame object
"""
import pandas as pd
import numpy as np
from dataclasses import make_dataclass

d = {'col1': [1, 2], 'col2': [3, 4]}
df1 = pd.DataFrame(data=d, dtype=np.int8)
print(df1)
print(df1.dtypes)

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
print(df2)

Point = make_dataclass("Point", [("x", int), ("y", int)])
df3 = pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
print(df3)

print(df3.at[1,'y']) # row 1, and y column

df = pd.DataFrame({'float': [1.0],
                   'int': [1],
                   'datetime': [pd.Timestamp('20180310')],
                   'string': ['foo']})

print(df)
print(df.info(verbose=True))
print(df.values)
print(df.axes)