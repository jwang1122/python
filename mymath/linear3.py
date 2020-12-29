"""
哥哥领工资$131，全部是$2和$5的票面，共40张。问每个票面多少张？
2x + 5y = 131
x + y = 40
"""
import numpy as np
import scipy.linalg as la

a = np.array([[2, 5], [1, 1]])
print(a)
b = np.array([[131],[40]])
print(b)
x = la.solve(a, b)
print(x)
