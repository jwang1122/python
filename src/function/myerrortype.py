class ValueTooBigError(Exception):
    pass

def factorial(n):
    if n > 10:
        raise ValueTooBigError(f"the input number n={n} is greater than 10.")
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

if __name__ == '__main__':
    x = factorial(11)
    print(x)