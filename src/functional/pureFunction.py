def m(n): # pure function only rely on argument variable
    return 2**n - 1

globalAdjustment = 3

def f(a, b, c): # depends on global state
    global globalAdjustment
    return a + b * c + globalAdjustment

if __name__ == '__main__':
    x = m(5)
    print(x)

    x = f( 3, 2, 1)
    print(x)