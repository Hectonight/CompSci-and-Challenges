import turtle
import math


def createEQ():
        print("Enter own function")
        userEQ = input()
        userEQ = userEQ.replace("^", "**")
        userEQ = userEQ.replace("sin", "math.sin")
        userEQ = userEQ.replace("cos", "math.cos")
        userEQ = userEQ.replace("tan", "math.tan")
        userEQ = userEQ.replace("csc", "math.csc")
        userEQ = userEQ.replace("sec", "math.sec")
        userEQ = userEQ.replace("cot", "math.cot")
        TurtleSetUp()
        return userEQ


def TurtleSetUp():
    # noinspection PyGlobalUndefined
    global line
    line = turtle.Turtle()
    line.speed(0)
    pos = [-350, 350, 0, 0, 0]
    for num in range(len(pos)):
        line.goto(pos[num], pos[-num - 1])


# noinspection PyUnusedLocal
def custom(x, eq=createEQ()):
    try:
        print(eval(eq))
        return eval(eq)
    except ZeroDivisionError:
        line.penup()
        return eval(eq.replace("x", "(x+0.1)"))


def makeGraph(func, color):
    line.penup()
    line.goto(-350, func(-350))
    line.pendown()
    line.color(color)
    for x in range(-350, 360):
        line.pendown()
        line.goto(x, func(x))


makeGraph(custom, "red")

turtle.Screen().exitonclick()
