import random
import math


def AreaUnderCurve():
    countA = 0
    countB = 0
    for trail in range(1000000):
        x = random.uniform(0, 5)
        y = random.uniform(0, 25)
        if y <= x**2:
            countA += 1
            countB += 1
        else:
            countB += 1
    return 125 * (countA / countB)


for num in range(21):
    print(AreaUnderCurve())
