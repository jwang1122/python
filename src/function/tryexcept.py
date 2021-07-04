"""
❗️⚡️User may pass wrong argument to function.
✋raise Error when bad thing happens.
👌👎catch the Error while calling the function
"""
from math import pi

def circle_area(r):
    if type(r) in [int, float]:
        return r * r * pi
    raise TypeError("Please check radius data type.")


if __name__ == '__main__':
    try:
        x = circle_area(2)
        print(f"the circle area of radius=2 is {x}.")
        x = circle_area(-2)
        print(f"the circle area of radius=-2 is {x}.")
        x = circle_area(2-3j) 
        print(x)
    except Exception as error:
        print(error)
    print("Done.")