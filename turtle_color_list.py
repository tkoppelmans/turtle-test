import turtle
from color_list import COLOR_LIST
from random import randint


pen = turtle.Turtle()

pen.pensize(100)
pen.speed(0)
pen.up()
pen.goto(-10,350)
pen.down()
color = 0
for x in range(1000):
	if color < 14:
		pen.pencolor(COLOR_LIST[color])
		print (COLOR_LIST[color])
		color += 1
	else :
		color = 0
	pen.fd(15)
	pen.right(2.5)