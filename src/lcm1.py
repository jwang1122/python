from gcd import *

def lcm(a, b):
    return int(a*b/findGCD(a,b))

if __name__ == '__main__':
    a, b = 12, 83
    result = lcm(a, b)
    print(f"the LCM of {a} and {b} is {result}.")
