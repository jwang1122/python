from range1 import range1 

def isprime(n):
    if n<2: return False
    # for j in range1(2, n//2):
    #     if n%j==0: return False
    # return True
    return len(tuple(filter(lambda j:n%j==0, range1(2, n//2))))==0

if __name__ == '__main__':
    list1 = list(filter(isprime, range1(2, 100)))
    print(list1)

    list1 = [23,12,44,27,17,59,43]
    list1 = list(filter(isprime, list1))
    print(list1)
