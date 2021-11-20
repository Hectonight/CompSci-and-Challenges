import random
import math


def AreaofCube():
    countA = 0
    countB = 0
    for trail in range(1000000):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(-1, 1)
        if (x ** 4) + (y ** 4) + (z ** 2) <= 1:
            countA += 1
            countB += 1
        else:
            countB += 1
    return 8 * (countA / countB)


for num in range(21):
    print(AreaofCube())
