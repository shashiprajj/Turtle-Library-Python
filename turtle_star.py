import turtle
import math
import random

shashi = turtle.Turtle()
shashi.getscreen().bgcolor("blue")
shashi.speed(50)

shashi.penup()
shashi.goto(-200, 100)
shashi.pendown()

def star(turtle, size):
	if size <= 10:
		return
	else:	
		for i in range(5):
			turtle.forward(size)
			star(turtle, size/3)		# inbetween it calls again the function and start it procedure again 
										# so that it can make star over star
			turtle.left(216)

star(shashi, 360)				# calls the def function


turtle.done()
