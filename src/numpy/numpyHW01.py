import numpy as np

a = np.full((5,5), 1)

for i in range(1,4):
    a[i,1:4] = [0,0,0]
a[2,2] = 9

print(a)

a = np.full((5,5), 1)
b = np.zeros((3,3))
b[1,1] = 9
a[1:-1,1:-1] = b
print(a)

