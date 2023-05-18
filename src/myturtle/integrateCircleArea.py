from turtle import *
from shapes import *
import numpy as np
import math

pen1 = Turtle()

radius = 200
pen1.color('black','red')
pen1.begin_fill()
drawCircle(pen1, 0, -radius, radius)

angle = math.pi/3
x = radius * np.cos(angle)
y = radius * np.sin(angle)

drawLine(pen1, -radius-20, 0, 0, 2*(radius+20))
drawLine(pen1, 0, -radius-20, -90, 2*(radius+20))

pen1.color('black','blue')
pen1.begin_fill()
drawRectangle(pen1, x, 0, 5, y)
pen1.end_fill()

drawLine(pen1, 0,0,-60,radius)

drawText(pen1, 220, 0, 'x')
drawText(pen1, 0, 220, 'y')
drawText(pen1, 10, 0, 'θ')
drawText(pen1, x-2, -13, 'dx')
drawText(pen1, x, y+10, '(x, y)')
drawText(pen1, x+10, 80, 'y')
drawText(pen1, x-40, -13, 'x')
drawText(pen1, x-60, 90, 'r')
drawText(pen1, x, y, '(r cos(θ), r sin(θ))')

mainloop()