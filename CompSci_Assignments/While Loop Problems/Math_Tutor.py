import random

count = 0

while count != 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = int(input(str(num1) + " + " + str(num2) + " = "))
    if num1 + num2 == answer:
        print("Right!\nGood job!")
        count += 1
    else:
        print("Wrong!")

