"""
2D array and linear algebra solution
"""
import numpy as np
import scipy.linalg as la

a = np.array([[1, 1],
              [0, 1]])
b = np.array([[2, 0],
              [3, 4]])

c = a * b
print(c)

c = a @ b
print(c)

c = a.dot(b)
print(c)

print("17: ",a.sum(axis=0)) # sum of each column

print(a.min(axis=1)) # min of each row

print("几个老头儿去赶集，上街看到一堆梨，一人一个多一个，一人俩梨少俩梨。")
# x - y = -1
# 2x - y = 2
a = np.array([[1, -1], [2, -1]])
b = np.array([[-1],[2]])

c = a @ -b
print(c)
print(f"{c[0][0]}个老头儿，{c[1][0]}个梨。")
c = a.dot(b)
print(c)
c = la.solve(a, b)
print(c)