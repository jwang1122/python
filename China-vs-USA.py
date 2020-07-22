"""
parse covid-19 data China vs. US
Issue: x label for all date due to date is string not actual Datetime object
"""
import matplotlib.pyplot as plt
from datetime import datetime

date1 = []
USConfirmed = []
date2 = []
ChinaConfirmed = []

first = True
with open('./data/data_minimal-20200720.csv', 'r') as covid_19:
    for row in covid_19:
#        print(row)
        line = row.split(',')
        if (line[1] == 'US'):
            mydate = datetime.strptime(line[0], '%Y-%m-%d')
            date1.append(mydate)
            confirmed = int(line[2]) # need convert to int
            USConfirmed.append(confirmed)
        if (line[1] == 'CH'):
            mydate = datetime.strptime(line[0], '%Y-%m-%d')
            date2.append(mydate)
            confirmed = int(line[2])
            ChinaConfirmed.append(confirmed)
# print ((date1))
# print ((USConfirmed))
# print ((date2))
# print ((ChinaConfirmed))
def plot():
    fig=plt.figure()
    ax=fig.add_subplot(111)#the 111 means 1x1 grid, first subplot

    x = date1
    y = USConfirmed
    ax.plot(x,y,c='r',ls='-',label='US')
    ax.plot(date2,ChinaConfirmed,c='g',ls='-',label='China')
    labels=ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')
    ax.set(xlabel='Date',ylabel='Confirmed',title='Coronavirus Report')#xlim means x axis limits, sets the limits for the x axis
    plt.legend(loc=2)
    plt.show()

plot()