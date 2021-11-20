from random import normalvariate


def trial():
    miles_total = 0
    while True:
        miles_needed = normalvariate(200, 20)
        gas_per_gal = normalvariate(20, 4)
        miles = 12 * gas_per_gal
        if miles >= miles_needed:
            miles_total += miles_needed
        else:
            miles_total += miles
            break
    return miles


miles_sum = []
for trials in range(1000):
    miles_sum.append(trial())

print("Average Miles Traveled:", sum(miles_sum)/1000)
