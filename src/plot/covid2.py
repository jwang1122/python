"""
parse covid-19 data US_NY vs US_TX Confirmed
"""
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# keep US_NY data
date1 = []
newyorkConfirmed = []
newyorkDeath = []
# keep US_TX data
date2 = []
texasConfirmed = []
texasDeath = []

first = True
with open('./data/data_minimal.csv', 'r') as covid_19:
#    reader = csv.reader(covid_19)
    for row in covid_19:
#        print(row)
        if first:
            first = False
            continue
        line = row.split(',')
        if (line[1]=='US_NY'):
            date1.append(datetime.strptime(line[0], '%Y-%m-%d'))
            confirmed = int(line[2])
            newyorkConfirmed.append(confirmed)
            death = line[3].strip()
            death = int(death) if len(death)>0 else 0
            newyorkDeath.append(int(death))
        if(line[1] == 'US_TX'):
            date2.append(datetime.strptime(line[0], '%Y-%m-%d'))
            confirmed = int(line[2])
            texasConfirmed.append(confirmed)
            death=line[3].strip()
            death = int(death) if len(death)>0 else 0
            texasDeath.append(death)
    
    covid_19.close()

#print(date1)
#print(newyorkConfirmed)
# print(len(date2))
fig=plt.figure()

x = date1
y = newyorkConfirmed
z = newyorkDeath

ax=fig.add_subplot(121)
ax.plot(x,y,c='r',ls='-',label='New York')
ax.plot(date2,texasConfirmed,c='g',ls='-',label='Texas')
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlabel='Date', ylabel='Confirmed',
       title='Coronavirus Report')

ax2=fig.add_subplot(1,2,2)
ax2.plot(x,z,c='r',ls='-',label='New York')
ax2.plot(date2,texasDeath,c='g',ls='-',label='Texas')
labels2 = ax2.get_xticklabels()
plt.setp(labels2, rotation=45, horizontalalignment='right')
ax2.set(xlabel='Date', ylabel='Death',
       title='Coronavirus Report')

ax.locator_params(axis='y', nbins=7)
plt.legend(loc=2)
plt.show()