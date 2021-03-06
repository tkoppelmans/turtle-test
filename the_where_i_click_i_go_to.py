# Step 1: Make all the "turtle" commands available to us.
import turtle
import random
from random import randint

# Step 2: Create a new turtle. We'll call it "bob"
pen = turtle.Turtle()
screen = turtle.Screen()

# Step 3: Move in the direction Bob's facing for 50 pixels
ps = 0
pen.speed(ps)
mypensize = 1
pen.pensize(mypensize)
r = 0.1
g = 0.1
b = 0.1
pen.pencolor(r,g,b)


def pen_up():
	pen.penup()

def pen_down():
	pen.pendown()

def zes_hoek():
	for x in range(6):
		pen.fd(100)
		pen.rt(60)

def size_bigger():
	global mypensize
	mypensize += 1
	pen.pensize(mypensize)
	print (mypensize)

def size_smaller():	
	global mypensize
	if mypensize == 1:
		print ('Can\'t get any smaller')
	else :
		mypensize -= 1
	pen.pensize(mypensize)
	print (mypensize)

def more_red():
	global r
	if r < 0.9:
		r += 0.1
	else :
		print ('NO! No more red!')
	pen.pencolor(r,g,b)
	print (r)

def more_green():
	global g
	if g < 0.9:
		g += 0.1
	else :
		print ('NO! No more green!')
	pen.pencolor(r,g,b)
	print (g)

def more_blue():
	global b
	if b < 0.9:
		b += 0.1
	else :
		print ('NO! No more blue!')
	pen.pencolor(r,g,b)
	print (b)

def reset_color():
	global r,g,b
	r = 0.1
	g = 0.1
	b = 0.1
	pen.pencolor(r,g,b)
	print (r,g,b)


def clear():
	global ps
	pen.reset()
	ps = 0
	pen.speed(ps)



def ohhhoo():
	the_x = randint(-325,325)
	the_y = randint(-325,325)
	pen.goto(the_x,the_y)


screen.onclick(pen.goto)
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")
screen.onkey(zes_hoek, "6")
screen.onkey(size_bigger, "Up")
screen.onkey(size_smaller, "Down")
screen.onkey(more_red, "r")
screen.onkey(more_green, "g")
screen.onkey(more_blue, "b")
screen.onkey(reset_color, "p")
screen.onkey(ohhhoo, "o")
screen.onkey(clear, "c")

screen.listen()
turtle.mainloop()