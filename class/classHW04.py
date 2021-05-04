from math import pi

class Circle:
    def area(r):
        return pi * r * r

    def diameter(r):
        return 2 * r

    def Circumference(r):
        return 2 * r * pi

        
c = Circle()
print(f"The class name of the instance c is '{type(c).__name__}'.")

for x in Circle.__dict__:
    print(x)

print(Circle.__dict__['area'])