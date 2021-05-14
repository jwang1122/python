"""
哥哥领工资$131，全部是$2和$5的票面，共40张。问每个票面多少张？
x: number of $2 bill
y: number of $5 bill

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
print(f"There are {x[0][0]:.0f} $2 bill, and {x[1][0]:.0f} $5 bill.")

total = 2*x[0][0] + 5*x[1][0]
print(f"Total of ${total:.0f}.")