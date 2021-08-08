# import package 
from turtle import * 
  
# method to draw ellipse 
def drawEclipse(pen, rad, ratio=2, forward=True): 
  # rad --> radius of arc 
  pen.pendown()
  pen.tilt(45)

  if forward:
    rad = -rad
  for i in range(2):       
    # two arcs 
    pen.circle(rad,90)
    pen.circle(rad//ratio,90) 
  pen.penup()



if __name__ == '__main__':
    
  # Main section 
  # tilt the shape to negative 45 
  # turtle.seth(90) 
  pen = Turtle()
  pen.hideturtle()
  # calling draw method 
  # drawEclipse(pen, 50, ratio=4)
  # pen.fd(-100)
  drawEclipse(pen, 50, forward=True)
  # drawEclipse(pen, 50, forward=False)

  # radius = 50
  # extent = 90
  # ratio = 2
  # pen.circle(radius,extent)  
  # pen.circle(radius//ratio,extent)  

  exitonclick()