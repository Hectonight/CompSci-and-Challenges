import turtle
import math
import sympy


def createEQ():
    print("Enter own function")
    userEQ = input()
    replace = {
        "^": "**",
        "sin": "math.sin",
        "cos": "math.cos",
        "tan": "math.tan",
        "csc": "math.csc",
        "sec": "math.sec",
        "cot": "math.cot",
        "pi": "math.pi",
        "ceil": "math.ceil",
        "floor": "math.floor",
        "amath.": "math.a",
        "sqrt": "math.sqrt",
        "comb": "math.comb",
        "copysign": "math.copysign",
        "factorial": "math.factorial",
        "gcd": "math.gcd",
        "lcm": "math.lcm",
        "exp": "math.exp",
        "log": "math.log",
        "tau": "math.tau",
        "e": "math.e",
        "smath.": "s",
        "cmath.": "c",
        "math.math.": "math."
    }

    for word in replace:
        userEQ = userEQ.replace(word, replace[word])

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
def custom(x, eq):
    try:
        float(eval(eq))
        if x != -350:
            line.pendown()
        return float((eval(eq)))
    except ZeroDivisionError:
        line.pendown()
        return float(eval(ZeroDivision(eq)))
    except TypeError:
        return None



def ZeroDivision(eq):
    equation = eq.replace("round(x)", "round(x) + 0.00000000000001")
    equation = equation.replace("x", "(x+0.00000000000001)")
    return equation


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
            pass


makeGraph(custom, "red")

turtle.Screen().exitonclick()
