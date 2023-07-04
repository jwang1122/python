import pandas as pd
import matplotlib.pyplot as plt

# create DataFrame from dict
d = {"col1":[1,2], 'col2':[3,4]}
df = pd.DataFrame(data=d)
print(df) 

plt.plot(df)
plt.show()

plt.plot(df["col1"], df["col2"])
plt.xlabel("col1")  # add x-axis label
plt.ylabel("col2")  # add y-axis label
plt.title("Plot of col1 vs col2")  # add title
plt.show()

d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
df = pd.DataFrame(data=d, index=[0, 1, 2, 3])
print(df)