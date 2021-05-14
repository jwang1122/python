"""
2016年时，父母年龄（整数）和是78岁，兄弟的年龄和是17岁。
四年后（2020年）父的年龄是弟的年龄的4倍，母的年龄是兄的年龄的3倍.
那么当父的年龄是兄的年龄的3倍时，是公元哪一年？

x1: father's age
x2: mather's age
x3: elder brother's age
x4: yonger brother's age
x5: the year that father's age is 3 times of elder brother.

x1 + x2 = 78
x3 + x4 = 17
x1 - 4*x4 = 12 << x1 + 4 = (x4+4)*4
x2 - 3*x3 = 8  << x2 + 4 = (x3+4)*3
x1 - 3*x3 - 2*x5 = -4032 << x1 + (x5-2016) = (x3 + (x5-2016))*3
"""

import numpy as np
import scipy.linalg as la

a = np.array([[1, 1, 0, 0, 0], [0, 0, 1, 1, 0], [1, 0, 0, -4, 0], [0, 1, -3, 0, 0],[1,0,-3,0,-2]])
b = np.array([[78], [17], [12], [8],[-4032]])
x = la.solve(a, b)
print(x)
print(f"The year {x[4][0]:.0f} father's age is 3 times of elder brother's age.")

"""
f+n = 3(x+n)
(f-x)/2 -x = n 
"""
print((x[0]-x[2])/(3-1) - x[2])
"""
n year later, father age will be 3 times of elder brother's age.
"""