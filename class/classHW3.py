class Rectangle:
    def __init__(self, width, height, /):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def circumference(self):
        return (self.width + self.height) * 2

if __name__ == '__main__':
    r1 = Rectangle(3, 4)
    print(r1.area())
    print(r1.circumference())