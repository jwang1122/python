"""
statistics.mode(data)

Return the single most common data point from discrete or nominal data. 
The mode (when it exists) is the most typical value and serves as 
a measure of central location.

If there are multiple modes with the same frequency, returns the 
first one encountered in the data. 
"""
from statistics import mode, multimode

m = mode([1, 1, 2, 3, 3, 3, 3, 4])
print(m)

m = mode([1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4])
print(m)

m = mode([1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4])
print(m)

m = mode(["red", "blue", "blue", "red", "green", "red", "red"])
print(m)

m = multimode([1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4])
print(m)

m = multimode('aabbbbccddddeeffffgg')
print(m)

