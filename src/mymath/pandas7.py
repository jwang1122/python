import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/data_minimal.csv')
# print(df.shape)
# print(df.columns)

# newyork = df[df.Key.eq('US_NY')]
newyork = df[df['Key']=='US_NY']
# print(newyork.shape)
# print(newyork.columns)
# print(newyork.dtypes)

newyork.plot("Date","Confirmed")
plt.title("New York Covid-19 Confirmed")
plt.xlabel("Date")
plt.ylabel('Confirmed')
plt.show()