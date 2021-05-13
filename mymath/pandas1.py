import pandas

data = pandas.read_csv('mymath/brain_size.csv', sep=';', na_values='.')

print(f"(rows, columns): {data.shape}")
print(data.columns)
print(data.Gender)

x = data[data['Gender'] == 'Female']['VIQ'].mean()
print(f"The average of VIQ for Female is {x}.")

# Box plots of different columns for each gender
groupby_gender = data.groupby('Gender')
groupby_gender.boxplot(column=['FSIQ', 'VIQ', 'PIQ'])

from pandas import plotting

# Scatter matrices for different columns
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])
plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])

import matplotlib.pyplot as plt
plt.show()