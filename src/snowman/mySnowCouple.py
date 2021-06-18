from turtle import *
from shapes import *

pen1 = Turtle()

pen1.color('darkred','darkred')
pen1.begin_fill()
drawRectangle(pen1, -100, 100, 50, 60)
pen1.end_fill()
pen1.color('darkred')
pen1.width(5)
drawLine(pen1, -110, 100, 0, 80)

mainloop()