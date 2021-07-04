"""
plot covid data that defined in csv file data_minimal.csv.
    - [Online data](https://open-covid-19.github.io/data/data_minimal.csv)

"""
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("src/data/data_minimal.csv")

x = data['Date']
y = data['Confirmed']

plt.plot(x,y)
plt.show()