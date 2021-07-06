"""
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
"""
import pandas as pd
import matplotlib.pyplot as plt

# compare deaths and confirmed
df = pd.read_csv("src/data/data_minimal.csv")
newYork = df[df['Key']=='US_NY']
print(newYork.columns)
newYork.plot(x='Date', y='Deaths')
plt.show()

# compare deaths of New York and Taxas
options = ['US_NY','US_TX']
ny = df.loc[df['Key'].isin(options)]
ny.plot(x='Date')
options = ['US_TX']
tx = df.loc[df['Key'].isin(options)]
tx.plot(x='Date')
plt.show()


# get values
print(ny.values)

# newYorkDeaths = [deaths for deaths in df['Deaths'] if df['Key']=='US_NY']
# print(newYorkDeaths)
# print(df.head(3))
# print(df)
# print(df.columns)
# print(df['Name'])
# print(df[['Name','Type 1']])
