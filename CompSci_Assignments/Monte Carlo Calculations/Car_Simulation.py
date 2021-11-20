import random


def trial(miles):
    total_miles = 0
    while True:
        total_miles += miles
        if random.randint(1, 100) == 1:
            return total_miles


trials = 5000
values = []
milesPerLoop = 1000
for TestTrial in range(trials):
    values.append(trial(milesPerLoop))

print("Least Lucky:", min(values))
print("Most Lucky:", max(values))
print("Average:", sum(values) / len(values))
