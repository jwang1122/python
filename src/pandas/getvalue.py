import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])

print(df)
print(df.loc['viper'])

df1 = df.loc[['viper','sidewinder']] # return a DataFrame, get group of rows
print(type(df1))
print(df1)

a = df.loc['cobra','shield'] # get value on give row and column
print(a)

df2 = df.loc['cobra':'viper', 'max_speed']
print(type(df2))
print(df2)

#setting values
df.loc[['viper', 'sidewinder'], ['shield']] = 50 # change column values
print(df)

df.loc['cobra'] = 10 #change row values
print(df)

df.loc[:, 'max_speed'] = 30 # change all values for give column
print(df)

df.loc[df['shield'] > 35] = 0 # change value on condition
print(df)

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=[7, 8, 9], columns=['max_speed', 'shield'])

print(df)
print(df.loc[:8])

# multi index
tuples = [
   ('cobra', 'mark i'), ('cobra', 'mark ii'),
   ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
   ('viper', 'mark ii'), ('viper', 'mark iii')
]
index = pd.MultiIndex.from_tuples(tuples)
values = [[12, 2], [0, 4], [10, 20],
        [1, 4], [7, 1], [16, 36]]
df = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index)

print(df)
print(df.loc['cobra'])
print(df.loc[('cobra', 'mark ii')])
print(df.loc['cobra', 'mark i'])
print(df.loc[[('cobra', 'mark ii')]])
print(df.loc[('cobra', 'mark i'), 'shield'])
print(df.loc[('cobra', 'mark i'):('viper', 'mark ii')])