from my_timer2 import *

def isPrime(x):
    flag = True

    for i in range(2, (x//2+1)):
        if(x % i == 0):
            flag = False
            break

    return flag and x != 1

@my_timer
def findPrimeWithIn(n):
    l = []
    for i in range(1, n):
        if isPrime(i):
            l.append(i)
    return l

if __name__ == "__main__":
    l = findPrimeWithIn(100000)
    # print(l)
    print(len(l))