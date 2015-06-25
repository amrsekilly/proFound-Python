# draw an art piece
import turtle

def draw_sq():
	# get a turtule
	chuck = turtle.Turtle()
	# get it some personality
	chuck.shape("turtle")
	chuck.color("brown")

	for i in range(0, 4):
		chuck.forward(100)
		chuck.right(90)
		chuck.speed(1)

def draw_circle():
	pink = turtle.Turtle()
	pink.shape("arrow")
	pink.color("red")

	pink.circle(20)


def draw_art():
	canv = turtle.Screen()
	canv.bgcolor("white")
	draw_sq()
	draw_circle()
	# close canvas on mouse click
	canv.exitonclick()



draw_art()





	