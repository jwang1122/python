from math import pi

def circle_area(r):
    return r*r*pi

if __name__ == '__main__':
    r = 3
    a = circle_area(r)
    print(f"The area with radius {r} is {a}.")
    print("The area with radius %d is %5.1f." %(r, a))
