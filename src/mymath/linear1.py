"""
几个老头儿去赶集，上街见着一堆梨，一人一个多一个，一人两梨少两梨。问：几个老头儿几个梨？
Some old man went shopping, there are some pears, if each man get one pear, there will
be additional one leftover; if each man get two pears, they need two more. How many
man and pears?

two variables linear algebra, let
x: the number of old man
y: the number of pears

x - y = -1
2x -y = 2
"""
import numpy as np
import scipy.linalg as la

a = np.array([[1, -1], [2, -1]])
b = np.array([[-1],[2]])
x = la.solve(a, b)
print(x)
print(f"There are {x[0][0]:.0f} old man and {x[1][0]:.0f} pears.")