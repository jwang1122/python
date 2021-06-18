"""
Create paadas DataFrame from csv file
"""
import pandas
from pandas import plotting
import matplotlib.pyplot as plt

data = pandas.read_csv('mymath/brain_size.csv', sep=';', na_values='.')
groupby_gender = data.groupby('Gender')
groupby_gender.boxplot(column=['FSIQ', 'VIQ', 'PIQ'])
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])
plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])

plt.show()