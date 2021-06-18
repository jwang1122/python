"""
Array Indexing, Slicing and Iterating
"""
import numpy as np

a = np.arange(10)**2
print(a)
print(a[3]) # Slicing

print(a[2:5]) # sub array
print(a)
a[:5:2] = 1000 # from start to position 5, exclusive, set every 2nd element to 1000
print(a)

b = a[::-1] # reversed a
print(b)

for x in a:
    print(f"{x**(1/3.):.02f}",'',end='')
print()

# Create 2D array from given function
def f(x,y):
    return 3*x + 2*y

a = np.fromfunction(f, (5,4), dtype=int) # 5 rows and 4 columns 2D array
print(a)
print(a[2,3])
print(a[-1])
b = a[::-1]
print(b)
b = a[::-1,-1]
print(b)

b = [i for i in a.flat]
print(b)

b = a.copy()
print(a)
print(b)
a[0][0] = 11 # assignment only affact array a
print(a)
print(b)
