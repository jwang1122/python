"""
鸡兔同笼：32个头，100 条腿，几只鸡，几只兔？
x：鸡
y: 兔
2x + 4y = 100
x + y = 32
"""
import numpy as np
import scipy.linalg as la

a = np.array([[2, 4], [1, 1]])
print(a)
b = np.array([[100],[32]])
print(b)
x = la.solve(a, b)
print(x)

there are 14 checken and 18 rabittes.
