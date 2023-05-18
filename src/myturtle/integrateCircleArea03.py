from turtle import *
from shapes import *
from integrateCircleArea04 import *
import numpy as np
import math

pen1 = Turtle()

radius = 200
pen1.color('black','yellow')
pen1.begin_fill()
drawCircle(pen1, 0, -radius, radius)
pen1.end_fill()

drawLine2(pen1, (-radius-20, 0), ((radius+20),0)) # draw x axis
drawEquilateral(pen1, (radius+20), -3, 30, 5)
drawLine(pen1, 0, -radius-20, 90, 2*(radius+20)) # draw y axis
drawEquilateral(pen1, 2, radius+20, 120, 5)
drawText(pen1, 220, 0, 'x')
drawText(pen1, 0, 230, 'y')

def rectangle(x, r, n):
    y = np.sqrt(r**2 - x**2)
    width = r/n

    pen1.color('black','blue')
    pen1.begin_fill()
    drawRectangle(pen1, x, 0, width, y)
    pen1.end_fill()
    return y*width

n = 100
sum = 0
for i in range(n):
    dx = rectangle(i*radius/n, radius, n)
    sum += dx

area = math.pi * radius**2/4
diff = sum - area

drawText(pen1, 20, 230, f'area = {sum:.2f}, should be {area:.2f}, difference is {diff:.2f}')

epsilon = 200
n, sum = findN(epsilon, radius)
drawText(pen1, 20, 210, f'when n={n}, the area difference={(sum-area):.2f} ϵ < {epsilon}, and sum={sum:.2f}')    
pen1.hideturtle()
mainloop()