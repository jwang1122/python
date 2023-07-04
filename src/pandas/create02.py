import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create DataFrame from dict
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
print(df) 

data = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)],
                dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")])

# rearange columns
df = pd.DataFrame(data, columns=['c', 'a'])
print(df) 