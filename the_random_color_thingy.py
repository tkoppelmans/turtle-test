# Step 1: Make all the "turtle" commands available to us.
import turtle
import random
from random import randint

# Step 2: Create a new turtle. We'll call it "bob"
pen = turtle.Turtle()

# Step 3: Move in the direction Bob's facing for 50 pixels
pen.speed(10)
for x in range(10000):
	the_x = randint(-325,325)
	the_y = randint(-325,325)

	r = random.random()
	g = random.random()
	b = random.random()

	pen.pencolor(r,g,b)
	print (r,g,b)
	pen.goto(the_x,the_y)

# Step 4: We're done!
turtle.done()