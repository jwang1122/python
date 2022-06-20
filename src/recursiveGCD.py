def recursiveGCD(a, b):
    if(b==0):
        return a
    else:
        return recursiveGCD(b, a%b)

if __name__ == '__main__':
    a = 60
    b = 48
    print(f"the GCD of {a} and {b} is : {recursiveGCD(b, a)}.")        
 