def triangle_area(a, b, c):
    """Return the area of a triangle using Heron's Formula
    where a, b, c are the side lengths of the triangle."""
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def rectangle_area(length, width):
    """Return the area of a rectangle."""
    return round(length * width, 2)


def prism_surface_area(a, b, c, h):
    """Returns the area of a triangular prism
    where the triangle has sides a, b, c
    and the height is h. PLEASE CALL THE TWO FUNCTIONS ABOVE
    YOUR ANSWER ONLY COUNTS IF YOU CALL triangle_area and rectangle_area"""
    return rectangle_area(a, h) + rectangle_area(c, h) + rectangle_area(b, h) + 2 * triangle_area(a, b, c)


def set_alarm(current_hour, delay):
    """Given a current hour of the day, and a number of hours
    to delay, return the hour of the day the alarm will go off.
    You can use 24-hour time, for example current_hour = 15 means 3pm."""
    time = current_hour + delay
    while time >= 24:
        time -= 24
    return time


def num_dimes(cents):
    """Given a number of cents, return the number of dimes we need to
    for that amount of change, if we can use quarters, nickels, dimes,
    and pennies, and we want to minimize the total number of coins."""
    return (cents - (25 * (cents // 25))) // 10


def pow_difference(a, b):
    """Returns the difference between a^b and b^a."""
    return (a ** b) - (b ** a)


def percent_change(start, finish):
    """Returns the percent of change when going from the starting value
    to the finishing value."""
    return round((finish - start) / start, 3)


print("Testing triangle_area")
print(triangle_area(5, 12, 13))
print(triangle_area(3, 4, 5))
print()

print("Testing rectangle_area")
print(rectangle_area(4.2, 0.8))
print(rectangle_area(3.4, 2))
print()

print("Testing prism_surface_area")
print(prism_surface_area(6, 8, 10, 5))
print(prism_surface_area(29, 20, 21, 10))
print()

print("Testing set_alarm")
print(set_alarm(7, 2))
print(set_alarm(8, 6))
print(set_alarm(15, 10))
print(set_alarm(12, 48))
print(set_alarm(20, 53))
print()

print("Testing num_dimes")
print(num_dimes(5))
print(num_dimes(13))
print(num_dimes(24))
print(num_dimes(27))
print(num_dimes(40))
print(num_dimes(94))
print(num_dimes(95))
print()

print("Testing pow_difference")
print(pow_difference(5, 1))
print(pow_difference(3, 7))
print(pow_difference(2, 10))
print()

print("Testing percent_change")
print(percent_change(50, 80))
print(percent_change(80, 50))
print(percent_change(0.4, 0.5))
print(percent_change(60, 54))
