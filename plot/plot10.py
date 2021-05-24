import matplotlib.pyplot as plt


slices = [20, 6, 3, 13]
status = ['todo', 'in progress', 'in test', 'done']
colors = ['#0052CC', '#F6C242ff', '#F6C242aa', '#008759']

plt.pie(
    x=slices,            # data
    labels=status,       # name of the slices
    colors=colors,       # colors
    startangle=90,       # angle at which start plotting
    shadow=True,         # drop shadow outline?
    explode=[0,1,0,0],   # which piece to explode out from the chart
    autopct='%1.2f%%',   # number formatting
    radius=1,            # size of the chart
)

plt.show()