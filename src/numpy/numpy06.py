"""
std = sqrt(mean(abs(x - x.mean())**2))
var = mean(abs(x - x.mean())**2).
"""
import numpy as np

a = [1,2,3,4]
print(np.std(a))
print(np.var(a))