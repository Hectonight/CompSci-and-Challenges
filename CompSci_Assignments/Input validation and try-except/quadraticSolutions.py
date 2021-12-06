from math import sqrt

while True:
    a = float(input("Enter a. "))
    if a != 0:
        break
    print("a cannot be zero.")
b = float(input("Enter b. "))
c = float(input("Enter c. "))

try:
    discrim = sqrt(((b ** 2) - (4 * a * c)))
    if discrim != 0:
        print("Two Solutions:", round((-b + discrim) / (2 * a), 1), round((-b - discrim) / (2 * a), 1))
    else:
        print("One Solution:", round((-b + discrim) / (2 * a), 1))

except:
    print("No real solutions")
