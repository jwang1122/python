import turtle

# create a turtle object
text = turtle.Turtle()

# set the turtle's color and font size
text.color('green')
text.pensize(1)
text.penup()
text.goto(-100, 0)
text.pendown()
text.write("Hello, World!", font=("Arial", 16, "normal"))

# exit the turtle window
turtle.done()
