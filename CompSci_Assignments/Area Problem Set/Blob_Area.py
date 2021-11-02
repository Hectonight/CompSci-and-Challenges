import random
import math


def blobArea():
    countA = 0
    countB = 0
    for trail in range(1000000):
        x = random.uniform(-2, 2)
        y = random.uniform(-1.5, 1.5)
        if (x ** 4) - (3 * (x ** 2)) + (y ** 4) <= 1:
            countA += 1
            countB += 1
        else:
            countB += 1
    return 12 * (countA / countB)


for num in range(21):
    print(blobArea())
