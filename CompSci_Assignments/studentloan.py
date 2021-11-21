balance = float(input("Enter starting balance. "))
apr = float(input("Enter APR as a decimal. "))
payment = float(input("Enter monthly payment. "))
intrest = apr / 12


paid = 0
months = 0

while balance > 0:
    balance -= payment
    paid += payment
    balance *= (1 + intrest)
    months += 1

paid += balance

print("Total paid = $" + str(round(paid, 2)))
print("Total number of months =",  months)

