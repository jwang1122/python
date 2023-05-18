import numpy as np
import math

def findN(epsilon, radius): # fo
    n = 10
    area = math.pi*radius**2/4
    while(True):
        sum = 0
        for i in range(0, n):
            x = i*radius/n
            y = np.sqrt(radius**2 - x**2)
            sum += radius/n * y 
        if sum - area < epsilon:
            break
        n += 1
    return n, sum

if __name__ == '__main__':
    r = 200
    e = float(input("input the epsilon that you expected: "))
    n, sum = findN(e,r)
    area = math.pi * r*r/4
    diff = sum-area
    print(f'when n = {n}, the difference={diff} < {e}.')