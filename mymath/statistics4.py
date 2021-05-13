"""
statistics.median(data)

Return the median (middle value) of numeric data, using the common 
“mean of middle two” method. If data is empty, StatisticsError is 
raised. data can be a sequence or iterable.
"""
from statistics import median, median_low, median_high, median_grouped

mid = median([1, 3, 5])
print(mid)

mid = median([6, 4, 1, 3, 5]) # odd number of values
print(mid)

mid = median([1, 2, 3, 4, 12, 16]) # even number of values
print(mid)

mid = median_low([1, 2, 3, 4, 12, 16]) # even number of values
print(mid)

mid = median_high((1, 2, 3, 4, 12, 16)) # even number of values
print(mid)
