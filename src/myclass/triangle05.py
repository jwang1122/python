# 
import matplotlib.pyplot as plt
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def rotate(self, angle):
        x = self.x
        y = self.y
        self.x = x * math.cos(angle) - y * math.sin(angle)
        self.y = x * math.sin(angle) + y * math.cos(angle)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __repr__(self):
        return f'Triangle[{self.p1},{self.p2},{self.p3}]'

    def rotate(self, angle):
        self.p1.rotate(angle)
        self.p2.rotate(angle)
        self.p3.rotate(angle)

    def draw(self):
        x = [self.p1.x, self.p2.x, self.p3.x, self.p1.x]
        y = [self.p1.y, self.p2.y, self.p3.y, self.p1.y]
        return x,y

def degree_to_radian(degrees):
    return degrees * (math.pi / 180)

if __name__ == '__main__':
    t1 = Triangle(Point(0,0),Point(5,9),Point(0,5))
    x1,y1 = t1.draw()
    angle = 90
    t1.rotate(degree_to_radian(angle))
    x2,y2 = t1.draw()
    plt.plot(x1,y1,'-r',x2,y2,'-b')
    # plt.axis([-10, 10, -10, 10])
    plt.title(f'Rotate a triangle by {angle} degree')
    plt.show()