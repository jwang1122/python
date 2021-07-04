from math import pi

def circle_area(r):
    return r * r * pi

# if __name__ == '__main__': # True if you run this program, or __name__=='circle', which is file name
x = circle_area(r=2) # call function without argument?
print(x)
print("Done.")