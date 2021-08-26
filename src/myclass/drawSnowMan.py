"""
draw snowman by using class Snowman
"""
from turtle import *
from snowman import *

pen1 = Turtle()
screen1 = Screen()
pen1.shape("turtle")


man = Snowman(0, -100, 20, 40, 70, True)
man.draw(pen1)

kid = Snowman(170, -100, 20, 30, 50, True)
kid.draw(pen1)

kid = Snowman(-270, -100, 30, 30, 40, False)
kid.draw(pen1)

woman = Snowman(-150, -100, 20, 40, 70, False)
woman.draw(pen1)

drawLine(pen1, -330, -100, 0, 570)
#pen1.hideturtle()


screen1.mainloop()