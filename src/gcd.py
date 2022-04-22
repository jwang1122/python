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
    a = 60
    b = 48
    print(f"the GCD of {a} and {b} is : {findGCD(a, b)}.")        
    