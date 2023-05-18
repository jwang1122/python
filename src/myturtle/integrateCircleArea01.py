from turtle import *
from shapes import *
import numpy as np
import math

pen1 = Turtle()

radius = 200
pen1.color('black','yellow')
pen1.begin_fill()
drawCircle(pen1, 0, -radius, radius)
pen1.end_fill()

angle = math.pi/6
x = radius * np.cos(angle)
y = radius * np.sin(angle)

drawLine2(pen1, (-radius-20, 0), ((radius+20),0)) # draw x axis
drawLine(pen1, 0, -radius-20, 90, 2*(radius+20)) # draw y axis

pen1.color('black','blue')
pen1.begin_fill()
p1 = (0,0)
p2=(radius*np.cos(angle), radius*np.sin(angle))
p3 = (radius*np.cos(angle+0.1), radius*np.sin(angle+0.1))
drawTriangle(pen1, p1, p2, p3)
pen1.end_fill()

drawText(pen1, 20, -2, 'θ')
drawText(pen1, 80, 60, 'r')
drawText(pen1, 20, 20, 'dθ')
drawText(pen1, 170, 110, 'r dθ')

pen1.hideturtle()

mainloop()