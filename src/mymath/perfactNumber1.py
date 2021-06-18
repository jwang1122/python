"""
total of 51 perfact number.
"""
def isPerfectNumber(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

def findPerfactNumber(start, end):
    l = []
    for x in range(start, end):
        if isPerfectNumber(x):
            l.append(x)
    return l

print(isPerfectNumber(6))
l = findPerfactNumber(40000,50000)
print(l)