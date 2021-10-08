temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26), \
        ("Tokyo", 27), ("New York", 28),("London", 22),("Beijing", 32)]

c2f = lambda data: (data[0], round((9 / 5) * data[1] + 32, 2))

def test():
    x = list(map(c2f, temps))
    print(x)

def mymap(f, data): # simulate how map works
    result = []
    for d in data:
        x = f(d)
        result.append(x)
    return result

def test1():
    z = mymap(c2f, temps)
    print(z)

if __name__ == '__main__':
    print(temps)
    print()
    test()
    print()
    test1()