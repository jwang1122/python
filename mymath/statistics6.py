"""
statistics.quantiles(data, *, n=4, method='exclusive')

Divide data into n continuous intervals with equal probability. 
Returns a list of n - 1 cut points separating the intervals.
"""
from statistics import quantiles

data = [105, 129, 87, 86, 111, 111, 89, 81, 108, 92, 110,
        100, 75, 105, 103, 109, 76, 119, 99, 91, 103, 129,
         106, 101, 84, 111, 74, 87, 86, 103, 103, 106, 86,
         111, 75, 87, 102, 121, 111, 88, 89, 101, 106, 95,
         103, 107, 101, 81, 109, 104]

print(len(data))
q = quantiles(data, n=10)
for i in q:
    print(i,'', end='')
print()