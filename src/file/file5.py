"""
plot data that defined in csv file.
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("src/data/students.csv")

x = data['First name']
y = data['Score']

plt.plot(x, y)

plt.xlabel('Student First Name')
plt.ylabel('Score')
plt.show()
