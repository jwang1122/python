import pandas as pd

df = pd.read_csv("src/data/pokemon.csv")
print(df.head(3))
print(df)
print(df.columns)
print(df['Name'])
print(df[['Name','Type 1']])
