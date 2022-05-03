from math import pi

def circleArea(radius):
    print("circleArea()... the input radius is", radius)
    if type(radius) not in [int, float]:
        print("circleArea(): the radius must to be [int, float].")
        return None
    if radius < 0:
        print("circleArea(): the radius must to be positive number.")
        return None
    return pi * radius**2

if __name__ == '__main__':
    x = circleArea(-2)
    print(x)