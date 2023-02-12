"""
In mathematics, the greatest common divisor (GCD) of two or more integers, 
which are not all zero, is the largest positive integer that divides 
each of the integers. For two integers x, y, the greatest common divisor 
of x and y is denoted {\displaystyle \gcd(x,y)}{\displaystyle \gcd(x,y)}. 
"""

def findGCD(x, y):
    if x>y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x %i ==0) and (y %i ==0)):
            gcd = i
    return gcd

if __name__ == '__main__':
    a = 12
    b = 8
    print(f"GCD({a}, {b}) = {findGCD(a, b)}.")        
    