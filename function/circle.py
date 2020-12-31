from math import pi

def circle_area(r):
    return r * r * pi

if __name__ == '__main__':
    x = circle_area() # call function without argument
    print(x)
    print("Done.")