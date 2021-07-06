import pandas as pd
from matplotlib import pyplot as plt

covid19 = pd.read_csv("src/data/data_minimal.csv")
# print(covid19)
print(type(covid19)) # <class 'pandas.core.frame.DataFrame'>
print(covid19.columns)
x = covid19.Key # get column 'Key' data: 
print(type(x)) # <class 'pandas.core.series.Series'>
print(covid19.Key.iloc[21969]) # Retrieve individual data
# print(covid19['Key'=='US_NY'])
newyork = covid19[covid19['Key']=='US_NY'] # retrieve only New York data
print(newyork)
newyork.plot(x='Date')
plt.show()

newyork_deaths = newyork[['Date','Deaths']] # grab only deaths column
print(newyork_deaths)
newyork_deaths.plot(x='Date')
plt.legend(['New York Deaths'])
plt.show()

texas = covid19[covid19['Key']=='US_TX'] # retrieve only New York data
# print(texas)
# texas.plot(x='Date')
# plt.show()

texas_deaths = texas[['Date','Deaths']] # grab only deaths column
print(texas_deaths)
texas_deaths.plot(x='Date')
plt.legend(['Texas Deaths'])
plt.show()

# for frame in [newyork_deaths, texas_deaths]:
#     plt.plot(frame['Date'], frame['Deaths'])
# plt.show()

ax = newyork_deaths.plot(x='Date')
texas_deaths.plot(x='Date',ax=ax)
plt.show()