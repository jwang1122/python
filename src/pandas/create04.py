import pandas as pd

ser = pd.Series([1, 2, 3], index=["a", "b", "c"])
df = pd.DataFrame(data=ser, index=["a", "c"])

print(df)