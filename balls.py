import turtle
import random
import time

	
def left_edge(ball, screen_width):
	if ball.xcor() < -screen_width / 2:
		return True
	else:
		return False

def right_edge(ball, screen_width):
	if ball.xcor() > screen_width / 2:
		return True
	else:
		return False	

def top_edge(ball, screen_height):
	if ball.ycor() > screen_height / 2:
		return True
	else:
		return False

def bottom_edge(ball, screen_height):
	if ball.ycor() < -screen_height / 2:
		return True
	else:
		return False			

def bounceBall(ball, new_direction):
	if new_direction == 'left' or new_direction == 'right':
		new_heading = 180 - ball.heading() #returns the turtles current heading
	elif new_direction == 'down' or new_direction == 'up':
		new_heading = 360 - ball.heading()

	return new_heading	


def new_head(balls):
	for k in range(0, len(balls)):
		head = balls[k].heading()
		if -45 <= head <= 45 or 135 <= head <= 225:
			balls[k].setheading(180-head)
		if 45 < head < 135 or 225 < head < 315:
			balls[k].setheading(360-head)
	return head			


def createBalls(num_balls):
	balls = []
	for k in range(0, num_balls):
		new_ball = turtle.Turtle()
		new_ball.shape('circle')
		new_ball.fillcolor('blue')
		new_ball.speed(0)
		new_ball.penup()
		new_ball.setheading(random.randint(1, 359))
		balls.append(new_ball)

	return balls	

#init screen size
screen_width = 800
screen_height = 600
turtle.setup(screen_width, screen_height)

#create turtle window
window = turtle.Screen()
window.title("Bouncing Balls")

#prompt user for execution time and number of balls
num_seconds = int(input('Enter number of seconds to run: '))
num_balls = int(input('Enter number of balls in simulation: '))

#create balls
balls = createBalls(num_balls)

#set start time
start_time = time.time()

#begin simulation
terminate = False

while not terminate:
	for k in range(0, len(balls)):
		balls[k].forward(15)

		#if two balls next to each other
		if balls[k].ycor() == balls[k-1].ycor() and balls[k].xcor() == balls[k-1].xcor():
			new_head(ball[k])
			new_head(balls[k-1])

		if left_edge(balls[k], screen_width):
			balls[k].setheading(bounceBall(balls[k], 'right'))
		elif right_edge(balls[k], screen_width):
			balls[k].setheading(bounceBall(balls[k], 'left'))
		elif top_edge(balls[k], screen_height):
			balls[k].setheading(bounceBall(balls[k], 'down'))
		elif bottom_edge(balls[k], screen_height):
			balls[k].setheading(bounceBall(balls[k], 'up'))		

		if time.time() - start_time > num_seconds:
			terminate = True	

turtle.exitonclick()			











