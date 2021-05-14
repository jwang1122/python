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
b = np.array([[100],[32]])
x = la.solve(a, b)
print(x)

print(f"There are {x[0][0]:.0f} chicken and {x[1][0]:.0f} rabbits.")
