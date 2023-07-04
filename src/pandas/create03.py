import pandas as pd
import numpy as np
from dataclasses import make_dataclass
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
points = pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
print(points)


x_values = points.apply(lambda row: row[0].x, axis=1)
y_values = points.apply(lambda row: row[0].y, axis=1)

plt.plot(x_values, y_values, 'o')  # 'o' for marker style, you can choose a different marker if desired
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of Points')
plt.show()

Point = make_dataclass("Point", [("x", int), ("y", int)])
df = pd.DataFrame([Point(3, 1), Point(0, 3), Point(2, 3)])
print(df)

plt.scatter(df['x'], df['y'], color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of Points')
plt.show()