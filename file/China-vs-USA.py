"""
parse covid-19 data China vs. US
Issue: x label for all date due to date is string not actual Datetime object
"""
import matplotlib.pyplot as plt

date1 = []
USConfirmed = []
date2 = []
ChinaConfirmed = []

first = True
with open('./data/data_minimal.csv', 'r') as covid_19:
    for row in covid_19:
#        print(row)
        line = row.split(',')
        if (line[1] == 'US'):
            date1.append(line[0])
            confirmed = int(line[2]) # need convert to int
            USConfirmed.append(confirmed)
        if (line[1] == 'CH'):
            date2.append(line[0])
            confirmed = int(line[2])
            ChinaConfirmed.append(confirmed)
# print ((date1))
# print ((USConfirmed))
# print ((date2))
# print ((ChinaConfirmed))
def ploy():
    fig=plt.figure()
    ax=fig.add_subplot(111)#the 111 means 1x1 grid, first subplot

    x = date1
    y = USConfirmed
    ax.plot(x,y,c='r',marker='*',ls='-',label='China')
    ax.plot(date2,ChinaConfirmed,c='g',marker='v',ls='-',label='US')
    labels=ax.get_xticklabels()
    plt.setp(labels, rotation=90, horizontalalignment='right')
    ax.set(xlim=['2020-03-04', '2020-04-04'],xlabel='Date',ylabel='Confirmed',title='Coronavirus Report')#xlim means x axis limits, sets the limits for the x axis
    plt.legend(loc=2)
    plt.show()