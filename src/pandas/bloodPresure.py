import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

sugar = pd.read_csv('data/bloodPresure.csv')

print(type(sugar))
print(sugar.axes)

fontP = font_manager.FontProperties()
fontP.set_family('SimHei')
fontP.set_size(12)

rows = len(sugar.index)
high1 = [140 for i in range(rows)]
high2 = [90 for i in range(rows)]
sugar['high1'] = high1
sugar['high2'] = high2


sugar.plot(x='Date',y=['高压午','high1','high2'])


plt.title("熙文血压变化图示", fontproperties=fontP)
plt.legend(loc=0,prop=fontP)
plt.xticks(rotation='45')
plt.show()

# sugar.plot(x='Date',y=high)
sugar.plot(x='Date',y='高压午')
plt.legend(loc=0,prop=fontP)
plt.xticks(rotation='45')
plt.show()

sugar.plot(x='Date',y='体重')
plt.legend(loc=0,prop=fontP)
plt.xticks(rotation='45')
plt.show()

avg = sugar.mean()
print("熙文血压平均值")
print(f"{avg}")