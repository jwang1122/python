from math import pi

def sphereVolume(r):
    v = 3/4 * pi * pow(r,2)
    return v
    
def sphereSurfaceArea(r):
    return 4 * pi * pow(r, 2)


if __name__ == '__main__':
    r = 2
    print(f"A sphere volume with radius={r} is {sphereVolume(r):.3f}.")