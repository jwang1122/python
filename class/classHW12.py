class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

r = 8
hw12 = Circle(r)
print(f"The circle area with radius={r} is {hw12.area()}")
print(f"The circle perimeter with radius={r} is {hw12.perimeter()}")
