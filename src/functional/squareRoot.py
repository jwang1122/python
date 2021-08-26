"""
calculate square root of 2 by function chain
"""
def next(n, x):
    return (x+n/x)/2


def recursion(e, x):
    n = 2
    a = next(n, x)
    b = next(n, a)
    if a-b < e:
        return b
    return recursion(e, b)

if __name__ == '__main__':
    n = 2
    f = lambda x: next(n, x) # lambda expression usage
    a0 = 1
    l1 = [round(x, 4) for x in (a0, f(a0), f(f(a0)), f(f(f(a0))), f(f(f(f(a0)))))]
    print(l1)

    x = recursive(0.0001, 1)
    print(f"{x:.4f}")