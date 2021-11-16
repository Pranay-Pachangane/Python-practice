import turtle

t = turtle.Turtle()

turtle.bgcolor("black")
turtle.pensize(3)
turtle.speed(0)

while(True):
	for i in range(6):
		for colors in["red", "blue", "magenta", "green", "yellow", "white"]:
			turtle.color(colors)
			turtle.circle(200)
			turtle.left(10)

turtle.hideturtle()
turtle.mainloop()