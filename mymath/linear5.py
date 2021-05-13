"""
某次数学考试考五道题，全班52人参加，共做对181道题，
已知每人至少做对1道题，做对1道的有7人，5道全对的有6人，
做对2道和3道的人数一样多，那么做对4道的人数有多少人？

x1: students who get 1 correct
x2: students who get 2 correct
x3: students who get 3 correct
x4: students who get 4 correct
x5: students who get 5 correct

x1+x2+x3+x4+x5=52
x1 = 7
x2 - x3 = 0
x5 = 6
x1 + 2*x2 + 3*x3 + 4*x4 +5*x5 = 181  
"""

import numpy as np
import scipy.linalg as la

