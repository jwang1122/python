import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from sklearn.linear_model import LinearRegression
import numpy as np

weight = pd.read_csv('data/bloodPresure.csv')

fontP = font_manager.FontProperties()
fontP.set_family('SimHei')
fontP.set_size(12)

x = [i for i in range(64)]
weight['x']=x
x = weight['x'].values.reshape(-1,1)
y = weight['体重']
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)
y_pred = linear_regressor.predict(x)
# intercept = f"{linear_regressor.intercept_:.2f}"
# coefficent = f"{linear_regressor.coef_:.3f}"


fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)

# Set titles for the figure and the subplot respectively
fig.suptitle('熙文体重线性回归分析', fontsize=14, fontweight='bold', fontproperties=fontP)

ax.set_xlabel('天数', fontproperties=fontP)
ax.set_ylabel('体重', fontproperties=fontP)
text= r"$y=-0.0462 \cdot x + 84.67$"
ax.text(0,80,text, fontsize=15)

ax.scatter(x, y)
ax.plot(x, y_pred, color='red')
plt.show()

