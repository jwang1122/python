from prime2 import *

def rangePrime(x,y):
    list1 = []
    for i in range (x,y+1):
        if (isPrime(i)):
            list1.append(i)
    return list1

if __name__ == '__main__':
    n1 = 40
    n2 = 50
    l1 = rangePrime(n1,n2)
    print(l1)
    print("The number of prime numbers between %d and %d is %d" %(n1,n2,len(l1)))
    print(f"The number of prime numbers between {n1} and {n2} is {len(l1)}")
    