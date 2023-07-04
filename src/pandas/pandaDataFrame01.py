import pandas as pd

df = pd.DataFrame({'date':['2000-03-10','2000-03-11','2000-03-12'], 'value':[2,3,4]})
print(df.shape)
print(df.columns)
print(df.info())

df['date'] = pd.to_datetime(df['date'])
print(df.info())