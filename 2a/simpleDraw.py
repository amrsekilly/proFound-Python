

import turtle


def draw_sq():
	canv = turtle.Screen()
	canv.bgcolor("white")

	# get a turtule
	chuck = turtle.Turtle()

	# move it forward
	chuck.forward(100)
	chuck.right(90)
	chuck.forward(100)
	chuck.right(90)
	chuck.forward(100)
	chuck.right(90)
	chuck.forward(100)
	chuck.right(90)
	
	# close canvas on mouse click
	canv.exitonclick()

# call fn
draw_sq()
