from math import pi

class Circle:
    def __init__(self, radius, /):
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2
    
    def circumference(self):
        return self.radius  * 2 * pi

if __name__ == '__main__':
    c1 = Circle(3)
    print(c1.area())
    print(c1.circumference())
    print(type(c1).__name__)