import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Define the three points of the triangle
point1 = (-100, -100)
point2 = (0, 100)
point3 = (100, -100)

# Move the turtle to the first point
my_turtle.penup()
my_turtle.goto(point1)
my_turtle.pendown()

# Draw the triangle
my_turtle.goto(point2)
my_turtle.goto(point3)
my_turtle.goto(point1)

# Hide the turtle and display the drawing
my_turtle.hideturtle()
turtle.done()
