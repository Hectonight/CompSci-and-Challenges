import turtle
from math import *


def createEQ():
    print("Enter own function")
    userEQ = input()
    userEQ = userEQ.replace("^", "**")
    return userEQ


def TurtleSetUp():
    # noinspection PyGlobalUndefined
    global line
    line = turtle.Turtle()
    line.speed(0)
    pos = [-350, 350, 0, 0]
    for num in range(len(pos)):
        line.goto(pos[num], pos[-num - 1])
        line.goto(0, 0)


# noinspection PyUnusedLocal
def custom(x, eq):
    try:
        float(eval(eq))
        line.pendown()
        return float((eval(eq)))
    except:
        return None


def makeGraph(func, color):
    eq = createEQ()
    print("How many points per unit?")
    points = int(input())
    TurtleSetUp()
    line.penup()
    try:
        line.goto(-350, func(-350, eq))
        line.pendown()
    except TypeError:
        pass
    line.color(color)
    for x in range(-350 * points, 360 * points):
        line.pendown()
        try:
            line.goto(x / points, func(x / points, eq))
        except TypeError:
            line.pendown()


makeGraph(custom, "red")

turtle.Screen().exitonclick()
