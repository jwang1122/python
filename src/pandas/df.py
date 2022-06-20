import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

sugar = pd.read_csv('data/bloodPresure.csv')

print(sugar)
print(type(sugar))
print(sugar.axes)
print(sugar.index)
print(sugar.columns)
print(sugar.values)
print(sugar.loc[5]) # get all column values on index=5
print(sugar.size) # data rows * columns
print(len(sugar.index)) # number of rows