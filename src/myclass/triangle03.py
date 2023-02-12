# use matplotlib draw triangle by given 3 points

import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def draw(self):
        x = [self.p1.x, self.p2.x, self.p3.x, self.p1.x]
        y = [self.p1.y, self.p2.y, self.p3.y, self.p1.y]
        plt.plot(x, y)
        plt.show()

p1 = Point(1, 1)
p2 = Point(5, 1)
p3 = Point(3, 5)
triangle = Triangle(p1, p2, p3)
triangle.draw()
