from math import pi

def area(*args, mod="circle"):
    if len(args)==1 and mod=='circle':
        r = args[0]
        return r*r*pi
    elif len(args)==1 and mod=="square":
        s = args[0]
        return s*s
    elif len(args)==2 and mod=="rectangle":
        width = args[0]
        height = args[1]
        return width*height
    elif len(args)==2 and mod=="triangle":
        side = args[0]
        height = args[1]
        return side*height/2.0
    else:
        return "Unsupported area calculation on mod: %s."%mod

if __name__ == '__main__':
    r = 1.0
    a = area(r)
    print(f"The circle area with radius {r} is {a}.")
    width = 2
    height = 3.2
    print(f"The rectangle area with width={width} and height={height} is {area(width,height,mod='rectangle')}.")
    side=3.2
    height=2
    a = area(side, height, mod="triangle")
    print(a)
    a = area(2,mod="hexagon")
    print(a)
    print("Done.")