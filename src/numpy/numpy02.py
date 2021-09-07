"""
linear algebra
"""
import numpy as np
a = np.ones((2,3))
b = np.full((3,2),2)
c = np.matmul(a,b)
print(c)

a = np.identity(3)
b = np.linalg.det(a) # determint 
print(b)

stats = np.array([[1,2,3],[4,5,6]])
min = np.min(stats)
print(min)
max = np.max(stats)
print(max)

min = np.min(stats, axis=1)
print(min)

total = np.sum(stats) # np.sum(stats, axis=1)
print(total)

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape((8,1))
print(after)

# vertically stacking vector
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
a = np.vstack([v1, v2])
print(a)

# horizontal stacking
a = np.hstack([v1,v2])
print(a)