def lcm(x, y):
    greater = x>y and x or y
    while True:
        if greater % x ==0 and greater % y ==0:
            lcm = greater
            break
        greater += 1
    return lcm

if __name__ == '__main__':
    a, b = 12, 83
    result = lcm(a, b)
    print(f"the LCM of {a} and {b} is {result}.")