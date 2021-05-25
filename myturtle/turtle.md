# Overview of available Turtle and Screen methods

- [Overview of available Turtle and Screen methods](#overview-of-available-turtle-and-screen-methods)
  - [References](#references)
  - [Turtle methods](#turtle-methods)
    - [Turtle motion Move and draw](#turtle-motion-move-and-draw)
    - [Tell Turtle’s state](#tell-turtles-state)
    - [Setting and measurement](#setting-and-measurement)
    - [Pen control Drawing state](#pen-control-drawing-state)
    - [Color control](#color-control)
    - [Filling](#filling)
    - [More drawing control](#more-drawing-control)
    - [Turtle state Visibility](#turtle-state-visibility)
    - [Appearance](#appearance)
    - [Using events](#using-events)
    - [Special Turtle methods](#special-turtle-methods)
    - [Methods of TurtleScreen/Screen Window control](#methods-of-turtlescreenscreen-window-control)
    - [Animation control](#animation-control)
    - [Using screen events](#using-screen-events)
    - [Settings and special methods](#settings-and-special-methods)
    - [Input methods](#input-methods)
    - [Methods specific to Screen](#methods-specific-to-screen)

## References
[Turtle Website](https://docs.python.org/3/library/turtle.html)

[Convert png to gif online](https://image.online-convert.com/convert-to-gif)

[Create a button by turtle](https://www.youtube.com/watch?v=tl5nBPKbmSI)

## Turtle methods
### Turtle motion Move and draw
* forward() | fd()
* backward() | bk() | back()
* right() | rt()
* left() | lt()
* goto() | setpos() | setposition()
* setx()
* sety()
* setheading() | seth()
* home()
* circle()
* dot()
* stamp()
* clearstamp()
* clearstamps()
* undo()
* speed()

### Tell Turtle’s state
* position() | pos()
* towards()
* xcor()
* ycor()
* heading()
* distance()

### Setting and measurement
* degrees()
* radians()

### Pen control Drawing state
* pendown() | pd() | down()
* penup() | pu() | up()
* pensize() | width()
* pen()
* isdown()

### Color control
* color()
* pencolor()
* fillcolor()

### Filling
* filling()
* begin_fill()
* end_fill()

### More drawing control
* reset()
* clear()
* write()

### Turtle state Visibility
* showturtle() | st()
* hideturtle() | ht()
* isvisible()

### Appearance
* shape()
* resizemode()
* shapesize() | turtlesize()
* shearfactor()
* settiltangle()
* tiltangle()
* tilt()
* shapetransform()
* get_shapepoly()

### Using events
* onclick()
* onrelease()
* ondrag()

### Special Turtle methods
* begin_poly()
* end_poly()
* get_poly()
* clone()
* getturtle() | getpen()
* getscreen()
* setundobuffer()
* undobufferentries()

### Methods of TurtleScreen/Screen Window control
* bgcolor()
* bgpic()
* clear() | clearscreen()
* reset() | resetscreen()
* screensize()
* setworldcoordinates()

### Animation control
* delay()
* tracer()
* update()

### Using screen events
* listen()
* onkey() | onkeyrelease()
* onkeypress()
* onclick() | onscreenclick()
* ontimer()
* mainloop() | done()

### Settings and special methods
* mode()
* colormode()
* getcanvas()
* getshapes()
* register_shape() | addshape()
* turtles()
* window_height()
* window_width()

### Input methods
* textinput()
* numinput()

### Methods specific to Screen
* bye()
* exitonclick()
* setup()
* title()