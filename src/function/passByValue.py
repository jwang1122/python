

def swap(x, y): # assign variable a value to  local variable x, b to local variable y
    print(x, y)
    tmp = x
    x = y
    y = tmp
    print(x, y)

if __name__ == '__main__':
    a, b = 3, 5
    swap(a, b)
    print(a, b)