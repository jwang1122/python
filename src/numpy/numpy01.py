"""
numpy basic
"""
import numpy as np

a = np.array([1,2,3], dtype='int16')
print(a)

b = np.array([[9.1, 8.3, 7.4],[6.4, 3.7,2.3]])
print(b)

print(a.ndim) # print out dimetion of a
print(b.ndim)
print(b.shape) # 2 row, 3 column

print(a.dtype) # data type of each element in array a
print(a.itemsize) # each element size in byte
print(a.size) # total number of elements
print(a.nbytes) # array total memory size in byte
print(b.dtype)
print(b.itemsize)

# modify element in array
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# get specific element [r, c]
print(a[1,5])

# get row 0
print(a[0,:])
# get coloum 2
print(a[:,2])

# [start:end:step]
print(a[0,1:6:2])

# modify element
a[1,5] = 20
print(a)

a[:,2] = [1,2]
print(a)

# 3 dimention array
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

print(b[0,1,1])

# modify
b[:,1,:] = [[9,9],[8,8]]
print(b)