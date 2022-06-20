def triangleArea(b, h):
    return b*h/2

if __name__ == '__main__':
    b,h = 12, 4
    print(f"a triangle area with base={b} and height={h} is {triangleArea(b, h):.3f}.")