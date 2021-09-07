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
print(f"total number of elements: {a.size}") # total number of elements
print(a.nbytes) # array total memory size in byte
print(b.dtype)
print(b.itemsize)

# modify element in array
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(f"2D array size: {a.size}")

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

# print(b[0,1,1])

# modify
b[:,1,:] = [[9,9],[8,8]]
print(b)

c = np.zeros(5)
print(len(c))
c = np.zeros((2,3,3))
print(c)

c = np.ones((4,2,2), dtype='float32')
print(c)

c = np.full((2,2), 99)
print(c)

c = np.full(a.shape, 4.5)
print(c)

c = np.full_like(a, 3)
print(c)

c = np.random.rand(4,2)
print(c)

c = np.random.random_sample(a.shape)
print(c)

c = np.random.randint(-4, 7, size=(3,3))
print(c)

c = np.identity(5)
print(c)

# repeat an array
c = np.array([1,2,3])
r = np.repeat(c, 3)
print(r)

c = np.array([[1,2,3]])
r = np.repeat(c, 3, axis=0)
print(r)

a = np.array([1,2,3,4])
b = a * 2
print(b)

b= np.sin(a)
print(b)