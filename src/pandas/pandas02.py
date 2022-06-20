import pandas as pd
import numpy as np

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
stocks = pd.read_csv('http://bit.ly/smallstocks', parse_dates=['Date'])
titanic = pd.read_csv('http://bit.ly/kaggletrain')
ufo = pd.read_csv('http://bit.ly/uforeports', parse_dates=['Time'])

print(drinks)