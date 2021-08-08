import turtle
import time
from turtle import Turtle
from random import randint
import random

# window setup
window = turtle.Screen()
window.title("Turtle Race")
turtle.bgcolor("forestgreen")
turtle.color("White")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200)
turtle.write("TURTLE RACE", font = "Times 15 bold")
turtle.penup()

# DIRT
turtle.setpos(-350, -180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(200)
turtle.end_fill()

# FINISH LINE
# turtle.penup()
# turtle.color("black")
# turtle.setpos(140, -100)

# turtle.speed(200)
# for i in range(20):
# 	turtle.begin_fill()
# 	turtle.forward(8)
# 	turtle.right(90)
# 	turtle.forward(8)
# 	turtle.right(90)
# 	turtle.forward(8)
# 	turtle.right(90)
# 	turtle.forward(8)
# 	turtle.right(90)
# 	turtle.end_fill()
# 	turtle.penup()
# 	turtle.forward(16)

# turtle.left(90)
# turtle.forward(0)
# turtle.left(90)

# for i in range(20):
# 	turtle.begin_fill()
# 	turtle.forward(8)
# 	turtle.right(90)
# 	turtle.forward(8)
# 	turtle.right(90)
# 	turtle.forward(8)
# 	turtle.right(90)
# 	turtle.forward(8)
# 	turtle.right(90)
# 	turtle.end_fill()
# 	turtle.penup()
# 	turtle.forward(16)

# FINISH LINE
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()
turtle.hideturtle()

for i in range(10):
	turtle.setpos(finish_line, (150 - (i*square_size*2 )))
	turtle.stamp()

for j in range(10):
	turtle.setpos(finish_line + square_size, ((150 - square_size)-(j*square_size*2)))
	turtle.stamp()

# TURTLE1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("yellow")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()	
	
# TURTLE2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("cyan")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()	

# TURTLE3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("red")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

# TURTLE4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("blue")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()

time.sleep(1)   # Pause the game for 1 second before starting the race

# MOVE THE TURTLES
for i in range(145):				# 145 is the value, up till turtle can move from its starting place
	turtle1.forward(randint(1, 5))	# randint is the function where any random integer value it takes from the given values(1, 5)
	turtle2.forward(randint(1, 5))
	turtle3.forward(randint(1, 5))
	turtle4.forward(randint(1, 5))

turtle.exitonclick()

#turtle.done()
