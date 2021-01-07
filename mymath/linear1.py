"""
几个老头儿去赶集，上街见着一堆梨，一人一个多一个，一人两梨少两梨。问：几个老头儿几个梨？
几个老头儿去赶集，上街见着一堆梨，一人两个多一个，一人仨梨少两梨。问：几个老头儿几个梨？
two variables linear algebra
x - y = -1
2x -y = 2
where x is the number of old man
y is the number of pears
"""
import numpy as np
import scipy.linalg as la

a = np.array([[1, -1], [2, -1]])
print(a)
b = np.array([[-1],[2]])
print(b)
x = la.solve(a, b)
print(x)