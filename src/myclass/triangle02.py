# add __repr__(self)

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
        print(f"Drawing triangle with points: {self}")

if __name__ == '__main__':
    p1 = Point(3,2)
    p2 = Point(5,9)
    p3 = Point(1,0)
    t1 = Triangle(p1,p2,p3)
    t1.draw()