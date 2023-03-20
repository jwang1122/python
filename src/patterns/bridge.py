class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at ({x}, {y}) with radius {radius}")

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2.circle at ({x}, {y}) with radius {radius}")

class Shape:
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    def draw(self):
        pass

    def resize(self, radius):
        pass

class CircleShape(Shape):
    def __init__(self, x, y, radius, drawing_api):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def resize(self, radius):
        self.radius = radius

# Usage
drawing_api1 = DrawingAPI1()
drawing_api2 = DrawingAPI2()

circle1 = CircleShape(1, 2, 3, drawing_api1)
circle1.draw()

circle2 = CircleShape(4, 5, 6, drawing_api2)
circle2.draw()

circle1.resize(4)
circle1.draw()

circle2.resize(7)
circle2.draw()
