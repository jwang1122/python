def whileGCD(a, b):
    while b:
        a, b = b, a%b
    return a

if __name__ == '__main__':
    a = 60
    b = 48
    print(f"the GCD of {a} and {b} is : {whileGCD(b, a)}.")        
