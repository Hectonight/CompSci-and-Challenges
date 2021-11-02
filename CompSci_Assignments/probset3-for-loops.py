import turtle


def polynomial1(x):
    return x ** 2 + 2 * x + 5


def polynomial2(x):
    return -x ** 3 + 5 * x + 10


def party_invitations(names):
    for name in names:
        print(f'Dear, {name}: You are invited to my party!')


def table(x_values, f):
    for value in x_values:
        print(value, f(value))


def multicolored_hexagon(turt, side_length):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for color in colors:
        turt.color(color)
        turt.forward(side_length)
        turt.left(60)


def turtle_path(turt, turn_angles):
    for angle in turn_angles:
        turt.forward(30)
        turt.left(angle)


print("Tester code for party_invitations")
names1 = ["Alice", "Bob", "Carol", "Dan", "Emily", "Fred"]
party_invitations(names1)
print()
names2 = ["Happy", "Sneezy", "Sleepy", "Grumpy", "Dopey", "Bashful", "Doc"]
party_invitations(names2)

x1 = [-10, -5, 0, 5, 10, 15, 20]
x2 = [0.1, 0.3, 0.5, 0.7, 0.9, 0.11, 0.13]

print("Tester code for table")
table(x1, polynomial1)
print()
table(x2, polynomial2)
print()
table(x1, polynomial2)
print()
table(x2, polynomial1)
print()

wn = turtle.Screen()

alice = turtle.Turtle()
bob = turtle.Turtle()

alice.shape("triangle")
bob.shape("square")

alice.penup()
alice.left(90)
alice.forward(200)
alice.pendown()

multicolored_hexagon(alice, 50)
multicolored_hexagon(bob, 100)

alice.penup()

alice.left(90)
alice.forward(50)
alice.pendown()

bob.forward(50)
angles = [150, 120, 90, 60, 30, 0, -30, -60, -90, -120, -150]

alice.penup()
alice.forward(100)
alice.pendown()

bob.penup()
bob.forward(100)
bob.pendown()

alice.pensize(5)
alice.color("black")

bob.pensize(5)
bob.color("black")

turtle_path(alice, angles)
turtle_path(bob, angles)

wn.exitonclick()
