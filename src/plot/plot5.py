import matplotlib.pyplot as plt

labels = ['To Do', 'In Progress', 'In Test', 'In Review', 'Done']
colors = ['#0052CC', '#F6C242ff', '#F6C242aa', '#F6C24266', '#008759']

day         = [1, 2, 3, 4, 5]
todo        = [10, 8, 6, 4, 2]
in_progress = [2, 3, 4, 3, 2]
in_test     = [7, 8, 7, 2, 2]
in_review   = [8, 5, 7, 8, 1]
done        = [0, 2, 4, 6, 12]

plt.stackplot(day, todo, in_progress, in_test, in_review, done, labels=labels, colors=colors)
plt.legend(loc='upper left')
plt.show()