

import turtle


def draw_sq():
	canv = turtle.Screen()
	canv.bgcolor("blue")

	# get a turtule
	chuck = turtle.Turtle()

	# move it forward
	chuck.forward(100)
	
	# close canvas on mouse click
	window.exitonclick()


# call fn
draw_sq()
