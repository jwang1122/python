"""
Any natural number that is not divisible by any other number 
except 1 and itself called Prime Number.
"""

def isPrime(Number):
    flag = True # assume the number is a prime number

    for i in range(2, (Number)):
        if(Number % i == 0):
            flag = False # can be divided by i, the number is not prime number
            break

    if (flag and Number != 1):
        print(" %d is a Prime Number" %Number)
    else:
        print(" %d is not a Prime Number" %Number)

if __name__ == '__main__':
    isPrime(43)