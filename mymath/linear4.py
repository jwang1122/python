"""
2016年时，父母年龄（整数）和是78岁，兄弟的年龄和是17岁。
四年后（2020年）父的年龄是弟的年龄的4倍，母的年龄是兄的年龄的3倍.
那么当父的年龄是兄的年龄的3倍时，是公元哪一年？

x1: father's age

"""

import numpy as np
import scipy.linalg as la

a = np.array([[1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, -4], [0, 1, -3, 0]])
print(a)
b = np.array([[78], [17], [12], [8]])
print(b)
x = la.solve(a, b)
print(x)

"""
f+n - (x+n) = 2(x+n)
(f-x)/2 -x = n 
"""
print((x[0]-x[2])/(3-1) - x[2])
"""
n year later, father age will be 3 times of elder brother's age.
"""