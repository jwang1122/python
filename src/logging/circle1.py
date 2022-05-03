"""
❗️⚡️User may pass wrong argument to function.
"""
from math import pi

def circle_area(r):
    assert type(r) in [int, float], "Radius must to be int or float."
    assert r > 0, "Radius must to be positive number."
    return r * r * pi

if __name__ == '__main__': 
    x = circle_area(2-3j) # 😢without check the calling argument, give you meaningless output
    print(x)
    print("Done.")