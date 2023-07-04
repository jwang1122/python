import pandas as pd

df1 = pd.DataFrame([1, 2, 3], index=["a", "b", "c"], columns=["x"])
df2 = pd.DataFrame(data=df1, index=["a", "c"])

print(df2)

df1 = pd.DataFrame(([1, 2], [4, 5], [7, 8]), index=["a", "b", "c"], columns=["x", "y"])
df2 = pd.DataFrame(data=df1, index=["a", "b", "c"])

print(df2)
