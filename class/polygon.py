class Polygon:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name

square = Polygon(4, "Square")
pentagon = Polygon(5, "Pentagon")
hexagon = Polygon(6, "hexagon")

print(square.sides)
print(pentagon.sides)
print(hexagon.sides)

