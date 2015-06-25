# draw an art piece
import turtle

def draw_sq():
	canv = turtle.Screen()
	canv.bgcolor("white")

	# get a turtule
	chuck = turtle.Turtle()

	# get it some personality
	chuck.shape("turtle")
	chuck.color("brown")

	for i in range(0, 4):
		chuck.forward(100)
		chuck.right(90)

	# close canvas on mouse click
	canv.exitonclick()


def draw_art():
	draw_sq()



draw_art()





	