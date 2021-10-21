import turtle
import random

random.seed(0)  # Initializes the random number generator.
# This is done so you get a predictable "random" number.

wn = turtle.Screen()  # Creates a variable for the screen.
wn.title("Problem 2: Scattered stamps")

ada = turtle.Turtle()
ada.shape("turtle")
ada.speed(0)
ada.penup()

last_point = (0, 0)  # You will need this variable. On each step, this represents the "previous" location of the turtle.
total_dist = 0  # Accumulator variable.

p = (0, 0)

for i in range(100):
    ada.goto(
        (random.randrange(-300, 300), random.randrange(-300, 300)))  # Sends the turtle to a random (x, y) on each step.
    total_dist += ada.distance(p)
    p = ada.position()

print("Total distance traveled =", round(total_dist), "pixels")

wn.exitonclick()
