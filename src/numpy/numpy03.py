import numpy as np

a = np.genfromtxt('data/data.txt', delimiter=',')
print(a.astype('int32'))
b = a>5
print(b)
print(a[a>50])
b = np.array([1,2,3,4,5,6,7,8,9])
print(b[[1,2,8]]) # new list from given indexes
print(a)
b = np.any(a > 50, axis=0) # any column which has value>50 will return True
print(b)
b = np.all(a>50, axis=0)
print(b)

b = ((a>50) & (a<100))
print(b)

a = np.genfromtxt('data/data2.txt', delimiter=',')
print(a)
print(a[2:4, 0:2])
print(a[[0,1,2,3],[1,2,3,4]])
print(a[[0,4,5],3:])