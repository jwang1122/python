# use matplotlib draw triangle by given 3 points

import matplotlib.pyplot as plt

def draw_triangle(point1, point2, point3):
    x_values = [point1[0], point2[0], point3[0]]
    y_values = [point1[1], point2[1], point3[1]]
    
    plt.plot(x_values, y_values, "ro-")
    plt.fill(x_values, y_values, "b")
    plt.axis([0, 10, 0, 10])
    plt.show()
    
point1 = (1, 1)
point2 = (5, 5)
point3 = (9, 1)

draw_triangle(point1, point2, point3)
