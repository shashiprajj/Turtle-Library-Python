import turtle
import math

#set background color
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create one turtle
george = turtle.Turtle()
george.color("black")
george.shape("turtle")
george.speed(10)

# Define a function to draw and fill a rectangle with the given
#dimensions and color
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

#define a function to draw and fill an equilateral right
#triangle with the given hypotenuse length and color. This
# is used to create a roof shape
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length/ math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()

# Define a function to draw and fill a parallelogram, used to
# draw the side of the house
def drawParallelogram(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(120)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(90)
    t.end_fill()

# define a function to draw four sun rays of the given length,
#for the sun of the given radius. The turtle starts in the
# centre of the circle
def drawFourRays(t, length, radius):
    for i in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length + radius)
        t.left(90)

#  Draw and fill the front end of the house
george.penup()
george.goto(-150, -120)
george.pendown()
drawRectangle(george, 100, 110, 'blue')

#draw and fill the front door
george.penup()
george.goto(-150, -120)
george.pendown()
drawRectangle(george, 40, 60, "light green")

# Front roof
george.penup()
george.goto(-150, -10)
george.pendown()
drawTriangle(george, 100, "magenta")

# side of the house
george.penup()
george.goto(-50, -120)
george.pendown()
drawParallelogram(george, 60, 110, "yellow")

#Window
george.penup()
george.goto(-30, -60)
george.pendown()
drawParallelogram(george, 20, 30, "brown")

# Side roof
george.penup()
george.goto(-50, -10)
george.pendown()
george.fillcolor("orange")
george.begin_fill()
george.left(30)
george.forward(60)
george.left(105)
george.forward(100/ math.sqrt(2))
george.left(75)
george.forward(60)
george.left(45)
george.end_fill()

# Tree Base
george.penup()
george.goto(100, -130)
george.pendown()
drawRectangle(george, 20, 40, "brown")

# Tree Top
george.penup()
george.goto(65, -90)
george.pendown()
drawTriangle(george, 90, "light green")
george.penup()
george.goto(70, -45)
george.pendown()
drawTriangle(george, 80, "light green")
george.penup()
george.goto(75, -5)
george.pendown()
drawTriangle(george, 70, "light green")

# Sun
george.penup()
george.goto(55, 110)
george.fillcolor("Yellow")
george.pendown()
george.begin_fill()
george.circle(24)
george.end_fill()

# Sun rays
george.penup()
george.goto(55, 134)
george.penup()
drawFourRays(george, 25, 24)
george.right(45)
drawFourRays(george, 15, 24)
george.left(45)

# Put down some Labels
george.color("black")
george.penup()
george.goto(-150, 70)
george.pendown()
george.write("House", None, None, "14pt bold")
george.penup()
george.goto(150, -150)
george.pendown()
george.write("Tree", None, None, "14pt bold")
george.penup()
george.goto(138, 150)
george.pendown()
george.write("Sun", None, None, "14pt bold")

# bring the turtle down to the front door, and we're done!
george.penup()
george.goto(-100, -150)
george.left(90)











































